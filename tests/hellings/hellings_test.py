import pytest
from networkx import MultiDiGraph
from pyformlang.cfg import CFG, Variable, Production, Terminal
from project.hellings.hellings import context_free_path_query


def create_test_cfg():
    # Create a simple CFG for testing
    cfg = CFG(
        variables={Variable("S"), Variable("A")},
        terminals={Terminal("a"), Terminal("b")},
        start_symbol=Variable("S"),
        productions={
            Production(Variable("S"), [Variable("A")]),
            Production(Variable("A"), [Terminal("a")]),
        },
    )
    return cfg


def create_test_graph():
    # Create a simple MultiDiGraph for testing
    graph = MultiDiGraph()
    graph.add_edge(1, 2, label="a")
    return graph


def test_context_free_path_query_basic():
    cfg = create_test_cfg()
    graph = create_test_graph()
    result = context_free_path_query(cfg, graph)
    assert len(result) == 1  # Expecting one match
    assert (1, 2) in result  # Check the specific pair
