from pyformlang.context_free_grammar import CFG, Variable
from pyformlang.regular_expression import Regex


class ExtendedContexFreeGrammar:
    def __init__(
        self,
        variables: set,
        productions: dict,
        start_symbol: Variable = Variable("S"),
    ):
        self.start_symbol = start_symbol
        self.variables = variables
        self.productions = productions


def build_ecfg_from_cfg(context_free_grammar: CFG):
    productions = {}
    start_symbol = context_free_grammar.start_symbol

    for production in context_free_grammar.productions:
        regex = Regex(
            ".".join(variable.value for variable in production.body)
            if len(production.body) > 0
            else " "
        )
        if production.head not in productions:
            productions[production.head] = regex
        else:
            productions[production.head] = productions[production.head].union(regex)

    return ExtendedContexFreeGrammar(
        variables=context_free_grammar.variables,
        productions=productions,
        start_symbol=start_symbol,
    )


def build_ecfg_from_text(text: str):
    variables = set()
    productions = {}

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        head_s, body_s = line.split("->")
        head = Variable(head_s.strip())
        variables.add(head)
        productions[head] = Regex(body_s)

    return ExtendedContexFreeGrammar(variables=variables, productions=productions)


def get_ecfg_from_file(file):
    with open(file) as f:
        ecfg = build_ecfg_from_text(f.read())
    return ecfg
