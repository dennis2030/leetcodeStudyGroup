class Solution(object):
	def canFinish(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""

		visited = [0 for i in xrange(numCourses)]
		edges = [[] for i in xrange(numCourses)]
		for p in prerequisites:
			edges[p[0]].append(p[1])

		def DFS(node):
			if visited[node] == -1:
				return False
			if visited[node] == 1:
				return True

			visited[node] = -1
			for next_node in edges[node]:
				if False == DFS(next_node):
					return False

			visited[node] = 1
			return True

		for i in xrange(numCourses):
			if False == DFS(i):
				return False

		return True
