graph = {
5: [11],
7: [11,8],
3: [8,10],
11:[2,9,10],
8: [9],
2: [],
9: [],
10: []
}

def add_edge(graph, node, link):
    if not node in graph:
        graph[node] = [link]
    else:
        graph[node] += [link]

def remove_edge(graph, node, link):
    if node in graph:
        graph[node].remove(link)
        nnode, nlink = True, True
        for v,w in graph.items():
            if node in w:
                nnode = False
            if link in w:
                nlink = False

        if nnode and not graph[node]:
            del graph[node]
 
        if nlink and not graph[link]:
            del graph[link]
    
# remove_edge(graph, 11,2)
print(graph)
# remove_edge(graph, 8,9)
remove_edge(graph, 11,2)
# add_edge(graph, 20,9)
print(graph)
