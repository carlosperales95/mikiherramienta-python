import internet_test as it
import bot
import gen_pass as gp
import os

def back_to_menu():
    u_input = input("\nHaz click en cualquier tecla para volver al menu: ")
    os.system("clear")
    return u_input


while True:
    print("######## MIKIHERRAMIENTA ########")
    print("Que herramienta quieres usar? (0 para salir)")
    print("1) Chat con Bot")
    print("2) Generar contraseñas")
    print("3) Prueba de internet")
    menu_input = input()

    try:
        converted_input = int(menu_input)
    except:
        print("\nOye eso no es un numero!")
        continue

    if converted_input == 0:
        print("\nSaliendo del programa...")
        break
    
    if converted_input == 1:
        bot.run_bot()
        if back_to_menu():
            continue
    
    if converted_input == 2:
        gp.give_me_five_pass()
        if back_to_menu():
            continue
    
    if converted_input == 3:
        it.test_my_speed()
        if back_to_menu():
            continue
