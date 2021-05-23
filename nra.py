


def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    path = []
    for node in unseenNodes:
        shortest_distance[node] = math.inf
    shortest_distance[start] = 0
    global dijkstra_loops
    while unseenNodes:
        dijkstra_loops+=1
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for neighbor, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[neighbor]:
                shortest_distance[neighbor] = weight + shortest_distance[minNode]
                predecessor[neighbor] = minNode
        unseenNodes.pop(minNode)
        if minNode==goal:
            break

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable.')
            break
    path.insert(0,start)
    if shortest_distance[goal] != math.inf:
        print("Dijkstra")
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))





def main():      
       
        out=sys.argv[1]
        source1=sys.argv[2]
        source2=sys.argv[3]
        source3=sys.argv[4]
        










if __name__ == '__main__':
  
   main()

