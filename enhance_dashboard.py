import re

# 1. Update index.html view-16-dashboard-main
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

dashboard_html = """
        <div class="header">
            <div>
                <h2>Hello, Alex</h2>
                <p class="text-muted" id="greeting-subtext">A calm afternoon awaits.</p>
            </div>
            <div class="avatar" onclick="navigate('50-profile-settings')">A</div>
        </div>
        
        <div class="glass-card text-center mb-4" style="position:relative; overflow:hidden; padding-top:30px; padding-bottom:30px;">
            <div class="bg-pulse"></div>
            <h3 class="mb-2" style="position:relative; z-index:2;">Resonance Score</h3>
            <div class="mood-score text-gradient mb-2" id="dash-score" style="font-size: 4.5rem; font-weight: 300; position:relative; z-index:2; line-height:1.1;">--</div>
            <p class="text-primary" id="dash-state" style="font-weight: 500; position:relative; z-index:2; letter-spacing:1px; margin-top:8px;">ANALYZING...</p>
            <p class="text-muted mt-2" id="dash-vagus" style="font-size: 0.8rem; position:relative; z-index:2;">Syncing with biometric sensors.</p>
        </div>
        
        <h4 class="mb-2 mt-4" style="font-size: 0.9rem; color:var(--text-muted); font-weight:500;">Quick Interventions</h4>
        <div style="display:flex; gap:12px; margin-bottom:24px; overflow-x:auto; padding-bottom:8px; scrollbar-width: none;">
            <div class="quick-action-pill" onclick="navigate('48-breathing-exercise')">🌬️ Breathe</div>
            <div class="quick-action-pill" onclick="navigate('47-meditation-player')">🎵 432Hz</div>
            <div class="quick-action-pill" onclick="navigate('42-chat-conversation')">💬 Talk</div>
            <div class="quick-action-pill" onclick="navigate('37-add-mood')">📝 Log</div>
        </div>
        
        <div class="glass-card mb-4" style="padding: 16px;">
            <h4 class="mb-2" style="font-size:0.95rem;">✦ Subconscious Sync</h4>
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-muted); margin-top: 12px;">
                <span>Pupil Dilation Variance</span>
                <span class="text-accent" id="dash-pupil" style="font-weight:500;">--</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-muted); margin-top: 10px;">
                <span>Micro-Respiration</span>
                <span class="text-primary" id="dash-resp" style="font-weight:500;">--</span>
            </div>
        </div>
        
        <div class="glass-card mb-4" style="padding: 16px;">
            <h4 class="mb-2" style="font-size:0.95rem;">🌤️ Environmental Engine</h4>
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-muted); margin-top: 12px;">
                <span>Ambient Noise Stress</span>
                <span class="text-primary" id="dash-noise" style="font-weight:500;">--</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-muted); margin-top: 10px;">
                <span>Barometric Pressure Drop</span>
                <span class="text-accent" id="dash-pressure" style="font-weight:500;">--</span>
            </div>
        </div>
"""
html = re.sub(r'<div id="view-16-dashboard-main" class="view">.*?</div>\s*<div id="view-17-dashboard-positive"', 
              f'<div id="view-16-dashboard-main" class="view">{dashboard_html}</div>\n    <div id="view-17-dashboard-positive"', 
              html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css
with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* Dashboard specific styles */
.bg-pulse {
    position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
    width: 140px; height: 140px; background: radial-gradient(circle, rgba(107, 142, 130, 0.15) 0%, rgba(107, 142, 130, 0) 70%);
    border-radius: 50%; z-index: 1; animation: scorePulse 3s infinite alternate ease-in-out;
}
@keyframes scorePulse { 0% { transform: translate(-50%, -50%) scale(1); } 100% { transform: translate(-50%, -50%) scale(1.4); } }

.quick-action-pill {
    background: var(--glass-bg); border: 1px solid var(--glass-border); border-top: 1px solid rgba(255,255,255,0.8);
    padding: 10px 18px; border-radius: 20px; font-size: 0.85rem; font-weight: 500; color: var(--text-main);
    white-space: nowrap; cursor: pointer; backdrop-filter: blur(8px); box-shadow: 0 4px 10px rgba(0,0,0,0.02);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.quick-action-pill:active { transform: scale(0.92); background: rgba(255,255,255,0.9); }
""")

# 3. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

backend_fetch_logic = """
// Dashboard Backend Fetch
window.fetchDashboardMetrics = async function() {
    try {
        const res = await fetch('http://localhost:3000/api/dashboard/metrics');
        const data = await res.json();
        
        // Animate Score
        const scoreEl = document.getElementById('dash-score');
        let current = 0;
        const target = data.resonanceScore || 84;
        const interval = setInterval(() => {
            current += 2;
            if (current >= target) {
                current = target;
                clearInterval(interval);
            }
            if (scoreEl) scoreEl.innerText = current;
        }, 20);

        // Update Text Fields
        document.getElementById('dash-state').innerText = data.state || 'BALANCED & PRESENT';
        document.getElementById('dash-vagus').innerText = 'Vagus nerve tone is ' + (data.vagusNerveTone || 'optimal') + '.';
        document.getElementById('dash-pupil').innerText = data.subconsciousSync?.pupilDilationVariance || 'Stable (1.2mm)';
        document.getElementById('dash-resp').innerText = data.subconsciousSync?.microRespiration || '14 bpm';
        document.getElementById('dash-noise').innerText = data.environmentalEngine?.ambientNoiseStress || 'Low (40dB)';
        document.getElementById('dash-pressure').innerText = data.environmentalEngine?.barometricPressure || 'Stable';
        
    } catch(e) {
        console.error("Backend fetch failed", e);
        document.getElementById('dash-score').innerText = '84'; // Fallback
        document.getElementById('dash-state').innerText = 'BALANCED & PRESENT';
        document.getElementById('dash-vagus').innerText = 'Vagus nerve tone is optimal. (Offline mode)';
    }
};

"""

# Hook into window.navigate
app_js = app_js.replace("if(target) target.classList.add('active');", """if(target) target.classList.add('active');
    
    // Trigger dashboard fetch
    if(targetId === '16-dashboard-main') {
        if(window.fetchDashboardMetrics) window.fetchDashboardMetrics();
    }
""")

# Append fetch logic to the end of file
app_js += "\n" + backend_fetch_logic

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

