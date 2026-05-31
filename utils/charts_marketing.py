import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# KPIs
# ==========================================

def panel_marketing_kpis(df):

    total_spent = df["mark_spent"].sum()

    total_revenue = df["revenue"].sum()

    total_clicks = df["clicks"].sum()

    total_orders = df["orders"].sum()

    roas = total_revenue / total_spent

    conversion = (
        total_orders / total_clicks
    ) * 100

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Investimento",
        f"R$ {total_spent:,.0f}"
    )

    c2.metric(
        "Receita",
        f"R$ {total_revenue:,.0f}"
    )

    c3.metric(
        "ROAS",
        f"{roas:.2f}x"
    )

    c4.metric(
        "Conversão",
        f"{conversion:.2f}%"
    )

# ==========================================
# ALCANCE POR CANAL
# ==========================================

def panel_impressions(df):

    df_group = (
        df
        .groupby("category")
        ["impressions"]
        .sum()
        .reset_index()
        .sort_values(
            "impressions",
            ascending=False
        )
    )

    fig = px.bar(
        df_group,
        x="category",
        y="impressions",
        title="📢 Alcance por Canal",
        text_auto=True
    )

    fig.update_traces(
        texttemplate='%{y:,.0f}'
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="Impressões",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================
# CTR POR CANAL
# ==========================================

def panel_ctr(df):

    df_group = (
        df
        .groupby("category")
        .agg({
            "clicks": "sum",
            "impressions": "sum"
        })
        .reset_index()
    )

    df_group["ctr"] = (
        df_group["clicks"]
        / df_group["impressions"]
    ) * 100

    fig = px.bar(
        df_group,
        x="category",
        y="ctr",
        title="🎯 CTR por Canal",
        text_auto=".2f"
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="CTR (%)",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.caption("""
CTR (Click Through Rate) representa a taxa de cliques
sobre o total de impressões da campanha.
""")

# ==========================================
# CONVERSÃO POR CANAL
# ==========================================

def panel_conversion(df):

    df_group = (
        df
        .groupby("category")
        .agg({
            "orders": "sum",
            "clicks": "sum"
        })
        .reset_index()
    )

    df_group["conversion"] = (
        df_group["orders"]
        / df_group["clicks"]
    ) * 100

    fig = px.bar(
        df_group,
        x="category",
        y="conversion",
        title="🛒 Conversão por Canal",
        text_auto=".2f"
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="Conversão (%)",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.caption("""
Conversão representa a porcentagem de usuários
que realizaram pedidos após clicar na campanha.
""")

# ==========================================
# TOP CAMPANHAS
# ==========================================

def panel_top_campaigns(df):

    df_group = (
        df
        .groupby("campaign_name")
        ["revenue"]
        .sum()
        .reset_index()
        .sort_values(
            "revenue",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        df_group,
        x="campaign_name",
        y="revenue",
        title="🏆 Campanhas com Maior Receita",
        text_auto=".2s"
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="Receita",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================
# INVESTIMENTO VS RECEITA
# ==========================================

def panel_scatter(df):

    fig = px.scatter(
        df,
        x="mark_spent",
        y="revenue",
        size="orders",
        color="category",
        hover_name="campaign_name",
        trendline="ols",
        title="💡 Investimento vs Receita",
        height=600,
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    fig.update_layout(
        xaxis_title="Investimento",
        yaxis_title="Receita"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.caption("""
Cada ponto representa uma campanha.
Campanhas acima da linha de tendência apresentaram
performance superior ao esperado.
""")

# ==========================================
# FUNIL
# ==========================================

def panel_funil(df):

    impressions = df["impressions"].sum()

    clicks = df["clicks"].sum()

    leads = df["leads"].sum()

    orders = df["orders"].sum()

    funnel = pd.DataFrame({
        "Etapa": [
            "Impressões",
            "Cliques",
            "Leads",
            "Pedidos"
        ],
        "Quantidade": [
            impressions,
            clicks,
            leads,
            orders
        ]
    })

    fig = px.funnel(
        funnel,
        x="Quantidade",
        y="Etapa",
        title="📉 Funil de Conversão"
    )

    fig.update_layout(
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.caption("""
O funil demonstra a redução progressiva de usuários
ao longo da jornada de aquisição.
""")