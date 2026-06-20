import { initializeApp } from "https://www.gstatic.com/firebasejs/9.22.1/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/9.22.1/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/9.22.1/firebase-firestore.js";

// Fetch Firebase configuration dynamically from backend to avoid hardcoding secrets
let firebaseConfig;
try {
    const res = await fetch("http://localhost:3000/api/config/firebase");
    firebaseConfig = await res.json();
} catch (e) {
    console.warn("Could not fetch Firebase config from backend. Make sure backend is running.");
    // Fallback for demonstration if backend is down
    firebaseConfig = {
        apiKey: "MISSING_API_KEY",
        authDomain: "neurowellai-49389.firebaseapp.com",
        projectId: "neurowellai-49389"
    };
}

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firebase services
export { firebaseConfig };
export const auth = getAuth(app);
export const db = getFirestore(app);

// In production, add Firebase App Check here to restrict API key usage.
