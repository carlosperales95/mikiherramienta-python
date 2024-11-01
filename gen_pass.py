import string as s
import secrets as sec

def generate_random_pass(length: int, symbols: bool, uppercase: bool):
    """
    The function generates a random password of a specified length with 
    optional symbols and uppercase letters.
    
    :param length: The `length` parameter specifies the length of the random password that will be generated
    :type length: int
    :param symbols: The `symbols` parameter in the `generate_random_pass` function is a boolean flag that determines whether symbols should be included in the generated password.
    If `symbols` is set to `True`, symbols such as `!@#$%^&*()` will be included in the pool of characters from which
    :type symbols: bool
    :param uppercase: The `uppercase` parameter in the `generate_random_pass` function determines whether uppercase letters should be included in the generated password. If `uppercase` is set to `True`, uppercase letters (A-Z) will be included in the pool of characters from which the random password is generated.
    If `uppercase
    :type uppercase: bool
    :return: The function `generate_random_pass` returns a randomly generated password based on the specified length, symbols, and uppercase parameters.
    """
    generated_pass = ""
    combi = s.ascii_lowercase + s.digits
    
    if uppercase:
        combi += s.ascii_uppercase

    if symbols:
        combi += s.punctuation

    for _, index in enumerate(range(length)):
        generated_pass += combi[sec.randbelow(len(combi))]
    return generated_pass
