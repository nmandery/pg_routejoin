from routejoin import dijkstra, common


def route_network(G, nodes=[]):
    """
    create paths between all nodes of the network

    returns a list of paths
    e.g.:
    [[18462, 19256, 19052, 19075, 18600, 18631, 18818, 18881, 18872],
     [18872, 18881, 18818, 18631, 18852, 18860]]
    """
    nodes_len = len(nodes)
    routes = []

    # be sure all nodes exists
    for node in nodes:
        if not node in G:
            raise common.MissingNodeError(node)

    if nodes_len < 2:
        raise common.NotEnoughNodesError()
    else:
        last_node = nodes[0]
        for next_node in nodes[1:]:
            route = dijkstra.shortest_path(G, last_node, next_node)

            # reduce the routing costs for the nodes of
            # this route in the graph, to get the following
            # routes to prefer the already included nodes
            for node in route:
                for neighbor in G[node].iterkeys():
                    # reduce the cost by 50%
                    G[neighbor][node] = int(G[neighbor][node] / 2)
                    G[node][neighbor] = int(G[node][neighbor] / 2)
            last_node = next_node

            routes.append(route)
    return routes
