const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('../frontend'));

// In-memory mock database
const users = [];
const chatHistory = [];
const userProfiles = {};
const userQuestionnaires = {};
const userGoals = {};
const userNotifications = {};
const userMoods = {};

console.log('🌱 Starting NeuroWell Privacy-Preserving Engine...');

// --- 1. AUTHENTICATION ENDPOINTS ---
app.post('/api/auth/signup', (req, res) => {
    const { email, password, name } = req.body;
    if (!email || !password) return res.status(400).json({ error: 'Email and password required' });
    
    users.push({ id: Date.now(), email, name });
    res.json({ message: 'User created securely. Data encrypted locally.', token: 'mock-jwt-token-777' });
});

app.post('/api/auth/login', (req, res) => {
    const { email, password } = req.body;
    if (!email || !password) return res.status(400).json({ error: 'Email and password required' });
    
    res.json({ message: 'Login successful', token: 'mock-jwt-token-777', userId: 1 });
});

// --- 2. DASHBOARD & BIOMETRIC ENDPOINTS ---
app.get('/api/dashboard/metrics', (req, res) => {
    // Simulating real-time local telemetry processing
    const metrics = {
        resonanceScore: Math.floor(Math.random() * (95 - 75 + 1) + 75), // Random between 75-95
        state: 'BALANCED & PRESENT',
        vagusNerveTone: 'Optimal',
        subconsciousSync: {
            pupilDilationVariance: 'Stable (1.2mm)',
            microRespiration: '14 bpm'
        },
        environmentalEngine: {
            ambientNoiseStress: 'Low (40dB)',
            barometricPressure: 'Stable'
        }
    };
    res.json(metrics);
});

// --- 3. EMOTION DETECTION & SCAN ENDPOINTS ---
app.post('/api/emotion/scan', (req, res) => {
    const { scanType, payload } = req.body;
    // Simulate analyzing biometric data
    setTimeout(() => {
        res.json({
            message: 'Scan processed locally',
            analysis: {
                stressLevel: 'Low',
                detectedEmotion: 'Calm',
                confidence: 0.92,
                recommendation: 'Maintain current breathing pattern.'
            }
        });
    }, 1500); // simulate processing delay
});

// --- 4. AI GUIDE / CHAT ENDPOINTS ---
app.post('/api/chat/message', (req, res) => {
    const { message } = req.body;
    if (!message) return res.status(400).json({ error: 'Message required' });

    chatHistory.push({ role: 'user', content: message });

    // Mock AI Therapist response generation based on sentiment
    let aiResponse = "I hear you. Tell me more about what you're feeling right now.";
    const lowerMsg = message.toLowerCase();
    
    if (lowerMsg.includes('stress') || lowerMsg.includes('anxi')) {
        aiResponse = "I can sense some tension. Let's do a quick somatic reset. Breathe in for 4 seconds, hold for 4, and exhale for 6.";
    } else if (lowerMsg.includes('sad') || lowerMsg.includes('down')) {
        aiResponse = "It's completely okay to feel that way. I'm here for you, in this private space. What triggered this feeling?";
    } else if (lowerMsg.includes('good') || lowerMsg.includes('great')) {
        aiResponse = "I'm glad to hear your resonance is high today. Let's capture this baseline for future insights.";
    }

    chatHistory.push({ role: 'ai', content: aiResponse });

    setTimeout(() => {
        res.json({ reply: aiResponse });
    }, 1000); // Simulate "typing"
});

// --- 5. NEURAL-ACOUSTIC GENERATION ---
app.get('/api/wellness/audio-stream', (req, res) => {
    // In a real app, this would stream generated audio chunks
    res.json({
        frequency: '432Hz',
        waveType: 'Theta',
        duration: '15:00',
        message: 'Synthesizing audio specifically for your current brainwave state.'
    });
});

// --- 6. BIOMETRIC RECOGNITION ENDPOINTS ---
app.post('/api/auth/webauthn/verify', (req, res) => {
    // Mock WebAuthn Fingerprint/FaceID verification
    setTimeout(() => res.json({ success: true, message: 'Fingerprint verified securely.' }), 800);
});

app.post('/api/biometric/face', (req, res) => {
    const { image } = req.body;
    if(!image) return res.status(400).json({error: 'No image provided'});
    // Mock face analysis
    setTimeout(() => res.json({ 
        success: true, 
        analysis: 'Micro-expressions indicate deep calmness. Pupil dilation stable at 1.2mm.' 
    }), 1200);
});

app.post('/api/biometric/voice', (req, res) => {
    const { transcript } = req.body;
    // Mock voice sentiment analysis
    setTimeout(() => res.json({ 
        success: true, 
        analysis: `Vocal cord tension is very low. Semantic analysis of "${transcript || 'audio'}" shows excellent resonance.` 
    }), 1500);
});

// --- 7. FORGOT PASSWORD (Stub) ---
app.post('/api/auth/forgot-password', (req, res) => {
    res.json({ message: 'Password reset link sent (mock).' });
});

// --- 8. USER PROFILE ---
app.post('/api/user/profile', (req, res) => {
    const { userId, age, gender, fullName, email } = req.body;
    userProfiles[userId] = { ...(userProfiles[userId] || {}), age, gender, fullName, email };
    res.json({ success: true });
});

app.get('/api/user/profile/:userId', (req, res) => {
    res.json({ data: userProfiles[req.params.userId] || null });
});

// --- 9. QUESTIONNAIRE ---
app.post('/api/user/questionnaire', (req, res) => {
    const { userId, ...answers } = req.body;
    userQuestionnaires[userId] = { ...answers, timestamp: new Date().toISOString() };
    res.json({ success: true });
});

// --- 10. GOALS ---
app.post('/api/user/goals', (req, res) => {
    const { userId, goals } = req.body;
    userGoals[userId] = { goals, updatedAt: new Date().toISOString() };
    res.json({ success: true });
});

// --- 11. NOTIFICATION PREFS ---
app.post('/api/user/notifications', (req, res) => {
    const { userId, ...prefs } = req.body;
    userNotifications[userId] = prefs;
    res.json({ success: true });
});

// --- 12. MOOD TRACKING ---
app.post('/api/user/mood', (req, res) => {
    const { userId, mood, notes, date } = req.body;
    if (!userMoods[userId]) userMoods[userId] = [];
    userMoods[userId].push({ mood, notes, date, timestamp: new Date().toISOString() });
    res.json({ success: true });
});

app.get('/api/user/mood/:userId', (req, res) => {
    res.json({ data: userMoods[req.params.userId] || [] });
});

app.listen(PORT, () => {
    console.log(`🌿 NeuroWell Backend API running on http://localhost:${PORT}`);
    console.log(`🔒 Privacy Mode: Active (Data processes locally in-memory)`);
});
