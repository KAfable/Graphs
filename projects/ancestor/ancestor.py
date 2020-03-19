
def earliest_ancestor(ancestors, starting_node):
    # what are the base cases?

    # build a graph
    # traverse the graph
    if ancestors == None:
        return starting_node

    # how the hell do you get ancestors?
    # filter through ancestors for the tuple
    def get_parents(ancestors, starting_node):
        return filter(lambda person: person[1] == starting_node, ancestors)
