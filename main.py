equipamentos = [{'nome': 'Kennedy', 'fabricante': 'GPA', 'modelo': 'Violeta', 'numero_de_serie': '12345KE', 'setor': 'Frente de Caixa', 'data_aquisicao': '22/09/2026', 'criticidade': 'média', 'status': 'operacional'}]

def cabecalho(nome):
  print("=" * 80)
  print("MAINTENANCECORE".center(80))
  print("Gestão de Manutenção Industrial".center(80))
  print("=" * 80)
  print(nome.center(80))
  print("=" * 80)

def exibir_lista(chave, valor):
  print(f"{chave} : {valor}")

def exibir_menu():

  cabecalho("Menu Principal")

  print("""
1. Equipamentos 
2. Chamados 
3. Ordens de Serviços 
4. Técnicos 
5. Estoque 
6. Manutenção Preventiva 
7. Relatórios 
8. Indicadores 
0. Sair 
      """)

def menu_principal():
  while True:
    
    exibir_menu();
    
    try:
      opcao = int(input("Escolha uma opção: "))
    except ValueError:
      print("Opcao Invalida.")
      input("Pressione ENTER para continuar...")
      continue

    #Sai do programa#
    if(opcao == 0):
      print("Saindo do programa...")
      break

    #Entra em Equipamentos#
    elif (opcao == 1):
      menu_equipamento()

    else:
      print("Opção Invalida. Digite alguma das opções")
      input("Pressione ENTER para continuar...")

########## PARTE DE EQUIPAMENTOS ##################################################################

def exibir_menu_equipamentos():
  cabecalho("Menu Equipamentos")
  print("""
1. Cadastrar Equipamento
2. Listar Equipamento
3. Consultar Equipamento
4. Editar Equipamento
5. Desativar Equipamento
6. Filtar Equipamento
7. Voltar
""")

def validar_criticidade():
  print("""
Criticidade:
1 - Baixa
2 - Média
3 - Alta
4 - Crítica
  """)

  while True:
    try:
      criticidade = int(input("Escolha a criticidade: "))
    except ValueError:
      print("Opcao Invalida.")
      input("Pressione ENTER para continuar...")
      continue

    if (criticidade == 1):
      return "baixa"
    elif (criticidade == 2):
      return "média"
    elif (criticidade == 3):
      return "alta"
    elif (criticidade == 4):
      return "crítica"
    else:
      print("Opção invalida\n")

def validar_status():
  print("""
Status:
1 - Operacional
2 - Em Manutenção
3 - Parado
4 - Desativado
  """)

  while True:
    try:
      status = int(input("Escolha o status: "))
    except ValueError:
      print("Opcao Invalida.")
      input("Pressione ENTER para continuar...")
      continue

    if (status == 1):
      return "operacional"
    elif (status == 2):
      return "em manutenção"
    elif (status == 3):
      return "parado"
    elif (status == 4):
      return "desativado"
    else:
      print("Opção invalida\n")

def cadastrar_equipamento():
  equipamento = {
    "nome" : input("Nome do equipamento: "),
    "fabricante" : input("Fabricante: "),
    "modelo" : input("Modelo: "),
    "numero_de_serie" : input("Número de Série: "),
    "setor" : input("Setor: "),
    "data_aquisicao" : input("Data de aquisição: "),
    
    "criticidade" : validar_criticidade(),
    "status" : validar_status()
  }
  
  db_equipamento_cria(equipamento)

############ BASE DE DADOS EQUIPAMENTO #####################################

def db_equipamento_cria(equipamento):
  equipamentos.append(equipamento)

def db_equipamento_lista():
  return equipamentos

def lista_de_equipamento(lista_equipamento):
  cabecalho("Lista de Equipamentos")
  for equipamento in lista_equipamento:
    print("-" * 80)
    for chave, valor in equipamento.items():
      exibir_lista(chave, valor)

def menu_equipamento():
  while True:

    exibir_menu_equipamentos()

    try:
      opcao = int(input("Escolha uma opção: "))
    except ValueError:
      print("Opcao Invalida.")
      input("Pressione ENTER para continuar...")
      continue
    
    #Sai do programa#
    if(opcao == 7):
      print("Voltando ao menu principal")
      break
    
    #Entra em Equipamentos#
    elif (opcao == 1):
      cadastrar_equipamento()

    elif (opcao == 2):
      lista_de_equipamento(db_equipamento_lista())
    
    else:
      print("Opção Invalida. Digite alguma das opções")
      input("Pressione ENTER para continuar...")

################ PROGRAMA PRINCIPAL ######################################

def main():
  menu_principal()

main()
