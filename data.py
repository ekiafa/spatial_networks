#Eftihia Kiafa AM:3003
import sys 




def main():      
       
        nodes_file=sys.argv[1]
        edges_file=sys.argv[2]
        
        with open(nodes_file,mode='r') as nodes,open(edges_file,mode='r')as edges,open('out.txt',mode='w',encoding='UTF8') as out:
                #for line in nodes:
                    #print(line)
                global edges_array,seen_nodes
                edges_array=dict()
                seen_nodes=[]
                for line in edges:
                    a=line.split(" ")
                    a.remove(a[0])
                    if a[0] not in seen_nodes:
                        seen_nodes.append(a[0])
                        edges_array[a[0]]=[a[1],a[2]]
                    else:
                        edges_array[a[0]].append([a[1],a[2]])
                print(edges_array)




if __name__ == '__main__':
  
   main()

