def fibo(n,a=0,b=1):
   while n!=0:
      return fibo(n-1,b,a+b)
   return a

for i in range(0,10):
   print(fibo(i))

#Imprime la suma de los numeros anteriores hasta llegar al decimo lugar (Serie de Fibonacci)