import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

chat_html = """
        <div class="header">
            <button class="back-btn" onclick="navigate('41-chat-home')">←</button>
            <h2>Chat Conversation</h2>
            <div></div>
        </div>
        
        <div class="chat-messages" style="display:flex; flex-direction:column; flex:1; gap:16px; overflow-y:auto; padding:10px 0;">
            <div class="msg msg-ai">Hello, I'm here. This is a secure, private space. How are you feeling today?</div>
        </div>
        
        <div style="display:flex; gap:10px; margin-top: auto; padding-top:10px;">
            <input type="text" class="input-field chat-input" placeholder="Type your feelings securely..." style="flex:1;">
            <button class="btn btn-primary chat-send-btn" style="width: 60px; padding: 0; display:flex; justify-content:center; align-items:center; font-size:1.5rem;">➤</button>
        </div>
"""

html = re.sub(r'<div id="view-42-chat-conversation" class="view">.*?</div>\s*<div id="view-43-suggested-replies"', 
              f'<div id="view-42-chat-conversation" class="view">{chat_html}</div>\n    <div id="view-43-suggested-replies"', 
              html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
