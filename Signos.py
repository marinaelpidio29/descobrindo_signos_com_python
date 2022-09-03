from datetime import datetime

lista_signos = [
    {'nome': 'Aries', 'data_inicio': '21/03', 'data_fim': '20/04'},
    {'nome': 'Touro', 'data_inicio': '21/04', 'data_fim': '20/05'},
    {'nome': 'Gêmeos','data_inicio':'21/05', 'data_fim': '20/06'},
    {'nome': 'Câncer','data_inicio': '21/06', 'data_fim': '21/07'},
    {'nome': 'Leão', 'data_inicio': '22/07', 'data_fim': '22/08'},
    {'nome': 'Virgem', 'data_inicio': '23/08', 'data_fim': '22/09'},
    {'nome': 'Libra', 'data_inicio': '23/09', 'data_fim': '22/10'},
    {'nome': 'Escorpião', 'data_inicio': '23/10', 'data_fim': '21/11'},
    {'nome': 'Sagitário', 'data_inicio': '22/11' , 'data_fim':'21/12'},
    {'nome': 'Capricórnio', 'data_inicio': '22/12', 'data_fim': '20/01'},
    {'nome': 'Aquário', 'data_inicio': '21/01', 'data_fim': '19/02'},
    {'nome': 'Peixes', 'data_inicio': '20/02', 'data_fim': '20/03'}
]

def captura_data(data):
    return datetime.strptime(data, "%d/%m").date()

def descobrir_signo(data):
    for signo in lista_signos:
        if data >= captura_data(signo["data_inicio"]) and data <= captura_data(signo["data_fim"]):
            return signo["nome"]
    return "Signo não identificado"



if __name__== '__main__':
    try:
        data = input("Digite a data de nascimento (dd/mm/yyy):")
        data = captura_data(data[:5])
        print(descobrir_signo(data))
    except ValueError:
        print('Data inválida')