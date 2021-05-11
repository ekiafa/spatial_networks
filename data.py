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
                #print(len(nodes_array))
                for line in edges:
                    a=line.split(" ")
                    a.remove(a[0])
                    if a[0] not in seen_nodes:
                        seen_nodes.append(a[0])
                        edges_array[a[0]]=[(a[1],a[2])]
                    else:
                        edges_array[a[0]].append((a[1],a[2]))
                #print(len(edges_array))
                #for i in nodes_array.items():#,edges_array.items()):
                #    print(i)
                for i in edges_array.items():
                    #print(i[0])
                    if nodes_array[i[0]]:
                        print(nodes_array[i[0]],i.values())



if __name__ == '__main__':
  
   main()

