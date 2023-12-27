from pyformlang.finite_automaton import State
from scipy import sparse
from scipy.sparse import block_diag, csr_matrix, vstack
import numpy
from project.regular_queries.nfa_boolean_matrices import BooleanFiniteAutomaton


def reachability(
    graph: BooleanFiniteAutomaton,
    regex: BooleanFiniteAutomaton,
    for_each_state: bool = False,
):
    direct_sum = {}

    for label in graph.boolean_matrices.keys() & regex.boolean_matrices.keys():
        direct_sum[label] = block_diag(
            (regex.boolean_matrices[label], graph.boolean_matrices[label])
        )

    front = (
        vstack([create_front(graph, regex) for st in graph.start_states])
        if for_each_state
        else create_front(graph, regex)
    )

    visited = csr_matrix(front.shape, dtype=bool)
    first_step = True

    while True:
        old_visited_nnz = visited.nnz

        for mtx in direct_sum.values():
            if first_step:
                step = numpy.dot(front, mtx)
            else:
                step = numpy.dot(visited, mtx)
            visited += transform_front(step, regex, for_each_state)
        first_step = False

        if old_visited_nnz == visited.nnz:
            break

    result = set()
    regex_states = list(regex.states_indices.keys())
    graph_states = list(graph.states_indices.keys())

    for row, col in zip(*visited.nonzero()):
        if (
            not col < regex.number_of_states
            and regex_states[row % regex.number_of_states] in regex.final_states
        ):
            state_index = col - regex.number_of_states
            if graph_states[state_index] in graph.final_states:
                if for_each_state:
                    result.add(
                        (State(row // regex.number_of_states), State(state_index))
                    )
                else:
                    result.add(State(state_index))

    return result


def create_front(graph, regex: BooleanFiniteAutomaton):
    n = graph.number_of_states
    k = regex.number_of_states

    front = sparse.lil_matrix((k, n + k))

    right_part = sparse.lil_array(
        [[state in graph.start_states for state in graph.states]]
    )

    for _, index in regex.states_indices.items():
        front[index, index] = True
        front[index, k:] = right_part

    return front.tocsr()


def transform_front(step: csr_matrix, regex, is_for_each_state):
    result = csr_matrix(step.shape, dtype=bool)
    for row, col in zip(*step.nonzero()):
        if col < regex.number_of_states:
            right_row_part = step[row, regex.number_of_states :]
            if right_row_part.nnz != 0:
                if not is_for_each_state:
                    result[col, col] = True
                    result[col, regex.number_of_states :] += right_row_part
                else:
                    state_number = row // regex.number_of_states
                    result[state_number * regex.number_of_states + col, col] = True
                    result[
                        state_number * regex.number_of_states + col,
                        regex.number_of_states :,
                    ] += right_row_part
    return result
