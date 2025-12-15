from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .rag.pipeline import responder_pergunta

def chat_view(request):
    resposta = None

    if request.method == "POST":
        pergunta = request.POST.get("pergunta")
        if pergunta:
            resposta = responder_pergunta(pergunta)

    return render(request, "bot/index.html", {"resposta": resposta})