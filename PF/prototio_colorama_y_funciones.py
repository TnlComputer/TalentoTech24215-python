import colorama
from colorama import Fore, Style

# Inicializa colorama
colorama.init(autoreset=True)

def mostrar_menu():
    print(Fore.GREEN + "=== Menú Principal ===")
    print(Fore.YELLOW + "1. Opción 1")
    print(Fore.YELLOW + "2. Opción 2")
    print(Fore.YELLOW + "3. Opción 3")
    print(Fore.RED + "4. Salir")
    print(Style.RESET_ALL)  # Resetea el estilo de texto a su valor predeterminado

def elegir_opcion():
    opcion = input(Fore.CYAN + "Elige una opción: ")
    return opcion

def ejecutar_opcion(opcion):
    if opcion == '1':
        print(Fore.GREEN + "Has elegido la Opción 1")
    elif opcion == '2':
        print(Fore.GREEN + "Has elegido la Opción 2")
    elif opcion == '3':
        print(Fore.GREEN + "Has elegido la Opción 3")
    elif opcion == '4':
        print(Fore.RED + "Saliendo...")
        exit()
    else:
        print(Fore.RED + "Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = elegir_opcion()
        ejecutar_opcion(opcion)
