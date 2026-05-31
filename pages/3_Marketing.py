import streamlit as st

from utils.data_loader import load_marketing_data

from utils.charts_marketing import (
    panel_marketing_kpis,
    panel_impressions,
    panel_ctr,
    panel_conversion,
    panel_top_campaigns,
    panel_scatter,
    panel_funil
)


st.set_page_config(
    page_title="Marketing Analytics",
    layout="wide"
)


st.markdown("""
<style>

/* KPI */

div[data-testid="metric-container"] {
    background-color: #111827;
    border: 1px solid #1f2937;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
}

/* CONTAINER */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

</style>
""", unsafe_allow_html=True)


df = load_marketing_data()


st.title("📢 Marketing Performance Analytics")

st.markdown("""
Análise estratégica de campanhas de marketing
com foco em aquisição de usuários,
conversão e retorno financeiro.
""")

st.markdown("---")


panel_marketing_kpis(df)

st.markdown("---")


col1, col2 = st.columns(2)

with col1:

    panel_impressions(df)

with col2:

    panel_ctr(df)

st.markdown("---")


col3, col4 = st.columns(2)

with col3:

    panel_conversion(df)

with col4:

    panel_funil(df)

st.markdown("---")


col5, col6 = st.columns(2)

with col5:

    panel_top_campaigns(df)

with col6:

    panel_scatter(df)

st.markdown("---")


st.markdown("""
### Insights da Análise

- Campanhas de Search tiveram maior eficiência
de conversão em relação ao volume de tráfego.

- Social Media teve maior alcance,
porém com menor retorno.

- Canais com maior ROAS (Return On Advertising Spend) demonstram maior potencial
de escalabilidade para aquisição de clientes.
""")

st.markdown("---")

st.markdown("""
##### Font CSV: https://www.kaggle.com/datasets/sinderpreet/analyze-the-marketing-spending?
""")