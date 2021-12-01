const socket = io();

socket.on('get_paths', (data) => {
    console.log(data)
    state.paths = [...state.paths, ...data];
});

socket.on('add_paths', (data) => {
    state.paths = [...state.paths, ...data];
});

socket.on('clear', () => {
    state.clear();
});

socket.on('undo', () => {
    if (state.paths > 0) {
        state.undo();
    } else {
        state.clear();
        socket.emit('get_paths');
    }
});

const chat = document.getElementById('chat-ul');
const chatInput = document.getElementById('chat-input');

const addChatItem = (username, message) => {
    const li = document.createElement('li');
    li.className = 'list-group-item disable-list';
    li.innerText = `${username}: ${message}`;
    chat.appendChild(li);
};

socket.on('chat', ({username, message}) => {
    console.log(username, message);
    addChatItem(username, message);
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
