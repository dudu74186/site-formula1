import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

# === CONFIGURAÇÃO ===
ARQUIVO = "locations_f1.json"

# === CARREGAMENTO E PREPARO DOS DADOS ===
def carregar_dados(arquivo):
    """Carrega, filtra e prepara os dados do arquivo JSON."""
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{arquivo}' não contém um JSON válido.")
        return []

    dados = [d for d in dados if d.get("x") and d.get("y") and "date" in d]
    for d in dados:
        d["ts"] = datetime.fromisoformat(d["date"].replace("Z", "+00:00"))
    dados.sort(key=lambda d: d["ts"])
    return dados

dados = carregar_dados(ARQUIVO)
if not dados:
    raise ValueError("Nenhum dado válido encontrado para animar!")

# === PRÉ-CÁLCULO DOS INTERVALOS ENTRE FRAMES ===
tempos = [d["ts"].timestamp() for d in dados]
intervalos = [
    max((tempos[i + 1] - tempos[i]) * 1000, 1)
    for i in range(len(tempos) - 1)
]
intervalos.append(100)

# === CONFIGURAÇÃO DO PLOT ===
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title("Localizações F1 (x vs y)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_xlim(min(d["x"] for d in dados) - 10, max(d["x"] for d in dados) + 10)
ax.set_ylim(min(d["y"] for d in dados) - 10, max(d["y"] for d in dados) + 10)
ax.grid(True)
ax.set_aspect('equal', adjustable='box')
linha, = ax.plot([], [], 'ro-', markersize=3, lw=2, label="Trajetória")
ponto_atual, = ax.plot([], [], 'go', markersize=8, label="Posição Atual")
info_tempo = ax.text(0.02, 0.95, '', transform=ax.transAxes, ha="left", va="top", fontsize=12)
ax.legend()

x_vals, y_vals = [], []
ani = None

# === FUNÇÃO DE ANIMAÇÃO (para FuncAnimation) ===
def update(i):
    """Função chamada para cada quadro (frame) da animação."""
    x_vals.append(dados[i]["x"])
    y_vals.append(dados[i]["y"])

    linha.set_data(x_vals, y_vals)

    # AQUI ESTÁ A CORREÇÃO: Passar os dados como listas
    ponto_atual.set_data([dados[i]["x"]], [dados[i]["y"]])

    timestamp_str = dados[i]["ts"].strftime('%H:%M:%S.%f')[:-3]
    info_tempo.set_text(f"Tempo: {timestamp_str}")

    if ani is not None and i < len(intervalos) - 1:
        ani.event_source.interval = intervalos[i]

    return linha, ponto_atual, info_tempo

# === CRIAÇÃO E EXECUÇÃO DA ANIMAÇÃO ===
ani = animation.FuncAnimation(
    fig=fig,
    func=update,
    frames=len(dados),
    interval=intervalos[0],
    blit=True,
    repeat=False
)

plt.show()