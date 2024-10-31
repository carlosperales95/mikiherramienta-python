import internet_test as it
import bot
import gen_pass as gp
import os

# Funcion de input para volver al menu
def back_to_menu():
    u_input = input("\nHaz click en cualquier tecla para volver al menu: ")
    os.system("clear")
    return u_input

# Funcion de print del menu y opciones
def print_menu(options):
    print("######## MIKIHERRAMIENTA ########\n")
    for idx, o in enumerate(options):
        print(f"{idx + 1}: {o}")

# Funcion de peticion de input y validacion de opciones
def ask_input(options):
    while True:
        menu_input = input("Que herramienta quieres usar? (0 para salir): ")
        try:
            converted_input = int(menu_input)
            if converted_input < 0 or converted_input > len(options):
                print(f"\nEl numero: {converted_input} no es una opcion valida!\n")
                continue
            return converted_input
        except:
            print("\nOye eso no es un numero! Intentalo de nuevo\n")
            continue

def main():
    while True:
        options = ["Chat con Bot", "Generar contraseñas", "Prueba de internet"]
        print_menu(options)

        # Pedir y validar input
        selected_option = ask_input(options)

        # Ejecutar en base al input
        if selected_option == 0:
            print("\nSaliendo del programa...")
            break
        
        if selected_option == 1:
            bot.run_bot()
            if back_to_menu():
                continue
        
        if selected_option == 2:
            gp.give_me_five_pass()
            if back_to_menu():
                continue
        
        if selected_option == 3:
            it.test_my_speed()
            if back_to_menu():
                continue

# Main func
if __name__ == "__main__":
    main()