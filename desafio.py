# --- Objetivo: Classificador de Nível de Player (MLBB Version) ---

# 1. Variáveis para armazenar informações
nome_player = input("Digite o nome do Player: ")
estrelas = int(input("Digite a quantidade de Estrelas: "))
nivel = ""

# 2. Estrutura de decisão para classificar o Rank
# Usamos operadores de comparação para definir os intervalos
if estrelas <= 10:
    nivel = "Warrior"
elif 11 <= estrelas <= 20:
    nivel = "Elite"
elif 21 <= estrelas <= 40:
    nivel = "Master"
elif 41 <= estrelas <= 70:
    nivel = "Grandmaster"
elif 71 <= estrelas <= 100:
    nivel = "Epic"
elif 101 <= estrelas <= 150:
    nivel = "Legend"
elif 151 <= estrelas <= 174:
    nivel = "Mythic"
elif 175 <= estrelas <= 199:
    nivel = "Mythical Honor"
elif 200 <= estrelas <= 249:
    nivel = "Mythical Glory"
else:
    nivel = "Mythical Immortal"

# 3. Saída formatada
print(f"O Player de nome **{nome_player}** está no nível de **{nivel}**")