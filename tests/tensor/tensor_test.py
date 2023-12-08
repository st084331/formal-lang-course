import pytest
from networkx import MultiDiGraph
from pyformlang.cfg import CFG, Variable
from project.tensor.tensor import specific_reachability


def create_graph(edges):
    graph = MultiDiGraph()
    for u, v, label in edges:
        graph.add_edge(u, v, label=label)
    return graph


def create_cfg(productions):
    cfg_text = "\n".join(productions)
    return CFG.from_text(cfg_text)


def test_basic_reachability():
    graph = create_graph([(0, 1, "a"), (1, 2, "b")])

    cfg = create_cfg(["S -> a B", "B -> b"])

    start_nodes = {0}
    final_nodes = {2}
    start_symbol = Variable("S")

    result = specific_reachability(graph, cfg, start_nodes, final_nodes, start_symbol)
    assert {(0, "S", 2)} == result


def test_no_reachability():
    graph = create_graph([(0, 1, "a"), (1, 2, "c")])
    cfg = create_cfg(["S -> a B", "B -> b"])
    start_nodes = {0}
    final_nodes = {2}
    start_symbol = Variable("S")

    result = specific_reachability(graph, cfg, start_nodes, final_nodes, start_symbol)
    assert result == set()


def test_multiple_reachability():
    graph = create_graph([(0, 1, "a"), (1, 2, "b"), (2, 3, "a"), (3, 4, "b")])
    cfg = create_cfg(["S -> a B", "B -> b"])
    start_nodes = {0, 2}
    final_nodes = {2, 4}
    start_symbol = Variable("S")

    result = specific_reachability(graph, cfg, start_nodes, final_nodes, start_symbol)
    assert {(0, "S", 2), (2, "S", 4)} == result
