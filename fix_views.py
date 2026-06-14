import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Profile Settings
profile_html = """
        <div class="header"><h2>Profile & Settings</h2></div>
        <div class="glass-card text-center mb-4 mt-4">
            <div class="avatar mx-auto mb-4" style="width:80px;height:80px;font-size:2rem;">A</div>
            <h3>Alex Doe</h3>
            <p class="text-primary mt-2">Local Privacy Mode: ACTIVE</p>
        </div>
        <button class="btn btn-glass mb-4 text-left w-100" onclick="navigate('49-privacy-dashboard')">🔒 Privacy Dashboard</button>
        <button class="btn btn-glass mb-4 text-left w-100" onclick="navigate('14-goals')">🎯 Edit Goals</button>
        <button class="btn btn-glass mb-4 text-left w-100" onclick="navigate('15-notifications')">🔔 Notifications</button>
        <button class="btn btn-danger w-100 mt-8" onclick="navigate('3-login')">Log Out</button>
"""
html = re.sub(r'<div id="view-50-profile-settings" class="view">.*?</div>\s*<!-- BOTTOM NAVIGATION -->', 
              f'<div id="view-50-profile-settings" class="view">{profile_html}</div>\n    <!-- BOTTOM NAVIGATION -->', 
              html, flags=re.DOTALL)


# 2. Fix Insights Overview
insights_html = """
        <div class="header"><h2>AI Insights</h2></div>
        <div class="glass-card mb-4 mt-4">
            <h3 class="mb-2">Your Resonance</h3>
            <p class="text-muted">Your emotional intelligence summary, processed 100% locally.</p>
        </div>
        <div class="stats-grid mb-4">
            <div class="stat-item glass-card" style="margin-bottom:0;" onclick="navigate('31-weekly-trends')">
                <span class="stat-label">Weekly Trends</span>
                <span class="stat-value text-primary">View ↗</span>
            </div>
            <div class="stat-item glass-card" style="margin-bottom:0;" onclick="navigate('32-monthly-analytics')">
                <span class="stat-label">Monthly</span>
                <span class="stat-value text-primary">View ↗</span>
            </div>
        </div>
        <button class="btn btn-glass mb-4 w-100 text-left" onclick="navigate('33-stress-breakdown')">📊 Stress Breakdown</button>
        <button class="btn btn-glass mb-4 w-100 text-left" onclick="navigate('34-trigger-detection')">🔍 Trigger Detection</button>
        <button class="btn btn-primary w-100 mt-4" onclick="navigate('46-wellness-suggestions')">Explore Therapies</button>
"""
html = re.sub(r'<div id="view-29-insights-overview" class="view">.*?</div>\s*<div id="view-30-mood-report"', 
              f'<div id="view-29-insights-overview" class="view">{insights_html}</div>\n    <div id="view-30-mood-report"', 
              html, flags=re.DOTALL)


# 3. Add FaceID/Fingerprint link to Login
login_html = """
        <div class="header">
            <button class="back-btn" onclick="navigate('2-welcome')">←</button>
            <h2>Login</h2>
            <div></div>
        </div>
        <div class="glass-card mt-4" style="flex:1;">
            <input type="email" class="input-field mb-4" placeholder="Email">
            <input type="password" class="input-field mb-4" placeholder="Password">
            <button class="btn btn-primary" onclick="navigate('16-dashboard-main')">Sign In</button>
            <div class="text-center mt-8">
                <a href="#" class="text-primary" onclick="navigate('8-biometric-login'); return false;" style="text-decoration:none; font-weight:500;">Use Face ID / Fingerprint</a>
            </div>
        </div>
"""
html = re.sub(r'<div id="view-3-login" class="view">.*?</div>\s*<div id="view-4-signup"', 
              f'<div id="view-3-login" class="view">{login_html}</div>\n    <div id="view-4-signup"', 
              html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
