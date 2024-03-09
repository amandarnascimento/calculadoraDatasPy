from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta  # pip install python-dateutil

def calcular_diferenca_tempo(data1, data2, tempo):
    if tempo == "1":  # Anos
        diferenca_anos = data1.year - data2.year
        if data1.month < data2.month or (data1.month == data2.month and data1.day < data2.day):
            diferenca_anos -= 1
        return f"{diferenca_anos} anos"
    elif tempo == "2":  # Meses
        diferenca_anos = data1.year - data2.year
        diferenca_meses = data1.month - data2.month
        diferenca_total = diferenca_anos * 12 + diferenca_meses
        return f"{diferenca_total} meses"
    elif tempo == "3":  # Dias
        diferenca = data1 - data2
        return f"{diferenca.days} dias"

def adicionar_tempo(data_input, tempo, adicao):
    data = datetime.strptime(data_input, "%Y/%m/%d").date()
    
    if tempo == "1":
        nova_data = data + relativedelta(years=adicao)
        return f"Adicionado {adicao} anos: {nova_data.strftime('%d/%m/%Y')}"
    elif tempo == "2":
        nova_data = data + relativedelta(months=adicao)
        return f"Adicionado {adicao} meses: {nova_data.strftime('%d/%m/%Y')}"
    elif tempo == "3":
        nova_data = data + timedelta(days=adicao)
        return f"Adicionado {adicao} dias: {nova_data.strftime('%d/%m/%Y')}"

def subtrair_tempo(data_input, tempo, subtracao):
    data_atual = datetime.strptime(data_input, "%Y/%m/%d").date()
    if tempo == "1":  # Anos
        nova_data = data_atual - relativedelta(years=subtracao)
        return f"Subtraído {subtracao} anos: {nova_data.strftime('%d/%m/%Y')}"
    elif tempo == "2":  # Meses
        nova_data = data_atual - relativedelta(months=subtracao)
        return f"Subtraído {subtracao} meses: {nova_data.strftime('%d/%m/%Y')}"
    elif tempo == "3":  # Dias
        nova_data = data_atual - timedelta(days=subtracao)
        return f"Subtraído {subtracao} dias: {nova_data.strftime('%d/%m/%Y')}"

while True:    
    operacao = int(input("Escolha uma das opções:\n[1] - adição\n[2] - subtração\n"))
    tempo = input("Escolha o que você deseja alterar:\n[1] - Anos\n[2] - Meses\n[3] - Dias: ")

    if operacao == 1:
        adicao = int(input("Digite a quantidade para adicionar: "))
        data_input = input("Digite a data no formato: yyyy/mm/dd (ano, mês, dia): ")
        print(adicionar_tempo(data_input, tempo, adicao))
        
    elif operacao == 2:
        subtracao = int(input("Digite a quantidade para subtrair: "))
        data_input = input("Digite a data no formato: yyyy/mm/dd (ano, mês, dia): ")
        print(subtrair_tempo(data_input, tempo, subtracao))

    perg = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if perg == 'N':
        break
