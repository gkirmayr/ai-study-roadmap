from .vectorstore import buscar_contexto
from .prompt import montar_prompt
from .llm import chamar_llm

def responder_pergunta(pergunta: str) -> str:
    contexto = buscar_contexto(pergunta)
    prompt = montar_prompt(pergunta, contexto)
    resposta = chamar_llm(prompt)
    return resposta
