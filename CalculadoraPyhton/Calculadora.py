import cmath

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero"
    else:
        return x / y

def complex_add(x, y):
    return complex(x) + complex(y)

def complex_subtract(x, y):
    return complex(x) - complex(y)

def complex_multiply(x, y):
    return complex(x) * complex(y

def complex_divide(x, y):
    if complex(y) == 0:
        return "Erro: Divisão por zero"
    else:
        return complex(x) / complex(y)

def main():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Adição de números complexos")
    print("6. Subtração de números complexos")
    print("7. Multiplicação de números complexos")
    print("8. Divisão de números complexos")

    escolha = input("Digite a opção (1/2/3/4/5/6/7/8): ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"Resultado: {add(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {subtract(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {multiply(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {divide(num1, num2)}")

    elif escolha in ['5', '6', '7', '8']:
        num1 = complex(input("Digite o primeiro número complexo (ex: 1+2j): "))
        num2 = complex(input("Digite o segundo número complexo (ex: 3+4j): "))

        if escolha == '5':
            print(f"Resultado: {complex_add(num1, num2)}")
        elif escolha == '6':
            print(f"Resultado: {complex_subtract(num1, num2)}")
        elif escolha == '7':
            print(f"Resultado: {complex_multiply(num1, num2)}")
        elif escolha == '8':
            print(f"Resultado: {complex_divide(num1, num2)}")

    else:
        print("Opção inválida")

if __name__ == "__main__":
    main()

