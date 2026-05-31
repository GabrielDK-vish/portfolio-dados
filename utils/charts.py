import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# FORMATAÇÃO
# ==========================================

def format_category(series):

    return (
        series
        .fillna("Não Informado")
        .str.replace("_", " ")
        .str.title()
    )

# ==========================================
# KPIs
# ==========================================

def panel_kpis(df):

    total_orders = df["order_id"].nunique()

    total_revenue = df["price"].sum()

    ticket_avg = total_revenue / total_orders

    items_sold = df["order_item_id"].count()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Pedidos",
        f"{total_orders:,}"
    )

    c2.metric(
        "Ticket Médio",
        f"R$ {ticket_avg:,.2f}"
    )

    c3.metric(
        "Itens Vendidos",
        f"{items_sold:,}"
    )

    c4.metric(
        "Faturamento",
        f"R$ {total_revenue:,.2f}"
    )

# ==========================================
# TICKET MÉDIO POR CATEGORIA
# ==========================================

def panel_ticket_categoria(df):

    df_group = (
        df
        .groupby("product_category_name_english")
        ["price"]
        .mean()
        .reset_index()
        .sort_values(
            "price",
            ascending=False
        )
        .head(10)
    )

    df_group["product_category_name_english"] = format_category(
        df_group["product_category_name_english"]
    )

    fig = px.bar(
        df_group,
        x="product_category_name_english",
        y="price",
        title="🎯 Ticket Médio por Categoria",
        text_auto=".2f"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================
# RECORRÊNCIA POR CATEGORIA
# ==========================================

def panel_recorrencia_categoria(df):

    recorrencia = (
        df
        .groupby([
            "customer_unique_id",
            "product_category_name_english"
        ])
        ["order_id"]
        .nunique()
        .reset_index()
    )

    recorrencia = (
        recorrencia
        .groupby("product_category_name_english")
        ["order_id"]
        .mean()
        .reset_index()
        .sort_values(
            "order_id",
            ascending=False
        )
        .head(10)
    )

    recorrencia["product_category_name_english"] = format_category(
        recorrencia["product_category_name_english"]
    )

    fig = px.bar(
        recorrencia,
        x="product_category_name_english",
        y="order_id",
        title="🔁 Categorias com Maior Recorrência",
        text_auto=".2f"
    )

    fig.update_layout(
        yaxis_title="Média de Compras"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================
# INTERVALO ENTRE COMPRAS
# ==========================================

def panel_intervalo_compras(df):

    df = df.sort_values(
        by=[
            "customer_unique_id",
            "order_purchase_timestamp"
        ]
    )

    df["previous_purchase"] = (
        df
        .groupby("customer_unique_id")
        ["order_purchase_timestamp"]
        .shift(1)
    )

    df["days_between"] = (
        df["order_purchase_timestamp"]
        - df["previous_purchase"]
    ).dt.days

    intervalo = (
        df
        .groupby("product_category_name_english")
        ["days_between"]
        .mean()
        .reset_index()
        .dropna()
        .sort_values(
            "days_between"
        )
        .head(10)
    )

    intervalo["product_category_name_english"] = format_category(
        intervalo["product_category_name_english"]
    )

    fig = px.bar(
        intervalo,
        x="product_category_name_english",
        y="days_between",
        title="⏳ Intervalo Médio Entre Compras (Dias)",
        text_auto=".1f"
    )

    fig.update_layout(
        yaxis_title="Dias"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================
# TOP PRODUTOS POR FATURAMENTO
# ==========================================

def panel_top_produtos_valor(df):

    produtos = (
        df
        .groupby("product_category_name_english")
        ["price"]
        .sum()
        .reset_index()
        .sort_values(
            "price",
            ascending=False
        )
        .head(10)
    )

    produtos["product_category_name_english"] = format_category(
        produtos["product_category_name_english"]
    )

    fig = px.bar(
        produtos,
        x="product_category_name_english",
        y="price",
        title="💰 Categorias com Maior Valor Vendido",
        text_auto=".2s"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================
# TOP PRODUTOS POR QUANTIDADE
# ==========================================

def panel_top_produtos_quantidade(df):

    produtos = (
        df
        .groupby("product_category_name_english")
        ["order_item_id"]
        .count()
        .reset_index()
        .sort_values(
            "order_item_id",
            ascending=False
        )
        .head(10)
    )

    produtos["product_category_name_english"] = format_category(
        produtos["product_category_name_english"]
    )

    fig = px.bar(
        produtos,
        x="product_category_name_english",
        y="order_item_id",
        title="📦 Categorias com Maior Volume de Vendas",
        text_auto=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )