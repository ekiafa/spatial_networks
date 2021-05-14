import sys,math 
import heapq


path=[]
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



def calculate_distances(graph, source,target):
    distances = {vertex: float('infinity') for vertex in graph}
    loops=0
    global path
    path=[]
    distances[source] = 0

    pq = [(0, source)]

    while len(pq) > 0:
        loops+=1
        
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:

            continue


        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            #print("from neighbor "+str(neighbor)+' the distance is '+str(distance))


            # Only consider this new path if it's better than any path we've
            # already found.
            if neighbor in graph and  distance < distances[neighbor]:
                path.append(neighbor)
                
                if neighbor==target:
                    print("Loops Dijkstra Algorithm : ",loops)
                    distances[neighbor] = distance
                    return distances[neighbor],path
                    
                
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
            

    #return distances[target],path

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
            
            print("Dijkstra Algorithm Dictance and Path : ",calculate_distances(graph, source,target))

















if __name__ == '__main__':
  
   main()

