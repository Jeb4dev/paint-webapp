const SIZE = [720, 640];

let canvas = null;
const state = {
    disabled: false,
    tool: 'brush',
    paths: [],
    color: document.getElementById('color-input').value,
    lastClick: 0,
    width: parseInt(document.getElementById('stroke-input').value),
    buffer: null,

    clear() {
        state.buffer.background(255);
        background(255);
        state.paths = [];
    },

    undo() {
        state.paths = state.paths.slice(0, -1);
    }
};

const hueb = new Huebee('.color-input', {
    notation: 'hex',

});

hueb.on('change', (color) => {
    state.color = color;
});

const toolButtons = document.getElementsByClassName('paint-tool');
const updateToolButtons = () => {
    Array.from(toolButtons).forEach((button) => {
        button.className = button.className.replace('btn-dark', 'btn-outline-dark');
        const dataTool = button.attributes.getNamedItem('data-tool');
        if (!state.disabled && dataTool !== null && dataTool.value === state.tool) {
            button.className = button.className.replace('btn-outline-dark', 'btn-dark');
        }
    });

};

updateToolButtons();

const limitStroke = (element, event) => {
    if (event.key.length === 1) {
        const re = /\d+/g;
        if (event.key.match(re) === null) {
            event.preventDefault();
        }
    }
};

const isSocket = () => typeof socket !== 'undefined';
const checkCoord = (x, y) => x >= 0 && y >= 0 && x <= SIZE[0] && y <= SIZE[1];
const checkLastClick = () => checkCoord(state.lastClick.x, state.lastClick.y);

const postImage = () => {
    const imgInput = document.getElementById('image-input');
    imgInput.value = state.buffer.elt.toDataURL();
}

const changeStroke = (element) => {
    let value = parseInt(element.value);
    const max = parseInt(element.max);
    const min = parseInt(element.min);

    if (value > max || value < min) {
        value = max;
    }

    element.value = value;
    state.width = value;
};

function changeTool(element) {
    const tool = element.attributes['data-tool'].value;
    if (tool === 'clear') {
        if (isSocket()) {
            socket.emit('clear');
        }
        state.clear();
    } else if (tool === 'download') {
        saveCanvas(canvas, `image-${Math.ceil(new Date() / 1000)}`, 'png');
    } else if (tool === 'undo') {
        if (isSocket()) {
            socket.emit('undo');
        } else {
            state.undo();
        }
    } else {
        state.tool = tool;
        updateToolButtons();
    }
}


function setup() {
    canvas = createCanvas(SIZE[0], SIZE[1]);
    canvas.parent('#canvas');
    state.buffer = createGraphics(SIZE[0], SIZE[1]);
    state.buffer.background(255);
    state.buffer.noFill();
    background(255);
}

function draw() {
    noFill();
    background(255);

    if (state.paths.length > 10) {
        state.paths.slice(0, -10).forEach((point) => {
            const {px, py, x, y} = point;
            state.buffer.stroke(point.color);
            state.buffer.strokeWeight(point.width);
            drawShape(point.tool, px, py, x, y, state.buffer);
        });
        state.paths = state.paths.slice(-10);
    }

    image(state.buffer, 0, 0, SIZE[0], SIZE[1]);


    state.paths.slice(-10).forEach((point) => {
        const {px, py, x, y} = point;
        stroke(point.color);
        strokeWeight(point.width);
        drawShape(point.tool, px, py, x, y, null);
    });


    if (mouseIsPressed && focused) {
        stroke(state.color);
        strokeWeight(state.width);
        if (state.tool === 'brush' || state.tool === 'rubber') {
            if (checkCoord(pmouseX, pmouseY) && checkCoord(mouseX, mouseY)) {
                const point = {
                    px: pmouseX,
                    py: pmouseY,
                    x: mouseX,
                    y: mouseY,
                    color: state.tool === 'rubber' ? '#fff' : state.color,
                    width: state.width,
                    tool: state.tool
                };
                state.paths.push(point);
                if (isSocket()) {
                    socket.emit('add_paths', [point]);
                }

            }
        } else {
            if (checkLastClick()) {
                drawShape(state.tool, state.lastClick.x, state.lastClick.y, mouseX, mouseY, null);
            }
        }
    }
}

function mousePressed() {
    state.lastClick = {
        x: mouseX,
        y: mouseY
    };
}

function mouseReleased() {
    if (state.tool !== 'brush' && state.tool !== 'rubber' && checkLastClick()) {
        const point = {
            px: state.lastClick.x,
            py: state.lastClick.y,
            x: mouseX,
            y: mouseY,
            color: state.tool === 'rubber' ? '#fff' : state.color,
            width: state.width,
            tool: state.tool
        };
        state.paths.push(point);
        if (isSocket()) {
            socket.emit('add_paths', [point]);
        }
    }
}
