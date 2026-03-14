Clientes = []
Pets = []
Servicos = []

def Cadastrar_Clientes():
 Nome = input("Digite seu nome: ")
 Documento = input("Digite seu documento: ")
 Telefone = input("Digite seu telefone: ")
 Endereco = input("Digite seu endereço: ")

 Cliente = {
   "Nome" : Nome,
   "Documento" : Documento,
   "Telefone": Telefone,
   "Endereco": Endereco
 }

 Clientes.append(Cliente)


def Cadastrar_Pets():
    NomePet = input("Digite o nome do pet: ")
    Raca = input("Digite a raça do seu pet: ")
    Sexo = input("Digite o sexo: ")
    DocumentoDono = input("Digite o documento do dono: ")

    Dono_Encontrado = False

    for Cliente in Clientes:
     if Cliente["Documento"] == DocumentoDono:
       Dono_Encontrado = True
       break
     else:
       print("O dono não foi cadastrado, faça o cadastro primeiro para prosseguir com o cadastro do pet")
       return
     
    Pet = {
     "NomePet" : NomePet,
     "Raca" : Raca,
     "Sexo" : Sexo,
     "DocumentoDono": DocumentoDono
    }
    Pets.append(Pet)
    print("Cadastro do pet feito com sucesso!")

 
def Listar_Clientes():
  print("== Clientes Cadastrados ==")
  for Cliente in Clientes:
    print("Nome: ", Cliente["Nome"])
    print("Documento: ", Cliente["Documento"])
    print("Telefone: ", Cliente["Telefone"])
    print("Endereço: ", Cliente["Endereco"])
    print("------------------------------------")

def Listar_Pets():
  print("== Pets Cadastrados ==")
  for Pet in Pets:
   print("Nome: ", Pet["NomePet"])
   print("Raca: ", Pet["Raca"])
   print("Sexo: ", Pet["Sexo"])
   print("---------------------")

def Cadastar_Servicos():
 Servicos_Disponiveis = {
      1:{'nome': 'Banho','preco': 80},
      2:{'nome': 'Tosa','preco': 100},
      3:{'nome': 'Consulta','preco': 120},
      4:{'nome': 'Hospedagem','preco': 150},
    }
 
 Nome_Pet = input("Digite o nome do pet (ou digite 0 para sair): ") 
 
 print("== Serviços ==")
 print("1 - Banho: R$ 80 ")
 print("2 - Tosa: R$ 100 ")
 print("3 - Consulta: R$ 120 ")
 print("4 - Hospedagem: R$ 150 ")

 while True:
   try:
     OpcaoServico = int(input("Selecione um serviço ou (digite 0 para sair):"))
     if OpcaoServico ==0:
       break
     if OpcaoServico in Servicos_Disponiveis:
       servico ={
         "pet": Nome_Pet,
         "servico": Servicos_Disponiveis[OpcaoServico]["nome"],
         "preco": Servicos_Disponiveis[OpcaoServico]["preco"]
       }
       Servicos.append(servico)
       print("Serviço cadastrado com sucesso!")
     elif OpcaoServico not in Servicos_Disponiveis:
       print ("Serviço não disponivel!")
   except ValueError:
    print("Entrada invalida, Digite um numero.")
   
def Buscar_Pet():
 Opcao_Busca = input("Digite o nome do pet que você deseja pesquisar: ")
 for pet, servicos in zip( Pets,Servicos):
   if pet["NomePet"] == Opcao_Busca:
     print("Nome: ", pet["NomePet"])
     print("Raca: ", pet["Raca"])
     print("Sexo: ", pet["Sexo"])
     print("Serviços registrados:",Servicos)
     print("---------------------") 
     break
   else:
     print("Pet não encontrado")
     return

def Relatorio():
 for cliente, pet, servico in zip(Clientes,Pets,Servicos):
   print("Cliente:", cliente , "| Pet:", pet, "| Serviços:", servico)

  
def Exibir_Menu():
 print("== SISTEMA PETSHOP ==")
 print("1 - Cadastrar Cliente")
 print("2 - Casdastrar Pet")
 print("3 - Listar Clientes")
 print("4 - Listar pets")
 print("5 - Registrar serviço")
 print("6 - Exibir relatório")
 print("7 - Buscar pet")
 print("8 - Sair")
 



