from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///assets/datasets/ecommerce.db"
)

def load_sales_data():

    query = """
    SELECT *
    FROM sales
    """

    return pd.read_sql(query, engine)