import re
import os

# --- 1. ENHANCE STYLE.CSS ---
new_css = """@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@300;400;500;600&display=swap');

:root {
    --bg-color: #f2f6f5; 
    --surface-color: #ffffff;
    --primary: #6b8e82; 
    --primary-light: #94b4a9;
    --primary-gradient: linear-gradient(135deg, #6b8e82, #8ea89e);
    --secondary: #7b95a3; 
    --accent: #d89f7a; 
    --danger: #d97b7b;
    --text-main: #2d3748; 
    --text-muted: #718096;
    --border-color: rgba(0, 0, 0, 0.05);
    --glass-bg: rgba(255, 255, 255, 0.7);
    --glass-border: rgba(255, 255, 255, 0.5);
    --shadow-glow: 0 10px 40px rgba(107, 142, 130, 0.15);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Inter', sans-serif;
    color: var(--text-main);
    overflow: hidden; 
    /* Dynamic Mesh Gradient Background */
    background: linear-gradient(-45deg, #f2f6f5, #e0ebe8, #e8f0ec, #dbe6e2);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
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
    transition: opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1), transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    overflow-y: auto; padding-bottom: 120px;
}
.view::-webkit-scrollbar { display: none; }
.view.active { display: flex; opacity: 1; transform: scale(1) translateY(0); z-index: 10; }
.view:not(.active) { transform: scale(0.98) translateY(10px); }

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
.btn-primary { background: var(--primary-gradient); color: white; box-shadow: 0 8px 25px rgba(107, 142, 130, 0.3); }
.btn-primary:active { transform: translateY(2px); box-shadow: 0 4px 10px rgba(107, 142, 130, 0.3); }
.btn-glass { background: rgba(255,255,255,0.4); border: 1px solid var(--glass-border); color: var(--text-main); backdrop-filter: blur(12px); box-shadow: 0 4px 15px rgba(0,0,0,0.02); border-top: 1px solid rgba(255,255,255,0.8);}
.btn-glass:active { background: rgba(255,255,255,0.7); }

.back-btn { background:none; border:none; color:var(--text-main); font-size:1.5rem; cursor:pointer; opacity: 0.7; transition: 0.3s;}
.back-btn:active { transform: translateX(-4px); }
.header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }

.glass-card {
    background: var(--glass-bg); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--glass-border); border-top: 1px solid rgba(255,255,255,0.9);
    border-radius: 24px; padding: 24px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.04), inset 0 2px 4px rgba(255,255,255,0.4);
    transition: transform 0.3s, box-shadow 0.3s;
}
.glass-card:active { transform: scale(0.98); }

.input-field {
    width: 100%; background: rgba(255,255,255,0.6); border: 1px solid var(--glass-border);
    color: var(--text-main); padding: 16px; border-radius: 16px; font-size: 1rem; font-family: 'Inter', sans-serif; outline: none;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); transition: 0.3s;
}
.input-field:focus { border-color: var(--primary-light); background: rgba(255,255,255,0.9); box-shadow: 0 0 0 4px rgba(107, 142, 130, 0.1); }

/* Floating Premium Bottom Nav */
.bottom-nav {
    position: absolute; bottom: 24px; left: 50%; transform: translateX(-50%);
    width: 90%; height: 75px; border-radius: 24px;
    background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(24px); 
    border: 1px solid rgba(255,255,255,0.6); border-top: 1px solid rgba(255,255,255,0.9);
    display: flex; justify-content: space-around; align-items: center; 
    z-index: 100; box-shadow: 0 10px 40px rgba(0,0,0,0.08); padding: 0 10px;
}

.nav-item { display: flex; flex-direction: column; align-items: center; gap: 4px; color: var(--text-muted); font-size: 0.7rem; cursor: pointer; transition: 0.4s cubic-bezier(0.4, 0, 0.2, 1); opacity: 0.6; position: relative;}
.nav-item.active { color: var(--primary); opacity: 1; font-weight: 600; }
.nav-icon { font-size: 1.5rem; transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1); }
.nav-item.active .nav-icon { transform: translateY(-4px) scale(1.1); text-shadow: 0 4px 10px rgba(107, 142, 130, 0.3); }

/* Decorative dot under active nav item */
.nav-item::after { content: ''; position: absolute; bottom: -8px; width: 4px; height: 4px; border-radius: 50%; background: var(--primary); opacity: 0; transition: 0.3s; }
.nav-item.active::after { opacity: 1; transform: translateY(-4px); }

.avatar { width: 48px; height: 48px; border-radius: 50%; background: var(--primary-gradient); color: white; display: flex; align-items: center; justify-content: center; font-weight: 500; font-family: 'Outfit'; cursor:pointer; font-size: 1.2rem; box-shadow: 0 4px 15px rgba(107, 142, 130, 0.3); border: 2px solid white;}

.logo-icon { font-size: 3.5rem; display: flex; justify-content: center; align-items: center; width: 100px; height: 100px; border-radius: 50%; background: var(--glass-bg); border: 1px solid var(--glass-border); box-shadow: var(--shadow-glow); }

.loader { width:40px; height:40px; border:3px solid rgba(107, 142, 130, 0.2); border-top:3px solid var(--primary); border-radius:50%; animation: spin 1s linear infinite; }
@keyframes spin { 100% { transform: rotate(360deg); } }

/* Breathing Circle Animation */
.breathing-circle {
    width: 200px; height: 200px; border-radius: 50%;
    background: radial-gradient(circle, rgba(107, 142, 130, 0.6) 0%, rgba(107, 142, 130, 0) 70%);
    box-shadow: 0 0 60px rgba(107, 142, 130, 0.3);
    margin: 40px auto;
    animation: breathe 10s cubic-bezier(0.4, 0, 0.2, 1) infinite;
    display: flex; align-items: center; justify-content: center;
    color: var(--primary); font-weight: 600; font-size: 1.2rem; letter-spacing: 2px;
}
@keyframes breathe {
    0% { transform: scale(0.8); opacity: 0.5; }
    40% { transform: scale(1.5); opacity: 1; } /* Inhale 4s */
    80% { transform: scale(1.5); opacity: 1; } /* Hold 4s */
    100% { transform: scale(0.8); opacity: 0.5; } /* Exhale 2s */
}

/* Audio Waves Animation */
.audio-waves { display: flex; justify-content: center; align-items: center; gap: 6px; height: 80px; margin: 40px 0; }
.wave { width: 8px; border-radius: 4px; background: var(--primary-gradient); animation: waveAnim 1.2s ease-in-out infinite alternate; box-shadow: 0 0 10px rgba(107, 142, 130, 0.4); }
.wave:nth-child(1) { height: 20%; animation-delay: 0.0s; }
.wave:nth-child(2) { height: 50%; animation-delay: 0.2s; }
.wave:nth-child(3) { height: 80%; animation-delay: 0.4s; }
.wave:nth-child(4) { height: 40%; animation-delay: 0.6s; }
.wave:nth-child(5) { height: 60%; animation-delay: 0.8s; }
@keyframes waveAnim { 0% { transform: scaleY(0.2); } 100% { transform: scaleY(1.5); } }

/* Chat Bubbles */
.chat-messages { flex: 1; overflow-y: auto; display: flex; flex-direction: column; gap: 16px; margin-bottom: 16px; padding-right: 8px; }
.msg { padding: 14px 18px; border-radius: 20px; font-size: 0.95rem; max-width: 85%; animation: msgFadeIn 0.3s ease; }
@keyframes msgFadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
.msg-user { background: var(--primary-gradient); color: white; align-self: flex-end; border-bottom-right-radius: 4px; box-shadow: 0 4px 15px rgba(107, 142, 130, 0.2); }
.msg-ai { background: rgba(255,255,255,0.8); border: 1px solid var(--glass-border); color: var(--text-main); align-self: flex-start; border-bottom-left-radius: 4px; }
"""

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(new_css)


# --- 2. ENHANCE INDEX.HTML SCREENS ---
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Feature: Breathing Exercise Screen
breathing_html = """
        <div class="header">
            <button class="back-btn" onclick="navigate('46-wellness-suggestions')">←</button>
            <h2>Somatic Reset</h2>
            <div></div>
        </div>
        <div class="glass-card text-center mt-4" style="flex:1; display:flex; flex-direction:column; justify-content:center;">
            <h3>Box Breathing</h3>
            <p class="text-muted mt-2">Follow the circle to reset your vagus nerve.</p>
            
            <div class="breathing-circle">Breathe</div>
            
            <div class="mt-8">
                <p class="text-primary mb-2">Inhale 4s • Hold 4s • Exhale 4s</p>
            </div>
            
            <button class="btn btn-glass mt-auto" onclick="navigate('16-dashboard-main')">End Session</button>
        </div>
"""
html = re.sub(r'<div id="view-48-breathing-exercise" class="view">.*?</div>\s*<div id="view-49-privacy-dashboard"', 
              f'<div id="view-48-breathing-exercise" class="view">{breathing_html}</div>\n    <div id="view-49-privacy-dashboard"', 
              html, flags=re.DOTALL)

# Feature: Meditation Player (Audio Therapy)
audio_html = """
        <div class="header">
            <button class="back-btn" onclick="navigate('46-wellness-suggestions')">←</button>
            <h2>Acoustic Therapy</h2>
            <div></div>
        </div>
        <div class="glass-card text-center mt-4" style="flex:1; display:flex; flex-direction:column; justify-content:center;">
            <h3>432Hz Theta Waves</h3>
            <p class="text-muted mt-2">Synthesized for your current resonance state.</p>
            
            <div class="audio-waves">
                <div class="wave"></div>
                <div class="wave"></div>
                <div class="wave"></div>
                <div class="wave"></div>
                <div class="wave"></div>
            </div>
            
            <h2 class="text-gradient mt-4" style="font-size:2.5rem; font-family:'Inter'; font-weight:300;">14:59</h2>
            
            <div style="display:flex; justify-content:center; gap:20px; align-items:center; margin-top: 40px;">
                <div class="avatar" style="width:40px; height:40px; background:var(--glass-bg); color:var(--text-main);">⏮</div>
                <div class="avatar" style="width:64px; height:64px; font-size:1.5rem;">⏸</div>
                <div class="avatar" style="width:40px; height:40px; background:var(--glass-bg); color:var(--text-main);">⏭</div>
            </div>
            
            <button class="btn btn-glass mt-auto" onclick="navigate('16-dashboard-main')">Finish Session</button>
        </div>
"""
html = re.sub(r'<div id="view-47-meditation-player" class="view">.*?</div>\s*<div id="view-48-breathing-exercise"', 
              f'<div id="view-47-meditation-player" class="view">{audio_html}</div>\n    <div id="view-48-breathing-exercise"', 
              html, flags=re.DOTALL)


# Feature: Privacy Vault
privacy_html = """
        <div class="header">
            <button class="back-btn" onclick="navigate('50-profile-settings')">←</button>
            <h2>Privacy Vault</h2>
            <div></div>
        </div>
        <div class="glass-card text-center mt-4 mb-4" style="border: 1px solid var(--primary-light);">
            <div class="logo-icon mx-auto mb-4" style="width:60px; height:60px; font-size:2rem; background: var(--primary-gradient); color:white;">🔒</div>
            <h3 class="text-primary">100% Local Processing</h3>
            <p class="text-muted mt-2">Your biometric and emotional data never leaves your device.</p>
        </div>
        
        <div class="glass-card mb-4" style="display:flex; justify-content:space-between; align-items:center; padding: 16px;">
            <div>
                <h4>Edge ML Engine</h4>
                <p class="text-muted" style="font-size:0.8rem;">Run AI models locally.</p>
            </div>
            <div style="width:44px; height:24px; background:var(--primary); border-radius:12px; position:relative;">
                <div style="width:20px; height:20px; background:white; border-radius:50%; position:absolute; top:2px; right:2px;"></div>
            </div>
        </div>
        
        <div class="glass-card mb-4" style="display:flex; justify-content:space-between; align-items:center; padding: 16px;">
            <div>
                <h4>E2E Encryption</h4>
                <p class="text-muted" style="font-size:0.8rem;">For local backup files.</p>
            </div>
            <div style="width:44px; height:24px; background:var(--primary); border-radius:12px; position:relative;">
                <div style="width:20px; height:20px; background:white; border-radius:50%; position:absolute; top:2px; right:2px;"></div>
            </div>
        </div>
        
        <button class="btn btn-danger w-100 mt-auto" onclick="alert('Local data securely wiped.')">Wipe Local Data</button>
"""
html = re.sub(r'<div id="view-49-privacy-dashboard" class="view">.*?</div>\s*<div id="view-50-profile-settings"', 
              f'<div id="view-49-privacy-dashboard" class="view">{privacy_html}</div>\n    <div id="view-50-profile-settings"', 
              html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
