const sendBtn = document.getElementById("sendBtn");
const userMessage = document.getElementById("userMessage");
const chatBody = document.getElementById("chatBody");
const typing = document.getElementById("typing");

sendBtn.addEventListener("click", sendMessage);

userMessage.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});

function addUserMessage(message) {

    const html = `
        <div class="user-message">
            <div class="message-head">
                👤 You
            </div>

            <div class="message-text">
                ${message}
            </div>
        </div>
    `;

    chatBody.insertAdjacentHTML("beforeend", html);

    scrollBottom();
}

function addBotMessage(message) {

    const html = `
        <div class="bot-message">

            <div class="message-head">
                🤖 SmartGov AI
            </div>

            <div class="message-text">
                ${message}
            </div>

        </div>
    `;

    chatBody.insertAdjacentHTML("beforeend", html);

    scrollBottom();
}

function scrollBottom() {

    chatBody.scrollTop = chatBody.scrollHeight;

}

async function sendMessage() {

    const message = userMessage.value.trim();

    if (message === "") return;

    addUserMessage(message);

    userMessage.value = "";

    typing.classList.remove("d-none");

    scrollBottom();

    try {

        const response = await fetch("http://127.0.0.1:8000/api/chat", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                message: message

            })

        });

        const data = await response.json();

        typing.classList.add("d-none");

        if (data.success) {

            addBotMessage(data.reply);

        } else {

            addBotMessage("❌ " + data.reply);

        }

    }
    catch (error) {

        typing.classList.add("d-none");

        addBotMessage("⚠ Unable to connect to SmartGov AI Server.");

        console.error(error);

    }

}

setTimeout(() => {

    scrollBottom();

}, 500);