const socket = io();

socket.on('connect', () => {
});

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
