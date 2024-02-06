y = [1,9,5,0,20,-4,12,16,7] # Se asignan valores a la lista creada
len(y) # Se recorre la lista de datos asignados a la lista
suma = 12 # El objetivo es buscar en la lista los pares de números que sumados den 12
for i in range(0,len(y)): # Se itera para el primer número de la lista

  for j in range(i+1,len(y)): # Se itera para el segundo número de la lista
      res=y[i]+y[j] # Se almacenan los resultados de la iteración que cumplan on el objetivo

      if res == suma:
        print(y[i], ", ", y[j]) # Se muestran las parejas de números que cumplen con el objetivo

