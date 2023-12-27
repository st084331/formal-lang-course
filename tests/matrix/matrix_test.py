from networkx import MultiDiGraph
from pyformlang.cfg import CFG, Variable

from project.matrix.matrix import find_pairs_matching_grammar


def build_graph(nodes, edges):
    graph = MultiDiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


def test_empty_graph():
    graph = build_graph(
        {},
        [],
    )

    cfg = CFG.from_text(
        """
                        S -> A B C
                        A -> a
                        B -> b
                        C -> c
                         """
    )
    res = find_pairs_matching_grammar(cfg, graph, {0}, {1})

    assert res == set()


def test_empty_grammar():
    graph = build_graph(
        {0, 1, 2, 3},
        [
            (0, 1, {"label": "a"}),
            (1, 2, {"label": "b"}),
            (2, 3, {"label": "c"}),
        ],
    )

    cfg = CFG.from_text("")
    res = find_pairs_matching_grammar(cfg, graph, {0}, {3})

    assert res == set()


def test_simple_path():
    graph = build_graph(
        {0, 1, 2, 3},
        [
            (0, 1, {"label": "a"}),
            (1, 2, {"label": "b"}),
            (2, 3, {"label": "c"}),
            (3, 0, {"label": "a"}),
        ],
    )

    cfg = CFG.from_text(
        """
                        S -> A B C
                        A -> a
                        B -> b
                        C -> c
                         """
    )
    res = find_pairs_matching_grammar(cfg, graph, {0}, {3})

    assert res == {(0, 3)}


def test_another_start_symbol():
    graph = build_graph(
        {0, 1, 2, 3},
        [
            (0, 1, {"label": "a"}),
            (1, 2, {"label": "a"}),
            (2, 3, {"label": "a"}),
        ],
    )

    cfg = CFG.from_text(
        """
                        S -> A
                        A -> a | a S
                        """
    )
    res = find_pairs_matching_grammar(
        cfg, graph, {0, 1, 2, 3}, {0, 1, 2, 3}, Variable("A")
    )
    assert res == set()

    cfg = CFG.from_text(
        """
                        A -> S
                        S -> a | a A
                        """
    )
    res = find_pairs_matching_grammar(
        cfg, graph, {0, 1, 2, 3}, {0, 1, 2, 3}, Variable("A")
    )
    assert res == {
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 3),
    }


def test_without_starts_and_finals():
    graph = build_graph(
        {0, 1, 2, 3},
        [
            (0, 1, {"label": "a"}),
            (1, 2, {"label": "b"}),
            (2, 3, {"label": "c"}),
        ],
    )

    cfg = CFG.from_text(
        """
                        S -> A
                        A -> a | a S
                        """
    )
    res = find_pairs_matching_grammar(cfg, graph)
    assert res == {(0, 1)}

    cfg = CFG.from_text("S -> a S b | a b")
    res = find_pairs_matching_grammar(cfg, graph)
    assert res == {(0, 2)}

    cfg = CFG.from_text(
        """
                        S -> A B C
                        A -> a
                        B -> b
                        C -> c
                         """
    )
    res = find_pairs_matching_grammar(cfg, graph)
    assert res == {(0, 3)}


def test_all_starts_and_finals():
    graph = build_graph(
        {0, 1, 2, 3},
        [
            (0, 1, {"label": "a"}),
            (1, 2, {"label": "a"}),
            (2, 3, {"label": "a"}),
        ],
    )

    cfg = CFG.from_text(
        """
                        S -> A
                        A -> a | a S
                        """
    )
    res = find_pairs_matching_grammar(cfg, graph, {0, 1, 2, 3}, {0, 1, 2, 3})

    assert res == {
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 3),
    }


def test_all_starts_and_finals_cycled_graph():
    graph = build_graph(
        {0, 1, 2, 3},
        [
            (0, 1, {"label": "a"}),
            (1, 2, {"label": "a"}),
            (2, 3, {"label": "a"}),
            (3, 0, {"label": "a"}),
        ],
    )
    cfg = CFG.from_text(
        """
                        S -> A
                        A -> a | a S
                        """
    )
    res = find_pairs_matching_grammar(cfg, graph, {0, 1, 2, 3}, {0, 1, 2, 3})

    assert res == {
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 0),
        (3, 1),
        (3, 2),
        (3, 3),
    }


def test_several_pathes():
    graph = build_graph(
        {0, 1, 2, 3, 4, 5, 6, 7},
        [
            (0, 1, {"label": "a"}),
            (1, 2, {"label": "b"}),
            (2, 3, {"label": "c"}),
            (0, 4, {"label": "a"}),
            (4, 5, {"label": "b"}),
            (5, 6, {"label": "c"}),
            (7, 1, {"label": "a"}),
        ],
    )

    cfg = CFG.from_text(
        """
                        S -> A B C
                        A -> a
                        B -> b
                        C -> c
                         """
    )
    res1 = find_pairs_matching_grammar(cfg, graph, {0}, {0, 1, 2, 3, 4, 5, 6})
    res2 = find_pairs_matching_grammar(cfg, graph, {0, 7}, {0, 1, 2, 3, 4, 5})

    assert res1 == {(0, 3), (0, 6)}
    assert res2 == {(0, 3), (7, 3)}


def test_alternating_grammar():
    graph = build_graph(
        {0, 1, 2, 3},
        [
            (0, 1, {"label": "a"}),
            (1, 2, {"label": "a"}),
            (2, 0, {"label": "a"}),
            (2, 3, {"label": "b"}),
            (3, 2, {"label": "b"}),
        ],
    )

    cfg = CFG.from_text("S -> a S b | a b")

    res = find_pairs_matching_grammar(cfg, graph, start_nodes={3})
    assert res == set()

    res = find_pairs_matching_grammar(cfg, graph, start_nodes={0}, final_nodes={2, 3})
    assert res == {(0, 2), (0, 3)}
