/**
 * Definition for undirected graph.
 * function UndirectedGraphNode(label) {
 *     this.label = label;
 *     this.neighbors = [];   // Array of UndirectedGraphNode
 * }
 */

/**
 * @param {UndirectedGraphNode} graph
 * @return {UndirectedGraphNode}
 */
var cloneGraph = function(graph) {
    if (graph === null) { return null; }
    var h = {};
    var f = (node) => {
        if (node.label in h) { return h[node.label]; }
        var n = new UndirectedGraphNode(node.label);
        h[node.label] = n;
        node.neighbors.forEach((g) => {
            n.neighbors.push(f(g));
        });
        return n;
    };
    return f(graph);
};
