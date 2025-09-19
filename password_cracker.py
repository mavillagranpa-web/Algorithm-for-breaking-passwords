import time
import matplotlib.pyplot as plt
from itertools import product

# Frase célebre de Itachi Uchiha
print("Soy… el fantasma de los Uchiha")  # "People's lives don't end when they die. It ends when they lose faith."

# Diccionario de mi alfabeto - El conocimiento es poder como diría Lelouch vi Britannia
Names = {
    1: "abcdefghijklmnopqrstuvwxyz",  # letras minúsculas - el alfabeto de los mortales
    2: "ABCDEFGHIJKLMNOPQRSTUVWXYZÑ",  # letras mayúsculas - el alfabeto de los dioses
    3: "0123456789",                   # números - el lenguaje universal
    4: "!@#$%^&*()-_=+,|{};:/?.",     # caracteres especiales - los sellos de jutsu
}

print("Conjuntos disponibles:", Names)  # "Todo el conocimiento del mundo a tu disposición" - Light Yagami

# Combinar todos los caracteres en un solo alfabeto - Como los poderes combinados en Fairy Tail
alfabeto = list(Names[1] + Names[2] + Names[3] + Names[4])

# Listas para almacenar datos para la gráfica - Los registros de batalla como en Attack on Titan
almacen = []  # tiempos - La cuarta dimensión como en Stein's Gate
inte = []     # intentos - Cada intento acerca más a la victoria como en Haikyuu!!

salir = "si"
salir = input("¿Desea ingresar más datos si/no? ")  # "La curiosidad es el motor del progreso" - Senku (Dr. Stone)

while salir.lower() == "si":
    # Definir la contraseña de prueba - El enigma a resolver como en Death Note
    contraseña = input("Ingrese una contraseña de prueba: ")

    # Verificar que todos los caracteres estén en el alfabeto - Como comprobar el terreno de batalla
    for ch in contraseña:
        if ch not in alfabeto:
            print(f"El carácter '{ch}' no está en el alfabeto definido. Agrega ese carácter al alfabeto o cambia la contraseña.")
            break  # "Un plan perfecto requiere todos los elementos en su lugar" - Lelouch

    # Contador para los intentos - Cada intento es un paso más cerca de descubrir la verdad
    intentos = 0
    encontrada = False  # "La verdad está ahí fuera" - X Files

    # Medir tiempo de inicio - Comienza la cuenta regresiva como en Attack on Titan
    inicio_total = time.perf_counter()

    #  - Fuerza bruta estilo One Punch Man
    for longitud in range(1, len(contraseña) + 1):
        for combo in product(alfabeto, repeat=longitud):
            intentos += 1  # "¡Plus Ultra!" - My Hero Academia (cada intento nos hace más fuertes)
            intento = "".join(combo)

            if intento == contraseña:
                encontrada = True  # "¡He encontrado el One Piece!" - Monkey D. Luffy
                break  # Misión cumplida

        if encontrada:
            break  # "El que persevera alcanza" - Naruto Uzumaki

    # Medir tiempo final - Fin de la batalla
    fin_total = time.perf_counter()
    tiempo_total = fin_total - inicio_total

    # Almacenar resultados - Registrar la victoria en los anales de la historia
    if encontrada:
        print("Contraseña encontrada:", contraseña)  # "El enigma ha sido resuelto" - Conan Edogawa
        print("Intentos realizados:", intentos)  # "Cuantos más intentos, más gloriosa es la victoria" - Erwin Smith
        print("Tiempo de ejecución: {:.6f} segundos".format(tiempo_total))  # "El tiempo no espera a nadie" - Tokyo Revengers
        almacen.append(tiempo_total)  # Añadir a los archivos históricos
        inte.append(intentos)  # Cada número cuenta una historia de perseverancia
    else:
        print("No se encontró la contraseña.")  # "A veces, la derrota enseña más que la victoria" - Rock Lee
        print("Intentos:", intentos)  # "El verdadero fracaso es no intentarlo" - Goku
        print("Tiempo: {:.6f} segundos".format(tiempo_total))  # "El tiempo perdido nunca se recupera" - Homura Akemi

    respeto = input("¿Desea ingresar más datos s/n? ")  # "¿Continuamos esta batalla?" - Levi Ackerman

# Mostrar resultados finales - El resumen de nuestras hazañas
print("\nResultados almacenados:")  # "Los registros de nuestras batallas" - Historia Reiss
print("Tiempos:", almacen)  # La línea temporal de nuestros esfuerzos
print("Intentos:", inte)  # El camino recorrido hacia la victoria

#  Visualizar nuestro progreso como en Dr. Stone
plt.plot(almacen, inte, color='purple', linewidth=2, marker='o')  # Línea púrpura como el Sharingan de Sasuke
plt.yscale("log")  # Escala logarítmica - "Para ver más allá de lo evidente" - Satoru Gojo

# Añadir etiquetas - "Etiquetar es comprender" - Shiroe (Log Horizon)
plt.xlabel("Tiempo (segundos)")  # "El inexorable flujo del tiempo" - Hit (Dragon Ball Super)
plt.ylabel("Intentos (escala logarítmica)")  # "La escala de nuestros esfuerzos" - All Might
plt.title("Crecimiento de Intentos vs Tiempo")  # "La relación entre esfuerzo y tiempo" - Jiraiya

# Mostrar la gráfica - Revelar la verdad oculta
plt.grid(True, which="both", linestyle='--', alpha=0.7)  # Una red como la de un cazador - Hunter x Hunter
plt.show()  # "¡Mira esto! Es el resultado de nuestro trabajo" - Edward Elric

# Frases finales épicas
print("Lo has logrado Madara, has adivinado la clave")  # "Incluso los dioses pueden ser derrotados" - Kratos 
print("Soy humano. Pero... También soy aquel que se alza en la cima de todas las razas... ¡Soy el León del Orgullo, pueden llamarme... Su majestad Escanor!")  # Quién no ama a Escanor
