import { useEffect, useState, useRef } from "react";
import "../styles/chatbot.css";
import "bootstrap-icons/font/bootstrap-icons.css";

function Chatbot() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { from: "bot", text: "Hi there! How can I help you?" },
  ]);
  const [input, setInput] = useState("");
  const chatBodyRef = useRef(null);

  // Auto-scroll to bottom when message updates
  useEffect(() => {
    if (chatBodyRef.current) {
      chatBodyRef.current.scrollTop =
        chatBodyRef.current.scrollHeight;
    }
  }, [messages]);

  // Load annyang (speech recognition)
  useEffect(() => {
    const script = document.createElement("script");
    script.src =
      "https://cdnjs.cloudflare.com/ajax/libs/annyang/2.6.0/annyang.min.js";
    script.async = true;
    document.body.appendChild(script);

    return () => {
      document.body.removeChild(script);
    };
  }, []);

  const toggleChat = () => {
    setIsOpen((prev) => !prev);
  };

  const sendMsg = () => {
    if (!input.trim()) return;

    setMessages((prev) => [
      ...prev,
      { from: "user", text: input },
      { from: "bot", text: "I received: " + input },
    ]);

    setInput("");
  };

  const [isListening, setIsListening] = useState(false);

  const stopListening = () => {
    if (window.annyang) {
      window.annyang.abort(); // HARD STOP mic
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
    // START listening
    window.annyang.start({
      autoRestart: false,
      continuous: false,
    });

    window.annyang.removeCallback("result"); // 🔥 IMPORTANT: prevent duplicates

    window.annyang.addCallback("result", (phrases) => {
      const spokenText = phrases[0];

      // 🔥 AUTO-SEND VOICE MESSAGE
      setMessages((prev) => [
        ...prev,
        { from: "user", text: spokenText },
        { from: "bot", text: "I received: " + spokenText },
      ]);

      setInput("");
      stopListening();
    });

    setIsListening(true);
  } else {
    // STOP listening
    stopListening();
  }
};

  return (
    <>
      {/* Floating Icon */}
      <div className="chatbot-icon" onClick={toggleChat}>
        <img src="/bot.jpeg" alt="bot" />
      </div>

      {/* Chatbot Box */}
      {isOpen && (
        <div className="chatbot">
          {/* Header */}
          <div className="chat-header">
            <span>CHATBOT</span>

            <div className="header-icons">
              <i className="bi bi-x-lg header-icon" onClick={toggleChat}></i>
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

          {/* Input */}
          <div className="chat-input">
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
                <i className={`bi ${isListening ? "bi-mic-mute-fill" : "bi-mic-fill"}`}></i>
            </button>


            <button className="send-btn" onClick={sendMsg}>
              <i className="bi bi-send-fill"></i>
            </button>
          </div>
        </div>
      )}
    </>
  );
}

export default Chatbot;
