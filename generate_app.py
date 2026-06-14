import json
import os

screens = [
    # 1. Auth
    ("1-splash", "Splash Screen"),
    ("2-welcome", "Welcome Screen"),
    ("3-login", "Login"),
    ("4-signup", "Signup"),
    ("5-otp", "OTP Verification"),
    ("6-forgot-password", "Forgot Password"),
    ("7-reset-password", "Reset Password"),
    ("8-biometric-login", "Biometric Login"),
    # 2. Onboarding
    ("9-onboarding-1", "Onboarding 1 (Intro)"),
    ("10-onboarding-2", "Onboarding 2 (Features)"),
    ("11-onboarding-3", "Onboarding 3 (Privacy)"),
    ("12-user-info", "User Info Form"),
    ("13-questionnaire", "Mental Health Questionnaire"),
    ("14-goals", "Goal Selection"),
    ("15-notifications", "Notification Preferences"),
    # 3. Dashboard
    ("16-dashboard-main", "Main Dashboard"),
    ("17-dashboard-positive", "Positive Mood Dashboard"),
    ("18-dashboard-stress", "High Stress Dashboard"),
    ("19-dashboard-weekly", "Weekly Summary Dashboard"),
    ("20-dashboard-empty", "Empty State Dashboard"),
    # 4. Emotion Detection
    ("21-emotion-home", "Emotion Detection Home"),
    ("22-voice-input", "Voice Input Screen"),
    ("23-voice-recording", "Voice Recording Screen"),
    ("24-voice-processing", "Voice Processing Screen"),
    ("25-text-input", "Text Input Screen"),
    ("26-text-analysis", "Text Analysis Result"),
    ("27-behavior-tracking", "Behavior Tracking Screen"),
    ("28-combined-analysis", "Combined Analysis Result"),
    # 5. AI Insights
    ("29-insights-overview", "AI Insights Overview"),
    ("30-mood-report", "Detailed Mood Report"),
    ("31-weekly-trends", "Weekly Trends"),
    ("32-monthly-analytics", "Monthly Analytics"),
    ("33-stress-breakdown", "Stress Breakdown"),
    ("34-trigger-detection", "Trigger Detection Screen"),
    ("35-ai-explanation", "AI Explanation Screen"),
    # 6. Mood Tracking
    ("36-mood-calendar", "Mood Calendar"),
    ("37-add-mood", "Add Mood Entry"),
    ("38-edit-mood", "Edit Mood Entry"),
    ("39-mood-timeline", "Mood Timeline"),
    ("40-mood-comparison", "Mood Comparison"),
    # 7. AI Chat
    ("41-chat-home", "Chat Home"),
    ("42-chat-conversation", "Chat Conversation"),
    ("43-suggested-replies", "Suggested Replies"),
    ("44-crisis-alert", "Crisis Alert Screen"),
    ("45-chat-history", "Chat History"),
    # 8. Wellness
    ("46-wellness-suggestions", "Wellness Suggestions"),
    ("47-meditation-player", "Meditation Player"),
    ("48-breathing-exercise", "Breathing Exercise Screen"),
    # 9. Privacy
    ("49-privacy-dashboard", "Privacy Dashboard"),
    ("50-profile-settings", "Profile & Settings"),
]

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>NeuroWell AI - Serenity SPA</title>
    <link rel="icon" type="image/png" href="logo.png">
    <link rel="stylesheet" href="style.css">
</head>
<body>
<div id="app">
"""

for id_name, title in screens:
    classes = "view active" if id_name == "1-splash" else "view"
    content = ""
    
    if id_name == "1-splash":
        content = """
        <div class="logo-container mx-auto mt-8 mb-4" onclick="navigate('2-welcome')">
            <img class="logo-icon" src="logo.png" style="border-radius:50%; object-fit:cover; padding:5px; background:var(--glass-bg);">
        </div>
        <h1 class="text-center">NeuroWell <span class="text-gradient">AI</span></h1>
        <p class="text-center text-muted mt-2">Harmonizing Mind & Environment</p>
        <div class="glass-card mt-8 mx-auto" style="width: 80%; text-align: center;">
            <p class="text-muted" style="font-size: 0.8rem;">Featuring Exclusive:</p>
            <p class="text-primary mt-2">✦ Subconscious Biometric Sync</p>
            <p class="text-primary mt-2">✦ Neural-Acoustic Therapy</p>
            <p class="text-primary mt-2">✦ Ambient Environment Engine</p>
        </div>
        """
    elif id_name == "2-welcome":
        content = """
        <div class="header"><h2>Welcome to Serenity</h2></div>
        <div class="glass-card mt-8 text-center" style="flex:1; display:flex; flex-direction:column; justify-content:center;">
            <p class="mb-4">Your private space for gentle emotional intelligence.</p>
            <button class="btn btn-primary mb-4" onclick="navigate('3-login')">Login</button>
            <button class="btn btn-glass" onclick="navigate('4-signup')">Sign Up</button>
        </div>
        """
    elif id_name == "3-login":
        content = """
        <div class="header">
            <button class="back-btn" onclick="navigate('2-welcome')">←</button>
            <h2>Login</h2>
            <div></div>
        </div>
        <div class="glass-card mt-4" style="flex:1;">
            <input type="email" class="input-field mb-4" placeholder="Email">
            <input type="password" class="input-field mb-4" placeholder="Password">
            <button class="btn btn-primary" onclick="navigate('16-dashboard-main')">Sign In</button>
        </div>
        """
    elif id_name == "16-dashboard-main":
        content = """
        <div class="header">
            <div>
                <h2>Hello, Alex</h2>
                <p class="text-muted">A calm afternoon awaits.</p>
            </div>
            <div class="avatar" onclick="navigate('50-profile-settings')">A</div>
        </div>
        
        <div class="glass-card text-center mb-4">
            <h3 class="mb-2">Resonance Score</h3>
            <div class="mood-score text-gradient mb-2" style="font-size: 3.5rem; font-weight: 300;">84</div>
            <p class="text-primary" style="font-weight: 500;">BALANCED & PRESENT</p>
            <p class="text-muted mt-2" style="font-size: 0.8rem;">Vagus nerve tone is optimal.</p>
        </div>
        
        <div class="glass-card mb-4" style="padding: 16px;">
            <h4 class="mb-2">✦ Subconscious Sync</h4>
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-muted);">
                <span>Pupil Dilation Variance</span>
                <span class="text-accent">Stable (1.2mm)</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-muted); margin-top: 8px;">
                <span>Micro-Respiration</span>
                <span class="text-primary">14 bpm</span>
            </div>
        </div>
        
        <div class="glass-card mb-4" style="padding: 16px;">
            <h4 class="mb-2">🌤️ Environmental Engine</h4>
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-muted);">
                <span>Ambient Noise Stress</span>
                <span class="text-primary">Low (40dB)</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-muted); margin-top: 8px;">
                <span>Barometric Pressure Drop</span>
                <span class="text-accent">Noticed (May cause fatigue)</span>
            </div>
        </div>
        """
    elif id_name == "21-emotion-home":
        content = """
        <div class="header"><h2>Analyze State</h2></div>
        <p class="text-muted mb-4">Choose a method to gently analyze your current resonance.</p>
        
        <div class="glass-card mb-4" onclick="navigate('22-voice-input')" style="cursor:pointer;">
            <h3>👁️ Optical-Respiratory Scan <span class="badge" style="background:var(--accent); color:white; font-size:0.6rem; vertical-align:middle;">NEW</span></h3>
            <p class="text-muted mt-2" style="font-size:0.85rem;">Tracks pupil dilation and chest micro-movements to detect hidden stress.</p>
        </div>
        
        <div class="glass-card mb-4" onclick="navigate('22-voice-input')" style="cursor:pointer;">
            <h3>🎤 Acoustic Biomarkers</h3>
            <p class="text-muted mt-2" style="font-size:0.85rem;">Analyzes vocal cord tension and cadence patterns.</p>
        </div>
        
        <div class="glass-card" onclick="navigate('25-text-input')" style="cursor:pointer;">
            <h3>💬 Semantic Sentiment</h3>
            <p class="text-muted mt-2" style="font-size:0.85rem;">Analyzes emotional undertones in your text.</p>
        </div>
        """
    elif id_name == "46-wellness-suggestions":
        content = """
        <div class="header">
            <button class="back-btn" onclick="navigate('29-insights-overview')">←</button>
            <h2>Therapies</h2>
            <div></div>
        </div>
        <div class="glass-card mb-4 mt-4" style="text-align:center;">
            <h3 class="mb-2">🎵 Neural-Acoustic Generation</h3>
            <p class="text-muted mb-4" style="font-size:0.85rem;">Real-time binaural frequencies synthesized specifically for your current brainwave state to induce calmness.</p>
            <div class="loader mx-auto mb-4" style="border-top-color: var(--accent);"></div>
            <p class="text-accent mb-4">Generating 432Hz Theta Waves...</p>
            <button class="btn btn-primary" onclick="navigate('47-meditation-player')">Begin Session</button>
        </div>
        <div class="glass-card mb-4">
            <h3 class="mb-2">🌬️ Somatic Reset</h3>
            <p class="text-muted" style="font-size:0.85rem;">A 2-minute physical engagement to reset your vagus nerve.</p>
            <button class="btn btn-glass mt-4" onclick="navigate('48-breathing-exercise')">Start Breathing</button>
        </div>
        """
    elif id_name == "41-chat-home":
        content = """
        <div class="header"><h2>AI Guide</h2></div>
        <div class="glass-card text-center mb-4" style="flex:1;">
            <img src="logo.png" class="logo-icon mb-4 mx-auto" style="width:80px; height:80px; border-radius:50%; object-fit:cover; padding:4px;">
            <h3 class="mb-2">Your Empathetic Guide</h3>
            <p class="text-muted mb-8">A private, non-judgmental space processing locally to preserve your peace of mind.</p>
            <button class="btn btn-primary" onclick="navigate('42-chat-conversation')">Talk to Guide</button>
        </div>
        """
    elif "onboarding" in id_name:
        next_map = {"9-onboarding-1": "10-onboarding-2", "10-onboarding-2": "11-onboarding-3", "11-onboarding-3": "12-user-info"}
        next_scr = next_map.get(id_name, "12-user-info")
        content = f"""
        <div class="header"><h2>{title}</h2></div>
        <div class="glass-card text-center" style="flex:1; display:flex; flex-direction:column; justify-content:center;">
            <h3 class="mb-4">Step {id_name.split('-')[-1]}</h3>
            <p class="text-muted mb-8">We are setting up your personalized environmental and biometric baseline.</p>
            <button class="btn btn-primary" onclick="navigate('{next_scr}')">Continue Gently</button>
        </div>
        """
    else:
        # Generic Placeholder
        content = f"""
        <div class="header">
            <button class="back-btn" onclick="navigate('16-dashboard-main')">←</button>
            <h2>{title}</h2>
            <div></div>
        </div>
        <div class="glass-card text-center mt-4" style="flex:1; display:flex; flex-direction:column; justify-content:center;">
            <img src="logo.png" class="logo-icon mx-auto mb-4" style="width:60px; height:60px; opacity:0.5; filter: grayscale(1); border-radius:50%;">
            <h3>{title}</h3>
            <p class="text-muted mt-4">Screen template resting peacefully.</p>
        </div>
        """
        
    html_content += f"""
    <div id="view-{id_name}" class="{classes}">
        {content}
    </div>
"""

html_content += """
    <!-- BOTTOM NAVIGATION -->
    <div class="bottom-nav" id="bottom-nav" style="display: none;">
        <div class="nav-item active" data-target="16-dashboard-main" onclick="navigate('16-dashboard-main')">
            <div class="nav-icon">🏠</div><span>Home</span>
        </div>
        <div class="nav-item" data-target="21-emotion-home" onclick="navigate('21-emotion-home')">
            <div class="nav-icon">🌿</div><span>Analyze</span>
        </div>
        <div class="nav-item" data-target="29-insights-overview" onclick="navigate('29-insights-overview')">
            <div class="nav-icon">📊</div><span>Insights</span>
        </div>
        <div class="nav-item" data-target="41-chat-home" onclick="navigate('41-chat-home')">
            <div class="nav-icon">💬</div><span>Guide</span>
        </div>
        <div class="nav-item" data-target="50-profile-settings" onclick="navigate('50-profile-settings')">
            <div class="nav-icon">👤</div><span>Profile</span>
        </div>
    </div>
</div>

<script src="app.js"></script>
</body>
</html>
"""

with open(os.path.join("frontend", "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

# Update CSS for Calming Theme
css_content = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@300;400;500;600&display=swap');

:root {
    --bg-color: #f2f6f5; /* Soft sage/grey background */
    --surface-color: #ffffff;
    --surface-light: #fafafa;
    --primary: #6b8e82; /* Calming sage green */
    --primary-light: #94b4a9;
    --primary-gradient: linear-gradient(135deg, #6b8e82, #8ea89e);
    --secondary: #7b95a3; /* Soft slate blue */
    --accent: #d89f7a; /* Warm terracotta */
    --danger: #d97b7b;
    --text-main: #2d3748; /* Soft dark grey for text */
    --text-muted: #718096;
    --border-color: rgba(0, 0, 0, 0.05);
    --glass-bg: rgba(255, 255, 255, 0.7);
    --glass-border: rgba(255, 255, 255, 0.5);
    --shadow-glow: 0 10px 40px rgba(107, 142, 130, 0.15);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Inter', sans-serif;
    background-color: var(--bg-color);
    color: var(--text-main);
    overflow: hidden; 
    background-image: radial-gradient(circle at top right, rgba(148, 180, 169, 0.2), transparent 50%),
                      radial-gradient(circle at bottom left, rgba(216, 159, 122, 0.15), transparent 50%);
}

h1, h2, h3, h4, h5 { font-family: 'Outfit', sans-serif; font-weight: 500; }

#app {
    width: 100%; max-width: 480px; margin: 0 auto; height: 100dvh;
    position: relative; overflow: hidden;
    box-shadow: 0 0 30px rgba(0,0,0,0.05);
    background: transparent;
}

.view {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    display: none; flex-direction: column; padding: 24px; opacity: 0;
    transition: opacity 0.4s ease, transform 0.4s ease;
    overflow-y: auto; padding-bottom: 90px;
}
.view::-webkit-scrollbar { display: none; }
.view.active { display: flex; opacity: 1; transform: scale(1); z-index: 10; }

.text-center { text-align: center; }
.text-left { text-align: left; }
.w-100 { width: 100%; }
.mt-2 { margin-top: 8px; }
.mt-4 { margin-top: 16px; }
.mb-2 { margin-bottom: 8px; }
.mb-4 { margin-bottom: 16px; }
.mt-8 { margin-top: 32px; }
.mb-8 { margin-bottom: 32px; }
.mx-auto { margin-left: auto; margin-right: auto; }
.mt-auto { margin-top: auto; }

.text-muted { color: var(--text-muted); font-size: 0.95rem; line-height: 1.5; }
.text-primary { color: var(--primary); font-weight: 500;}
.text-accent { color: var(--accent); font-weight: 500;}
.text-danger { color: var(--danger); }
.text-gradient {
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.btn {
    width: 100%; padding: 16px; border-radius: 16px; border: none;
    font-family: 'Outfit', sans-serif; font-size: 1.05rem; font-weight: 500;
    cursor: pointer; transition: all 0.3s;
    box-shadow: 0 4px 14px rgba(0,0,0,0.05);
}
.btn-primary { background: var(--primary-gradient); color: white; box-shadow: 0 4px 15px rgba(107, 142, 130, 0.3); }
.btn-primary:active { transform: translateY(2px); box-shadow: 0 2px 5px rgba(107, 142, 130, 0.3); }
.btn-glass { background: var(--glass-bg); border: 1px solid var(--glass-border); color: var(--primary); backdrop-filter: blur(8px); }
.btn-glass:active { background: rgba(255,255,255,0.9); }

.back-btn { background:none; border:none; color:var(--text-main); font-size:1.5rem; cursor:pointer; opacity: 0.7; }
.header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }

.glass-card {
    background: var(--glass-bg); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--glass-border); border-radius: 24px; padding: 24px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.04);
}

.input-field {
    width: 100%; background: rgba(255,255,255,0.8); border: 1px solid rgba(0,0,0,0.05);
    color: var(--text-main); padding: 16px; border-radius: 16px; font-size: 1rem; font-family: 'Inter', sans-serif; outline: none;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
}
.input-field:focus { border-color: var(--primary-light); background: #ffffff; }

.bottom-nav {
    position: absolute; bottom: 0; left: 0; width: 100%; height: 85px;
    background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(20px); border-top: 1px solid var(--border-color);
    display: flex; justify-content: space-around; align-items: center; padding-bottom: 16px; z-index: 100;
}

.nav-item { display: flex; flex-direction: column; align-items: center; gap: 6px; color: var(--text-muted); font-size: 0.75rem; cursor: pointer; transition: 0.3s; opacity: 0.6;}
.nav-item.active { color: var(--primary); opacity: 1; font-weight: 500;}
.nav-icon { font-size: 1.5rem; transition: transform 0.3s; }
.nav-item.active .nav-icon { transform: translateY(-4px); }

.avatar { width: 48px; height: 48px; border-radius: 50%; background: var(--primary-light); color: white; display: flex; align-items: center; justify-content: center; font-weight: 500; font-family: 'Outfit'; cursor:pointer; font-size: 1.2rem; }

.logo-icon { font-size: 3.5rem; display: flex; justify-content: center; align-items: center; width: 100px; height: 100px; border-radius: 50%; background: var(--glass-bg); border: 1px solid var(--glass-border); box-shadow: var(--shadow-glow); }

.loader { width:40px; height:40px; border:3px solid rgba(107, 142, 130, 0.2); border-top:3px solid var(--primary); border-radius:50%; animation: spin 1s linear infinite; }
@keyframes spin { 100% { transform: rotate(360deg); } }
"""

with open(os.path.join("frontend", "style.css"), "w", encoding="utf-8") as f:
    f.write(css_content)

print("Theme updated to Serenity (Stress-Reducing) with New Features!")
