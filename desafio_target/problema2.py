def fibonacci(input):
    """
    Recebe um int 'input' e retorna uma string informando se ele faz parte da sequência de Fibonacci ou não

    """
    # Caso base
    if input == 0 or input == 1:
        return True

    # Inicializa os dois primeiros termos da sequência
    x = 0
    y = 1

    # Enquanto y for menor do que input, calcula o próximo valor da sequência e atribui a y
    while y < input:
        x, y = y, x + y
        # Se y se igualar ao valor do input, ele faz parte da sequência de Fibonacci
        if y == input:
            f'{n} faz parte da sequência de Fibonacci.'

    # Se y passar do valor do input, ele não faz parte da sequência de Fibonacci
    return f'{n} não faz parte da sequência de Fibonacci.'


n = int(input())
print(fibonacci(n))
