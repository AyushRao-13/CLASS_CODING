import { useEffect, useState, useRef } from "react";
import "../styles/chatbot.css";
import "bootstrap-icons/font/bootstrap-icons.css";

function Chatbot() {
  /* ---------------- STATE ---------------- */
  const [isOpen, setIsOpen] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [messages, setMessages] = useState([
    { from: "bot", text: "Hi there! How can I help you?" },
  ]);
  const [input, setInput] = useState("");
  const [isListening, setIsListening] = useState(false);
  const [os, setOs] = useState("linux");

  const chatBodyRef = useRef(null);

  /* ---------------- EFFECTS ---------------- */

  // Auto-scroll messages
  useEffect(() => {
    if (chatBodyRef.current) {
      chatBodyRef.current.scrollTop = chatBodyRef.current.scrollHeight;
    }
  }, [messages]);

  // Load annyang
  useEffect(() => {
    const script = document.createElement("script");
    script.src =
      "https://cdnjs.cloudflare.com/ajax/libs/annyang/2.6.0/annyang.min.js";
    script.async = true;
    document.body.appendChild(script);

    return () => document.body.removeChild(script);
  }, []);

  /* ---------------- CHAT FUNCTIONS ---------------- */

  const toggleChat = () => {
    setIsOpen((prev) => !prev);
    setIsFullscreen(false); // reset fullscreen on close
  };

  const toggleFullscreen = () => {
    setIsFullscreen((prev) => !prev);
  };

  const sendMsg = async (textFromVoice = null) => {
    const msg = textFromVoice ?? input;
    if (!msg.trim()) return;

    setMessages((prev) => [...prev, { from: "user", text: msg }]);
    setInput("");

    try {
      const res = await fetch("http://localhost:5000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message: msg.toLowerCase(),
          os: os,
        }),
      });

      const data = await res.json();

      setMessages((prev) => [
        ...prev,
        { from: "bot", text: data.reply },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        { from: "bot", text: "⚠️ Backend not reachable." },
      ]);
    }
  };

  /* ---------------- MIC FUNCTIONS ---------------- */

  const stopListening = () => {
    if (window.annyang) {
      window.annyang.abort();
      window.annyang.removeCallback("result");
    }
    setIsListening(false);
  };

  const toggleListening = () => {
    if (!window.annyang) {
      alert("Speech recognition not supported");
      return;
    }

    if (!isListening) {
      window.annyang.start({ autoRestart: false, continuous: false });
      window.annyang.removeCallback("result");

      window.annyang.addCallback("result", (phrases) => {
        sendMsg(phrases[0]);
        stopListening();
      });

      setIsListening(true);
    } else {
      stopListening();
    }
  };

  /* ---------------- UI ---------------- */

  return (
    <>
      {/* Floating icon */}
      <div className="chatbot-icon" onClick={toggleChat}>
        <img src="/bot.jpeg" alt="bot" />
      </div>

      {isOpen && (
        <div className={`chatbot ${isFullscreen ? "fullscreen" : ""}`}>
          {/* Header */}
          <div className="chat-header">
            <span>CHATBOT</span>

            <div className="header-icons">
              <i
                className={`bi ${
                  isFullscreen
                    ? "bi-fullscreen-exit"
                    : "bi-arrows-fullscreen"
                } header-icon`}
                title="Toggle fullscreen"
                onClick={toggleFullscreen}
              ></i>

              <i
                className="bi bi-x-lg header-icon"
                title="Close"
                onClick={toggleChat}
              ></i>
            </div>
          </div>

          {/* Messages */}
          <div className="chat-body" ref={chatBodyRef}>
            {messages.map((msg, index) => (
              <div
                key={index}
                className={
                  msg.from === "bot" ? "bot-message" : "user-message"
                }
              >
                {msg.text}
              </div>
            ))}
          </div>

          {/* Input bar */}
          <div className="chat-input">
            <select
              value={os}
              onChange={(e) => setOs(e.target.value)}
              className="os-select"
            >
              <option value="linux">Linux</option>
              <option value="windows">Windows</option>
            </select>

            <input
              type="text"
              placeholder="Ask Chatbot..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMsg()}
            />

            <button
              className={`mic-btn ${isListening ? "listening" : ""}`}
              onClick={toggleListening}
            >
              <i
                className={`bi ${
                  isListening ? "bi-mic-mute-fill" : "bi-mic-fill"
                }`}
              ></i>
            </button>

            <button className="send-btn" onClick={() => sendMsg()}>
              <i className="bi bi-send-fill"></i>
            </button>
          </div>
        </div>
      )}
    </>
  );
}

export default Chatbot;
