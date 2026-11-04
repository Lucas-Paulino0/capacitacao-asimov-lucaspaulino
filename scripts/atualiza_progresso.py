from pathlib import Path

TOTAL_SEMANAS = 10
INICIO = "<!-- PROGRESSO:INICIO -->"
FIM = "<!-- PROGRESSO:FIM -->"

# Pasta raiz do repositório (o script está em scripts/, então sobe um nível)
raiz = Path(__file__).resolve().parent.parent
readme = raiz / "README.md"

# Conta as pastas da raiz cujo nome começa com "semana-"
pastas = [p for p in raiz.glob("semana-*") if p.is_dir()]
entregues = min(len(pastas), TOTAL_SEMANAS)

# Monta a barra: █ para entregues, ░ para as que faltam
barra = "█" * entregues + "░" * (TOTAL_SEMANAS - entregues)
linha = f"**Progresso:** {barra} {entregues}/{TOTAL_SEMANAS} semanas"

# Separa o README em: antes do INICIO | entre os marcadores | depois do FIM
texto = readme.read_text(encoding="utf-8")
antes, resto = texto.split(INICIO)
_, depois = resto.split(FIM)

# Reconstrói o arquivo trocando só o que está entre os marcadores
novo = antes + INICIO + "\n" + linha + "\n" + FIM + depois

if novo != texto:
    readme.write_text(novo, encoding="utf-8", newline="\n")
    print(f"README atualizado: {entregues}/{TOTAL_SEMANAS} semanas")
else:
    print("README já estava atualizado")
