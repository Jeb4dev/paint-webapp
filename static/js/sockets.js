const socket = io();
const messageTag = document.getElementById('js-socket-message');


const chat = document.getElementById('chat-ul');
const chatInput = document.getElementById('chat-input');

const addChatItem = (username, message) => {
    const li = document.createElement('li');
    li.className = 'list-group-item disable-list';
    li.innerText = `${username}: ${message}`;
    chat.appendChild(li);
};

socket.on('chat', ({username, message, completed}) => {
    console.log(username, message, completed);
    if (!completed || (completed && gameState.completed)) {
        addChatItem(username, message, completed);
    }
});

const chatSend = () => {
    const value = chatInput.value.trim();
    if (value.length > 0) {
        chatInput.value = '';
        socket.emit('chat', value);
    }
};

const onChatKeypress = (event) => {
    if (event.key === 'Enter') {
        chatSend();
    }
};
