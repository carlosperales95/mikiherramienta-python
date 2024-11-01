import json
import re
import random

# This Python class defines a ChatBot that interacts with users by responding to their input based on predefined responses and scores.
class ChatBot():
    def __init__(self, resp_file, default_responses):
        """
        The function initializes attributes and loads responses from a JSON file.
        
        :param resp_file: The `resp_file` parameter is a file that contains responses for the chatbot. The `load_json` method is used to load these responses from the file into the chatbot's memory. This allows the chatbot to access a variety of responses to use during conversations with users
        :param default_responses: The `default_responses` parameter in the `__init__` method is likely a variable that stores some default responses for the conversation. These responses are used when the system does not have a specific response for a given input or scenario.
        It is passed as an argument to the `__init__`
        """
        self.TERMINATE_STRING = "adios"
        self.MENU_HINT = f'La conversacion acabara cuando se escriba la palabra \"{self.TERMINATE_STRING}\"'
        self.GOODBYE_MESSAGE = 'Adios, hasta la proxima!!'
        self.EMPTY_RESPONSE = "Tio me aburro, dime algo!"
        self.responses = self.load_json(resp_file)
        self.default_responses = default_responses

    def speak(self, content):
        """
        The function "speak" in Python prints a message with the prefix "Bot:" followed by the content provided as an argument.
        
        :param content: The `content` parameter in the `speak` method is a variable that holds the message or content that the bot will speak out. When you call the `speak` method and pass a message as the `content` argument, the bot will print out that message with the prefix "Bot
        """
        print(f"Bot: {content}")

    def ask_input(self):
        """
        The `ask_input` function prompts the user for input with the message "Tu: " and returns the input provided by the user.
        :return: The `input("Tu: ")` function is being returned. This function prompts the user to enter some input with the message "Tu: " and returns whatever the user types in.
        """
        return input("Tu: ")

    def load_json(self, file):
        """
        The function `load_json` reads and loads a JSON file.
        
        :param file: The `file` parameter in the `load_json` function is the file path to the JSON file that you want to load and parse. This function reads the contents of the specified JSON file and returns the parsed data as a Python dictionary
        :return: The function `load_json` is returning the contents of the JSON file `bot_responses` after loading it using the `json.load()` method.
        """
        with open(file) as bot_responses:
            return json.load(bot_responses)

    def random_string(self):
        """
        The `random_string` function randomly selects and returns a response from a list of default responses.
        :return: A random string from the `default_responses` list is being returned.
        """
        resp_count = len(self.default_responses)
        random_index = random.randrange(resp_count)
        return self.default_responses[random_index]

    def score_responses(self, words):
        """
        This function calculates a score for each response based on the presence of required words in the user input.
        
        :param words: It seems like you were about to provide some information about the 'words' parameter, but the content is missing. Could you please provide the details or let me know how I can assist you further with the 'score_responses' function?
        :return: The function `score_responses` returns a list of scores for each response based on the words provided as input.
        """
        score_list = []
        for response in self.responses:
            response_score = 0
            required_score = 0
            required_words = response["required_words"]
            
            if required_words:
                for word in words:
                    if word in required_words:
                        required_score += 1
                
            if required_score == len(required_words):
                for word in words:
                    if word in response["user_input"]:
                        response_score += 1
                score_list.append(response_score)
        return score_list
    
    def get_response(self, input):
        """
        The `get_response` function processes user input to determine the best response based on a scoring mechanism and returns the corresponding bot response.
        
        :param input: The `get_response` method takes an input message as a parameter. If the input message is empty, it returns `self.EMPTY_RESPONSE`. Otherwise, it splits the input message into words, converts them to lowercase, and scores the responses based on the words in the input message. It will then select the best response
        :return: The `get_response` method returns a response based on the input provided. If the input is empty, it returns `self.EMPTY_RESPONSE`. Otherwise, it processes the input, scores the responses, and returns the best response from the list of possible responses.
        If the best response has a score of 0, it returns a random string.
        """
        if input == "":
            return self.EMPTY_RESPONSE
        
        split_msg = re.split(r'\s+|[,;?!.-]\s*', input.lower())
        score_list = self.score_responses(split_msg)
        best_response = max(score_list)
        response_index = score_list.index(best_response)

        if best_response != 0:
            return self.responses[response_index]["bot_response"]

        return self.random_string()

    def run_bot(self):
        """
        The `run_bot` function displays a menu hint, prompts the user for input, responds based on the input until a termination string is entered, and then says a goodbye message.
        """
        print(f'\n{self.MENU_HINT}')
        while True:
            user_input = self.ask_input()
            if user_input == self.TERMINATE_STRING:
                self.speak(self.GOODBYE_MESSAGE)
                break
            self.speak(self.get_response(user_input))
    