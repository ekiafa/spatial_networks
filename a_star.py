#Eftihia Kiafa AM:3003
import sys,math
from math import sqrt
from collections import deque

def euclidean_distance(p1,stop_node):

    distance = sqrt( (stop_node[0]-p1[0])*(stop_node[0]-p1[0]) + (stop_node[1]-p1[1])* (stop_node[1]-p1[1]))

    return distance


def dijkstra_algorithm(graph, start_node, stop_node):
    
    # unseen is a list of nodes which have been visited, but who's neighbors
    # haven't all been inspected, starts off with the start node
    # seen is a list of nodes which have been visited
    # and who's neighbors have been inspected
    unseen = set([start_node])
    seen = set([])

    # dist contains current distances from start_node to all other nodes
    # the default value (if it's not found in the map) is +infinity
    dist = {}
    loops=0
    dist[start_node] = 0

    # predecessors contains an adjacency map of all nodes
    predecessors = {}
    predecessors[start_node] = start_node

    while len(unseen) > 0:
        loops+=1
        n = None

        # find a node with the lowest value of f() - evaluation function
        for v in unseen:
            if n == None or dist[v] < dist[n] :
                n = v;

        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == stop_node:
            path = []

            while predecessors[n] != n:
                path.append(n)
                n = predecessors[n]

            path.append(start_node)

            path.reverse()
        
            print("Dijkstra's Path found: {}".format(path))
            print("Distance:",dist[stop_node])
            print("Loops:",loops)
            return path

        # for all neighbors of the current node do
        for m, weight in graph[n].items():
            # if the current node isn't in both unseen and seen
            # add it to unseen and note n as it's predecessor
            if m not in unseen and m not in seen:
                unseen.add(m)
                predecessors[m] = n
                dist[m] = dist[n] + weight

            # otherwise, check if it's quicker to first visit n, then m
            # and if it is, update predecessor data and dist data
            # and if the node was in the seen, move it to unseen
            else:
                if dist[m] > dist[n] + weight:
                    dist[m] = dist[n] + weight
                    predecessors[m] = n

                    if m in seen:
                        seen.remove(m)
                        unseen.add(m)

        # remove n from the unseen, and add it to seen
        # because all of his neighbors were inspected
        unseen.remove(n)
        seen.add(n)

    print('Path does not exist!')
    return None


def a_star_algorithm(node_points,graph, start_node, stop_node):
    
    # unseen is a list of nodes which have been visited, but who's neighbors
    # haven't all been inspected, starts off with the start node
    # seen is a list of nodes which have been visited
    # and who's neighbors have been inspected
    unseen = set([start_node])
    seen = set([])

    # dist contains current distances from start_node to all other nodes
    # the default value (if it's not found in the map) is +infinity
    dist = {}
    loops=0
    dist[start_node] = 0

    # predecessors contains an adjacency map of all nodes
    predecessors = {}
    predecessors[start_node] = start_node

    while len(unseen) > 0:
        loops+=1
        n = None

        # find a node with the lowest value of f() - evaluation function
        for v in unseen:
            if n == None or dist[v] + euclidean_distance(node_points[str(v)],node_points[str(stop_node)]) < dist[n] + euclidean_distance(node_points[str(n)],node_points[str(stop_node)]):
                n = v;

        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == stop_node:
            path = []

            while predecessors[n] != n:
                path.append(n)
                n = predecessors[n]
                
            path.append(start_node)
            
            path.reverse()
            
            print(" A-star's Path found: {}".format(path))
            print("Distance:",dist[stop_node])
            print("Loops:",loops)
            
            return path

        # for all neighbors of the current node do
        for m, weight in graph[n].items():
            # if the current node isn't in both unseen and seen
            # add it to unseen and note n as it's parent
            if m not in unseen and m not in seen:
                unseen.add(m)
                predecessors[m] = n
                dist[m] = dist[n] + weight
                #print(dist[m])

            # otherwise, check if it's quicker to first visit n, then m
            # and if it is, update predecessor data and g data
            # and if the node was in the seen, move it to unseen
            else:
                if dist[m] > dist[n] + weight:
                    dist[m] = dist[n] + weight
                    predecessors[m] = n
                    
                    if m in seen:
                        seen.remove(m)
                        unseen.add(m)

        # remove n from the unseen, and add it to seen
        # because all of his neighbors were inspected
        
        unseen.remove(n)
        seen.add(n)

    print('Path does not exist!')
    return None



def main():      
       
        out=sys.argv[1]
        source=sys.argv[2]
        target=sys.argv[3]

        with open('out.txt' ,mode='r') as pointers:
            
            graph=dict()
            node_points=dict()
            for line in pointers:
                node=line.split(' ')[0]
                lst=line.split(' ')[3:]
                
                res_dct = {lst[i]: float(lst[i + 1]) for i in range(0, len(lst), 2)} #array to dictionary
                graph[node]=res_dct
                lst_to_floats = [float(item) for item in line.split(' ')[1:3]]
                node_points[node]=lst_to_floats
        
        dijkstra_algorithm(graph, source, target)
        print("\n")
        a_star_algorithm(node_points,graph, source, target)









if __name__ == '__main__':
  
   main()

