from langchain_chroma.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

CAMINHO_DB = "db"

def buscar_contexto(pergunta: str) -> str:
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004"
    )

    db = Chroma(
        persist_directory=CAMINHO_DB,
        embedding_function=embeddings
    )

    resultados = db.similarity_search_with_relevance_scores(
        pergunta, k=5
    )

    if len(resultados) == 0 or resultados[0][1] < 0.3:
        return "Desculpe, não tenho resposta para essa pergunta."

    textos = [res[0].page_content for res in resultados]
    return "\n\n---\n\n".join(textos)
