#Eftihia Kiafa AM:3003
import sys
import heapq

global paths1,paths2,paths3
paths1={}
paths2={}
paths3={}


def get_route(predecessor, i, route):
    
    if int(i) >= 0:
        get_route(predecessor, predecessor[int(i)], route)
        route.append(str(i))

def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    predecessor = [-1]*len(graph)

    pq = [(0, starting_vertex)]
    route=[]
    
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessor[int(neighbor)]=current_vertex
                
                heapq.heappush(pq, (distance, neighbor))

    for i in range(1, len(graph)):
        if i != starting_vertex and distances[str(i)] != sys.maxsize:
            get_route(predecessor, int(i), route)
            
            yield i,distances[str(i)],route  #incrementaly call in nra
            route.clear()
            
    return distances




def nra1(graph,source1,source2,source3):
    #upper and lower bounds dictionaries
    f_ub=dict()
    f_lb=dict()
    final_ub=dict() #there are nodes that all initial nodes have visited

    paths1={}
    paths2={}
    paths3={}
    #arrays for saving the element that we see in each res1,res2,res3
    r1_array=dict.fromkeys(graph, 0)
    r2_array=dict.fromkeys(graph, 0)
    r3_array=dict.fromkeys(graph, 0)
    #calculate distances for each initial node
    res1=calculate_distances(graph, source1)
    
    res2=calculate_distances(graph, source2)
    res3=calculate_distances(graph, source3)
    counter=0
    previous_m=0
    for i,j,k in zip(res1,res2,res3):
        
        a=str(i[0])
        b=str(j[0])
        c=str(k[0])
        paths1[str(i[0])]=(str(i[1]),str(i[2]))
        paths2[str(j[0])]=(str(j[1]),str(j[2]))
        paths3[str(k[0])]=(str(k[1]),str(k[2]))

        r1_array[a]=i[1]
        r2_array[b]=j[1]
        r3_array[c]=k[1]
        #calc lower bounds sums
        if a not in f_lb:
            f_lb[a]=i[1]
        else:
            f_lb[a]+=i[1]
        if b not in f_lb:
            f_lb[b]=j[1]
        else:
            f_lb[b]+=j[1]            
        if c not in f_lb:
            f_lb[c]=k[1]
        else:
            f_lb[c]+=k[1]

        # there are 3 possible situations:        
        #calc upper bounds sums 
        #1.We have see the element in one of three r1_array,r2_array,r3_array and not in f_ub
        
        if a not in f_ub:
            if a in r1_array or a in r2_array or a in r3_array:
                f_ub[a]=i[1]+j[1]+k[1]


        if b not in f_ub:
            if b in r1_array or b in r2_array or b in r3_array:
                f_ub[b]=i[1]+j[1]+k[1]


        if c not in f_ub:
            if c in r1_array or c in r2_array or c in r3_array:
                f_ub[c]=i[1]+j[1]+k[1]



        #2.We have see the element in two of three r1_array,r2_array,r3_array
        if a in r1_array and a in r2_array:
            f_ub[a]=r1_array[a]+r2_array[a]+k[1]
        elif a in r1_array and a in r3_array:
            f_ub[a]=r1_array[a]+r3_array[a]+j[1]
        else:
            f_ub[a]=r2_array[a]+r3_array[a]+i[1]


        if b in r1_array and b in r2_array:
            f_ub[b]=r1_array[b]+r2_array[b]+k[1]
        elif b in r1_array and b in r3_array:
            f_ub[b]=r1_array[b]+r3_array[b]+j[1]
        else:
            f_ub[b]=r2_array[b]+r3_array[b]+i[1]


        if c in r1_array and c in r2_array:
            f_ub[c]=r1_array[c]+r2_array[c]+k[1]
        elif b in r1_array and b in r3_array:
            f_ub[c]=r1_array[c]+r3_array[c]+j[1]
        else:
            f_ub[c]=r2_array[c]+r3_array[c]+i[1]




        #3.We have see the element in three of three r1_array,r2_array,r3_array
        if a in r1_array and a in r2_array and a in r3_array:
            final_ub[a]=max(r1_array[a],r2_array[a],r3_array[a])

        if b in r1_array and b in r1_array and b in r1_array:
            final_ub[b]=max(r1_array[b],r2_array[b],r3_array[b])
           
        if c in r1_array and c in r1_array and c in r1_array:
            final_ub[c]=max(r1_array[c],r2_array[c],r3_array[c])  


        if (max(f_lb, key=f_lb.get)>=max(final_ub, key=final_ub.get)):
            m=min(final_ub, key=final_ub.get)
            
            if m== previous_m:
                counter+=1
                if counter>=2000:
            
                    print("best meeting point:",m)
                    print("Shortest path distance:",final_ub[str(m)])
                    print("paths:")
                    print(paths1[str(m)])
                    print(paths2[str(m)])
                    print(paths3[str(m)])
                    return 
            else:
                counter=0
            
            previous_m=m
    
        
    


def main():      
        
        out=sys.argv[1]
        source1=sys.argv[2]
        source2=sys.argv[3]
        source3=sys.argv[4]


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


        
        nra1(graph,source1,source2,source3)





if __name__ == '__main__':
  
   main()

