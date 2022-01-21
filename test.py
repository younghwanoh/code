from toposort import MyDAG
from toposort_no_cycle import MyDAG as MyDAG_
import random


# TBD
def random_dag(n_node, n_edge):
    """Generate a random DAG of n_node and n_edge."""
    graph = MyDAG({})

    for i in range(n_node):
        graph.add_node(i)

    while n_edge > 0:
        a, b = random.sample(range(0, n_node-1), 2)
        n_edge -= 1
        print(a,b)

        graph.add_edge(a, b)
        if is_acyclic(G):
            n_edge -= 1
        else:
            graph.remove_edge(a, b)
    return graph


random_dag(10, 10)
