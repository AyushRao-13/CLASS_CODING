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

function startListening() {
    const micBtn = document.querySelector(".mic-btn");
    const micIcon = document.getElementById("micIcon");

    micBtn.classList.add("listening");
   

    annyang.start();

    annyang.addCallback("result", (phrases) => {
        document.getElementById("userInput").value = phrases[0];
        sendMsg();
    });

    annyang.addCallback("end", () => {
        micBtn.classList.remove("listening");
       
    });
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
