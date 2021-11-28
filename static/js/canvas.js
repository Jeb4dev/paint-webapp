const state = {
    disabled: false,
    tool: 'brush',
    paths: [],
    color: '#000',
    lastClick: 0,
    width: parseInt(document.getElementById('stroke-input').value),
    buffer: null,
};

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
        state.buffer.background(255);
        background(255);
    } else {
        state.tool = tool;
        updateToolButtons();
    }
}


function setup() {
    const canvas = createCanvas(800, 800);
    canvas.parent('#canvas');
    state.buffer = createGraphics(800, 800);
    state.buffer.background(255);
    state.buffer.noFill();
    background(255);
}

function draw() {
    noFill();
    background(255);

    if (state.paths.length > 0) {
        state.paths.forEach((point) => {
            const {px, py, x, y} = point;
            state.buffer.stroke(point.color);
            state.buffer.strokeWeight(point.width);
            drawShape(point.tool, px, py, x, y, state.buffer);
        });
        state.paths = [];
    }

    image(state.buffer, 0, 0, 800, 800);


    if (mouseIsPressed && focused) {
        stroke(state.color);
        strokeWeight(state.width);
        if (state.tool === 'brush' || state.tool === 'rubber') {
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
        } else {
            drawShape(state.tool, state.lastClick.x, state.lastClick.y, mouseX, mouseY, null);
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
    if (state.tool !== 'brush' && state.tool !== 'rubber') {
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
    }
}
