
def calculadora():
    """
    Implementa uma calculadora simples com operações de soma, subtração,
    multiplicação e divisão. O programa lida com erros de entrada e divisão por zero.
    """
    while True:
        # Exibe o menu de opções para o usuário
        print("\n--- Calculadora Simples ---")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        print("---------------------------")

        # Solicita a escolha do usuário
        escolha = input("Escolha uma operação (1-5): ")

        # Verifica se o usuário quer sair
        if escolha == '5':
            print("Saindo da calculadora. Até mais!")
            break

        # Bloco try/except para lidar com erros de entrada de números
        try:
            # Pede os dois números ao usuário
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            # Realiza a operação com base na escolha do usuário
            if escolha == '1':
                resultado = num1 + num2
                print(f"O resultado da soma é: {resultado}")
            elif escolha == '2':
                resultado = num1 - num2
                print(f"O resultado da subtração é: {resultado}")
            elif escolha == '3':
                resultado = num1 * num2
                print(f"O resultado da multiplicação é: {resultado}")
            elif escolha == '4':
                # Bloco try/except específico para divisão por zero
                if num2 == 0:
                    print("Erro: Não é possível dividir por zero.")
                else:
                    resultado = num1 / num2
                    print(f"O resultado da divisão é: {resultado}")
            else:
                print("Opção inválida! Por favor, escolha um número de 1 a 5.")

        except ValueError:
            # Mensagem de erro para entradas que não são números
            print("Entrada inválida! Por favor, digite apenas números.")
        except Exception as e:
            # Mensagem de erro genérica para outros tipos de erro inesperados
            print(f"Ocorreu um erro inesperado: {e}")

# Inicia a calculadora
calculadora()