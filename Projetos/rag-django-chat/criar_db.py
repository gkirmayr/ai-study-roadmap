from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter #importante para dividir textos grandes em pedaços menores
from langchain_chroma.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

# Pega o caminho exato onde ESTE arquivo (criar_db.py) está
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Junta o caminho atual com a pasta "base"
pasta_base = os.path.join(diretorio_atual, "base")

#As duas linhas de cima garantem que o código funcione independentemente de onde ele seja executado. Garantido que sempre vai encontrar a pasta "base" corretamente. Isso é boa prática para evitar erros de caminho relativos.

def criar_db():
    #carregar_documentos
    documentos = carregar_documentos()
    
    # dividir os documentos em pedaços menores(chunks)
    chunks = dividir_em_chunks(documentos)

    # vetoriar os chunks com o processo de embedding
    vetoriar_chunks(chunks)

def carregar_documentos():
    carregador = PyPDFDirectoryLoader(pasta_base)
    documentos = carregador.load()
    return documentos

def dividir_em_chunks(documentos):
    separador_documentos = RecursiveCharacterTextSplitter(
        chunk_size=1000, # tamanho de cada chunk em caracteres
        chunk_overlap=200, # sobreposição entre os chunks para manter o contexto
        length_function=len,# importante para contar os caracteres corretamente
        add_start_index=True,# importante para rastrear a posição original do texto, opcional
    )

    chunks = separador_documentos.split_documents(documentos)
    print(f"Número de chunks criados: {len(chunks)}")
    return chunks

def vetoriar_chunks(chunks):
    # Configurando o modelo de embeddings do Google
    google_embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")  
    db = Chroma.from_documents(documents=chunks,
    embedding=google_embeddings,
    persist_directory="db")
    print("Salvando o banco de dados vetorial em disco...")

criar_db()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    