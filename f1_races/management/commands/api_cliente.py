import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import colormaps
import time
from datetime import datetime

# === 1. Carregar e preparar os dados ===
df = pd.read_csv("./location.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

df_filtered = df[["date", "driver_number", "x", "y"]].copy()
timestamps = sorted(df_filtered["date"].unique())

# === 2. Organizar os dados por piloto ===
pilotos_data = {}
for driver_number, group in df_filtered.groupby("driver_number"):
    pilotos_data[driver_number] = {
        "data": list(zip(group["date"], group["x"], group["y"])),
        "x_rastro": [],
        "y_rastro": [],
        "cor": None
    }

# === 3. Atribuir cores diferentes a cada piloto ===
cmap = colormaps.get_cmap("tab10")
for idx, (driver, dados) in enumerate(pilotos_data.items()):
    dados["cor"] = cmap(idx / max(1, len(pilotos_data) - 1))

# === 4. Preparar o gráfico ===
fig, ax = plt.subplots()
ax.set_xlim(df["x"].min() - 1000, df["x"].max() + 1000)
ax.set_ylim(df["y"].min() - 1000, df["y"].max() + 1000)

rastros = {}
bolinhas = {}

for driver, dados in pilotos_data.items():
    rastros[driver], = ax.plot([], [], color='black', linewidth=1)
    bolinhas[driver], = ax.plot([], [], 'o', color=dados["cor"], label=f"Piloto {driver}")

plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.tight_layout()
plt.ion()  # Ativa modo interativo

# === 5. Loop manual com tempo real ===
for i in range(len(timestamps)):
    tempo_atual = timestamps[i]

    for driver, dados in pilotos_data.items():
        for data, x, y in dados["data"]:
            if data == tempo_atual:
                dados["x_rastro"].append(x)
                dados["y_rastro"].append(y)
                rastros[driver].set_data(dados["x_rastro"], dados["y_rastro"])
                bolinhas[driver].set_data([x], [y])
                break

    ax.set_title(f"Tempo: {tempo_atual.strftime('%H:%M:%S.%f')[:-3]}")
    plt.pause(0.001)  # Atualiza a tela

    # Esperar o tempo real entre frames
    if i < len(timestamps) - 1:
        diff = (timestamps[i+1] - tempo_atual).total_seconds()
        time.sleep(diff)

plt.ioff()
plt.show()
