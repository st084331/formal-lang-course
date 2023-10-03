from pyformlang.regular_expression import Regex
from networkx import MultiDiGraph
from project.regular_queries.regular_queries import (
    regular_queries_for_multiple_starting_vertices,
)


def test_regular_queries_for_multiple_starting_vertices():
    graph = MultiDiGraph()
    graph.add_edges_from(
        [
            (0, 1, {"label": "a"}),
            (0, 2, {"label": "c"}),
            (0, 3, {"label": "b"}),
            (3, 4, {"label": "d"}),
        ]
    )
    regex = Regex("(a|b)d*")
    result = regular_queries_for_multiple_starting_vertices(graph, regex, {0})
    assert result == {1, 3, 4}


def test_regular_queries_for_multiple_starting_vertices_for_each():
    graph = MultiDiGraph()
    graph.add_edges_from(
        [
            (0, 1, {"label": "a"}),
            (0, 2, {"label": "b"}),
            (1, 2, {"label": "b"}),
            (2, 2, {"label": "c"}),
        ]
    )
    regex = Regex("b*")
    result = regular_queries_for_multiple_starting_vertices(
        graph, regex, {0, 1}, {2}, True
    )
    assert result == {(0, 2), (1, 2)}
