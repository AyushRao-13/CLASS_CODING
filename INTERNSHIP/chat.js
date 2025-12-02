function toggleChat() {
    const box = document.getElementById("c1");
    box.style.display = (box.style.display === "flex") ? "none" : "flex";
}

let listening = false;

const recognizer = new OnionSpeech({
    lang: "en-US",
    continuous: false,
    interimResults: false
});

function startListening() {
    const micBtn = document.querySelector(".mic-btn");

    if (!listening) {
        listening = true;
        micBtn.classList.add("listening");
        recognizer.start();

        recognizer.onresult = (text) => {
            document.getElementById("userInput").value = text;
            sendMsg();
        };

        recognizer.onend = () => {
            listening = false;
            micBtn.classList.remove("listening");
        };

    } else {
        recognizer.stop();
        listening = false;
        micBtn.classList.remove("listening");
    }
}

function sendMsg() {
    const input = document.getElementById("userInput");
    const body = document.getElementById("chatBody");

    const text = input.value.trim();
    if (!text) return;

    body.innerHTML += `<div class='user-message'>${text}</div>`;
    input.value = "";
    body.scrollTop = body.scrollHeight;

    setTimeout(() => {
        body.innerHTML += `<div class='bot-message'>You said: "${text}" 🙂</div>`;
        body.scrollTop = body.scrollHeight;
    }, 600);
}