# verificar_modelos.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

print("--- Consultando o Google... ---")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"Modelo disponível: {m.name}")
except Exception as e:
    print(f"Erro ao listar: {e}")