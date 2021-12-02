const socket = io();
const drawUi = document.getElementById('draw-ui');
const messageTag = document.getElementById('js-socket-message');
const toolBar = document.getElementById('tool-bar');

const gameState = {
    state: 'WAIT_FOR_START',
    isDrawer: false,
    word: '',
    completed: false
};

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

socket.on('state_changed', (newState) => {
    if (newState !== gameState.state) {
        state.disabled = true;
        toolBar.hidden = true;
        if (newState === 'WAIT_FOR_START') {
            messageTag.innerText = 'Waiting players for start';
            drawUi.hidden = true;
        } else {
            console.log('draw');
            messageTag.innerText = '';
            drawUi.hidden = false;
        }
        gameState.state = newState;
        gameState.isDrawer = false;
        gameState.word = '';
        gameState.completed = false;
    }
});

socket.on('set_word', (word) => {
    console.log('drawer', word);
    gameState.isDrawer = true;
    gameState.word = word;
    messageTag.innerText = `Draw: ${word}`;
    gameState.completed = true;
    state.disabled = false;
    toolBar.hidden = false;
});

socket.on('user_completed', (word) => {
    if (!gameState.completed) {
        gameState.completed = true;
        gameState.word = word;
        messageTag.innerText = `You guessed the word: ${gameState.word}`;
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
