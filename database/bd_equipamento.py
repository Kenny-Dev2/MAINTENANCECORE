EQUIPAMENTOS = [{'id': 1, 'codigo': 'EQP-01', 'nome': 'Forno', 'fabricante': 'Kennedy', 'modelo': 'V8', 'numero_de_serie': '584568', 'setor': 'Padaria', 'data_aquisicao': '02/10/2026', 'criticidade': 'média', 'status': 'operacional'}]

def db_equipamento_cria(equipamento):
  EQUIPAMENTOS.append(equipamento)

def db_equipamento_lista():
  return EQUIPAMENTOS