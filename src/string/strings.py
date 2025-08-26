class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
        # Comparamos el texto con su inverso
        return texto_limpio == texto_limpio[::-1]
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        invertida = ""
        for caracter in texto:
            invertida = caracter + invertida  # Va agregando al inicio
        return invertida
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        vocales = "aeiouAEIOU"
        contador = 0
        for letra in texto:
            if letra in vocales:
                contador += 1
        return contador
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        vocales = "aeiouAEIOU"
        contador = 0
        for letra in texto:
            if letra.isalpha() and letra not in vocales:  # es letra y no es vocal
                contador += 1
        return contador
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
         # Convertimos a minúsculas y quitamos espacios
        t1 = texto1.replace(" ", "").lower()
        t2 = texto2.replace(" ", "").lower()
        
        # Ordenamos los caracteres y comparamos
        return sorted(t1) == sorted(t2)
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
         # Usamos split() para dividir el texto por espacios
        palabras = texto.split()
        
        # Retornamos cuántas palabras hay
        return len(palabras)
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        # Dividimos el texto en palabras
        palabras = texto.split()
        
        # Ponemos en mayúscula la primera letra de cada palabra
        palabras_mayus = [p[0].upper() + p[1:] if p else '' for p in palabras]
        
        # Reconstruimos la cadena
        return " ".join(palabras_mayus)
        
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        resultado = []
        anterior_espacio = False

        for c in texto:
            if c == " ":
                if not anterior_espacio:
                    resultado.append(c)   # agregamos un solo espacio
                    anterior_espacio = True
                # si ya había un espacio, no agregamos el duplicado
            else:
                resultado.append(c)
                anterior_espacio = False

        return "".join(resultado)
        
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
            # Editor: Jhon Rodriguez (26/08/2025)
        if not texto:  # si la cadena está vacía
            return False

        # si empieza con signo + o -, lo quitamos para verificar lo que queda
        if texto[0] in ['-', '+']:
            texto = texto[1:]

        # si después del signo está vacía (ej: "+" o "-"), no es un número
        if not texto:
            return False

        # recorremos cada carácter y validamos que sean dígitos (0-9)
        for c in texto:
            if c < '0' or c > '9':
                return False

        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        pass
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass