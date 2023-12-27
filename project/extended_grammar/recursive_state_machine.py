from pyformlang.cfg import Variable
from project.extended_grammar.extended_context_free_grammar import (
    ExtendedContexFreeGrammar,
)


class RecursiveStateMachine:
    def __init__(self, start: Variable, boxes: dict):
        self.start = start
        self.boxes = boxes


def build_recursive_state_machine_from_extended_context_free_grammar(
    extended_context_free_grammar: ExtendedContexFreeGrammar,
):
    boxes = {}
    for key, finite_automaton in extended_context_free_grammar.productions.items():
        boxes[key] = finite_automaton.to_epsilon_nfa()
    return RecursiveStateMachine(
        start=extended_context_free_grammar.start_symbol, boxes=boxes
    )


def minimize_recursive_state_machine(recursive_state_machine: RecursiveStateMachine):
    minimal_recursive_state_machine = RecursiveStateMachine(
        start=recursive_state_machine.start, boxes={}
    )
    for v, nondeterministic_finite_automaton in recursive_state_machine.boxes.items():
        minimal_recursive_state_machine.boxes[
            v
        ] = nondeterministic_finite_automaton.minimize()
    return minimal_recursive_state_machine
