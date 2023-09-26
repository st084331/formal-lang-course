from networkx import MultiDiGraph
from pyformlang.regular_expression import Regex

from project.automaton_builder.NFA_builder import build_nfa_from_graph
from project.automaton_builder.DFA_builder import build_mdfa
from project.regular_queries_for_vertex_pairs.nfa_boolean_matrices import (
    BooleanFiniteAutomaton,
    intersect,
)


def regular_queries_for_vertex_pairs(
    graph: MultiDiGraph, regex: Regex, start_states: set, final_states: set
) -> set:
    result = set()

    nfa = build_nfa_from_graph(
        graph=graph, start_states=start_states, final_states=final_states
    )
    dfa = build_mdfa(regex)

    boolean_matrix_for_graph = BooleanFiniteAutomaton(nfa)
    boolean_matrix_for_query = BooleanFiniteAutomaton(dfa)

    boolean_matrix_intersected = intersect(
        boolean_matrix_for_graph, boolean_matrix_for_query
    )

    start_states = boolean_matrix_intersected.start_states
    final_states = boolean_matrix_intersected.final_states

    transitive = boolean_matrix_intersected.get_transitive_closure()

    for first_state, second_state in zip(*transitive.nonzero()):
        if first_state in start_states and second_state in final_states:
            result.add(
                (
                    first_state // boolean_matrix_for_query.number_of_states,
                    second_state // boolean_matrix_for_query.number_of_states,
                )
            )

    return result
