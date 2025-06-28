document.getElementById('chat-form').addEventListener('submit', async function (e) {
  e.preventDefault();
  const input = document.getElementById('user-input');
  const message = input.value.trim();
  if (!message) return;

  appendMessage('user', message);
  input.value = '';

const response = await fetch('https://adxania-chatbot.onrender.com/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({ message, tone: "professional" })
  });

  const data = await response.json();
  appendMessage('bot', data.response);
});

function appendMessage(sender, text) {
  const msg = document.createElement('div');
  msg.className = `chat-message ${sender}`;
  msg.textContent = text;
  document.getElementById('chat-box').appendChild(msg);
  document.getElementById('chat-box').scrollTop = document.getElementById('chat-box').scrollHeight;
}
