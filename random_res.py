import random

def random_string():
    possible_resp = [
        "Yo ni idea de eso man, no estoy puesto",
        "No te entiendo un carajo, quieres vocalizar?",
        "Amigo no entiendo nada di lo ke me dise!",
        "Repite que no se que me estas contando"
    ]

    resp_count = len(possible_resp)
    random_index = random.randrange(resp_count)

    return possible_resp[random_index]

