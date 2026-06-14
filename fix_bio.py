import re

# 1. Fix index.html view-21-emotion-home
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

emotion_home = """
        <div class="header"><h2>Analyze State</h2></div>
        <p class="text-muted mb-4">Choose a method to gently analyze your current resonance.</p>
        
        <div class="glass-card mb-4" onclick="navigate('27-behavior-tracking'); setupCamera()" style="cursor:pointer;">
            <h3>👁️ Optical-Respiratory Scan <span class="badge" style="background:var(--accent); color:white; font-size:0.6rem; vertical-align:middle;">FACE ID</span></h3>
            <p class="text-muted mt-2" style="font-size:0.85rem;">Tracks pupil dilation and chest micro-movements to detect hidden stress.</p>
        </div>
        
        <div class="glass-card mb-4" onclick="navigate('22-voice-input'); setupVoice()" style="cursor:pointer;">
            <h3>🎤 Acoustic Biomarkers <span class="badge" style="background:var(--secondary); color:white; font-size:0.6rem; vertical-align:middle;">VOICE</span></h3>
            <p class="text-muted mt-2" style="font-size:0.85rem;">Analyzes vocal cord tension and cadence patterns.</p>
        </div>
        
        <div class="glass-card" onclick="navigate('8-biometric-login'); setupFingerprint()" style="cursor:pointer;">
            <h3>👆 Fingerprint Sensor <span class="badge" style="background:var(--primary); color:white; font-size:0.6rem; vertical-align:middle;">TOUCH</span></h3>
            <p class="text-muted mt-2" style="font-size:0.85rem;">Simulates WebAuthn native hardware verification for stress tracking.</p>
        </div>
"""

html = re.sub(r'<div id="view-21-emotion-home" class="view">.*?</div>\s*<div id="view-22-voice-input"', 
              f'<div id="view-21-emotion-home" class="view">{emotion_home}</div>\n    <div id="view-22-voice-input"', 
              html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Fix app.js fingerprint logic
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

new_fp_logic = """
// 1. Fingerprint (WebAuthn Mock)
window.setupFingerprint = function() {
    const fpBtn = document.getElementById('fingerprint-btn');
    if(fpBtn) {
        // Remove old listeners by cloning
        const newBtn = fpBtn.cloneNode(true);
        fpBtn.parentNode.replaceChild(newBtn, fpBtn);
        
        const status = document.getElementById('webauthn-status');
        status.innerText = 'Tap the icon to authenticate securely via WebAuthn.';
        status.className = 'text-muted mt-4';
        
        newBtn.addEventListener('click', async () => {
            status.innerText = 'Scanning...';
            status.className = 'text-accent mt-4';
            try {
                // Mocking native prompt delay
                await new Promise(r => setTimeout(r, 1000));
                
                const res = await fetch('http://localhost:3000/api/auth/webauthn/verify', { method: 'POST' });
                const data = await res.json();
                
                status.innerText = data.message;
                status.className = 'text-primary mt-4';
                setTimeout(() => navigate('29-insights-overview'), 1500); // Go to insights instead of dashboard
            } catch(e) {
                status.innerText = 'Failed to connect to backend.';
                status.className = 'text-danger mt-4';
            }
        });
    }
};

// Also attach on load just in case they come from Login screen
document.addEventListener('DOMContentLoaded', () => {
    // We can just rely on onclick="navigate('8-biometric-login'); setupFingerprint()" in html.
    // For login screen we can inject it.
});
"""

# Replace old fingerprint logic block
app_js = re.sub(r'// 1\. Fingerprint \(WebAuthn Mock\).*?// 2\. Voice Recognition \(Web Speech API\)', 
                f'{new_fp_logic}\n// 2. Voice Recognition (Web Speech API)', 
                app_js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

