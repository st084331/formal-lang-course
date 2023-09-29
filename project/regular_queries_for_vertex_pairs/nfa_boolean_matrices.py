from scipy import sparse
from pyformlang.finite_automaton import NondeterministicFiniteAutomaton


class BooleanFiniteAutomaton:
    number_of_states: int
    start_states: set
    final_states: set
    states_indices: dict
    boolean_matrices: dict

    def __init__(self, nfa: NondeterministicFiniteAutomaton = None):
        if nfa is None:
            self.number_of_states = 0
            self.start_states = set()
            self.final_states = set()
            self.states_indices = {}
            self.boolean_matrices = {}
        else:
            self.number_of_states = len(nfa.states)
            self.start_states = nfa.start_states
            self.final_states = nfa.final_states
            self.states_indices = {
                state: index for (index, state) in enumerate(nfa.states)
            }
            self.boolean_matrices = self.build_boolean_matrix_for_nfa(nfa)

    def build_boolean_matrix_for_nfa(
        self, nfa: NondeterministicFiniteAutomaton
    ) -> dict:
        matrix = dict()
        for first_state, transition in nfa.to_dict().items():
            for label, target_states in transition.items():
                if not isinstance(target_states, set):
                    target_states = {target_states}

                for state in target_states:
                    if label not in matrix:
                        matrix[label] = sparse.dok_matrix(
                            (self.number_of_states, self.number_of_states), dtype=bool
                        )
                    first_state_index = self.states_indices.get(first_state)
                    state_index = self.states_indices.get(state)
                    matrix[label][first_state_index, state_index] = True

        return matrix

    def get_transitive_closure(self):
        if len(self.boolean_matrices) == 0:
            return sparse.dok_matrix((0, 0), dtype=bool)

        transitive_closure = sum(self.boolean_matrices.values())
        previous = transitive_closure.nnz
        current = 0

        while previous != current:
            transitive_closure += transitive_closure @ transitive_closure
            previous = current
            current = transitive_closure.nnz

        return transitive_closure


def intersect(
    first_automaton: BooleanFiniteAutomaton, second_automaton: BooleanFiniteAutomaton
) -> BooleanFiniteAutomaton:
    result_automaton = BooleanFiniteAutomaton()

    labels = (
        first_automaton.boolean_matrices.keys()
        & second_automaton.boolean_matrices.keys()
    )

    for label in labels:
        result_automaton.boolean_matrices[label] = sparse.kron(
            first_automaton.boolean_matrices[label],
            second_automaton.boolean_matrices[label],
        )

    for first_state, first_index in first_automaton.states_indices.items():
        for second_state, second_index in second_automaton.states_indices.items():
            state_index = first_index * second_automaton.number_of_states + second_index

            result_automaton.states_indices[state_index] = state_index

            if (
                first_state in first_automaton.start_states
                and second_state in second_automaton.start_states
            ):
                result_automaton.start_states.add(state_index)

            if (
                first_state in first_automaton.final_states
                and second_state in second_automaton.final_states
            ):
                result_automaton.final_states.add(state_index)

    result_automaton.number_of_states = (
        first_automaton.number_of_states * second_automaton.number_of_states
    )

    return result_automaton
