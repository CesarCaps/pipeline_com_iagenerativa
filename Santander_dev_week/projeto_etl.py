import pandas as pd
from pathlib import Path
import google.generativeai as genai
import time

ROOT_PATH = Path(__file__).parent
caminho_entrada_dados = ROOT_PATH / "Dados" / "base_de_dados.csv"
caminho_saida = ROOT_PATH / "Dados" / "dados_processados.csv"
chave_API = "coloque a sua chave aqui" #ATENÇÃÃÃÃÃOOO
genai.configure(api_key = chave_API)
model = genai.GenerativeModel('gemini-1.5-flash')

def extracao_dados(caminho):
    try:
        dados = pd.read_csv(caminho, sep=',')
        print("extração concluída")
        return dados
    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
        return None

def transformacao_dados(dados):
    try:
        if dados is None:
            print("Nenhum dado para transformar.")
            return None
        else:
            # Transformação dos dados para identificar as bandeiras dos cartões
            def identificar_bandeira(cartao):
                if cartao.startswith('4'):
                    return 'Visa'
                elif cartao.startswith('5'):
                    return 'Mastercard'
                else:
                    return 'Bandeira não identificada'

            dados['Bandeira'] = dados['Cartão'].apply(identificar_bandeira)
            print("transformação concluída")
            return dados
        
    except Exception as e:
        print(f"Erro ao transformar dados: {e}")
        return None

def carregamento(df, caminho_destino):
    if df is None: return
    
    # Garante que a pasta de destino exista
    caminho_destino.parent.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(caminho_destino, index=False)
    print(f"Dados salvos com sucesso em: {caminho_destino}")

def gerar_mensagens_personalizadas(df):
    if df is None: return None
    
    mensagens = []
    print("--- Iniciando Geração de Mensagens com IA (Aguarde...) ---")
    
    # Processando apenas os 10 primeiros para teste
    for index, linha in df.head(10).iterrows():
        prompt = f"Crie uma saudação de 1 frase para {linha['Nome']}, cliente do cartão {linha['Bandeira']}."
        
        try:
            response = model.generate_content(prompt)
            mensagens.append(response.text.strip())
            print(f"Mensagem criada para: {linha['Nome']}")
            time.sleep(2) # Pausa de 2 segundos entre cada nome
        except Exception as e:
            mensagens.append("Bem-vindo ao nosso banco!")
            print(f"Erro no Gemini: {e}")

    df_final = df.head(10).copy()
    df_final['Mensagem_IA'] = mensagens
    return df_final

df_extração = extracao_dados(caminho_entrada_dados) #A VARIÁVEL AGORA POSSUI OS DADOS EXTRAÍDOS
df_transformação = transformacao_dados(df_extração) #A VARIÁVEL AGORA POSSUI OS DADOS TRANSFORMADOS
carregamento(df_transformação, caminho_saida)

