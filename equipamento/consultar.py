from database.bd_equipamento import db_equipamento_lista

from utils.exibir_lista import exibir_lista

def buscar_equipamento(campo, valor_procurado, lista_equipamento):
  equipamento_encontrado = []

  for equipamento in lista_equipamento:
    if str(equipamento[campo]).lower() == str(valor_procurado).lower():
      equipamento_encontrado.append(equipamento)

  return equipamento_encontrado

def consultar_equipamento():
  print("""
Consultar Equipamento por:

1 - ID
2 - Código
3 - Nome
4 - Fabricante
5 - Modelo
6 - Número de série
7 - Setor
8 - Criticidade
9 - Status

""")

  campo = {
    1: "id",
    2: "codigo",
    3: "nome",
    4: "fabricante",
    5: "modelo",
    6: "numero_de_serie",
    7: "setor",
    8: "criticidade",
    9: "status"
  }

  try:
    opcao = int(input("Escolha um campo: "))
  except ValueError:
    print("Opção Invalida")
    return

  if opcao not in campo:
    print("opção Invalida")
    return

  valor = input("Digite o valor para pesquisar: ")

  equipamentos = buscar_equipamento(campo[opcao], valor, db_equipamento_lista())

  if not equipamentos:
    print("Nenhum equipamento encontrado")
    return

  for equipamento in equipamentos:
    print("-" * 80)
    for chave, valor in equipamento.items():
      exibir_lista(chave, valor)