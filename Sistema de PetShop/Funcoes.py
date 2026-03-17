Clientes = []
Pets = []
Servicos = []

def Cadastrar_Clientes():
 Nome = input("Digite o nome do cliente: ")
 Documento = input("Digite o documento do cliente: ")
 
 """Validação do Documento do cliente na hora do cadastro.
    Esse loop pega o documento digitado e compara com o que aparece dentro
    da lista Clientes, caso o documento apareça é enviado um mensagem de error
    como podemos ver na linha 15"""
 
 for Cliente in Clientes:
   if Cliente["Documento"] == Documento:
     print(" ERROR O cliente já está cadastrado!")
     return
   
 Telefone = input("Digite o telefone do cliente: ")
 Endereco = input("Digite o endereço do cliente: ")

 Cliente = {
   "Nome" : Nome,
   "Documento" : Documento,
   "Telefone": Telefone,
   "Endereco": Endereco
   }

 Clientes.append(Cliente)


def Cadastrar_Pets():
    NomePet = input("Digite o nome do pet: ")
    DocumentoDono = input("Digite o documento do dono: ")

    for Pet in Pets:
      if Pet["NomePet"] == NomePet and Pet["DocumentoDono"] == DocumentoDono:
       print("ERROR o Pet já está cadastrado em nosso sistema")
       return

    for Cliente in Clientes:
     if Cliente["Documento"] == DocumentoDono:
       break
    else:
     print("O dono não foi cadastrado. Cadastre o cliente primeiro.")
     return

    Raca = input("Digite a raça do seu pet: ")
    Sexo = input("Digite o sexo: ")

     
    Pet = {
     "NomePet" : NomePet,
     "Raca" : Raca,
     "Sexo" : Sexo,
     "DocumentoDono": DocumentoDono,
     "Servicos":[]
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

def Cadastrar_Servicos():
    Servicos_Disponiveis = {
        1: {'nome': 'Banho', 'preco': 80},
        2: {'nome': 'Tosa', 'preco': 100},
        3: {'nome': 'Consulta', 'preco': 120},
        4: {'nome': 'Hospedagem', 'preco': 150},
    }

    Nome_Pet = input("Nome do pet (0 para cancelar): ")
    if Nome_Pet == "0":
        return

    # Procura o pet
    for Pet in Pets:
        if Pet["NomePet"] == Nome_Pet:
            break
    else:
        print("Pet não encontrado!")
        return

    print("Serviços disponíveis:")
    for k, v in Servicos_Disponiveis.items():
        print(f"{k} - {v['nome']} R$ {v['preco']}")

    opcao = int(input("Escolha o serviço: "))
    if opcao in Servicos_Disponiveis:
        servico = Servicos_Disponiveis[opcao]
        Pet["Servicos"].append(servico)
        print("Serviço cadastrado com sucesso!")
    else:
        print("Serviço inválido!")
   
def Buscar_Pet():
    Documento_Busca = input("Digite o documento do dono: ")
    for Cliente in Clientes:
        if Cliente["Documento"] == Documento_Busca:
            print("Nome do Dono: ", Cliente["Nome"])
            for Pet in Pets:
                if Pet["DocumentoDono"] == Documento_Busca:
                    print("Nome do Pet: ", Pet["NomePet"])
                    print("Raca: ", Pet["Raca"])
                    print("Sexo: ", Pet["Sexo"])
                    if Pet["Servicos"]:
                        print("Serviços Cadastrados: ")
                        for servico in Pet["Servicos"]:
                            print(f"{servico['nome']} | {servico['preco']}")
                    else:
                        print("Nenhum serviço encontrado")
                        print("---------------------") 
                    break
            else:
                print("Pet não encontrado")
                print("---------------------") 
                return

def Relatorio():
 for Cliente in Clientes:
   print("Cliente: ", Cliente["Nome"])
   print("Documento: ",Cliente["Documento"])
   print("Telefone: ", Cliente["Telefone"])
   print("Endereço: ", Cliente["Endereco"])
   print(" ------------------------------- ")
   for Pet in Pets:
     if Pet["DocumentoDono"] == Cliente["Documento"]:
       print("Pet:", Pet["NomePet"])
       print("Raca: ", Pet["Raca"])
       print("Sexo: ", Pet["Sexo"])
       (" ------------------------------- ")
       if Pet["Servicos"]:
         print("Serviços realizados: ")
         for Servico in Pet["Servicos"]:
           print(f" - {Servico['nome']} | R$ {Servico['preco']}")
   else:
     print("Nenhum serviço cadastrado")
     print(" ------------------------------- ")
       
  
def Exibir_Menu():
 print("== SISTEMA PETSHOP ==")
 print("1 - Cadastrar Cliente")
 print("2 - Cadastrar Pet")
 print("3 - Listar Clientes")
 print("4 - Listar pets")
 print("5 - Registrar serviço")
 print("6 - Exibir relatório")
 print("7 - Buscar pet")
 print("8 - Sair")
 



