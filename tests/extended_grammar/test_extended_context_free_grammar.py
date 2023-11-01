from os import path

from pyformlang.regular_expression import Regex
from pyformlang.cfg import Variable
from project.grammar_utility.grammar_to_weak_chomsky_form import (
    read_contex_free_grammar_from_file,
)
from project.extended_grammar.extended_context_free_grammar import (
    build_extended_context_free_grammar_from_context_free_grammar,
    ExtendedContexFreeGrammar,
)


def test_ExtendedContexFreeGrammar():
    context_free_grammar = read_contex_free_grammar_from_file(
        path.abspath(path.join("files", "test_ExtendedContexFreeGrammar"))
    )
    extended_context_free_grammar = (
        build_extended_context_free_grammar_from_context_free_grammar(
            context_free_grammar
        )
    )

    expected_extended_context_free_grammar = ExtendedContexFreeGrammar(
        variables={Variable("S"), Variable("A")},
        productions={Variable("S"): Regex("A"), Variable("A"): Regex("(((S.S)|c)|b)")},
    )

    assert (
        extended_context_free_grammar.variables
        == expected_extended_context_free_grammar.variables
    )
    assert (
        extended_context_free_grammar.start_symbol
        == expected_extended_context_free_grammar.start_symbol
    )

    variables = []
    for production in extended_context_free_grammar.productions.items():
        assert production[0] not in variables
        variables.append(production[0])
