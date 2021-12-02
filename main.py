def main():
   valor = 0
   while valor < 1:
      valor = int(input("Introduce un numero natural"))

   i = 0
   total = 0
   print("Lista de valores:")
   while total+i < valor:
      total = total + i
      print(i)
      i += 1


   print("Total de la suma: ",total)
if __name__ == '__main__':
   main()

