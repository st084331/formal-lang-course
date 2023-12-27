from os import path

from project.grammar_utility.grammar_to_weak_chomsky_form import (
    contex_free_grammar_to_weak_chomsky_form,
    read_contex_free_grammar_from_file,
)
from pyformlang.cfg import CFG, Variable
from pathlib import Path


def test_contex_free_grammar_to_weak_chomsky_form():
    contex_free_grammar = CFG.from_text("S -> a", Variable("S"))
    expected_grammar = CFG.from_text("S -> a", Variable("S"))
    weak_chomsky_form = contex_free_grammar_to_weak_chomsky_form(contex_free_grammar)
    assert weak_chomsky_form.start_symbol == expected_grammar.start_symbol
    assert weak_chomsky_form.productions == expected_grammar.productions


def test_read_contex_free_grammar_from_file():
    expected_grammar = CFG.from_text("S -> a", Variable("S"))
    contex_free_grammar = read_contex_free_grammar_from_file(
        Path(path.join("tests", "grammar_utility", "grammar.txt"))
    )
    assert contex_free_grammar.start_symbol == expected_grammar.start_symbol
    assert contex_free_grammar.productions == expected_grammar.productions
