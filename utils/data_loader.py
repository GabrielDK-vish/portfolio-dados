import pandas as pd

def load_sales_data():

    dt_orders = pd.read_csv(
        "assets/datasets/olist_orders_dataset.csv"
    )

    dt_items = pd.read_csv(
        "assets/datasets/olist_order_items_dataset.csv"
    )

    dt_products = pd.read_csv(
        "assets/datasets/olist_products_dataset.csv"
    )

    dt_category = pd.read_csv(
        "assets/datasets/product_category_name_translation.csv"
    )

    dt_customers = pd.read_csv(
        "assets/datasets/olist_customers_dataset.csv"
    )

    # ==========================================
    # TRADUÇÃO DE CATEGORIAS
    # ==========================================

    dt_products = dt_products.merge(
        dt_category,
        on="product_category_name",
        how="left"
    )

    # ==========================================
    # DATAFRAME ANALÍTICO
    # ==========================================

    df_sales = (
        dt_items
        .merge(
            dt_orders,
            on="order_id",
            how="left"
        )
        .merge(
            dt_products,
            on="product_id",
            how="left"
        )
        .merge(
            dt_customers,
            on="customer_id",
            how="left"
        )
    )

    # ==========================================
    # DATAS
    # ==========================================

    df_sales["order_purchase_timestamp"] = pd.to_datetime(
        df_sales["order_purchase_timestamp"]
    )

    return df_sales

def load_marketing_data():

    return pd.read_csv(
        "assets/datasets/Marketing.csv"
    )