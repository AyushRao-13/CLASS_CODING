function toggleChat() {
    const box = document.getElementById("c1");
    box.style.display = (box.style.display === "flex") ? "none" : "flex";
}

const fullscreenBtn = document.getElementById("fullscreenBtn");
const chatbox = document.getElementById("c1");

fullscreenBtn.addEventListener("click", () => {
    chatbox.classList.toggle("fullscreen");

    if (chatbox.classList.contains("fullscreen")) {
        fullscreenBtn.classList.remove("bi-arrows-fullscreen");
        fullscreenBtn.classList.add("bi-fullscreen-exit");
    } else {
        fullscreenBtn.classList.remove("bi-fullscreen-exit");
        fullscreenBtn.classList.add("bi-arrows-fullscreen");
    }
});


let commandExecuted = true;

if (annyang) {

    var commands = {
        'show me *tag': function(tag) {
            document.getElementById("userInput").value = "Show me " + tag;
            sendMsg();
        },

        'calculate :month stats': function(month) {
            document.getElementById("userInput").value = "Calculate " + month + " stats";
            sendMsg();
        },

        'say hello (to my little) friend': function() {
            document.getElementById("userInput").value = "Hello friend";
            sendMsg();
        },

        'clear chat': function () {
            commandExecuted = true;
            document.getElementById("chatBody").innerHTML = "";
        },
    };

    annyang.addCommands(commands);
    annyang.setLanguage("en-US");
}

annyang.addCallback("result", function (phrases) {

    if (commandExecuted) {
        commandExecuted = false;
        return;
    }

    document.getElementById("userInput").value = phrases[0];
    sendMsg();
});

annyang.addCallback("end", function () {
    isListening = false;
    document.querySelector(".mic-btn").classList.remove("listening");
});

let isListening = false;

function startListening() {
    const micBtn = document.querySelector(".mic-btn");

    if (isListening) {
        annyang.abort();
        isListening = false;
        micBtn.classList.remove("listening");
        return;
    }

    isListening = true;
    micBtn.classList.add("listening");

    annyang.start({ autoRestart: false, continuous: true });
}

async function sendToFlask(text) {
    try {
        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();
        return data.reply;
    } catch (error) {
        return "⚠️ Error connecting to server.";
    }
}

// 🔐 Trigger forensic scripts via backend (Node / Flask gateway)
async function runForensics(os = "windows") {
    const body = document.getElementById("chatBody");

    body.innerHTML += `<div class='bot-message'>🕵️ Starting forensic capture (${os})...</div>`;
    body.scrollTop = body.scrollHeight;

    try {
        const res = await fetch("http://127.0.0.1:3000/run-forensics", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ os })
        });

        const data = await res.json();

        body.innerHTML += `<div class='bot-message'>✅ ${data.message}</div>`;
    } catch (err) {
        body.innerHTML += `<div class='bot-message'>⚠️ Failed to start forensic capture</div>`;
    }

    body.scrollTop = body.scrollHeight;
}


async function sendMsg() {
    const input = document.getElementById("userInput");
    const body = document.getElementById("chatBody");

    const text = input.value.trim();
    if (!text) return;

    body.innerHTML += `<div class='user-message'>${text}</div>`;
    input.value = "";
    body.scrollTop = body.scrollHeight;

    const reply = await sendToFlask(text);

    setTimeout(() => {
        body.innerHTML += `<div class='bot-message'>${reply}</div>`;
        body.scrollTop = body.scrollHeight;
    }, 400);
}
