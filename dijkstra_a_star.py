import sys,math 
import heapq

""""def dijkstra(pointers_array,source,target):
    unseen=[]
    seen=[]
    for i in pointers_array:
        spd=math.inf
        path=[]
        unseen.append(i)
    heap=[]
    heapq.heapify(heap)
    heapq.heappush(source)
    while len(heap)!=0:
      top=heap[0]
      heapq.heappop(heap[0]) 
      seen.append(top)
      if top==target:
          return path
      for i in neighbors[top]:
          if i not in seen:
              if spd(source,i)>spd(source,top):
                 spd(source,i)=spd(source,top) 
                 path

def spd(first_node,second_node):"""


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
                res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)} #array to dictionary
                graph[node]=res_dct
                node_points[node]=line.split(' ')[1:3]
            

        
















if __name__ == '__main__':
  
   main()

