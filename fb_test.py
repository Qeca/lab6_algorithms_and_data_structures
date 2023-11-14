import unittest

from graph import Graph, T, Edge
from fb import ford_bellman


class MyTestDeep(unittest.TestCase):
    def test_ford_bellman(self):
        vertexes: list[Edge[str]] = [
            Edge("A", "B", -3),
            Edge("B", "A", 4),
            Edge("B", "C", 5),
            Edge("B", "F", 7),
            Edge("C", "E", 1),
            Edge("C", "A", 6),
            Edge("E", "B", 5),
            Edge("E", "F", 6),
            Edge("F", "A", -4),
            Edge("F", "C", 8),
            Edge("D", "A", 2),
            Edge("D", "C", -1),
            Edge("D", "E", 3),
            Edge("G", "D", 5),
            Edge("G", "E", 2),
            Edge("G", "F", 1),
        ]

        graph: Graph[str] = Graph[str](is_directed=True)

        for it in vertexes:
            graph.add_edge(it.start_edge, it.finish_edge, it.weight)

        path, cost = ford_bellman(graph, "A", "F")
        self.assertEqual(f"Path: {path} with cost: {cost}", f"Path: ['F', 'B', 'A'] with cost: 4")


if __name__ == '__main__':
    unittest.main()
