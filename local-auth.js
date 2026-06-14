// NeuroWell Local Auth & Data Controller
// Replaces Firebase with local Express backend + localStorage session

const API = 'http://localhost:3000/api';

// ─── Session Helpers ───────────────────────────────────────────────────────────
function getSession() {
    const raw = localStorage.getItem('nw_user');
    return raw ? JSON.parse(raw) : null;
}
function setSession(data) {
    localStorage.setItem('nw_user', JSON.stringify(data));
}
function clearSession() {
    localStorage.removeItem('nw_user');
}

// ─── Update UI with logged-in user ────────────────────────────────────────────
function updateUIForLoggedInUser(profileData) {
    const name = profileData.fullName || profileData.name || 'User';
    const firstName = name.split(' ')[0];

    const greetingEl = document.querySelector('#view-16-dashboard-main h2');
    if (greetingEl) greetingEl.innerText = `Hello, ${firstName}`;

    const profileNameEl = document.querySelector('#view-50-profile-settings h3');
    if (profileNameEl) profileNameEl.innerText = name;

    const initials = name.split(' ').map(n => n[0]).join('').toUpperCase();
    document.querySelectorAll('.avatar').forEach(av => {
        if (av.innerText.length <= 2) av.innerText = initials;
    });
}

// ─── Init: Check Existing Session ─────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    const session = getSession();
    if (session) {
        updateUIForLoggedInUser(session);

        // If on an auth screen, redirect to dashboard
        const currentView = document.querySelector('.view.active')?.id;
        const authViews = ['view-1-splash', 'view-2-welcome', 'view-3-login', 'view-4-signup', 'view-6-forgot-password'];
        if (authViews.includes(currentView)) {
            setTimeout(() => window.navigate('16-dashboard-main'), 100);
        }
    }

    // ── 1. Sign Up ──────────────────────────────────────────────────────────────
    const signupBtn = document.getElementById('signup-btn');
    if (signupBtn) {
        signupBtn.onclick = async () => {
            const name = document.getElementById('signup-name').value.trim();
            const email = document.getElementById('signup-email').value.trim();
            const password = document.getElementById('signup-password').value;

            if (!name || !email || !password) return alert('Please fill all fields');

            signupBtn.innerText = 'Creating account...';
            signupBtn.disabled = true;

            try {
                const res = await fetch(`${API}/auth/signup`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password, name })
                });
                const data = await res.json();

                if (data.token) {
                    const user = { name, email, token: data.token, fullName: name };
                    setSession(user);
                    updateUIForLoggedInUser(user);
                    window.navigate('12-user-info');
                } else {
                    alert('Signup failed: ' + (data.error || 'Unknown error'));
                }
            } catch (e) {
                alert('Could not reach server. Make sure it is running.');
            }

            signupBtn.innerText = 'Sign Up';
            signupBtn.disabled = false;
        };
    }

    // ── 2. Login ────────────────────────────────────────────────────────────────
    const loginBtn = document.getElementById('login-btn');
    if (loginBtn) {
        loginBtn.onclick = async () => {
            const email = document.getElementById('login-email').value.trim();
            const password = document.getElementById('login-password').value;

            if (!email || !password) return alert('Please enter email and password');

            loginBtn.innerText = 'Signing in...';
            loginBtn.disabled = true;

            try {
                const res = await fetch(`${API}/auth/login`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });
                const data = await res.json();

                if (data.token) {
                    const name = email.split('@')[0];
                    const user = { name, email, token: data.token, fullName: name };
                    setSession(user);
                    updateUIForLoggedInUser(user);
                    window.navigate('16-dashboard-main');
                } else {
                    alert('Login failed: ' + (data.error || 'Invalid credentials'));
                }
            } catch (e) {
                alert('Could not reach server. Make sure it is running.');
            }

            loginBtn.innerText = 'Sign In';
            loginBtn.disabled = false;
        };
    }

    // ── 3. Logout ───────────────────────────────────────────────────────────────
    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
        logoutBtn.onclick = () => {
            clearSession();
            window.navigate('2-welcome');
        };
    }

    // ── 4. Forgot Password ──────────────────────────────────────────────────────
    const forgotBtn = document.getElementById('forgot-btn');
    if (forgotBtn) {
        forgotBtn.onclick = async () => {
            const email = document.getElementById('forgot-email').value.trim();
            if (!email) return alert('Please enter your email');

            try {
                await fetch(`${API}/auth/forgot-password`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email })
                });
            } catch (e) { /* backend may not exist, ignore */ }

            alert('If that email exists, a reset link has been sent!');
            window.navigate('3-login');
        };
    }

    // ── 5. Save Profile Info ────────────────────────────────────────────────────
    const profileSaveBtn = document.getElementById('profile-save-btn');
    if (profileSaveBtn) {
        profileSaveBtn.onclick = async () => {
            const age = document.getElementById('profile-age').value;
            const gender = document.getElementById('profile-gender').value;
            const session = getSession();
            if (!session) return alert('Please log in first');

            try {
                await fetch(`${API}/user/profile`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ userId: session.email, age, gender })
                });
            } catch (e) { /* offline — proceed anyway */ }

            setSession({ ...session, age, gender });
            window.navigate('13-questionnaire');
        };
    }

    // ── 6. Save Questionnaire ───────────────────────────────────────────────────
    const qSaveBtn = document.getElementById('q-save-btn');
    if (qSaveBtn) {
        qSaveBtn.onclick = async () => {
            const session = getSession();
            if (!session) return alert('Please log in first');

            const answers = {
                stressLevel: document.getElementById('q-stress').value,
                sleepQuality: document.getElementById('q-sleep').value,
                moodScore: document.getElementById('q-mood').value,
                anxietyLevel: document.getElementById('q-anxiety').value
            };

            try {
                await fetch(`${API}/user/questionnaire`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ userId: session.email, ...answers })
                });
            } catch (e) { /* offline — proceed anyway */ }

            window.navigate('14-goals');
        };
    }

    // ── 7. Save Goals ───────────────────────────────────────────────────────────
    const goalsSaveBtn = document.getElementById('goals-save-btn');
    if (goalsSaveBtn) {
        goalsSaveBtn.onclick = async () => {
            const session = getSession();
            if (!session) return alert('Please log in first');

            const selectedGoals = Array.from(
                document.querySelectorAll('input[name="goal"]:checked')
            ).map(cb => cb.value);

            try {
                await fetch(`${API}/user/goals`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ userId: session.email, goals: selectedGoals })
                });
            } catch (e) { /* offline — proceed anyway */ }

            window.navigate('15-notifications');
        };
    }

    // ── 8. Save Notification Prefs ──────────────────────────────────────────────
    const prefsSaveBtn = document.getElementById('prefs-save-btn');
    if (prefsSaveBtn) {
        prefsSaveBtn.onclick = async () => {
            const session = getSession();
            if (!session) return alert('Please log in first');

            const prefs = {
                dailyReminder: document.getElementById('pref-daily').checked,
                weeklyReport: document.getElementById('pref-weekly').checked,
                meditationReminder: document.getElementById('pref-meditation').checked
            };

            try {
                await fetch(`${API}/user/notifications`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ userId: session.email, ...prefs })
                });
            } catch (e) { /* offline — proceed anyway */ }

            window.navigate('16-dashboard-main');
        };
    }

    // ── 9. Save Mood Entry ──────────────────────────────────────────────────────
    const moodSaveBtn = document.getElementById('mood-save-btn');
    if (moodSaveBtn) {
        moodSaveBtn.onclick = async () => {
            const session = getSession();
            if (!session) return alert('Please log in first');

            const moodScoreEl = document.getElementById('mood-entry-score');
            const moodNotesEl = document.getElementById('mood-entry-notes');

            const moodData = {
                mood: moodScoreEl ? moodScoreEl.value : '5',
                notes: moodNotesEl ? moodNotesEl.value : '',
                date: new Date().toISOString().split('T')[0]
            };

            moodSaveBtn.innerText = 'Saving...';
            moodSaveBtn.disabled = true;

            try {
                await fetch(`${API}/user/mood`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ userId: session.email, ...moodData })
                });
                alert('Mood logged successfully!');
                window.navigate('16-dashboard-main');
            } catch (e) {
                alert('Failed to save mood. Backend may be offline.');
            }

            moodSaveBtn.innerText = 'Save Entry';
            moodSaveBtn.disabled = false;
        };
    }
});
