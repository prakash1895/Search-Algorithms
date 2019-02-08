from collections import defaultdict
import sys

class Graph:
	def __init__(self, filename, start='S', goal='G'):

		self.start = start
		self.goal = goal
		edges, heuristic = self.read_txt(filename)
		self.heuristic = heuristic
		self.graph_dict = defaultdict(list)
		self.generate_graph(edges)
		self.L = 2

	def read_txt(self, filename):
		lines = [line.rstrip('\n') for line in open(filename)]
		hash_idx = lines.index('#####')
		end_idx = lines.index('')

		edges = []
		for edge_line in lines[0:hash_idx]:
			words = edge_line.split()
			tup = (words[0], words[1], float(words[2]))
			edges.append(tup)

		heuristic = {}
		heuristic[self.goal] = 0.0
		for heuristic_line in lines[hash_idx+1:end_idx]:
			words = heuristic_line.split()
			heuristic[words[0]] = float(words[1])
		return edges, heuristic

	def generate_graph(self, edges):
		for (n1, n2, weight) in edges:
			self.graph_dict[n1].append((weight, n2))
			self.graph_dict[n2].append((weight, n1))

	def expand_node(self, node):
		return self.graph_dict[node]

	def is_loop(self, queue_str):
		sort_str = sorted(queue_str)
		n = len(sort_str) - 1
		for i in range(n):
			if sort_str[i] == sort_str[i+1]:
				return True
		return False

	def handle_DFS(self, queue_list, front, current_node): # Depth First Search
		children = sorted([child_node[1] for child_node in self.expand_node(current_node)])
		for child_node in children[::-1]:
			new_queue = (0.00, child_node + front[1])
			if self.is_loop(child_node+front[1]) == False:
				queue_list.insert(0, new_queue)
		return queue_list
	
	def handle_BFS(self, queue_list, front, current_node): # Breadth First Search
		children = sorted([child_node[1] for child_node in self.expand_node(current_node)])
		for child_node in children:
			new_queue = (0.00, child_node + front[1])
			if self.is_loop(child_node+front[1]) == False:
				queue_list.append(new_queue)
		return queue_list

	def handle_depth_limited(self, queue_list, front, current_node): # Depth Limted Search
		children = sorted([child_node[1] for child_node in self.expand_node(current_node)])
		if len(front[1]) > (self.L):
			return queue_list

		else:
			for child_node in children[::-1]:
				new_queue = (0.00, child_node + front[1])
				if self.is_loop(child_node+front[1]) == False:
					queue_list.insert(0, new_queue)
		return queue_list
						
	def handle_depth_iterative(self): # Iterative Deepening Search
		max_depth = len(self.graph_dict.keys())
		for i in range(max_depth):
			print "\n L = {}".format(i)
			self.L = i
			if self.General_Search('depth_limited', 'uninformed') == True:
				break

	def handle_uniform_cost(self, queue_list, front, current_node):
		children = sorted([child_node for child_node in self.expand_node(current_node)])
		for child_node in children:
			new_cost = child_node[0] + front[0]
			new_path = child_node[1] + front[1]
			new_queue = (new_cost, new_path)
			if self.is_loop(new_path) == False:
				queue_list.append(new_queue)
		queue_list.sort()
		for i in range(len(queue_list)-1):
			if queue_list[i][0] == queue_list[i+1][0] and queue_list[i][1][0] == queue_list[i+1][1][0] and len(queue_list[i+1][1]) < len(queue_list[i][1]):
				queue_list[i], queue_list[i+1] = queue_list[i+1], queue_list[i]
		return queue_list

	def handle_greedy(self, queue_list, front, current_node):
		children = sorted([child_node for child_node in self.expand_node(current_node)])
		for child_node in children:
			new_heuristic = self.heuristic[child_node[1]] 
			new_path = child_node[1] + front[1]
			new_queue = (new_heuristic, new_path)
			if self.is_loop(new_path) == False:
				queue_list.append(new_queue)
		queue_list.sort()
		for i in range(len(queue_list)-1):
			if queue_list[i][0] == queue_list[i+1][0] and queue_list[i][1][0] == queue_list[i+1][1][0] and len(queue_list[i+1][1]) < len(queue_list[i][1]):
				queue_list[i], queue_list[i+1] = queue_list[i+1], queue_list[i]
		return queue_list

	def handle_astar(self, queue_list, front, current_node):
		children = sorted([child_node for child_node in self.expand_node(current_node)])
		for child_node in children:
			new_cost = round(child_node[0] + front[0] + self.heuristic[child_node[1]] - self.heuristic[front[1][0]], 2)
			new_path = child_node[1] + front[1]
			new_queue = (new_cost, new_path)
			if self.is_loop(new_path) == False:
				flag = 2
				for i in range(len(queue_list)):
					if new_path[0] == queue_list[i][1][0]:
						if new_cost >= queue_list[i][0]:
							flag = 0
						else:
							flag = 1
							idx = i
				if flag == 1:
					queue_list.pop(idx)
					queue_list.append(new_queue)
				elif flag == 2:
					queue_list.append(new_queue)
		queue_list.sort()
		return queue_list

	def handle_beam(self, queue_list, front, current_node):
		children = sorted([child_node[1] for child_node in self.expand_node(current_node)])

		for child_node in children:
			new_heuristic = self.heuristic[child_node] 
			new_path = child_node + front[1]
			new_queue = (new_heuristic, new_path)
			if self.is_loop(new_path) == False:
				queue_list.append(new_queue)

		if len(queue_list) > 2:
			if len(queue_list[0][1]) == len(queue_list[1][1]):
				(m1, m2) = sorted((queue_list.index(sorted(queue_list)[0]), queue_list.index(sorted(queue_list)[1])))
				queue_list = [queue_list[m1], queue_list[m2]]
		return queue_list

	def handle_hillclimbing(self, queue_list, front, current_node):
		children = sorted([(self.heuristic[child_node[1]], child_node[1]) for child_node in self.expand_node(current_node)])
		best_child = children[0]

		if best_child == None:
			queue_list = []

		else:
			new_heuristic = self.heuristic[best_child[1]] 
			new_path = best_child[1] + front[1]
			new_queue = (new_heuristic, new_path)
			if self.is_loop(new_path) == False:
				queue_list.append(new_queue)
		return queue_list

	def print_expansion(self, search_type, queue_list):
		if search_type == 'uninformed':
			print "    ", queue_list[0][1][0], " \t", [x[1] for x in queue_list]

		else:
			print "    ", queue_list[0][1][0], " \t", queue_list

	def General_Search(self, search_method, search_type):
		if search_type == 'heuristic':
			initial_cost = self.heuristic[self.start]
		else:
			initial_cost = 0.00

		print " Expanded\tQueue "
		queue_list = [(initial_cost, self.start)]

		while len(queue_list) != 0:
			self.print_expansion(search_type, queue_list)
			front = queue_list.pop(0)
			current_node = front[1][0]

			if current_node == self.goal:
				print " Goal Reached!"
				print " Goal Path: ", front[1][::-1]
				print ""
				return True

			if search_method == 'depth_first':
				queue_list = self.handle_DFS(queue_list, front, current_node)

			elif search_method == 'breadth_first':
				queue_list = self.handle_BFS(queue_list, front, current_node)

			elif search_method == 'depth_limited':
				queue_list = self.handle_depth_limited(queue_list, front, current_node)

			elif search_method == 'uniform_cost':
				queue_list = self.handle_uniform_cost(queue_list, front, current_node)

			elif search_method == 'greedy':
				queue_list = self.handle_greedy(queue_list, front, current_node)

			elif search_method == 'astar':
				queue_list = self.handle_astar(queue_list, front, current_node)

			elif search_method == 'beam':
				queue_list = self.handle_beam(queue_list, front, current_node)

			elif search_method == 'hillclimbing':
				queue_list = self.handle_hillclimbing(queue_list, front, current_node)

		print " Failure to find path between S and G"
		return False

if __name__ == '__main__':
	
	filename = sys.argv[1]
	search_type = sys.argv[2]

	graph_obj = Graph(filename)
	
	if search_type == 'depth_first':
		print "\n Depth 1st Search \n"
		graph_obj.General_Search('depth_first', 'uninformed')
		
	elif search_type == 'breadth_first':
		print "\n Breadth 1st Search \n"
		graph_obj.General_Search('breadth_first', 'uninformed')
		
	elif search_type == 'depth_limited':
		print "\n Depth-Limted Search (Depth Limit = 2) \n"
		graph_obj.General_Search('depth_limited', 'uninformed')

	elif search_type == 'depth_iterative':
		print "\n Iterative Deepening Search"
		graph_obj.handle_depth_iterative() # Calls General_Search('depth_limited') iteratively

	elif search_type == 'uniform_cost':
		print "\n Uniform Cost Search \n"
		graph_obj.General_Search('uniform_cost', 'informed')
		
	elif search_type == 'greedy':
		print "\n Greedy Search \n"
		graph_obj.General_Search('greedy', 'heuristic')
		
	elif search_type == 'astar':
		print "\n A* Search \n"
		graph_obj.General_Search('astar', 'heuristic')

	elif search_type == 'beam':
		print "\n Beam Search (w = 2)\n"
		graph_obj.General_Search('beam', 'heuristic')

	elif search_type == 'hillclimbing':
		print "\n HillClimbing Search \n"
		graph_obj.General_Search('hillclimbing', 'heuristic')
		
	elif search_type == 'ALL':
		print "\n (1) Depth 1st Search \n"
		graph_obj.General_Search('depth_first', 'uninformed')
		print "\n (2) Breadth 1st Search \n"
		graph_obj.General_Search('breadth_first', 'uninformed')
		print "\n (3) Depth-Limted Search (Depth Limit = 2) \n"
		graph_obj.General_Search('depth_limited', 'uninformed')
		print "\n (4) Iterative Deepening Search"
		graph_obj.handle_depth_iterative()
		print "\n (5) Uniform Cost Search \n"
		graph_obj.General_Search('uniform_cost', 'informed')
		print "\n (6) Greedy Search \n"
		graph_obj.General_Search('greedy', 'heuristic')
		print "\n (7) A* Search \n"
		graph_obj.General_Search('astar', 'heuristic')
		print "\n (8) Beam Search (w = 2)\n"
		graph_obj.General_Search('beam', 'heuristic')
		print "\n (9) HillClimbing Search \n"
		graph_obj.General_Search('hillclimbing', 'heuristic')
		
	else:
		print "Invalid Choice!"
		print "Check the keyword and try again!"
		print ""




