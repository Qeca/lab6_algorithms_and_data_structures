import math
from dataclasses import dataclass
from typing import Generic, Optional

from graph import Graph, T, Edge


@dataclass
class _Node(Generic[T]):
    cost: int
    predecessor: Optional[T]


def ford_bellman(graph: Graph[T], start: T, end: T) -> tuple[list[T], int]:
    nodes: dict[T, _Node[T]] = {}

    def foreach(vertex: T) -> None:
        nodes[vertex] = _Node[T](math.inf, None)

    graph.for_each_vertex(foreach)
    nodes[start].cost = 0

    amount_vertex = graph.amount_vertexes()

    def calc(edge: Edge[T]) -> None:
        cost = nodes[edge.start_edge].cost + edge.weight
        if cost < nodes[edge.finish_edge].cost:
            nodes[edge.finish_edge].cost = cost
            vertex = edge.start_edge
            nodes[edge.finish_edge].predecessor = vertex

    for i in range(0, amount_vertex - 1):
        graph.for_each_edge(calc)

    # проверка на наличие отрицательного цикла
    has_negative_loop = False

    def negative_search(edge: Edge[T]) -> None:
        nonlocal has_negative_loop
        if (nodes[edge.start_edge].cost + edge.weight <
                nodes[edge.finish_edge].cost):
            has_negative_loop = True
    graph.for_each_edge(negative_search)

    if has_negative_loop:
        return [], 0

    vertex: Optional[T] = end
    path: list[T] = []
    while vertex is not None:
        path.append(vertex)
        vertex = nodes[vertex].predecessor

    return path, nodes[end].cost


if __name__ == '__main__':
    ...
