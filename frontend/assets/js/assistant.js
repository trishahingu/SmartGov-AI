const sendBtn = document.getElementById("sendBtn");
const chatBody = document.getElementById("chatBody");
const userMessage = document.getElementById("userMessage");

sendBtn.addEventListener("click", sendMessage);

function sendMessage() {

const message = userMessage.value.trim();

if(message==="") return;

chatBody.innerHTML += `

<div class="user-message">

${message}

</div>

`;

userMessage.value="";

setTimeout(()=>{

chatBody.innerHTML += `

<div class="bot-message">

Thank you.

This AI Assistant will be connected to the backend API in the next step.

</div>

`;

chatBody.scrollTop=chatBody.scrollHeight;

},700);

}