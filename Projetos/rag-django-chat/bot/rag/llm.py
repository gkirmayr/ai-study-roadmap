from langchain_google_genai import ChatGoogleGenerativeAI

def chamar_llm(prompt):
    modelo = ChatGoogleGenerativeAI(
        model="gemini-flash-latest"
    )

    response = modelo.invoke(prompt)

    if isinstance(response.content, list):
        return response.content[0]["text"]

    return response.content
