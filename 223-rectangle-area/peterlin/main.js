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
var computeArea = function(A, B, C, D, E, F, G, H) {
    var width = Math.max(0, Math.min(C, G) - Math.max(A, E));
    var height = Math.max(0, Math.min(D, H) - Math.max(B, F));
    return (C-A)*(D-B) + (G-E)*(H-F) - width * height;
};
