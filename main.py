# Importando as funções dos outros arquivos

from soma import somar

from subtracao import subtrair

from multiplicacao import multiplicar

from divisao import dividir



def exibir_menu():

    print("\n=== CALCULADORA PYTHON ===")

    print("1. Soma (+)")

    print("2. Subtração (-)")

    print("3. Multiplicação (*)")

    print("4. Divisão (/)")

    print("0. Sair")



def main():

    while True:

        exibir_menu()

        

        opcao = input("Escolha uma opção: ")



        if opcao == '0':

            print("Saindo da calculadora... Até logo!")

            break



        if opcao not in ['1', '2', '3', '4']:

            print("Opção inválida! Tente novamente.")

            continue



        try:

            num1 = float(input("Digite o primeiro número: "))

            num2 = float(input("Digite o segundo número: "))

        except ValueError:

            print("Erro: Por favor, digite apenas números válidos.")

            continue



        resultado = 0



        if opcao == '1':

            resultado = somar(num1, num2)

            print(f"Resultado: {num1} + {num2} = {resultado}")



        elif opcao == '2':

            resultado = subtrair(num1, num2)

            print(f"Resultado: {num1} - {num2} = {resultado}")



        elif opcao == '3':

            resultado = multiplicar(num1, num2)

            print(f"Resultado: {num1} * {num2} = {resultado}")



        elif opcao == '4':

            resultado = dividir(num1, num2)

            if resultado is None:

                print("Erro: Não é possível dividir por zero!")

            else:

                print(f"Resultado: {num1} / {num2} = {resultado}")



if __name__ == "__main__":

    main()
