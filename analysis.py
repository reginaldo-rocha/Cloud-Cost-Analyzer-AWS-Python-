import pandas as pd
import matplotlib.pyplot as plt

# carregar CSV
df = pd.read_csv("data/costs.csv")

# limpar nomes de colunas
df.columns = [c.strip() for c in df.columns]

# agrupar por serviço
cost_by_service = (
    df.groupby("Service")["UnblendedCost"]
    .sum()
    .sort_values(ascending=False)
)

# mostrar no terminal
print("\nTop serviços:")
print(cost_by_service.head(5))

# gerar gráfico
cost_by_service.head(5).plot(kind="bar")

plt.title("Top 5 Serviços por Custo")
plt.xlabel("Serviço")
plt.ylabel("Custo ($)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()