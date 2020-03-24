from Ej4_b import histogram

items = [] 
  
# numero de elementos de la lista
n = int(input("Ingrese el numero de elementos que tenga la lista : "))
print("Escriba los numeros de la lista: ")
  
for i in range(0, n): 
    ele = int(input()) 
  
    items.append(ele) 

histogram(items)