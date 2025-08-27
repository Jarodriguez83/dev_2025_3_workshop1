import random
class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
        Returns:
            str: "jugador1", "jugador2", "empate" o "invalid"
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
        """
        # Normalizamos las entradas
        j1 = jugador1.lower()
        j2 = jugador2.lower()
        # Validar entradas
        opciones = ["piedra", "papel", "tijera"]
        if j1 not in opciones or j2 not in opciones:
            return "invalid"
        # Caso empate
        if j1 == j2:
            return "empate"
        # Reglas del juego
        if (j1 == "piedra" and j2 == "tijera") or \
        (j1 == "tijera" and j2 == "papel") or \
        (j1 == "papel" and j2 == "piedra"):
            return "jugador1"
        else:
            return "jugador2"
    
    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe. 
        Args: 
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío) 
        Returns: 
            str: "X", "O", "empate" o "continua" 
        Ejemplo: 
            [["X", "X", "X"], 
            ["O", "O", " "], 
            [" ", " ", " "]] -> "X"
        """
       
        # --- 1. Verificación de Ganador ---
        
        # 1.1. Verificación de Filas
        for i in range(3):
            if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != " ":
                return tablero[i][0]

        # 1.2. Verificación de Columnas
        for j in range(3):
            if tablero[0][j] == tablero[1][j] == tablero[2][j] and tablero[0][j] != " ":
                return tablero[0][j]

        # 1.3. Verificación de Diagonales
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
            return tablero[0][0]
        
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
            return tablero[0][2]

        # --- 2. Verificación de Empate y Continuación ---
        
        hay_espacio_vacio = False
        for fila in tablero:
            if " " in fila:
                hay_espacio_vacio = True
                break
        
        if not hay_espacio_vacio:
            return "empate"
        
        # Si no hay ganador ni empate, el juego continúa
        return "continua"

    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind. 
        Args: 
            longitud (int): Número de posiciones en la combinación colores_disponibles 
            (list): Lista de colores disponibles 
        Returns: 
            list: Combinación de colores de la longitud especificada 
        Ejemplo: 
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) -> ["rojo", "azul", "rojo", "verde"]
        """
        return [random.choice(colores_disponibles) for _ in range(longitud)]
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal. 
        Args: 
            desde_fila (int): Fila inicial (0-7) desde_col 
            (int): Columna inicial (0-7) hasta_fila 
            (int): Fila destino (0-7) hasta_col 
            (int): Columna destino (0-7) 
            tablero (list): Matriz 8x8 representando el tablero 
        Returns: 
            bool: True si el movimiento es válido, False si no Reglas: 
        - La torre se mueve horizontal o verticalmente - No puede saltar sobre otras piezas
        """
        # Validar que las coordenadas estén dentro del tablero (0 a 7)
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 
                0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False
        # No permitir movimiento nulo
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        # Pieza inicial y destino
        pieza_inicial = tablero[desde_fila][desde_col]
        pieza_destino = tablero[hasta_fila][hasta_col]
        # No puede capturar su misma pieza
        if pieza_destino != " " and pieza_destino == pieza_inicial:
            return False
        # Movimiento horizontal
        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False
            return True
        # Movimiento vertical
        if desde_col == hasta_col:
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False
            return True
        # Si no es ni fila ni columna → inválido
        return False