import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [stress, setStress] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      axios.get("http://127.0.0.1:8000/stress")
        .then(res => setStress(res.data.stress_score));
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ textAlign: "center", marginTop: "100px" }}>
      <h1>NeuroSync Dashboard</h1>
      <h2>Live Cognitive Stress Score</h2>
      <div style={{
        fontSize: "50px",
        color: stress > 70 ? "red" : "green"
      }}>
        {stress}
      </div>

      {stress > 75 && (
        <h3 style={{ color: "red" }}>
          ⚠ High Stress Detected! Please Take a Break.
        </h3>
      )}
    </div>
  );
}

export default App;