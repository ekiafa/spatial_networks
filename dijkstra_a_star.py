import sys,math 
import heapq

def dijkstra(pointers_array,source,target):
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

def spd(first_node,second_node):




def main():      
       
        out=sys.argv[1]
        source=sys.argv[2]
        target=sys.argv[3]

        with open('out.txt' ,mode='r') as pointers:
            for line in pointers:
                print(line)
















if __name__ == '__main__':
  
   main()

