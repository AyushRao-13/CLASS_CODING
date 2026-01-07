const express = require("express");
const cors = require("cors");
const { exec } = require("child_process");

const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

/* ================= SAFE COMMAND MAPS ================= */

// Linux commands (WSL)
const linuxCommands = {
  "run linux forensic capture": {
    type: "script",
    command: "/home/ayush/forensic_scripts/capture.sh",
  },
};

// Windows (PowerShell) commands
const windowsCommands = {
  "run forensic capture": "E:\\forensic_scripts\\capture.ps1",
};

/* ================= HELPER FUNCTION ================= */

function runCommand(os, command, callback) {
  if (os === "windows") {
    exec(
      `powershell.exe -NoProfile -ExecutionPolicy Bypass -File "${command}"`,
      {
        timeout: 0,
        maxBuffer: 1024 * 1024 * 20,
      },
      callback
    );
  } else {
    // Linux via WSL (non-blocking)
    exec(
      `"C:\\Windows\\System32\\wsl.exe" bash -lc "bash /home/ayush/forensic_scripts/capture.sh> /tmp/linux_forensic.log 2>&1"`,
      { timeout: 0 },
      () => {
        callback(
          null,
          "✅ Linux forensic capture started.\n📁 Output: C:\\forensics\\linux",
          ""
        );
      }
    );
  }
}

/* ================= CHAT API ================= */

app.post("/api/chat", (req, res) => {
  const { message, os } = req.body;

  if (!message || !os) {
    return res.status(400).json({
      reply: "❌ message and os are required",
    });
  }

  const text = message.toLowerCase().trim();

  /* ---------- NORMAL CHAT ---------- */

  if (text.includes("hello")) {
    return res.json({ reply: "Hello! How can I assist you?" });
  }

  if (text.includes("time")) {
    return res.json({
      reply: "🕒 Server time: " + new Date().toLocaleTimeString(),
    });
  }

  if (text.includes("help")) {
    return res.json({
      reply:
        "Try:\n- run forensic capture (Windows)\n- run linux forensic capture (Linux)",
    });
  }

  /* ---------- COMMAND MATCHING ---------- */

  let command = null;

  if (os === "windows") {
    const key = Object.keys(windowsCommands).find((k) =>
      text.includes(k)
    );
    command = key ? windowsCommands[key] : null;
  } else {
    const key = Object.keys(linuxCommands).find((k) =>
      text.includes(k)
    );
    command = key ? linuxCommands[key].command : null;
  }

  if (!command) {
    return res.json({
      reply: "❌ Command not allowed or not recognized.",
    });
  }

  /* ---------- EXECUTION ---------- */

  runCommand(os, command, (error, stdout, stderr) => {
    if (error) {
      return res.json({
        reply: `❌ Error:\n${stderr || error.message}`,
      });
    }

    res.json({
      reply:
        stdout?.trim() ||
        "✅ Forensic capture triggered successfully.",
    });
  });
});

/* ================= START SERVER ================= */

app.listen(PORT, () => {
  console.log(`🚀 Backend running at http://localhost:${PORT}`);
});