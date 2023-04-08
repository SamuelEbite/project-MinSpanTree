from typing import Dict, List, Tuple


def prims_algorithm(graph: Dict[Tuple[str, str], int]) -> Dict[Tuple[str, str], int]:
    """Return the minimum spanning tree of a weighted undirected graph."""
    nodes = set(sum(graph.keys(), ()))
    visited_nodes = set()
    start_node = next(iter(nodes))
    visited_nodes.add(start_node)
    tree = {}
    while len(visited_nodes) < len(nodes):
        min_edge = None
        for edge in graph:
            if edge[0] in visited_nodes and edge[1] not in visited_nodes:
                if min_edge is None or graph[edge] < graph[min_edge]:
                    min_edge = edge
            elif edge[1] in visited_nodes and edge[0] not in visited_nodes:
                if min_edge is None or graph[edge] < graph[min_edge]:
                    min_edge = edge[::-1]
        tree[min_edge] = graph[min_edge]
        visited_nodes.add(min_edge[1])
    return tree


def read_graph() -> Dict[Tuple[str, str], int]:
    """Read a weighted undirected graph from standard input."""
    graph = {}
    while True:
        try:
            nodes = input("Enter the nodes of an edge (or press enter to stop): ")
            if not nodes:
                break
            node1, node2 = nodes.split()
            weight = int(input("Enter the weight of the edge: "))
            graph[(node1, node2)] = weight
            graph[(node2, node1)] = weight
        except ValueError:
            print("Invalid input!")
    return graph


def start() -> None:
    """Starts the minimum spanning tree program."""
    graph = read_graph()
    solution = prims_algorithm(graph)
    print("--------------------------")
    print("The minimum spanning tree edges are:", end=" ")
    cost = 0
    for edge in solution:
        cost += solution[edge]
        print(edge, end=" ")
    print()
    print("Total cost:", cost)


def main() -> None:
    """Prints the menu and prompts user input."""
    print("Menu:")
    print("1. Read graph from standard input")
    print("2. Start program")
    print("3. Exit")
    while True:
        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                graph = read_graph()
                tree = prims_algorithm(graph)
                print("The minimum spanning tree of the graph is:")
                for edge, weight in tree.items():
                    print(f"{edge[0]} -- {edge[1]} : {weight}")
                total_weight = sum(tree.values())
                print(f"Total weight: {total_weight}")
            elif choice == 2:
                start()
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input!")


if __name__ == '__main__':
    main()
