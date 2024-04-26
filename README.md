# Painel eSUS

## Descrição
O Painel eSUS é um sistema para visualização e análise de dados de saúde provenientes do eSUS-AB (Sistema de Informação em Saúde para Atenção Básica). Ele permite aos profissionais de saúde e gestores monitorar indicadores de saúde.

## Funcionalidades
- Visualização de dados de atendimentos de saúde
- Filtragem de dados por data de atendimento, condição de saúde e unidade de saúde

## Como funciona
O Painel eSUS é desenvolvido em Python utilizando o framework Flask para criar uma API REST que fornece acesso aos dados de saúde armazenados em um arquivo csv. Os dados são carregados a partir de um arquivo CSV contendo os registros de atendimentos.

## Instalação e Uso
1. Clone o repositório para o seu ambiente local: git clone https://github.com/seu-usuario/painel-esus.git

2. Navegue até o diretório do projeto: cd painel-esus

  
3. Instale as dependências do Python (certifique-se de ter o Python e o pip instalados): pip install -r requirements.txt

4.  Execute o aplicativo Flask: Flask run


5. Abra o navegador e acesse o Painel eSUS em `http://localhost:5000/api/v1/atendimentos`

6. Para acessar os atendimentos em uma data específica (substitua 'YYYY-mm-dd' pela data desejada): http://localhost:5000/api/v1/atendimentos?data_atendimento=YYYY-mm-dd

7.Para acessar os atendimentos com uma condição de saúde específica (substitua 'condicao' pela condição desejada): http://localhost:5000/api/v1/atendimentos?condicao_saude=condicao

8.Para acessar os atendimentos em uma unidade de saúde específica (substitua 'unidade' pelo nome da unidade desejada): http://localhost:5000/api/v1/atendimentos?unidade=unidade


