import random
import pandas as pd

print("------------------------------------------------")

print("\nExercício 1: Variáveis e Operadores, Limpando e Formatando Dados")

valor_bruto = "R$ 1.500,75"
cliente = " maRiA  silva "
valor_bruto = valor_bruto.replace("R$ ", "").replace(".", "").replace(",", ".")
imposto = 0.15
valor_liquido = float(valor_bruto) * (1 - imposto)

print(f"Cliente: {cliente.strip().title()} | Valor Líquido: {valor_liquido:.2f}")

print("------------------------------------------------")

print("\nExercício 2: Estrutura Condicional (Foco: Regras de Negócio)")

score = random.randint(0, 1000) 
 
tempo_conta_anos = random.randint(0, 10)

if score > 800 and tempo_conta_anos > 5:
    print("Risco Baixísmo - Aprovar Imediato.")
elif 500 < score <= 800:
    print("Moderado - Enviar para Análise Humana")
elif score<500 or tempo_conta_anos < 1:
    print("Risco Alto - Bloquear")
else:
    print("Erro")

print(score)
print(tempo_conta_anos)

print("------------------------------------------------")

print("\nExercicio 3 - Estruturas de Repetição (Foco: Processamento em Lote/ETL)")

logs = [200, 200, 404, 500, 200, 404, 200, 500, 200]

cont_erros = 0

for log in logs:
    if log != 200:
        cont_erros += 1
    
    if log == 500:
        print("Crítico: Servidor caiu!")
        

print("Quantidade de erros: ", cont_erros)

print("------------------------------------------------")

print("\nExercício 4 - Funções (Foco: Modularização e Reutilização)")  


# A -> indica que a função retornará um tipo de variável
"""
    O type hinting é uma prática recomendada que aumenta a robustez e a 
    manutenibilidade do código Python, tornando-o mais seguro e fácil de trabalhar em projetos
    maiores ou em equipe
"""
def calcular_churn(clientes_ativos_inicio: int, clientes_cancelados: int) -> float:
    

    if clientes_ativos_inicio == 0:
        return 0.0
       
    
    resultado = (clientes_cancelados / clientes_ativos_inicio) * 100   

    return resultado
    
clientes_ativos = 5
clientes_cancelados = 2


print("\n", calcular_churn(clientes_ativos, clientes_cancelados))

print("\n------------------------------------------------")


print("\nExercício 5 - Desafio Integrado: O Classificador de Leads")

candidatos = [
    {'nome': 'Ana', 'python': 8, 'sql': 7},
    {'nome': 'Bia', 'python': 5, 'sql': 9},
    {'nome': 'Caio', 'python': 9, 'sql': 2},
]

# O Python sabe iterar direto em listas de dicionários. 
# Jeito Pythonico: candidato['python'] (Direto ao ponto).
for candidato in candidatos:
    soma = candidato['python'] + candidato['sql']
 

    if soma >= 12 and candidato['python'] >= 3 and candidato['sql'] >= 3:
        print("\n", candidato['nome'], "aprovado")
    else:
        print("\n", candidato['nome'], "reprovado")

print("\n------------------------------------------------")


print("\nExercício 6 - Estruturas de Dados (Listas e Dictionaries)")

usuarios = [
    {"id": 1, "nome": "Alice", "idade": 30, "email": "alice@nttdata.com", "ativo": True},
    {"id": 2, "nome": "Bob", "idade": 17, "email": "bob@nttdata.com", "ativo": True}, # Menor de idade
    {"id": 3, "nome": "Carol", "idade": 25, "email": "carol@nttdata.com", "ativo": False}, # Inativo
    {"id": 4, "nome": "Dave", "idade": 40, "email": "dave@nttdata.com", "ativo": True},
]

emails_ativos = []

for user in usuarios:
    #Em Python, não precisamos comparar True == True. 
    # Se a variável já é um booleano, basta colocar o nome dela.
    if user['ativo'] and user['idade'] >= 18: 
        emails_ativos.append(user['email'])

print("\n", emails_ativos)

print("\n------------------------------------------------")

print("\nExercício 7 - Tratamento de Erros (try / except) ")

produtos = [
    {"item": "Teclado", "preco": 100},
    {"item": "Mouse", "preco": 50},
    {"item": "Monitor"}, # ERRO 1: Chave 'preco' faltando (KeyError)
    {"item": "Cabo HDMI", "preco": "trinta"}, # ERRO 2: Tipo errado (ValueError na conversão)
    {"item": "Headset", "preco": 200},
]

total_estoque = 0

for produto in produtos:
    try:
        total_estoque += int(produto['preco'])
    except KeyError:# Sniper 1: Captura só se faltar a chave
        print(f"\nErro: Item '{produto['item']}' sem etiqueta de preço.")
    except ValueError: # Sniper 2: Captura só se a conversão int() falhar
        print(f"\nErro: Item '{produto['item']}' com preço mal formatado.")
    except Exception as e: # A rede de segurança final (opcional)
        print(f"\nErro inesperado: {e}")

print("\n valor do estoque:", total_estoque)

print("\n------------------------------------------------")

print("\n Execício 8 - Programação Orientada a Objetos (POO)")

class Funcionario():
    # --- Construtor ---
    def __init__(self, nome, salario_inicial):
        self.nome = nome
        # O _ antes indica: "Privado/Protegido". Use o Setter para mexer aqui!
        self._salario = salario_inicial

    # --- O SETTER --- (Grava com segurança)
    def set_salario(self, novo_valor):
        if novo_valor > 0:
            self._salario = novo_valor
            print(f"Salário de {self.nome} alterado")
        else:
            print("Erro: Salário não pode ser negativo")

    # --- O GETTER --- (Ler o dado)
    def get_salario(self):
        return self._salario

    # --- Métodos ---
    def aumentar_salario(self, percentual):
        aumento = self._salario * (percentual /100)
        self._salario += aumento


# --- USANDO A CLASSE (Instanciando Objetos) ---

# 1. Criando o objeto (O __init__ roda aqui)
funcionario1 = Funcionario("Maria", 2400)

# 2. Usando o Getter
print(f"\nSalario atua: {funcionario1.get_salario()}")

# 3. Usando o Setter
funcionario1.set_salario(-100)

# 4. Usando o Setter (Correto)
funcionario1.set_salario(2400)

funcionario1.aumentar_salario(10)
print(f"\nSalario novo: {funcionario1.get_salario()}")

print("\n------------------------------------------------")

print("\n Exercício 9 - O Simulador de Modelo de IA")

class ModeloIA():

    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.treinado = False
        self.acuracia = 0.0

    def __str__(self):
        status = "Pronto" if self.treinado else "Não treinado"
        return f"[Modelo IA] Nome: {self.nome} | Tipo: {self.tipo} | Status: {status}"


    def treinar(self):
        self.treinado = True
        self.acuracia = random.uniform(0.5, 0.99)

        print(f"Modelo treinado! Acurácia atingida: {self.acuracia:.2f}")

    def fazer_previsao(self, dados):
        
        if self.treinado:
            print(f"Prevendo resultado para '{dados}'... Acurácia do modelo: {self.acuracia:.2f}")
        else:
            print("ERRO: O modelo precisa ser treinado antes de prever!")


# 1. Instancie o modelo
meu_modelo = ModeloIA("Chatbot NTT", "NLP")

# 2. Tente prever ANTES de treinar (Tem que dar erro)
meu_modelo.fazer_previsao("Olá, tudo bem?")

# 3. Treine o modelo
meu_modelo.treinar()

# 4. Tente prever DEPOIS de treinar (Tem que funcionar)
meu_modelo.fazer_previsao("Olá, tudo bem?")    

print(meu_modelo)

print("\n------------------------------------------------")





