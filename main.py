# pip install python-dotenv langchain langchain-community langchain-chroma chromadb openai pypdf
from langchain_chroma.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

CAMINHO_DB = "db"  # Diretório onde o banco de dados vetorial será salvo

propmt_template = """Você é um assistente de IA especializado em responder perguntas do usuário: {pergunta} com base em documentos fornecidos. 
Utilize apenas as informações: {base_conhecimento} contidas nos documentos para formular suas respostas. 
Se a informação não estiver presente nos documentos,
responda com "Desculpe, não sei a resposta para essa pergunta."""

def perguntar():
    pergunta = input("Escreva sua pergunta sobre siglas do mundo TECH: ")

    # Carregar o banco de dados vetorial

    function_embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    db = Chroma(persist_directory=CAMINHO_DB, embedding_function=function_embeddings)  

    # comparar a similaridade da pergunta com os documentos no banco de dados

    resultados = db.similarity_search_with_relevance_scores(pergunta, k=3) # Retorna os 3 documentos mais similares

    if len(resultados) == 0 or resultados[0][1] < 0.4:  # Verifica se há resultados e se a similaridade é suficiente
        print("Desculpe, não sei a resposta para essa pergunta.")
        return
    
    textos_resultado = []

    for resultado in resultados:
        texto = resultado[0].page_content
        textos_resultado.append(texto)

    base_conhecimento = "\n\n---\n\n".join(textos_resultado)#Une todos os elementos da lista em uma única string, separando-os por quebras de linha e "---"
    propmt = PromptTemplate.from_template(propmt_template)
    prompt = propmt.invoke({"pergunta": pergunta, "base_conhecimento": base_conhecimento})
    print("prompt gerado:\n", prompt)

    modelo = GoogleGenerativeAI(model="models/generative-bison-004")

perguntar()