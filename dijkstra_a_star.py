import sys 





def main():      
       
        out=sys.argv[1]
        start=sys.argv[2]
        finish=sys.argv[3]

        with open('out.txt' ,mode='r') as pointers:
            for line in pointers:
                print(line)
















if __name__ == '__main__':
  
   main()

