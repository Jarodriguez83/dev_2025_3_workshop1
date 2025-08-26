import math
class Stats:
    def promedio(self, numeros):
        """
        Calcula la media aritmética de una lista de números.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La media aritmética de los números
            
        Ejemplo:
            promedio([1, 2, 3, 4, 5]) -> 3.0
        """
        if len(numeros) == 0:   # evitar división por cero
            return 0
        
        suma = 0
        for num in numeros:
            suma += num
        
        return suma / len(numeros)
    
    def mediana(self, numeros):
        """
        Encuentra el valor mediano de una lista de números.
        Para listas con número par de elementos, retorna el promedio de los dos valores centrales.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: El valor mediano
            
        Ejemplo:
            mediana([1, 2, 3, 4, 5]) -> 3.0
            mediana([1, 2, 3, 4]) -> 2.5
        """
        if len(numeros) == 0:
            return 0
    
        numeros_ordenados = sorted(numeros)  # ordenamos la lista
        n = len(numeros_ordenados)
        medio = n // 2  # índice central
        
        if n % 2 == 1:  # si es impar
            return float(numeros_ordenados[medio])
        else:  # si es par
            return (numeros_ordenados[medio - 1] + numeros_ordenados[medio]) / 2
    
    def moda(self, numeros):
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        Si hay empate, retorna el primer valor encontrado.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: El valor más frecuente
            
        Ejemplo:
            moda([1, 2, 2, 3, 3, 3]) -> 3
        """
        if len(numeros) == 0:
            return None  # lista vacía
    
        max_repeticiones = 0
        valor_moda = numeros[0]
        
        for num in numeros:
            repeticiones = numeros.count(num)  # cuántas veces aparece num
            if repeticiones > max_repeticiones:
                max_repeticiones = repeticiones
                valor_moda = num
        
        return valor_moda
    
    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar de una lista de números.
        Usa la fórmula de desviación estándar poblacional.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La desviación estándar
            
        Ejemplo:
            desviacion_estandar([1, 2, 3, 4, 5]) -> 1.41...
        """
        if len(numeros) == 0:
            return 0.0
    
        # calcular promedio
        suma = 0
        for num in numeros:
            suma += num
        promedio = suma / len(numeros)
        
        # calcular suma de cuadrados de las diferencias
        suma_cuadrados = 0
        for num in numeros:
            suma_cuadrados += (num - promedio) ** 2
        
        # desviación estándar
        varianza = suma_cuadrados / len(numeros)
        return math.sqrt(varianza)
    
    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        La varianza es el cuadrado de la desviación estándar.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La varianza
            
        Ejemplo:
            varianza([1, 2, 3, 4, 5]) -> 2.0
        """
        if not numeros:
            return 0.0  # lista vacía → varianza cero
        
        media = sum(numeros) / len(numeros)
        suma_cuadrados = sum((x - media) ** 2 for x in numeros)
        return suma_cuadrados / len(numeros)
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: La diferencia entre max y min
            
        Ejemplo:
            rango([1, 5, 3, 9, 2]) -> 8
        """
        if not numeros:  # lista vacía
                return 0
        return max(numeros) - min(numeros)