import sys,math 
import heapq


path=[]
dijkstra_loops=0
'''

loops=0
def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):

    if src == dest:
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)

        print('shortest path : '+str(list(reversed(path))))
        print("cost="+str(distances[dest]))     
    else :     
        
        if not visited: 
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        
        global loops
        loops+=1
        dijkstra(graph,x,dest,visited,distances,predecessors)
'''
"""       
def dijkstra(graph,source,target):
    unseen=[]
    seen=[]
    spd=dict()
    path=dict()
    for i in graph:
        spd[source,i]=math.inf
        path[source,i]=None
        unseen.append(i)
    heap=[]
    heapq.heapify(heap)

    heapq.heappush(heap,source)
    
    while len(heap)!=0:
      top=heap[0]
      heapq.heappop(heap) 
      seen.append(top)
      if top==target:
          return path
      for i in graph[top].items():
          if i not in seen:
              print(i[0])
              print(spd[source,i[0]])
              if spd[source,i[0]]>spd[source,top]:
                print("mpainei")
                spd[source,i[0]]=spd[source,top] + i[1]
                path[source,i[0]]=path[source,top]+[top,i[0]]
                heapq.heappush(heap,i[0])
                print(heap)
       
    return heap

"""


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

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
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


"""

def calculate_distances(graph, source,target):
    distances = {vertex: float('infinity') for vertex in graph}
    loops=0
    global path
    path=[]
    distances[source] = 0
    predecessors={}

    pq = [(0, source)]

    while len(pq) > 0:
        loops+=1
        
        current_distance, current_vertex = heapq.heappop(pq)
        if current_vertex=='55':
            print('true')
            #break


        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:

            continue


        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            #print("from neighbor "+str(neighbor)+' the distance is '+str(distance))


            # Only consider this new path if it's better than any path we've
            # already found.
            if neighbor in graph and  current_distance + weight < distances[neighbor]:
                #print("from neighbor "+str(neighbor)+' the distance is '+str(current_distance + weight))
                path.append(neighbor)
                
                if current_vertex==target:
                    print("Loops Dijkstra Algorithm : ",loops)
                    distances[neighbor] = current_distance + weight
                    predecessors[neighbor] = target
                    #print(predecessors.values().unique())
                    return distances[neighbor]
                    
                predecessors[neighbor] = current_vertex
                distances[neighbor] = current_distance + weight
                
                heapq.heappush(pq, (current_distance + weight, neighbor))
    
            

    #return distances[target],path
"""

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
            print(dijkstra(graph,source,target))
            print(dijkstra_loops)

















if __name__ == '__main__':
  
   main()

