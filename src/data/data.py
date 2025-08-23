class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        # Editor: Jhon Rodriguez (23/08/2025)
        # Creamos una nueva lista vacía para ir guardando los elementos al revés
        invertida = []
        # Recorremos la lista original desde el último elemento hasta el primero
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        # Retornamos la lista invertida
        return invertida
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        # Editor: Jhon Rodriguez (23/08/2025)
        # Recorremos la lista elemento por elemento
        for i in range(len(lista)):
            # Comparamos el elemento actual con el que buscamos
            if lista[i] == elemento:
                return i  # Retornamos el índice si lo encontramos
        # Si no se encontró, devolvemos -1
        return -1
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        resultado = []
        for elemento in lista:
            duplicado = False
            for e in resultado:
                if e == elemento and type(e) == type(elemento):  
                    # Verifica igualdad de valor y mismo tipo
                    duplicado = True
                    break
            if not duplicado:
                resultado.append(elemento)
        return resultado
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
        Returns:
            list: Lista combinada y ordenada
        """
        # Editor: Jhon Rodriguez (23/08/2025)
        i, j = 0, 0
        resultado = []
        # Recorremos ambas listas hasta que una se acabe
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        # Agregamos los elementos restantes de lista1 o lista2
        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1
        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1
        return resultado
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
        Returns:
            list: Lista rotada
        """
        # Editor: Jhon Rodriguez (23/08/2025)
        if not lista:
            return []
        n = len(lista)
        k = k % n  # Para evitar rotaciones mayores al tamaño de la lista
        # Rotamos dividiendo en dos partes
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante 
        Returns:
            int: El número que falta en la secuencia
        """
        # Editor: Jhon Rodriguez (23/08/2025)
        n = len(lista) + 1  # Porque falta uno
        suma_esperada = n * (n + 1) // 2  # Fórmula de Gauss
        suma_real = sum(lista)
        return suma_esperada - suma_real
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        # Editor: Jhon Rodriguez (23/08/2025)
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        # Editor: Jhon Rodriguez (23/08/2025)
        pila = []
        def push(elemento):
            pila.append(elemento)
        def pop():
            if not pila:
                return None  # Si está vacía no se puede extraer
            return pila.pop()
        def peek():
            if not pila:
                return None  # Si está vacía no hay elemento en la cima
            return pila[-1]
        def is_empty():
            return len(pila) == 0
        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        # Editor: Jhon Rodriguez (23/08/2025)
        cola = []
        def enqueue(elemento):
            cola.append(elemento)  # Agrega al final de la lista
        def dequeue():
            if not cola:
                return None  # Si está vacía, no hay nada que sacar
            return cola.pop(0)  # Saca el primero en entrar
        def peek():
            if not cola:
                return None  # Si está vacía, no hay elemento al frente
            return cola[0]  # Devuelve el primero en entrar sin quitarlo
        def is_empty():
            return len(cola) == 0  # True si está vacía
        return {
            "enqueue": enqueue,
            "dequeue": dequeue,
            "peek": peek,
            "is_empty": is_empty
        }
        
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        Args:
            matriz (list): Lista de listas que representa una matriz
        Returns:
            list: Matriz transpuesta
        """
        if not matriz:  # matriz vacía
            return []
        filas = len(matriz)
        columnas = len(matriz[0])
        # Creamos la nueva matriz con dimensión invertida
        transpuesta = []
        for j in range(columnas):
            nueva_fila = []
            for i in range(filas):
                nueva_fila.append(matriz[i][j])
            transpuesta.append(nueva_fila)
        return transpuesta