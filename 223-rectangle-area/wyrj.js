/**
 * @param {number} A
 * @param {number} B
 * @param {number} C
 * @param {number} D
 * @param {number} E
 * @param {number} F
 * @param {number} G
 * @param {number} H
 * @return {number}
 */
function Coord(x, y) {
    this.x = x;
    this.y = y;
}
Coord.prototype = {
    isBottomLeftOf(c) {
        return this.x < c.x && this.y < c.y;
    },
};
function Rectangle(left, bottom, right, top) {
    this.bl = new Coord(left, bottom);
    this.tr = new Coord(right, top);
}
Rectangle.prototype = {
    getArea: function() {
        return (this.tr.x - this.bl.x) * (this.tr.y - this.bl.y);
    },
    getOverlap: function(r) {
        if (!this.bl.isBottomLeftOf(r.tr) || !r.bl.isBottomLeftOf(this.tr)) {
            return null;
        }
        return new Rectangle(Math.max(this.bl.x, r.bl.x),
                            Math.max(this.bl.y, r.bl.y),
                            Math.min(this.tr.x, r.tr.x),
                            Math.min(this.tr.y, r.tr.y));
    },
};
var computeArea = function(A, B, C, D, E, F, G, H) {
    var r1 = new Rectangle(A, B, C, D);
    var r2 = new Rectangle(E, F, G, H);
    var o = r1.getOverlap(r2);
    return r1.getArea() + r2.getArea() - (o ? o.getArea() : 0);
};