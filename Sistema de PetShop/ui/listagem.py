from repositories.dados import Clientes, Pets

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
