import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Patch Biometric Login
bio_login = """
        <div class="header">
            <button class="back-btn" onclick="navigate('3-login')">←</button>
            <h2>Biometric Login</h2>
            <div></div>
        </div>
        <div class="glass-card text-center mt-4" style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center;">
            <div id="fingerprint-btn" class="logo-icon mx-auto mb-4" style="font-size:3rem; cursor:pointer; filter:none; opacity:1; width:100px; height:100px;">👆</div>
            <h3>Fingerprint / Face ID</h3>
            <p class="text-muted mt-4" id="webauthn-status">Tap the icon to authenticate securely via WebAuthn.</p>
        </div>
"""
html = re.sub(r'<div id="view-8-biometric-login" class="view">.*?</div>\s*<div id="view-9-onboarding-1"', 
              f'<div id="view-8-biometric-login" class="view">{bio_login}</div>\n    <div id="view-9-onboarding-1"', 
              html, flags=re.DOTALL)

# 2. Patch Voice Input
voice_input = """
        <div class="header">
            <button class="back-btn" onclick="navigate('21-emotion-home')">←</button>
            <h2>Voice Recognition</h2>
            <div></div>
        </div>
        <div class="glass-card text-center mt-4" style="flex:1; display:flex; flex-direction:column; justify-content:center;">
            <div class="mic-btn mx-auto mb-4" id="voice-record-btn" style="filter:none; opacity:1;">🎤</div>
            <p class="text-muted" id="voice-status">Tap to start recording.</p>
            <div id="voice-transcript" class="mt-4 text-primary" style="min-height: 40px; font-style: italic;"></div>
        </div>
"""
html = re.sub(r'<div id="view-22-voice-input" class="view">.*?</div>\s*<div id="view-23-voice-recording"', 
              f'<div id="view-22-voice-input" class="view">{voice_input}</div>\n    <div id="view-23-voice-recording"', 
              html, flags=re.DOTALL)

# 3. Patch Face Scan (Using Behavior Tracking view)
face_input = """
        <div class="header">
            <button class="back-btn" onclick="navigate('21-emotion-home')">←</button>
            <h2>Face Recognition</h2>
            <div></div>
        </div>
        <div class="glass-card text-center mt-4" style="flex:1; display:flex; flex-direction:column; align-items:center;">
            <video id="face-video" autoplay playsinline style="width:100%; border-radius:16px; background:#000; height: 300px; object-fit: cover;"></video>
            <canvas id="face-canvas" style="display:none;"></canvas>
            <button class="btn btn-primary mt-4" id="capture-face-btn">Capture & Analyze</button>
            <p class="text-muted mt-4" id="face-status">Waiting to start camera...</p>
        </div>
"""
html = re.sub(r'<div id="view-27-behavior-tracking" class="view">.*?</div>\s*<div id="view-28-combined-analysis"', 
              f'<div id="view-27-behavior-tracking" class="view">{face_input}</div>\n    <div id="view-28-combined-analysis"', 
              html, flags=re.DOTALL)

# 4. Link it correctly in emotion home
html = html.replace("navigate('22-voice-input')", "navigate('22-voice-input'); setupVoice()")
html = html.replace("navigate('27-behavior-tracking')", "navigate('27-behavior-tracking'); setupCamera()")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
