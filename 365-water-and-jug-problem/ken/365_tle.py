class Solution(object):
	def canMeasureWater(self, x, y, z):
		"""
		:type x: int
		:type y: int
		:type z: int
		:rtype: bool
		"""

		max_x = x
		max_y = y

		init_state = (0, 0)
		visited_states = set()

		def PourX2Y(state):
			x = state[0]
			y = state[1]
			pour = min(x, max_y - y)
			x -= pour
			y += pour
			return (x, y)
		def PourY2X(state):
			x = state[0]
			y = state[1]
			pour = min(max_x - x, y)
			x += pour
			y -= pour
			return (x, y)

		def GenAllState(state):
			all_states = set()

			fill_x = (max_x, state[1])
			fill_y = (state[0], max_y)
			empty_x = (0, state[1])
			empty_y = (state[0], 0)
			pour_x_to_y = PourX2Y(state)
			pour_y_to_x = PourY2X(state)

			all_states.add(fill_x)
			all_states.add(fill_y)
			all_states.add(empty_x)
			all_states.add(empty_y)
			all_states.add(pour_x_to_y)
			all_states.add(pour_y_to_x)

			all_states.remove(state)

			return all_states


		def Found(state):
			return state[0] == z or state[1] == z or state[0] + state[1] == z

		def DFS(state):
			if Found(state):
				return True

			if state in visited_states:
				return False

			visited_states.add(state)

			all_states = GenAllState(state)

			for state in all_states:
				if DFS(state):
					return True

			return False

		def BFS(state):
			not_visited = set()
			not_visited.add(state)

			while len(not_visited):
				state = not_visited.pop()
				if Found(state):
					return True
				if state in visited_states:
					continue

				visited_states.add(state)
				not_visited |= GenAllState(state) - visited_states

			return False

		return BFS((x, y))

a = Solution()
# print a.canMeasureWater(3,5,4)
# print a.canMeasureWater(2,6,5)
# print a.canMeasureWater(1,2,3)
# print a.canMeasureWater(22003, 31237, 1)