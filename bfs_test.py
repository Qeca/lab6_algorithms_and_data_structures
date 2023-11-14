import unittest
from bfs import Edge, Graph, bfs

class MyTestCase(unittest.TestCase):
    def test_something(self):
        vertexes: list[Edge[str]] = [
            Edge("A", "B"),
            Edge("A", "C"),
            Edge("C", "F"),
            Edge("C", "G"),
            Edge("G", "M"),
            Edge("G", "N"),
            Edge("B", "D"),
            Edge("B", "E"),
            Edge("D", "H"),
            Edge("D", "I"),
            Edge("D", "J"),
            Edge("E", "K"),
            Edge("E", "L"),
        ]

        graph: Graph[str] = Graph[str]()

        for it in vertexes:
            graph.add_edge_without_weight(it.start_edge, it.finish_edge)

        def bsf_walk(vertex: str) -> bool:
            print(vertex + " ", end='')
            return vertex == "K"

        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        sys.stdout = StringIO()

        bfs(graph, "A", bsf_walk)
        printed_output = sys.stdout.getvalue()

        sys.stdout = saved_stdout
        self.assertEqual(printed_output, "A B C D E F G H I J K ")


if __name__ == '__main__':
    unittest.main()
