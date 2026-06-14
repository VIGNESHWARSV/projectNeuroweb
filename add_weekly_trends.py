import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

weekly_trends_html = """
        <div class="header">
            <button class="back-btn" onclick="navigate('29-insights-overview')">←</button>
            <h2>Weekly Trends</h2>
            <div></div>
        </div>
        
        <div class="glass-card mb-4" style="padding: 24px 16px;">
            <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:16px;">
                <div>
                    <p class="text-muted" style="font-size:0.85rem;">Avg Resonance</p>
                    <h2 class="text-primary" style="font-size:2.5rem;">78 <span style="font-size:1rem; color:var(--primary-light);">+5%</span></h2>
                </div>
                <div style="text-align:right;">
                    <p class="text-muted" style="font-size:0.85rem;">Highest</p>
                    <p class="text-accent" style="font-weight:600;">Thursday</p>
                </div>
            </div>
            
            <!-- CSS Bar Chart -->
            <div style="display:flex; justify-content:space-between; align-items:flex-end; height:150px; margin-top:30px; gap:8px;">
                <!-- Mon -->
                <div style="display:flex; flex-direction:column; align-items:center; flex:1;">
                    <div style="width:100%; height:60px; background:rgba(107, 142, 130, 0.4); border-radius:6px; transition:0.3s;"></div>
                    <p class="text-muted mt-2" style="font-size:0.75rem;">M</p>
                </div>
                <!-- Tue -->
                <div style="display:flex; flex-direction:column; align-items:center; flex:1;">
                    <div style="width:100%; height:80px; background:rgba(107, 142, 130, 0.6); border-radius:6px; transition:0.3s;"></div>
                    <p class="text-muted mt-2" style="font-size:0.75rem;">T</p>
                </div>
                <!-- Wed -->
                <div style="display:flex; flex-direction:column; align-items:center; flex:1;">
                    <div style="width:100%; height:45px; background:rgba(216, 159, 122, 0.7); border-radius:6px; transition:0.3s;"></div>
                    <p class="text-muted mt-2" style="font-size:0.75rem;">W</p>
                </div>
                <!-- Thu -->
                <div style="display:flex; flex-direction:column; align-items:center; flex:1;">
                    <div style="width:100%; height:120px; background:var(--primary-gradient); border-radius:6px; transition:0.3s; box-shadow:0 4px 10px rgba(107, 142, 130, 0.3);"></div>
                    <p class="text-primary mt-2" style="font-size:0.75rem; font-weight:600;">T</p>
                </div>
                <!-- Fri -->
                <div style="display:flex; flex-direction:column; align-items:center; flex:1;">
                    <div style="width:100%; height:90px; background:rgba(107, 142, 130, 0.6); border-radius:6px; transition:0.3s;"></div>
                    <p class="text-muted mt-2" style="font-size:0.75rem;">F</p>
                </div>
                <!-- Sat -->
                <div style="display:flex; flex-direction:column; align-items:center; flex:1;">
                    <div style="width:100%; height:100px; background:rgba(107, 142, 130, 0.7); border-radius:6px; transition:0.3s;"></div>
                    <p class="text-muted mt-2" style="font-size:0.75rem;">S</p>
                </div>
                <!-- Sun -->
                <div style="display:flex; flex-direction:column; align-items:center; flex:1;">
                    <div style="width:100%; height:85px; background:rgba(107, 142, 130, 0.5); border-radius:6px; transition:0.3s;"></div>
                    <p class="text-muted mt-2" style="font-size:0.75rem;">S</p>
                </div>
            </div>
        </div>
        
        <div class="glass-card mb-4" style="padding: 16px;">
            <h4 class="mb-2" style="font-size:0.95rem;">Key Insights</h4>
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-muted); margin-top: 12px; border-bottom:1px solid rgba(0,0,0,0.05); padding-bottom:8px;">
                <span>Deep Sleep Correlation</span>
                <span class="text-primary" style="font-weight:500;">High Impact (+12%)</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-muted); margin-top: 10px;">
                <span>Social Activity Impact</span>
                <span class="text-accent" style="font-weight:500;">Draining (-4%)</span>
            </div>
        </div>
"""
html = re.sub(r'<div id="view-31-weekly-trends" class="view">.*?</div>\s*<div id="view-32-monthly-analytics"', 
              f'<div id="view-31-weekly-trends" class="view">{weekly_trends_html}</div>\n    <div id="view-32-monthly-analytics"', 
              html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
