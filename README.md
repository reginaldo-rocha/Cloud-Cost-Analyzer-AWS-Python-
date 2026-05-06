# 🚀 Cloud Cost Analyzer (AWS + Python)

Projeto simples e prático de análise de custos cloud utilizando dados da AWS e Python (Pandas).

<img width="1536" height="1024" alt="ChatGPT Image 5 de mai  de 2026, 23_15_16" src="https://github.com/user-attachments/assets/0eafad83-d96f-417f-9c0e-e72d279e7244" />

---

## 🎯 Objetivo

Construir um pipeline básico de dados para:

* Extrair custos da AWS
* Processar dados com Python
* Gerar insights de FinOps

---

## ☁️ Fonte de dados


Os dados foram extraídos do **Cost Explorer da AWS**
(Amazon Web Services)

---

## 🧱 Arquitetura

```
AWS Cost Explorer → CSV → Python (Pandas) → Insights
```

---

## 🔄 Fluxo do projeto

1. Acessar AWS Cost Explorer
2. Gerar relatório de custos
3. Exportar CSV
4. Processar dados com Python
5. Gerar insights

---

## 📊 Análise realizada

* Custo total
* Custo por serviço
* Top serviços mais caros
* Distribuição de custos

---

## 📸 Prints do projeto

### 🔹 Cost Explorer (AWS)

<img width="1349" height="609" alt="aws" src="https://github.com/user-attachments/assets/6c203885-f561-42b7-ae83-c9ea78c308ae" />



### 🔹 Dataset (CSV)

<img width="1362" height="570" alt="Captura de tela 2026-05-06 001835" src="https://github.com/user-attachments/assets/2bcd7dbb-2a47-44ff-9b27-b00377cd073e" />


### 🔹 Execução no VS Code

<img width="1358" height="686" alt="resultado" src="https://github.com/user-attachments/assets/42634cb7-b665-4416-aa3d-1a3e430a4ecf" />


### 🔹 Gráfico de custos

<img width="1353" height="757" alt="imagem" src="https://github.com/user-attachments/assets/3571defb-671f-45fd-8374-221174a44b7e" />


---

## 🧠 Insights (exemplo)

* Amazon EC2 representa maior parte do custo total
* Amazon RDS possui custo relevante constante
* AWS Lambda apresenta baixo custo operacional
* Possível oportunidade de otimização em compute

---

## 🛠️ Tecnologias

* Python
* Pandas
* AWS Cost Explorer
* S3 (opcional)

---

## ▶️ Como executar

```bash
pip install pandas matplotlib
python analysis.py
```

---

## 🚀 Próximos passos

* Automatizar ingestão de dados
* Criar dashboard (Power BI / Streamlit)
* Adicionar múltiplas clouds (Azure / OCI)
* Implementar detecção de anomalias

---

## 📌 Autor

Projeto desenvolvido para estudo de **Cloud + FinOps + Dados**
