import sys
from itertools import chain


def dijkstra_algorithm(graph, start_node,stop_node):
    
    # open_list is a list of nodes which have been visited, but who's neighbors
    # haven't all been inspected, starts off with the start node
    # closed_list is a list of nodes which have been visited
    # and who's neighbors have been inspected
    open_list = set([start_node])
    closed_list = set([])

    # g contains current distances from start_node to all other nodes
    # the default value (if it's not found in the map) is +infinity
    g = {}
    loops=0
    g[start_node] = 0

    # parents contains an adjacency map of all nodes
    parents = {}
    parents[start_node] = start_node
    
    while len(open_list) > 0:
        loops+=1
        n = None

        # find a node with the lowest value of f() - evaluation function
        for v in open_list:
            if n == None or g[v] < g[n] :
                n = v;

        if n == None:
            print('Path does not exist!')
            return None
    
        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        
        if n ==stop_node :
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start_node)
            
            path.reverse()
            
            print([g[stop_node],path])


            return path
        
        # for all neighbors of the current node do
        for m, weight in graph[n].items():
            # if the current node isn't in both open_list and closed_list
            # add it to open_list and note n as it's parent
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                
                
                g[m] = g[n] + weight

            # otherwise, check if it's quicker to first visit n, then m
            # and if it is, update parent data and g data
            # and if the node was in the closed_list, move it to open_list
            else:
                if g[m] > g[n] + weight:
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
    return 

import heapq


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                
                heapq.heappush(pq, (distance, neighbor))
    return distances





def nra(graph,source1,source2,source3,source4,source5,source6):
           
            
            s1=calculate_distances(graph, source1)
            s2=calculate_distances(graph, source2)
            s3=calculate_distances(graph, source3)
            s4=calculate_distances(graph, source4)
            s5=calculate_distances(graph, source5)
            s6=calculate_distances(graph, source6)
                        
            c = dict(sorted(chain(s1.items(), s2.items(),s3.items(),s4.items(), s5.items(),s6.items()), key=lambda t: t[1]))
            n=min(c, key=c.get)
            
            print("best meeting point:",n)
            print("Shortest path distance:",c[n])
            print("paths:")
            dijkstra_algorithm(graph, source1,n)
            dijkstra_algorithm(graph, source2,n)
            dijkstra_algorithm(graph, source3,n)
            dijkstra_algorithm(graph, source4,n)
            dijkstra_algorithm(graph, source5,n)
            dijkstra_algorithm(graph, source6,n)           
                
                                         







def main():      
       
        out=sys.argv[1]
        source1=sys.argv[2]
        source2=sys.argv[3]
        source3=sys.argv[4]
        source4=sys.argv[5]
        source5=sys.argv[6]
        source6=sys.argv[7]

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

        
        nra(graph,source1,source2,source3,source4,source5,source6)







if __name__ == '__main__':
  
   main()

