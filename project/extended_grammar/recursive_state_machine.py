from pyformlang.cfg import Variable
from project.extended_grammar.extended_context_free_grammar import (
    ExtendedContexFreeGrammar,
)


class RecursiveStateMachine:
    def __init__(self, start: Variable, boxes: dict):
        self.start = start
        self.boxes = boxes


def build_rsm_from_ecfg(ecfg: ExtendedContexFreeGrammar):
    boxes = {}
    for key, finite_automaton in ecfg.productions.items():
        boxes[key] = finite_automaton.to_epsilon_nfa()
    return RecursiveStateMachine(start=ecfg.start_symbol, boxes=boxes)


def minimize_rsm(rsm: RecursiveStateMachine):
    min_rsm = RecursiveStateMachine(start=rsm.start, boxes={})
    for v, nondeterministic_finite_automaton in rsm.boxes.items():
        min_rsm.boxes[v] = nondeterministic_finite_automaton.minimize()
    return min_rsm
