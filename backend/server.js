const express = require('express');
const cors = require('cors');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;
const JWT_SECRET = process.env.JWT_SECRET || 'fallback_super_secret_jwt_key_change_in_prod';

// --- SECURITY MIDDLEWARE ---
app.use(helmet());
app.use(cors({
    origin: ['http://localhost:3000', 'https://neurowellai-49389.web.app'],
    credentials: true
}));
app.use(express.json({ limit: '50kb' }));
app.use(express.static('../'));

// Rate Limiting
const authLimiter = rateLimit({ windowMs: 15 * 60 * 1000, max: 10 }); // 10 req / 15 min
const apiLimiter = rateLimit({ windowMs: 15 * 60 * 1000, max: 100 }); // 100 req / 15 min
app.use('/api/auth', authLimiter);
app.use('/api/', apiLimiter);

// --- JWT AUTHENTICATION MIDDLEWARE ---
const authenticateToken = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];
    
    if (!token) return res.status(401).json({ error: 'Access denied. No token provided.' });
    
    jwt.verify(token, JWT_SECRET, (err, user) => {
        if (err) return res.status(403).json({ error: 'Invalid token.' });
        req.user = user;
        next();
    });
};

// --- DATA SANITIZATION UTILS ---
const escapeHtml = (unsafe) => {
    if (!unsafe || typeof unsafe !== 'string') return '';
    return unsafe
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
};

// In-memory mock database
const users = [];
const chatHistory = [];
const userProfiles = {};
const userQuestionnaires = {};
const userGoals = {};
const userNotifications = {};
const userMoods = {};

console.log('🌱 Starting NeuroWell Privacy-Preserving Engine...');

// --- 0. CONFIG ENDPOINT ---
app.get('/api/config/firebase', (req, res) => {
    // In production, these should be loaded strictly from process.env
    res.json({
        apiKey: process.env.FIREBASE_API_KEY || "AIzaSyDVsIsC0O670V8GDF8NmDm4z4prqGkCDZU",
        authDomain: "neurowellai-49389.firebaseapp.com",
        projectId: "neurowellai-49389",
        storageBucket: "neurowellai-49389.firebasestorage.app",
        messagingSenderId: "296899830526",
        appId: "1:296899830526:web:20fd87ac25219c44effbaf",
        measurementId: "G-R86DHQEGTT"
    });
});

// --- 1. AUTHENTICATION ENDPOINTS ---
app.post('/api/auth/signup', async (req, res) => {
    try {
        const { email, password, name } = req.body;
        if (!email || !password) return res.status(400).json({ error: 'Email and password required' });
        
        const existingUser = users.find(u => u.email === email);
        if (existingUser) return res.status(400).json({ error: 'Email already exists' });

        const hashedPassword = await bcrypt.hash(password, 12);
        const newUser = { id: Date.now().toString(), email, name, password: hashedPassword };
        users.push(newUser);
        
        const token = jwt.sign({ id: newUser.id, email: newUser.email }, JWT_SECRET, { expiresIn: '24h' });
        res.json({ message: 'User created securely.', token, userId: newUser.id });
    } catch (e) {
        res.status(500).json({ error: 'Server error' });
    }
});

app.post('/api/auth/login', async (req, res) => {
    try {
        const { email, password } = req.body;
        if (!email || !password) return res.status(400).json({ error: 'Email and password required' });
        
        const user = users.find(u => u.email === email);
        if (!user) return res.status(401).json({ error: 'Invalid credentials' });

        const validPassword = await bcrypt.compare(password, user.password);
        if (!validPassword) return res.status(401).json({ error: 'Invalid credentials' });

        const token = jwt.sign({ id: user.id, email: user.email }, JWT_SECRET, { expiresIn: '24h' });
        res.json({ message: 'Login successful', token, userId: user.id });
    } catch (e) {
        res.status(500).json({ error: 'Server error' });
    }
});

app.post('/api/auth/forgot-password', (req, res) => {
    // Basic rate-limited stub
    res.json({ message: 'If an account exists, a reset link was sent.' });
});

app.post('/api/auth/webauthn/verify', authenticateToken, (req, res) => {
    // Mock WebAuthn
    setTimeout(() => res.json({ success: true, message: 'Fingerprint verified securely.' }), 800);
});

// --- APPLY AUTH MIDDLEWARE TO ALL ROUTES BELOW ---
app.use('/api', authenticateToken);

// --- 2. DASHBOARD & BIOMETRIC ENDPOINTS ---
app.get('/api/dashboard/metrics', (req, res) => {
    const metrics = {
        resonanceScore: Math.floor(Math.random() * (95 - 75 + 1) + 75),
        state: 'BALANCED & PRESENT',
        vagusNerveTone: 'Optimal',
        subconsciousSync: { pupilDilationVariance: 'Stable (1.2mm)', microRespiration: '14 bpm' },
        environmentalEngine: { ambientNoiseStress: 'Low (40dB)', barometricPressure: 'Stable' }
    };
    res.json(metrics);
});

// --- 3. EMOTION DETECTION & SCAN ENDPOINTS ---
app.post('/api/emotion/scan', (req, res) => {
    setTimeout(() => {
        res.json({
            message: 'Scan processed locally',
            analysis: { stressLevel: 'Low', detectedEmotion: 'Calm', confidence: 0.92, recommendation: 'Maintain current breathing pattern.' }
        });
    }, 1500);
});

// --- 4. AI GUIDE / CHAT ENDPOINTS ---
app.post('/api/chat/message', (req, res) => {
    let { message } = req.body;
    if (!message || typeof message !== 'string') return res.status(400).json({ error: 'Message required' });
    message = escapeHtml(message);

    chatHistory.push({ role: 'user', content: message, userId: req.user.id });

    let aiResponse = "I hear you. Tell me more about what you're feeling right now.";
    const lowerMsg = message.toLowerCase();
    
    if (lowerMsg.includes('stress') || lowerMsg.includes('anxi')) {
        aiResponse = "I can sense some tension. Let's do a quick somatic reset. Breathe in for 4 seconds, hold for 4, and exhale for 6.";
    } else if (lowerMsg.includes('sad') || lowerMsg.includes('down')) {
        aiResponse = "It's completely okay to feel that way. I'm here for you, in this private space. What triggered this feeling?";
    } else if (lowerMsg.includes('good') || lowerMsg.includes('great')) {
        aiResponse = "I'm glad to hear your resonance is high today. Let's capture this baseline for future insights.";
    }

    chatHistory.push({ role: 'ai', content: aiResponse, userId: req.user.id });

    setTimeout(() => res.json({ reply: aiResponse }), 1000);
});

// --- 5. NEURAL-ACOUSTIC GENERATION ---
app.get('/api/wellness/audio-stream', (req, res) => {
    res.json({ frequency: '432Hz', waveType: 'Theta', duration: '15:00', message: 'Synthesizing audio specifically for your state.' });
});

// --- 6. BIOMETRIC RECOGNITION ENDPOINTS ---
app.post('/api/biometric/face', (req, res) => {
    if(!req.body.image) return res.status(400).json({error: 'No image provided'});
    setTimeout(() => res.json({ success: true, analysis: 'Micro-expressions indicate deep calmness. Pupil dilation stable at 1.2mm.' }), 1200);
});

app.post('/api/biometric/voice', (req, res) => {
    const safeTranscript = escapeHtml(req.body.transcript || 'audio');
    setTimeout(() => res.json({ 
        success: true, 
        analysis: `Vocal cord tension is very low. Semantic analysis of "${safeTranscript}" shows excellent resonance.` 
    }), 1500);
});

// --- 8. USER PROFILE ---
app.post('/api/user/profile', (req, res) => {
    const { age, gender, fullName, email } = req.body;
    userProfiles[req.user.id] = { ...(userProfiles[req.user.id] || {}), age, gender, fullName, email };
    res.json({ success: true });
});

app.get('/api/user/profile', (req, res) => {
    res.json({ data: userProfiles[req.user.id] || null });
});

// --- 9. QUESTIONNAIRE ---
app.post('/api/user/questionnaire', (req, res) => {
    const answers = req.body;
    userQuestionnaires[req.user.id] = { ...answers, timestamp: new Date().toISOString() };
    res.json({ success: true });
});

// --- 10. GOALS ---
app.post('/api/user/goals', (req, res) => {
    const { goals } = req.body;
    userGoals[req.user.id] = { goals, updatedAt: new Date().toISOString() };
    res.json({ success: true });
});

// --- 11. NOTIFICATION PREFS ---
app.post('/api/user/notifications', (req, res) => {
    const prefs = req.body;
    userNotifications[req.user.id] = prefs;
    res.json({ success: true });
});

// --- 12. MOOD TRACKING ---
app.post('/api/user/mood', (req, res) => {
    const { mood, notes, date } = req.body;
    if (!userMoods[req.user.id]) userMoods[req.user.id] = [];
    userMoods[req.user.id].push({ mood, notes: escapeHtml(notes), date, timestamp: new Date().toISOString() });
    res.json({ success: true });
});

app.get('/api/user/mood', (req, res) => {
    res.json({ data: userMoods[req.user.id] || [] });
});

app.listen(PORT, () => {
    console.log(`🌿 NeuroWell Backend API running on http://localhost:${PORT}`);
    console.log(`🔒 Privacy Mode: Active (Data processes locally in-memory)`);
});
