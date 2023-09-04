#1. Escreva uma função recursiva em Python que calcule a soma dos primeiros N números inteiros positivos.
def soma_primeiros_n_inteiros(N):
    if N == 1:
        return 1
    else:
        return N + soma_primeiros_n_inteiros(N - 1)
N = int(input("Digite um número inteiro positivo N: "))
if N <= 0:
    print("N deve ser um número inteiro positivo.")
else:
    resultado = soma_primeiros_n_inteiros(N)
    print(f"A soma dos primeiros {N} números inteiros positivos é {resultado}")

#2. Escreva uma função recursiva para calcular o número fatorial de um número inteiro positivo.
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
n = int(input("Digite um número inteiro positivo: "))
if n < 0:
    print("O número deve ser inteiro positivo.")
else:
    resultado = fatorial(n)
    print(f"O fatorial de {n} é {resultado}")

#3. Escreva uma função que use uma pilha para inverter uma string.
def inverter_string(string):
    pilha = []

    for char in string:
        pilha.append(char)

    string_invertida = ""
    while pilha:
        string_invertida += pilha.pop()

    return string_invertida

string_original = input("Digite uma palavra: ")
string_invertida = inverter_string(string_original)
print("Palavra original:", string_original)
print("Palavra invertida:", string_invertida)

#4. Escreva uma função que converte um número decimal em sua representação binária usando uma pilha.
def decimal_para_binario(decimal):
    if decimal == 0:
        return "0"

    pilha = []
    while decimal > 0:
        resto = decimal % 2
        pilha.append(resto)
        decimal //= 2

    binario = "".join(map(str, reversed(pilha)))
    return binario

decimal = int(input("Digite um número decimal: "))
binario = decimal_para_binario(decimal)
print(f"A representação binária de {decimal} é {binario}")

#5. Implemente um histórico de comandos de um editor de texto simples usando uma pilha. A cada vez que um comando é executado, ele é adicionado à pilha. Implemente a capacidade de desfazer um comando usando a pilha.
historico_comandos = []
texto = ""

def executar_comando(comando):
    global texto
    texto += comando
    historico_comandos.append(comando)

def desfazer():
    global texto
    if historico_comandos:
        comando_desfeito = historico_comandos.pop()
        texto = texto[:-len(comando_desfeito)]

def exibir_texto():
    print(texto)

# Exemplo de uso:
executar_comando("Texto 1, ")
executar_comando("Texto 2, ")
executar_comando("Texto 3 ")

print("Texto atual:")
exibir_texto()

print("\nDesfazendo um comando:")
desfazer()
exibir_texto()

print("\nDesfazendo outro comando:")
desfazer()
exibir_texto()