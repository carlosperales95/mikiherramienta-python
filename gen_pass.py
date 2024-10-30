import string as s
import secrets as sec

def generate_random_pass(length: int, symbols: bool, uppercase: bool):
    generated_pass = ""
    combi = s.ascii_lowercase + s.digits
    
    if uppercase:
        combi += s.ascii_uppercase

    if symbols:
        combi += s.punctuation

    for _, index in enumerate(range(length)):
        generated_pass += combi[sec.randbelow(len(combi))]

    return generated_pass

def give_me_five_pass():
    print("\n")
    for _, index in enumerate(range(5)):
        password = generate_random_pass(length=20, symbols=True, uppercase=True)
        print(index + 1, "::", password)