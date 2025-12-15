from langchain_core.prompts import PromptTemplate

PROMPT_TEMPLATE = """
Você é um assistente de IA e especialista em tecnologia.
Sua missão é responder à pergunta: {pergunta}

Use o seguinte contexto recuperado para montar sua resposta:
{base_conhecimento}

Regras:
1. Priorize as informações do contexto.
2. Se o contexto citar o termo mas não definir, explique brevemente.
3. Responda de forma completa e didática.

Se o assunto não tiver relação com o contexto, diga:
"Desculpe, esse assunto não está no meu material de estudo."
"""

def montar_prompt(pergunta: str, contexto: str):
    prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
    return prompt.invoke({
        "pergunta": pergunta,
        "base_conhecimento": contexto
    })
