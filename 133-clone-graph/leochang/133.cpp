/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
public:
	UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
		if (node == NULL) return node;

		if (hashMap.find(node) != hashMap.end()) {
			return hashMap[node];
		}

		UndirectedGraphNode *newNode = new UndirectedGraphNode(node->label);
		hashMap.insert(pair<UndirectedGraphNode*, UndirectedGraphNode*>(node, newNode));
		for (UndirectedGraphNode* neigh : node->neighbors) {
			hashMap[node]->neighbors.push_back(cloneGraph(neigh));
		}

		return hashMap[node];
	}
private:
	unordered_map<UndirectedGraphNode*, UndirectedGraphNode*> hashMap;
};
