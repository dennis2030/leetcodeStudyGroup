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
    let map = {};
    function getCloneNode(n) {
        if (map[n.label]) return map[n.label];
        let node = new UndirectedGraphNode(n.label);
        map[n.label] = node;
        node.neighbors = n.neighbors.map((m) => getCloneNode(m));
        return node;
    }
    return graph && getCloneNode(graph);
};
