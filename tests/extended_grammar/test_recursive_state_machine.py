from os import path

from pyformlang.regular_expression import Regex
from pyformlang.cfg import Variable
from project.automaton_builder.DFA_builder import build_mdfa
from project.extended_grammar.extended_context_free_grammar import (
    get_extended_context_free_grammar_from_file,
)
from project.extended_grammar.recursive_state_machine import (
    build_recursive_state_machine_from_extended_context_free_grammar,
    minimize_recursive_state_machine,
)


def test_recursive_state_machine_from_extended_context_free_grammar():
    extended_context_free_grammar = get_extended_context_free_grammar_from_file(
        path.abspath(path.join("files", "test_RecursiveStateMachine"))
    )
    recursive_state_machine = (
        build_recursive_state_machine_from_extended_context_free_grammar(
            extended_context_free_grammar
        )
    )
    expected_productions = {
        Variable("S"): Regex("A B C"),
        Variable("A"): Regex("a"),
        Variable("B"): Regex("b"),
        Variable("C"): Regex("(c | S)"),
    }

    assert recursive_state_machine.start == Variable("S")
    assert all(
        recursive_state_machine.boxes[var].is_equivalent_to(
            expected_productions[var].to_epsilon_nfa()
        )
        for var in expected_productions.keys()
    )


def test_minimize_recursive_state_machine():
    extended_context_free_grammar = get_extended_context_free_grammar_from_file(
        path.abspath(path.join("files", "test_RecursiveStateMachine"))
    )
    recursive_state_machine = (
        build_recursive_state_machine_from_extended_context_free_grammar(
            extended_context_free_grammar
        )
    )

    assert all(
        minimize_recursive_state_machine(recursive_state_machine).boxes[var]
        == build_mdfa(extended_context_free_grammar.productions[var])
        for var in extended_context_free_grammar.productions.keys()
    )
