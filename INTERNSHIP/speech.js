export class OnionSpeech {
    constructor(config = {}) {
        this.lang = config.lang || "en-US";
        this.continuous = config.continuous || false;
        this.interimResults = config.interimResults || false;

        const SpeechRecognition = 
            window.SpeechRecognition || window.webkitSpeechRecognition;

        if (!SpeechRecognition) {
            throw new Error("Speech Recognition not supported in this browser.");
        }

        this.recognition = new SpeechRecognition();
        this.recognition.lang = this.lang;
        this.recognition.continuous = this.continuous;
        this.recognition.interimResults = this.interimResults;

        this.onresult = null;
        this.onend = null;

        this.recognition.onresult = (event) => {
            const text = event.results[0][0].transcript;
            if (this.onresult) this.onresult(text);
        };

        this.recognition.onend = () => {
            if (this.onend) this.onend();
        };
    }

    start() {
        this.recognition.start();
    }

    stop() {
        this.recognition.stop();
    }
}
