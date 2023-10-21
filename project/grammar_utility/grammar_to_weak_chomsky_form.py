from pathlib import Path
from pyformlang.cfg import CFG, Variable


def contex_free_grammar_to_weak_chomsky_form(contex_free_grammar: CFG) -> CFG:
    contex_free_grammar = (
        contex_free_grammar.remove_useless_symbols()
        .eliminate_unit_productions()
        .remove_useless_symbols()
    )
    productions_to_decompose = (
        contex_free_grammar._get_productions_with_only_single_terminals()
    )
    new_productions = contex_free_grammar._decompose_productions(
        productions_to_decompose
    )

    return CFG(
        start_symbol=contex_free_grammar._start_symbol,
        productions=set(new_productions),
    )


def read_contex_free_grammar_from_file(
    path_to_grammar: Path, starting_nonterminal: str = "S"
) -> CFG:
    with open(path_to_grammar, "r") as file:
        grammar = file.read()

    return CFG.from_text(grammar, Variable(starting_nonterminal))
