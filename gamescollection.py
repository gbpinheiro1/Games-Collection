# SISTEMA PARA COLECIONADORES DE GAMES

#Arquivo para armazenar os dados cadastrados
file = 'games.txt'

#Verificar se o arquivo existe
def file_exists(file_name):
    try:
        f = open(file_name, 'rt') #Apenas leitura (read)
        f.close()

    except FileNotFoundError:
        return False

    else:
        return True
    
#Função para criar o arquivo, caso ele não exista
def create_file(file_name):
    try:
        f = open(file_name, 'wt+') #Escrita e modificação
        f.close()

    except:
        print('Erro na criação do arquivo.\n')

    else:
        print(f'Arquivo {file_name} criado com sucesso!\n')


if file_exists(file):
    print('Lista de games encontrada no sistema!')

else:
    print('Lista de games não encontrada no sistema! Criando uma... ')
    create_file(file)
        



print('--- COLEÇÃO DE GAMES --- \n') 
print('1- Cadastrar um Jogo Novo')
print('2- Listar os Jogos Cadastrados')
print('3- Descobrir os seus Consoles Preferidos')
print('4- Sair \n')

#Validação da escolha do usuário
while True: 
    option = input('Digite o número da opção que você deseja utilizar: ')

    if(option == '1'):
        game_name = input('\nQual é o nome do jogo que você deseja cadastrar? ')
        console_name = input('\nE em qual console você jogou ele? ')
        print('\nJogo Cadastrado!\n')

    elif(option == '2'):
        print('Lista dos jogos cadastrados')

    elif(option=='3'):
        print('Dados dos Consoles Preferidos')

    elif(option=='4'):
        print('\nObrigado por utilizar nosso sistema! Volte aqui quando tiver novos jogos para cadastrar!')
        break

    else:
        print('Ops! Opção inválida! Tente Novamente.')

    




