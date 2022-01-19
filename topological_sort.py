g = {
5: [11],
7: [11,8],
3: [8,10],
11:[2,9,10],
8: [9],
2: [],
9: [],
10: []
}

from collections import Counter

class tsorter:
    def __init__(self, graph):
        self.graph = graph
        self.count = Counter(sum([ v for v in graph.values() ], []))
        for key in g.keys():
            if not key in self.count:
                self.count[key] = 0

    def add_edge(self, start, end):
        if not start in self.graph:
            self.graph[start] = [end]
            self.count[start] += 1
        else:
            if end in self.graph[start]:
                print("Edge already exists")
                return
            self.graph[start] += [end]
        self.count[end] += 1

    def remove_edge(self, start, end):
        if start in self.graph:
            self.graph[start].remove(end)
            self.count[end] -= 1
            assert self.count.values() >= 0

    def pprint(self):
        print("# Debug DAGs ========= ")
        for i,v in self.graph.items():
            print("{:3} -> {}".format(i, v))

    def inbounded(self):
        return filter(lambda x: self.count[x] == 0, dict(self.count))

    def topological_sort(self):
        sorted_list = []
        for start in self.inbounded():
            sorted_list.append(start)
            for end in self.graph[start]:
                self.remove_edge(start, end)

            if self.count[start] == 0:
                del self.graph[start]
            if self.count[end] == 0:
                del self.graph[end]
            
        return

sg = tsorter(g)
sg.pprint()
sg.remove_edge(11,2)
sg.add_edge(110,2)
print(sg.inbounded())
print(sg.count)
sg.pprint()
