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

const drawShape = (shape, px, py, x, y, buffer = null) => {
    const drawFunctions = {
        rect: drawRect,
        circle: drawEllipse,
        triangle: drawTriangle,
        line: drawLine,
        brush: drawLine,
        rubber: drawLine
    };
    drawFunctions[shape](px, py, x, y, buffer);
};

const drawRect = (px, py, x, y, buffer = null) => {
    (buffer || window).rect(
        px, py,
        x - px,
        y - py
    );
};

const drawEllipse = (px, py, x, y, buffer = null) => {
    const center = getRectCenter(px, py, x, y);
    (buffer || window).ellipse(
        center.x,
        center.y,
        center.w,
        center.h
    );
};

const drawLine = (px, py, x, y, buffer = null) => {
    (buffer || window).line(px, py, x, y);
};

const drawTriangle = (px, py, x, y, buffer = null) => {
    const center = getRectCenter(px, py, x, y);
    (buffer || window).triangle(
        px, y,
        px + center.w / 2, py,
        x, y
    );
};

const doFill = (needFill, color, buffer = null) => {
    if (needFill) {
        (buffer || window).fill(color);
    } else {
        (buffer || window).noFill();
    }
}
