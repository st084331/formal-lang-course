from networkx import MultiDiGraph
from scipy.sparse import dok_matrix, lil_matrix, csr_matrix
from pyformlang.cfg import CFG, Terminal, Variable


def convert_cfg_to_rka(cfg: CFG):
    rka_productions = set()

    for production in cfg.productions:
        head = production.head
        body = production.body
        if len(body) <= 2 and (len(body) == 0 or isinstance(body[0], Terminal)):
            rka_productions.add(production)
        else:
            pass

    rka_cfg = CFG(
        variables=cfg.variables,
        terminals=cfg.terminals,
        start_symbol=cfg.start_symbol,
        productions=rka_productions,
    )
    return rka_cfg


def create_terminal_matrix(graph, terminal, num_nodes):
    matrix = dok_matrix((num_nodes, num_nodes), dtype=bool)
    if isinstance(terminal, Terminal):
        for u, v, data in graph.edges(data=True):
            if data.get("label") == terminal.value:
                matrix[u, v] = True
    return matrix


def tensor_reachability(graph: MultiDiGraph, cfg: CFG):
    rka = convert_cfg_to_rka(cfg)
    num_nodes = graph.number_of_nodes()
    matrices = {
        nonterminal: lil_matrix((num_nodes, num_nodes), dtype=bool)
        for nonterminal in rka.variables
    }

    for u, v, data in graph.edges(data=True):
        label = data.get("label", None)
        if label:
            for production in rka.productions:
                if (
                    len(production.body) == 1
                    and isinstance(production.body[0], Terminal)
                    and production.body[0].value == label
                ):
                    matrices[production.head][u, v] = True

    change_detected = True
    while change_detected:
        change_detected = False
        for production in rka.productions:
            if len(production.body) == 2:
                symbol1, symbol2 = production.body
                mat1 = (
                    matrices[symbol1]
                    if isinstance(symbol1, Variable)
                    else create_terminal_matrix(graph, symbol1, num_nodes)
                )
                mat2 = (
                    matrices[symbol2]
                    if isinstance(symbol2, Variable)
                    else create_terminal_matrix(graph, symbol2, num_nodes)
                )
                tensor_product = mat1 @ mat2
                head_matrix = matrices[production.head]
                prev_nonzero = head_matrix.count_nonzero()
                head_matrix = head_matrix + tensor_product
                head_matrix_csr = csr_matrix(head_matrix)
                head_matrix_csr.eliminate_zeros()
                if head_matrix_csr.count_nonzero() > prev_nonzero:
                    change_detected = True
                # Convert it back to lil_matrix for further updates
                matrices[production.head] = lil_matrix(head_matrix_csr)

    result = set()
    for variable, matrix in matrices.items():
        matrix = matrix.todok()  # Convert to DOK for efficient nonzero iteration
        for (i, j), _ in matrix.items():
            result.add((i, variable, j))

    return result


def specific_reachability(graph, cfg, start_nodes, final_nodes, nonterminal):
    reachability_results = tensor_reachability(graph, cfg)
    filtered_results = {
        (u, var, v)
        for (u, var, v) in reachability_results
        if var == nonterminal and u in start_nodes and v in final_nodes
    }
    return filtered_results
