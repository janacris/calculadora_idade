# Programa para calcular a idade do usuário

def calcular_idade(ano_nascimento):
    ano_atual = 2022
    return ano_atual - ano_nascimento

def main():
    nome = input("Digite seu nome completo: ")
    
    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            
            if 1922 <= ano_nascimento <= 2021:
                idade = calcular_idade(ano_nascimento)
                print(f"{nome}, você completou ou completará {idade} anos em 2022.")
                break
            else:
                print("Ano inválido. Por favor, digite um ano entre 1922 e 2021.")
                
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para o ano de nascimento.")

# Executa o programa
main()
