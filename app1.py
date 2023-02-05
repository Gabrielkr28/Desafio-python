import os

cwd = os.getcwd()

file_exists = os.path.exists('config.json')

if not file_exists:
    open("config.json", "x")

print('Escolha uma as opções: \n')
print('1 - Read configuration - (Escrever no arquivo)')
print('2 - Write configuration - (Ler arquivo)')

valor = input()

if valor != '1' and valor != '2':
    while (valor != '2') and (valor != '1'):
        print('Digite um valor entre 1 e 2!')
        valor = input()
elif valor == '1':
    if os.path.getsize("config.json") == 0:
        print('O arquivo está vazio!')
    else:
        fileRead = open("config.json", "r")
        print(fileRead.readlines())
elif valor == '2':
    print('Informe o nome do servidor:')
    name = input()
    print('Informe o IP do servidor:')
    ip = input()
    print('Informe a senha do servidor:')
    password = input()

if valor == '2':
    fileWrite = open("config.json", "w")
    fileWrite.write('"server_name":' + name)
    fileWrite.write('"server_ip":' + ip)
    fileWrite.write('"server_ip":' + password)
    print('Informações salvas com sucesso! \n')
    fileWrite = open("config.json", "r")
    print(fileWrite.readlines())
