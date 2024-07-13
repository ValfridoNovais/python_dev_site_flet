import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import kendalltau
import pandas as pd

# Dados
dados = {
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "IMV 2024": [1.74, 0.29, 2.03, 3.19, 3.78, 3.19],
    "IMV 2023": [2.00, 0.57, 3.15, 1.14, 1.14, 1.72],
    "IPQ 2024": [106.38, 12.77, 29.79, 25.53, 38.30, 38.30],
    "IPQ AUDITADO": [234.04, 55.32, 72.34, 68.09, 123.40, 123.40],
    "IPQ 2023": [21.28, 42.55, 8.51, 46.81, 25.53, 34.04]
}

# DataFrame
df = pd.DataFrame(dados)

# Função para gerar gráficos de correlação de Kendall com rótulos
def grafico_kendall(x, y, xlabel, ylabel, title, labels):
    correlation, _ = kendalltau(df[x], df[y])
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x=x, y=y, data=df)
    sns.regplot(x=x, y=y, data=df, scatter=False, color='red', label=f'Kendall Tau: {correlation:.2f}')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    for i, label in enumerate(labels):
        plt.annotate(label, (df[x][i], df[y][i]), textcoords="offset points", xytext=(5,-5), ha='center')
    plt.show()

# Gráfico 1: IMV 2024 vs IMV 2023
grafico_kendall("IMV 2024", "IMV 2023", "IMV 2024", "IMV 2023", "Gráfico de Correlação de Kendall entre IMV 2024 e IMV 2023", df["Mês"])

# Gráfico 2: IPQ 2024 vs IPQ 2023
grafico_kendall("IPQ 2024", "IPQ 2023", "IPQ 2024", "IPQ 2023", "Gráfico de Correlação de Kendall entre IPQ 2024 e IPQ 2023", df["Mês"])

# Gráfico 3: IMV 2024 vs IPQ 2024
grafico_kendall("IMV 2024", "IPQ 2024", "IMV 2024", "IPQ 2024", "Gráfico de Correlação de Kendall entre IMV 2024 e IPQ 2024", df["Mês"])
