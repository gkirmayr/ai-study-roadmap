# 🤖 RAG Chat com Django

Este projeto é uma **PoC (Proof of Concept)** de um **chat inteligente utilizando arquitetura RAG (Retrieval-Augmented Generation)** integrado a um **backend em Django**.

O foco principal do projeto é **aprender e aplicar padrões reais de mercado**, priorizando **arquitetura, organização de código e separação de responsabilidades**, em vez de apenas fazer a aplicação “funcionar”.

---

## 🎯 Objetivo do Projeto

* Criar um backend em Django capaz de receber perguntas de usuários
* Processar essas perguntas utilizando uma arquitetura **RAG**
* Recuperar contexto a partir de uma base de conhecimento vetorial
* Gerar respostas com um **LLM (Large Language Model)**
* Retornar a resposta ao front-end de forma organizada

Este projeto foi desenvolvido com foco em **aprendizado prático**, inspirado em padrões utilizados em ambientes corporativos.

---

## 🧠 Conceitos e Tecnologias Utilizadas

* **Django** — Backend web e orquestração HTTP
* **Arquitetura RAG (Retrieval-Augmented Generation)**
* **Embeddings** para representação semântica de texto
* **Busca vetorial** com banco persistente
* **LLMs (Large Language Models)**
* **Separação de responsabilidades (SRP)**
* **Boas práticas de arquitetura backend**

---

## 🏗️ Visão Geral da Arquitetura

A arquitetura segue o princípio de desacoplamento entre camadas:

```
Usuário
 → Requisição HTTP
 → Django (URL → View)
 → Pipeline RAG
     → Embeddings
     → Busca vetorial
     → Montagem de contexto
     → Prompt
     → LLM
 → Django retorna resposta
 → Usuário
```

### Princípios aplicados:

* O **Django não contém lógica de IA**
* O **RAG não conhece o Django**
* A integração acontece apenas na **view**
* Cada módulo possui **uma responsabilidade clara**

---

## 📁 Estrutura do Projeto

```
rag-django-chat/
│
├── manage.py
├── criar_db.py
├── verifica_modelo.py
│
├── config/                 # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── bot/                    # App principal
│   ├── views.py            # Entrada das requisições HTTP
│   ├── urls.py
│   ├── templates/
│   │   └── bot/
│   │       └── index.html
│   └── rag/                # Lógica RAG isolada
│       ├── vectorstore.py  # Busca vetorial
│       ├── prompt.py       # Prompt engineering
│       ├── llm.py          # Comunicação com LLM
│       └── pipeline.py     # Orquestração RAG
│
├── db/                     # Base vetorial persistida
└── README.md
```

---

## 🔄 Fluxo de Funcionamento

1. O usuário acessa a aplicação pelo navegador
2. O front-end envia uma requisição HTTP
3. O Django resolve a URL e chama a **view**
4. A view delega o processamento ao **pipeline RAG**
5. O RAG executa:

   * Geração de embeddings da pergunta
   * Busca vetorial com **score mínimo de similaridade**
   * Montagem do contexto
   * Criação do prompt
   * Chamada ao modelo de linguagem
6. A resposta é retornada à view
7. O Django devolve a resposta ao usuário

---

## ▶️ Como Executar o Projeto

### 1️⃣ Criar e ativar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate    # Windows
```

---

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
GOOGLE_API_KEY=sua_chave_aqui
```

---

### 4️⃣ Executar o servidor

```bash
python manage.py runserver
```

Acesse:

```
http://127.0.0.1:8000/
```

---

## 🧪 Status do Projeto

* ✅ Estrutura funcional
* ✅ Arquitetura RAG integrada ao Django
* ✅ Separação de responsabilidades
* 🔄 Em evolução contínua

---

## 🚀 Próximos Passos

* Expor o RAG via API REST
* Adicionar testes unitários
* Implementar cache e otimizações
* Tornar LLM e banco vetorial plugáveis
* Adicionar observabilidade

---

## 👩‍💻 Autora

**Gaby**
Estagiária de Desenvolvimento | Ciência da Computação
Interesses: IA aplicada, arquitetura backend, sistemas inteligentes

---

> Projeto desenvolvido para fins educacionais e evolução técnica em Inteligência Artificial aplicada.
