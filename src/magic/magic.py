class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        if n < 0:
                raise ValueError("n debe ser un número entero no negativo")
        elif n == 0:
                return 0
        elif n == 1:
                return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
                a, b = b, a + b
        return b
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        secuencia = [0, 1]
        for _ in range(2, n):
            secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        # Revisar divisores desde 3 hasta sqrt(n), saltando pares
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        primos = []
        for i in range(2, n + 1):
            if self.es_primo(i):  # usamos la función definida antes
                primos.append(i)
        return primos
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n < 2:
            return False  # no hay números perfectos menores que 2

        suma_divisores = 0
        for i in range(1, n):
            if n % i == 0:  # si i es divisor
                suma_divisores += i

        return suma_divisores == n
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        if filas <= 0:
            return []

        triangulo = [[1]]  # primera fila

        for i in range(1, filas):
            fila_anterior = triangulo[-1]
            nueva_fila = [1]  # empieza con 1
            for j in range(1, len(fila_anterior)):
                nueva_fila.append(fila_anterior[j-1] + fila_anterior[j])
            nueva_fila.append(1)  # termina con 1
            triangulo.append(nueva_fila)

        return triangulo
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        if n == 0 or n == 1:
            return 1

        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
        
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        while b != 0:
            residuo = a % b
            a = b
            b = residuo
        return a
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        def mcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x
        
        if a == 0 or b == 0:
            return 0  # El MCM con 0 se define como 0
        
        return abs(a * b) // mcd(a, b)

    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        suma = 0
        while n > 0:
            digito = n % 10   # saco el último dígito
            suma += digito    # lo sumo
            n = n // 10       # quito el último dígito
        return suma
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
            # Contar la cantidad de dígitos
        digitos = len(str(n))
        suma = 0
        temp = n

        while temp > 0:
            digito = temp % 10       # tomo el último dígito
            suma += digito ** digitos
            temp = temp // 10        # quito el último dígito
        
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        n = len(matriz)
        if n == 0:
            return False
        
        # Verificar que sea cuadrada
        for fila in matriz:
            if len(fila) != n:
                return False
        
        # Suma de referencia (primera fila)
        suma_objetivo = sum(matriz[0])
        
        # Verificar filas
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
        
        # Verificar columnas
        for col in range(n):
            suma_col = sum(matriz[fila][col] for fila in range(n))
            if suma_col != suma_objetivo:
                return False
        
        # Verificar diagonal principal
        suma_diag1 = sum(matriz[i][i] for i in range(n))
        if suma_diag1 != suma_objetivo:
            return False
        
        # Verificar diagonal secundaria
        suma_diag2 = sum(matriz[i][n - 1 - i] for i in range(n))
        if suma_diag2 != suma_objetivo:
            return False
        
        return True