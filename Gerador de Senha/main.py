# Imports

from os import system
import random

# Vars

caracteres_permitidos = ''
qntd_caracteres = 0
senha = []
continuar = 'y'
senhas_salvas = []

# Functions

def reiniciar():
    global caracteres_permitidos, qntd_caracteres, senha, continuar
    caracteres_permitidos = ''
    qntd_caracteres = 0
    senha = []
    continuar = 'y'

# Code
while continuar.lower() in 'y s':
    system('cls')
    caracteres_permitidos = str(input('Escolha os caracteres:\n > '))
    qntd_caracteres = int(input('Quantos caracteres terão:\n > '))
    while qntd_caracteres < len(caracteres_permitidos):
        qntd_caracteres = int(input('Entrada inválida!\n Digite um número maior ou igual a quantidade de caracteres da sua senha!\n > '))
    for i in range(qntd_caracteres):
        senha.append(caracteres_permitidos[random.randint(0, len(caracteres_permitidos) - 1)])
    senha = ''.join(senha)
    print(senha)
    continuar = str(input('Criar outra senha?\n > '))
    if continuar.lower() in 's y':
        senhas_salvas.append(senha)
        ver_senhas = str(input('Deseja ver as suas senhas anteriores?\n > '))
        if ver_senhas.lower() in 'y s':
            print('Senhas:\n','\n'.join(senhas_salvas))
            input()
        reiniciar()
