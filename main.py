import modules.internet_test as it
import modules.bot as bot
import modules.gen_pass as gp
import os

# This Python class represents a tool called MikiHerramienta that offers options such as chatting with a bot, generating passwords, and testing internet speed.
class MikiHerramienta():
    def __init__(self):
        """
        This Python code snippet initializes various string constants and lists for a program related to a tool called "MIKIHERRAMIENTA" with options like chatting with a bot, generating passwords, and testing internet connectivity.
        """
        self.APP_TITLE = "MIKIHERRAMIENTA"
        self.PROMPT_CHOOSE_OPTION = "Que herramienta quieres usar? (0 para salir): "
        self.PROMPT_BACK_TO_MENU = "Haz click en cualquier tecla para volver al menu: "
        self.PROMPT_NAN = "Oye eso no es un numero! Intentalo de nuevo"
        self.EXIT_MSG = "Saliendo del programa..."
        self.OPTIONS = ["Chat con Bot", "Generar contraseñas", "Prueba de internet"]
        self.BOT_FILE = 'data/text_bot.json'
        self.DEFAULT_BOT_ANS = [
            "Yo ni idea de eso man, no estoy puesto",
            "No te entiendo un carajo, quieres vocalizar?",
            "Amigo no entiendo nada di lo ke me dise!",
            "Repite que no se que me estas contando"
        ]
        
    def back_to_menu(self):
        """
        The `back_to_menu` function takes user input to return to the main menu after clearing the screen.
        :return: the user input received from the prompt for going back to the menu.
        """
        u_input = input(f"\n{self.PROMPT_BACK_TO_MENU}")
        os.system("clear")
        return u_input

    def print_menu(self):
        """
        The `print_menu` function in Python prints a menu with options stored in the `OPTIONS` attribute of the class, preceded by the `APP_TITLE`.
        """
        print(f"######## {self.APP_TITLE} ########\n")
        for idx, o in enumerate(self.OPTIONS):
            print(f"{idx + 1}: {o}")

    def ask_input(self):
        """
        The function `ask_input` takes user input, validates it, and returns the input as an integer if it is within a specified range.
        :return: The `converted_input` variable is being returned.
        """
        while True:
            menu_input = input(self.PROMPT_CHOOSE_OPTION)
            try:
                converted_input = int(menu_input)
                if converted_input < 0 or converted_input > len(self.OPTIONS):
                    print(f"\nEl numero: {converted_input} no es una opcion valida!\n")
                    continue
                return converted_input
            except:
                print(f"\n{self.PROMPT_NAN}\n")
                continue

    def chat_with_bot(self):
        """
        This function initializes a chatbot object and runs the chatbot.
        """
        my_bot = bot.ChatBot(self.BOT_FILE, self.DEFAULT_BOT_ANS)
        my_bot.run_bot()
    
    def gen_secure_passwords(self):
        """
        The function `gen_secure_passwords` generates and prints five secure passwords with a length of 20 characters containing symbols and uppercase letters.
        """
        print("\n")
        for _, index in enumerate(range(5)):
            password = gp.generate_random_pass(length=20, symbols=True, uppercase=True)
            print(index + 1, "::", password)

    def test_my_speed(self):
        """
        The function `test_my_speed` creates an instance of `InternetTest` and performs a full test.
        """
        my_it = it.InternetTest()
        my_it.full_test()

    def run(self):
        """
        The `run` function displays a menu, prompts the user for input, and executes different actions based on the selected option until the user chooses to exit.
        """
        while True:
            self.print_menu()
            selected_option = self.ask_input()

            if selected_option == 0:
                print(f"\n{self.EXIT_MSG}")
                break

            if selected_option == 1:
                self.chat_with_bot()
            
            if selected_option == 2:
                self.gen_secure_passwords()
            
            if selected_option == 3:
                self.test_my_speed()
                
            if self.back_to_menu():
                    continue

# Main function
if __name__ == "__main__":
    mh = MikiHerramienta()
    mh.run()