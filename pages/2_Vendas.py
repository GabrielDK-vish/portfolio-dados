import streamlit as st

from utils.data_loader import load_sales_data

from utils.charts import (
    panel_kpis,
    panel_ticket_categoria,
    panel_recorrencia_categoria,
    panel_intervalo_compras,
    panel_top_produtos_valor,
    panel_top_produtos_quantidade
)

st.markdown("""
<style>

/* KPI CARDS */

div[data-testid="metric-container"] {
    background-color: #111827;
    border: 1px solid #1f2937;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
}

/* TÍTULO KPI */

div[data-testid="metric-container"] label {
    color: #9ca3af !important;
    font-size: 15px !important;
}

/* VALOR KPI */

div[data-testid="metric-container"] div {
    color: white !important;
}

/* ESPAÇAMENTO */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

</style>
""", unsafe_allow_html=True)



st.set_page_config(
    page_title="Painel de Vendas",
    layout="wide"
)


df_sales = load_sales_data()


st.title("📈 Painel de Vendas")

st.markdown("""
Análise estratégica de vendas utilizando dados
de e-commerce com foco em categorias,
faturamento e comportamento de compra.
            
Insight ao final da página.
""")

st.markdown("---")


panel_kpis(df_sales)

st.markdown("---")


col1, col2 = st.columns(2)

with col1:

    panel_ticket_categoria(df_sales)

with col2:

    panel_recorrencia_categoria(df_sales)

st.markdown("---")


col3, col4 = st.columns(2)

with col3:

    panel_intervalo_compras(df_sales)

with col4:

    panel_top_produtos_valor(df_sales)

st.markdown("---")


panel_top_produtos_quantidade(df_sales)


st.markdown("""
### Insights da Análise

A análise dos gráficos demonstra que a maior taxa média de recorrência
entre categorias está próxima de **1.10 compras por cliente**,
indicando baixa frequência de recompra no e-commerce analisado.

Esse comportamento sugere uma forte dependência de aquisição contínua
de novos clientes para sustentação do volume de vendas,
além de possíveis desafios relacionados à retenção e fidelização.

Também é possível observar diferenças relevantes entre categorias,
indicando que determinados segmentos possuem maior potencial
de recorrência e relacionamento de longo prazo com clientes.
""")