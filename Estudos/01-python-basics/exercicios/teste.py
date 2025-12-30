arquivos = ["doc1.txt", "doc2.txt", "doc3.txt"]

# ❌ Jeito antigo (Verboso)
caminhos = []
for arquivo in arquivos:
    caminhos.append(f"/data/{arquivo}")

# ✅ Jeito Moderno (List Comprehension)
# Lê-se: "Para cada arquivo na lista arquivos, aplique a f-string"
caminhos = [f"/data/{arquivo}" for arquivo in arquivos]

print(caminhos)
# Saída: ['/data/doc1.txt', '/data/doc2.txt', '/data/doc3.txt']