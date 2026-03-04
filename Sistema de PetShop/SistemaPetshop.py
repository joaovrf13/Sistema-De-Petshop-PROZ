from Funcoes import Exibir_Menu, Cadastrar_Clientes, Cadastrar_Pets, Listar_Clientes, Listar_Pets

Exibir_Menu()

while True:
 opcao = input("Digite uma opção: ")
 if opcao == '1':
     Cadastrar_Clientes()
     Exibir_Menu()
 elif opcao == '2':
     Cadastrar_Pets()
     Exibir_Menu()
 elif opcao == '3':
    Listar_Clientes()
    Exibir_Menu()
 elif opcao == '4':
    Listar_Pets()
    Exibir_Menu()
 else:
     Exibir_Menu()
