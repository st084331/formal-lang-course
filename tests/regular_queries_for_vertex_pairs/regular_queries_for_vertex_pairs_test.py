import cfpq_data
from project.regular_queries_for_vertex_pairs.nfa_boolean_matrices import (
    BooleanFiniteAutomaton,
    intersect,
)
from project.regular_queries_for_vertex_pairs.regular_queries_for_vertex_pairs import (
    regular_queries_for_vertex_pairs,
)
from pyformlang.finite_automaton import NondeterministicFiniteAutomaton
from pyformlang.regular_expression import Regex


def test_get_transitive_closure():
    nfa = NondeterministicFiniteAutomaton()
    nfa.add_transitions([(1, "a", 2), (2, "b", 3)])

    boolean_matrix = BooleanFiniteAutomaton(nfa)
    transitive_closure = boolean_matrix.get_transitive_closure()

    assert transitive_closure.sum() == transitive_closure.size


def test_intersect():
    first_nfa = NondeterministicFiniteAutomaton()
    first_nfa.add_start_state(0)
    first_nfa.add_final_state(1)
    first_nfa.add_transitions([(0, "b", 1), (1, "a", 1)])
    boolean_first_nfa = BooleanFiniteAutomaton(first_nfa)

    second_nfa = NondeterministicFiniteAutomaton()
    second_nfa.add_start_state(0)
    second_nfa.add_final_state(2)
    second_nfa.add_transitions([(0, "с", 0), (0, "b", 1), (1, "c", 1), (1, "a", 2)])
    boolean_second_nfa = BooleanFiniteAutomaton(second_nfa)

    expected_nfa = NondeterministicFiniteAutomaton()
    expected_nfa.add_start_state(0)
    expected_nfa.add_final_state(5)
    expected_nfa.add_transitions([(4, "a", 5), (0, "b", 4)])
    expected_intersection = BooleanFiniteAutomaton(expected_nfa)

    actual_intersection = intersect(boolean_first_nfa, boolean_second_nfa)

    assert actual_intersection.number_of_states == len(first_nfa.states) * len(
        second_nfa.states
    )
    assert actual_intersection.start_states == expected_intersection.start_states
    assert actual_intersection.final_states == expected_intersection.final_states
    for label in actual_intersection.boolean_matrices.keys():
        assert (
            actual_intersection.boolean_matrices[label].nnz
            == expected_intersection.boolean_matrices[label].nnz
        )


def test_regular_queries_for_vertex_pairs():
    graph = cfpq_data.labeled_two_cycles_graph(3, 3, labels=("a", "b"), common_node=0)
    regex = Regex("a|b")
    result = regular_queries_for_vertex_pairs(
        graph=graph, regex=regex, start_states={0}, final_states={1}
    )
    assert result == {(0, 1)}
