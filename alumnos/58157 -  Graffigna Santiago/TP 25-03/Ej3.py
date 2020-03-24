def histogram(items):
    print("\n")
    for i in items:
        graph = ''
        times = i
        while( times > 0 ):
            graph += '*'
            times = times - 1
        print(graph)

#histogram([8, 5, 8, 15, 21])
items = [] 
  
# numero de elementos de la lista
n = int(input("Ingrese el numero de elementos que tenga la lista : ")) 
  
for i in range(0, n): 
    ele = int(input()) 
  
    items.append(ele) 

histogram(items)