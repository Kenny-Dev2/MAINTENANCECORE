from database.bd_equipamento import db_equipamento_lista

from menus.cabecalho import cabecalho

from utils.exibir_lista import exibir_lista

def lista_de_equipamento():
  lista = db_equipamento_lista()

  cabecalho("Lista de Equipamentos")
  for equipamento in lista:
    print("-" * 80)
    for chave, valor in equipamento.items():
      exibir_lista(chave, valor)