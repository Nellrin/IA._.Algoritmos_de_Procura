##########################################
#    A*
##########################################

def procura_aStar(self, start, end):
    # open_list is a list of nodes which have been visited, but who's neighbors
    # haven't all been inspected, starts off with the start node
    # closed_list is a list of nodes which have been visited
    # and who's neighbors have been inspected
    open_list = {start}
    closed_list = set([])

    # g contains current distances from start_node to all other nodes
    # the default value (if it's not found in the map) is +infinity
    g = {}  ##  g é apra substiruir pelo peso  ???

    g[start] = 0

    # parents contains an adjacency map of all nodes
    parents = {}
    parents[start] = start
    n = None
    while len(open_list) > 0:
        # find a node with the lowest value of f() - evaluation function
        calc_heurist = {}
        flag = 0
        for v in open_list:
            if n == None:
                n = v
            else:
                flag = 1
                calc_heurist[v] = g[v] + self.getH(v)
        if flag == 1:
            min_estima = self.calcula_est(calc_heurist)
            n = min_estima
        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == end:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start)

            reconst_path.reverse()

            #print('Path found: {}'.format(reconst_path))
            return (reconst_path, self.calcula_custo(reconst_path))

        # for all neighbors of the current node do
        for (m, weight) in self.getNeighbours(n):  # definir função getneighbours  tem de ter um par nodo peso
            # if the current node isn't in both open_list and closed_list
            # add it to open_list and note n as it's parent
            if self.getH(m) > 0 and m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight

            # otherwise, check if it's quicker to first visit n, then m
            # and if it is, update parent data and g data
            # and if the node was in the closed_list, move it to open_list
            else:
                if self.getH(m) > 0 and g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_list.remove(n)
        closed_list.add(n)

    print('Path does not exist!')
    return None