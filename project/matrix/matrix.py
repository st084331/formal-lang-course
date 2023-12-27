from networkx import MultiDiGraph
from pyformlang.cfg import CFG, Variable
from scipy.sparse import lil_matrix

from project.grammar_utility.grammar_to_weak_chomsky_form import (
    contex_free_grammar_to_weak_chomsky_form,
)


def compute_matrix_from_cfg_and_graph(cfg: CFG, graph: MultiDiGraph):
    weak_chomsky_form_grammar = contex_free_grammar_to_weak_chomsky_form(cfg)

    epsilon_productions = set()
    terminal_productions = set()
    variable_productions = set()

    for production in weak_chomsky_form_grammar.productions:
        if len(production.body) == 1:
            terminal_productions.add(production)
        elif len(production.body) == 2:
            variable_productions.add(production)
        else:
            epsilon_productions.add(production)

    num_nodes = graph.number_of_nodes()
    variable_to_matrix = {}

    for variable in weak_chomsky_form_grammar.variables:
        variable_to_matrix[variable] = lil_matrix((num_nodes, num_nodes), dtype=bool)

    for u, v, label in graph.edges(data="label"):
        for production in terminal_productions:
            if label == production.body[0].value:
                variable_to_matrix[production.head][u, v] = True

    for node in graph.nodes:
        i = list(graph.nodes).index(node)
        for production in epsilon_productions:
            variable_to_matrix[production][i, i] = True

    while True:
        flag = False
        for production in variable_productions:
            prev_nonzero = variable_to_matrix[production.head].count_nonzero()
            variable_to_matrix[production.head] += (
                variable_to_matrix[production.body[0]]
                @ variable_to_matrix[production.body[1]]
            )

            if not flag:
                flag = (
                    prev_nonzero != variable_to_matrix[production.head].count_nonzero()
                )

        if not flag:
            break

    result = set()
    for variable, matrix in variable_to_matrix.items():
        rows, cols = matrix.nonzero()
        for i in range(len(rows)):
            result.add(
                (list(graph.nodes)[rows[i]], variable, list(graph.nodes)[cols[i]])
            )

    return result


def find_pairs_matching_grammar(
    cfg: CFG,
    graph: MultiDiGraph,
    start_nodes: set = None,
    final_nodes: set = None,
    start_symbol: Variable = Variable("S"),
):
    if not start_nodes:
        start_nodes = set(graph.nodes)
    if not final_nodes:
        final_nodes = set(graph.nodes)

    matrix_cfpq_result = compute_matrix_from_cfg_and_graph(cfg, graph)

    result = set()
    for v1, variable, v2 in matrix_cfpq_result:
        if variable == start_symbol and v1 in start_nodes and v2 in final_nodes:
            result.add((v1, v2))

    return result
