from ui.menu import Exibir_Menu
from ui.listagem import Listar_Clientes, Listar_Pets
from services.petshop_service import (
    Cadastrar_Clientes,
    Cadastrar_Pets,
    Cadastrar_Servicos,
    Relatorio,
    Buscar_Pet,
    Faturamento
)
while True:
 Exibir_Menu()
 opcao = input("Digite uma opção: ")

 if opcao == '1':
     Cadastrar_Clientes()
 elif opcao == '2':
     Cadastrar_Pets()
 elif opcao == '3':
    Listar_Clientes()
 elif opcao == '4':
    Listar_Pets()
 elif opcao == '5':
     Cadastrar_Servicos()
 elif opcao == '6':
     Relatorio()
 elif opcao =='7':
     Buscar_Pet()
 elif opcao == '8':
     Faturamento()
 elif opcao == '9':
     print("Saindo do Programa...")
     break
 else:
     print("Opção Invalida")