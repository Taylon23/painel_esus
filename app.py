from flask import Flask, request, jsonify, make_response
import csv
import os
import logging

app = Flask(__name__)

# Configuração de Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cache para os dados do CSV
CACHE_DADOS_ATENDIMENTOS = None

# Carrega os dados do arquivo CSV com tratamento de erro
def carregar_dados_csv(nome_arquivo):
    if not os.path.isfile(nome_arquivo):
        logger.error(f"Arquivo {nome_arquivo} não encontrado.")
        raise FileNotFoundError(f"Arquivo {nome_arquivo} não encontrado.")

    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            dados = [linha for linha in leitor_csv]
        logger.info("Dados do CSV carregados com sucesso.")
        return dados
    except Exception as e:
        logger.error(f"Erro ao carregar o arquivo CSV: {str(e)}")
        raise

# Inicializa o cache dos dados
def get_dados_atendimentos():
    global CACHE_DADOS_ATENDIMENTOS
    if CACHE_DADOS_ATENDIMENTOS is None:
        CACHE_DADOS_ATENDIMENTOS = carregar_dados_csv('atendimentos.csv')
    return CACHE_DADOS_ATENDIMENTOS

# Validação simples dos parâmetros
def validar_parametros(param, nome_param):
    if param and not param.isalnum():
        logger.warning(f"Parâmetro inválido detectado: {nome_param}")
        raise ValueError(f"Parâmetro '{nome_param}' contém caracteres inválidos.")

# Rota para o endpoint /api/v1/atendimentos
@app.route('/api/v1/atendimentos', methods=['GET'])
def buscar_atendimentos():
    try:
        # Obtem parâmetros de consulta da URL
        data_atendimento = request.args.get('data_atendimento')
        condicao_saude = request.args.get('condicao_saude')
        unidade = request.args.get('unidade')

        # Valida os parâmetros recebidos
        validar_parametros(data_atendimento, 'data_atendimento')
        validar_parametros(condicao_saude, 'condicao_saude')
        validar_parametros(unidade, 'unidade')

        # Filtra os dados conforme os parâmetros fornecidos
        resultados = get_dados_atendimentos()
        if data_atendimento:
            resultados = [atendimento for atendimento in resultados if atendimento['data_atendimento'] == data_atendimento]
        if condicao_saude:
            resultados = [atendimento for atendimento in resultados if atendimento['condicao_saude'] == condicao_saude]
        if unidade:
            resultados = [atendimento for atendimento in resultados if atendimento['unidade'] == unidade]

        # Resposta com cabeçalhos seguros
        response = make_response(jsonify(resultados), 200)
        response.headers['Content-Type'] = 'application/json'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        return response

    except ValueError as ve:
        logger.error(f"Erro de validação: {str(ve)}")
        return jsonify({"erro": str(ve)}), 400
    except FileNotFoundError as fe:
        return jsonify({"erro": str(fe)}), 500
    except Exception as e:
        logger.error(f"Erro interno do servidor: {str(e)}")
        return jsonify({"erro": "Erro interno do servidor"}), 500

if __name__ == '__main__':
    app.run(debug=False, port=8001, host='0.0.0.0')