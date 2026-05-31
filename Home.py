import streamlit as st

# header
st.set_page_config(
    page_title="Gabriel R. - Portfólio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Menu lateral
with st.sidebar:

    st.title("📊 Navegação")

    st.markdown("---")

    st.write("""
    Explore os projetos e análises disponíveis
    nas páginas ao lado.
    """)

# conteudo home

st.title("Gabriel R. De Carvalho - Portfólio")

st.markdown("---")

st.write("""
Esse portfólio foi criado com intuito de apresentar competencias relativas
a análise de dados em diversos ambientes.
""")

st.markdown("## Seções")

col1, col2 = st.columns(2)

with col1:

    st.info("""
    👨‍💻 Sobre Mim - Competencias Profissionais
    """)

    st.info("""
    📈 Vendas - Análise de Dados Operacionais em E-Commerce
    """)

    st.info("""
    📢 Marketing - Análise de Dados voltados a marketing e seu impacto
    """)

    #st.info("""
    #📊 KPIs - Análise de Dados voltados a apresentação Gerencial para tomada de decisões
    #""")

#with col2:
#
 #   st.info("""
  #  🌎 Geografico - Análise de Dados Geograficos/Geoespaciais
   # """)

    #st.info("""
    #🔍 Exploratoria - Análise de dados realizada em maior profundidade para insights
    #""")

    #st.info("""
   # 👨‍💻 Sobre Mim - Competencias Profissionais
  #  """)

st.markdown("---")

st.caption("Navegação pelo menu lateral a esquerda")