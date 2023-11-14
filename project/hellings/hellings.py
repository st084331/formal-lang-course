from networkx import MultiDiGraph
from pyformlang.cfg import CFG, Variable
from project.grammar_utility.grammar_to_weak_chomsky_form import (
    contex_free_grammar_to_weak_chomsky_form,
)


def hellings_closure(context_free_grammar: CFG, input_graph: MultiDiGraph):
    try:
        weak_chomsky_normal_form = contex_free_grammar_to_weak_chomsky_form(
            context_free_grammar
        )
    except Exception as e:
        raise ValueError(f"Error in converting grammar to weak Chomsky form: {e}")

    # Initialize sets for different types of productions
    epsilon_productions = set()
    terminal_productions = set()
    variable_productions = set()

    # Classify the productions into appropriate sets
    for production in weak_chomsky_normal_form.productions:
        if len(production.body) == 1:
            terminal_productions.add(production)
        elif len(production.body) == 2:
            variable_productions.add(production)
        else:
            epsilon_productions.add(production)

    # Initialize result list for storing triples
    triples_result = []

    # Process terminal productions
    for first_node, second_node, label in input_graph.edges(data="label"):
        for production in terminal_productions:
            if label == production.body[0].value:
                triples_result.append((first_node, production.head, second_node))

    # Process epsilon productions
    for node in input_graph.nodes:
        for production in epsilon_productions:
            triples_result.append((node, production.head, node))

    # Initialize queue with the initial result
    processing_queue = triples_result.copy()

    # Process variable productions
    while len(processing_queue) > 0:
        (node1, variable, node2) = processing_queue.pop(0)

        for x, intermediate_var, z in triples_result:
            if z == node1:
                for prod in variable_productions:
                    new_triple = (x, prod.head, node2)
                    if (
                        prod.body[0] == intermediate_var
                        and prod.body[1] == variable
                        and new_triple not in triples_result
                    ):
                        processing_queue.append(new_triple)
                        triples_result.append(new_triple)

            if x == node2:
                for prod in variable_productions:
                    new_triple = (node1, prod.head, z)
                    if (
                        prod.body[0] == variable
                        and prod.body[1] == intermediate_var
                        and new_triple not in triples_result
                    ):
                        processing_queue.append(new_triple)
                        triples_result.append(new_triple)

    return triples_result


def context_free_path_query(
    context_free_grammar: CFG,
    input_graph: MultiDiGraph,
    start_nodes: set = None,
    final_nodes: set = None,
    start_symbol: Variable = Variable("S"),
):
    # Set default values for start and final nodes if not provided
    if not start_nodes:
        start_nodes = set(input_graph.nodes)
    if not final_nodes:
        final_nodes = set(input_graph.nodes)

    # Compute the Hellings closure
    hellings_closure_result = hellings_closure(context_free_grammar, input_graph)

    # Initialize result set
    query_result = set()

    # Filter the result based on start symbol, start nodes, and final nodes
    for node1, variable, node2 in hellings_closure_result:
        if variable == start_symbol and node1 in start_nodes and node2 in final_nodes:
            query_result.add((node1, node2))

    return query_result
