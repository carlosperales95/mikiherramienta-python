import json
import re
import random_res as rres

# AI Doc writer (mintlify)
def load_json(file):
    # cmd/ctrl + shift + .
    # With -> para abrir archivos
    with open(file) as bot_responses:
        # print(f"Cargando respuestas de {file}")
        return json.load(bot_responses)

responses = load_json('text_bot.json')

def get_response(input):
    if input == "":
        return "Tio me aburro, dime algo"
    
    split_msg = re.split(r'\s+|[,;?!.-]\s*', input.lower())
    score_list = []
    for response in responses:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]
        
        if required_words:
            for word in split_msg:
                if word in required_words:
                    required_score += 1
            
        if required_score == len(required_words):
            # In en for -> valor en lista
            for word in split_msg:
                # In en if -> evalua si valor en lista
                if word in response["user_input"]:
                    response_score += 1
            score_list.append(response_score)
        
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    if best_response != 0:
        return responses[response_index]["bot_response"]

    return rres.random_string()

def run_bot():
    print('\nLa conversacion acabara cuando se escriba la palabra \"adios\"')
    while True:
        user_input = input("Tu: ")
        if user_input == "adios":
            print("Bot: Adios, hasta la proxima!!")
            break
        print("Bot: ", get_response(user_input))
