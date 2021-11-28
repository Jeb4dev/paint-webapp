const state = {
    disabled: false,
    tool: 'brush',
    paths: [],
    color: '#000',
    lastClick: 0,
    width: parseInt(document.getElementById('stroke-input').value)
};

const getRectCenter = (px, py, x, y) => {
    const w = x - px;
    const h = y - py;

    return {
        x: px + w / 2,
        y: py + h / 2,
        w,
        h,
    };
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
        state.paths = [];
        background(255);
    } else {
        state.tool = tool;
        updateToolButtons();
    }
}

const drawShape = (shape, px, py, x, y) => {
    const drawFunctions = {
        rect: drawRect,
        circle: drawEllipse,
        triangle: drawTriangle,
        line: drawLine
    };
    drawFunctions[shape](px, py, x, y);
}

const drawRect = (px, py, x, y) => {
    rect(
        px, py,
        x - px,
        y - py
    );
};

const drawEllipse = (px, py, x, y) => {
    const center = getRectCenter(px, py, x, y);
    ellipse(
        center.x,
        center.y,
        center.w,
        center.h
    );
};

const drawLine = (px, py, x, y) => {
    line(px, py, x, y);
}

const drawTriangle = (px, py, x, y) => {
    const center = getRectCenter(px, py, x, y);
    triangle(
        px, y,
        px + center.w / 2, py,
        x, y
    );
}


function setup() {
    const canvas = createCanvas(800, 800);
    canvas.parent('#canvas');
    background(255);
}

function draw() {
    noFill();
    background(255);

    state.paths.forEach((point) => {
        const {px, py, x, y} = point;
        stroke(point.color);
        strokeWeight(point.width);
        if (point.tool === 'brush' || point.tool === 'rubber') {
            line(point.px, point.py, point.x, point.y);
        } else {
            drawShape(point.tool, px, py, x, y);
        }
    });

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
            drawShape(state.tool, state.lastClick.x, state.lastClick.y, mouseX, mouseY);
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
