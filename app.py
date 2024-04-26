from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

# Carrega os dados do arquivo CSV
def carregar_dados_csv(nome_arquivo):
    with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        dados = [linha for linha in leitor_csv]
    return dados

dados_atendimentos = carregar_dados_csv('atendimentos.csv')

# Definir rota para o endpoint /api/v1/atendimentos
@app.route('/api/v1/atendimentos', methods=['GET'])
def buscar_atendimentos():
    # Obtem parâmetros de consulta da URL
    data_atendimento = request.args.get('data_atendimento')
    condicao_saude = request.args.get('condicao_saude')
    unidade = request.args.get('unidade')

    # Filtra os dados conforme os parâmetros fornecidos
    resultados = dados_atendimentos
    if data_atendimento:
        resultados = [atendimento for atendimento in resultados if atendimento['data_atendimento'] == data_atendimento]
    if condicao_saude:
        resultados = [atendimento for atendimento in resultados if atendimento['condicao_saude'] == condicao_saude]
    if unidade:
        resultados = [atendimento for atendimento in resultados if atendimento['unidade'] == unidade]

    # Retorna os resultados em formato JSON
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=False,port=8001)
