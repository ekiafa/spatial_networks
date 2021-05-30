#Eftihia Kiafa AM:3003
import sys 

def main():      
       
        nodes_file=sys.argv[1]
        edges_file=sys.argv[2]
        
        with open(nodes_file,mode='r') as nodes,open(edges_file,mode='r')as edges,open('out.txt',mode='w',encoding='UTF8') as out:

                edges_array=dict()
                seen_nodes=[]
                nodes_array=dict()
                for line in nodes:
                    a=line.split(" ")
                    nodes_array[a[0]]=(a[1],a[2])
                
                for line in edges:
                    a=line.split(" ")
                    a.remove(a[0])
                    if a[0] not in seen_nodes:
                        seen_nodes.append(a[0])                        
                        edges_array[a[0]]=[(a[1],a[2])]
                        if a[1] not in seen_nodes:
                            seen_nodes.append(a[1])
                            edges_array[a[1]]=[(a[0],a[2])]
                        else:
                            edges_array[a[1]].append((a[0],a[2]))
                        
                    else:
                        
                        edges_array[a[0]].append((a[1],a[2]))
                        if a[1] not in seen_nodes:
                            seen_nodes.append(a[1])
                            edges_array[a[1]]=[(a[0],a[2])]
                        else:
                            edges_array[a[1]].append((a[0],a[2]))
                for i in edges_array.items():
                    if nodes_array[i[0]]:
                        first_out = [item for t in i[1] for item in t]
                        new_out=[s.strip() for s in first_out]
                        sys.stdout=out
                        print(i[0],nodes_array[i[0]][0],nodes_array[i[0]][1].rstrip("\n"),' '.join(new_out))



if __name__ == '__main__':
  
   main()

