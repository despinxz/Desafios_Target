def inverter(string):
    """
    Recebe uma string e a retorna invertida.
    """

    new_string = ''

    for i in range(0, len(string)):
        new_string += string[len(string) - i - 1]

    return new_string


string = input()
print(inverter(string))
