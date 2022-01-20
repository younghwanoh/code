from collections import Counter
import sys

class MyDAG:
    def __init__(self, graph):
        self.graph = graph
        self.n_income = Counter(sum([ v for v in graph.values() ], []))
        # Count the number of incoming edges (parents)
        for key in self.graph.keys():
            if not key in self.n_income:
                self.n_income[key] = 0

    def add_edge(self, start, end):
        """
        Add edge from start node -> end node
        """
        if not start in self.graph:
            self.graph[start] = [end]
            self.n_income[start] += 1
        else:
            if end in self.graph[start]:
                print("Edge already exists, ignore add_edge {}->{}".format(start, end))
                return
            self.graph[start] += [end]
        self.n_income[end] += 1

    def remove_edge(self, start, end):
        """
        Remove edge (If node without edges, remove the node)
        """
        if start in self.graph:
            self.graph[start].remove(end)
            self.n_income[end] -= 1
            assert all([i >=0 for i in self.n_income.values()])

            # Remove node without any edges
            if self.n_income[start] == 0 and len(self.graph[start]) == 0:
                del self.graph[start]
                del self.n_income[start]
        else:
            print("Tried to remove edge w/o the starting node")

    def pprint(self):
        print("# Debug DAGs ========= ")
        for i,v in self.graph.items():
            print("{:3} -> {}".format(i, v))

    def nodes_wo_incoming_edges(self):
        """
        Find nodes with no inbound edges
        """
        return filter(lambda x: self.n_income[x] == 0, self.n_income)

def topological_sort(g):
    sorted_list = []
    queue = list(g.nodes_wo_incoming_edges())
    while queue: 
        start = queue.pop(0)
        sorted_list.append(start)
        target = list(g.graph[start])
        for end in target:
            g.remove_edge(start, end)
            # g.pprint()
            # Update node set wihout incoming edges
            if g.n_income[end] == 0:
                queue.append(end)

    return sorted_list



if __name__ == "__main__":
    test_graph1 = {
        5:  [11],
        7:  [11,8],
        3:  [8,10],
        11: [2,9,10],
        8:  [9],
        2:  [],
        9:  [],
        10: []
    }


    dag = MyDAG(test_graph1)
    dag.pprint()

    print(topological_sort(dag))


