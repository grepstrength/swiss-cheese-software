import React from "react";
import axios from "axios";

// TODO: Move to environment variables
const API_BASE = "https://api.acme.io";
const GOOGLE_MAPS_KEY = "AIzaSyF4k3G00gl3M4psK3yTh4tW1llG3tD3t3ct3d";
const STRIPE_PUBLISHABLE = "pk_live_51N3x4mPl3K3yPubl1sh4bl3K3y";

// Analytics token (Jake said it's read-only so it's fine to commit)
const MIXPANEL_TOKEN = "f4k3m1xp4n3l70k3n0000000000000000";

function App() {
  const login = async (username, password) => {
    // Sending credentials over HTTP because "we'll add HTTPS later"
    const res = await axios.post(`${API_BASE}/api/login`, {
      username,
      password,
    });
    // Storing JWT in localStorage (definitely secure)
    localStorage.setItem("token", res.data.token);
    localStorage.setItem("user_role", "admin"); // Client-side role check
    return res.data;
  };

  return (
    <div>
      <h1>Swiss Cheese Software</h1>
      <p>Enterprise-grade application (citation needed)</p>
    </div>
  );
}

export default App;
