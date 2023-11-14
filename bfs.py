from typing import Callable
from MySet import MySet
from collections import deque
from graph import Graph, T, AdjacentEdge, Edge


def bfs(graph: Graph[T], start: T, walkfunc: Callable[[T], bool]) -> None:
    queue = deque()
    visited = MySet[T]()
    queue.append(start)

    def __foreach(edge: AdjacentEdge[T]) -> None:
        if not visited.contains(edge.finish_edge):
            queue.append(edge.finish_edge)

    while queue:
        vertex = queue.popleft()

        if walkfunc(vertex):
            return

        visited.add(vertex)

        graph.for_each_adjacent_edge(vertex, __foreach)


if __name__ == '__main__':
    ...