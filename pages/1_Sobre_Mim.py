import streamlit as st


st.set_page_config(
    page_title="Sobre Mim",
    layout="wide"
)


st.title("👨‍💻 Sobre Mim")

st.markdown("---")


col_foto, col_info = st.columns([1, 3])

with col_foto:

    st.image(
        "https://media.licdn.com/dms/image/v2/D4D03AQGstyyWCHOyuA/profile-displayphoto-shrink_400_400/B4DZWVj3rbH4Ag-/0/1741970964535?e=1780531200&v=beta&t=wb3uI3h5e8yc7ACj0mLKE223jDZ7BqKT0Bwtbab_Qz4",
        width=250
    )

with col_info:

    st.write("# Gabriel Ramos de Carvalho")

    st.write("### Analista de Dados & Engenheiro de Dados")

    st.write("📍 Zona Leste de São Paulo")

    st.write("🎂 27 anos")

    st.write("""
    Profissional focado na área de dados, com experiência em
    automação, análise de informações e ambientes cloud,
    utilizando principalmente Python, Google Cloud Platform
    e Power BI.
    """)

st.markdown("---")


aba1, aba2, aba3, aba4 = st.tabs([
    "💼 Experiências",
    "🛠 Competências",
    "📜 Certificações",
    "🎯 Hobbies"
])


with aba1:

    st.write("## Experiências")

    st.info("""
    ### Assistente de BI  
    **Dez/2025 ~ Mar/2026**

    Atuação em ambiente de call center de forma terceirizada,
    participando da implantação de cultura de dados e desenvolvimento
    de modelos analíticos voltados para análises operacionais diárias.
    """)

    st.info("""
    ### Assistente de Dados  
    **Mar/2025 ~ Set/2025**

    Atuação em startup voltada para análise de dados,
    desenvolvimento de dashboards gerenciais e operacionais,
    integração de dados em ambiente cloud (GCP),
    implementação de arquitetura medalhão utilizando Data Lake
    para auditoria e análise exploratória de expansão de negócio.
    """)


with aba2:

    st.write("## Competências")

    c1, c2 = st.columns(2)

    with c1:

        st.success("""
        ### Linguagens

        - Python
        - SQL
        - Go
        """)

        st.success("""
        ### Bibliotecas

        - Pandas
        - NumPy
        - Plotly
        - Scikit-Learn
        - Seaborn
        - Streamlit
        """)

    with c2:

        st.success("""
        ### Ferramentas

        - Power BI
        - Looker Studio
        - Excel
        - Git
        - R
        """)

        st.success("""
        ### Banco de Dados & Cloud

        - PostgreSQL
        - Google Cloud Platform
        - Supabase
        """)


with aba3:

    st.write("## Certificações")

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.image(
            "assets/certificacoes/datalake_gcp.jfif",
            use_container_width=True
        )

        st.markdown("""
        #### Modernizing Data Lakes and Data Warehouses with Google Cloud
        """)

        st.caption("Google Cloud")


    with col2:

        st.image(
            "assets/certificacoes/fiaap.jfif",
            use_container_width=True
        )

        st.markdown("""
        #### Python Developer  
        """)

        st.caption("FIAP")


    with col3:

        st.image(
            "assets/certificacoes/ibm.jfif",
            use_container_width=True
        )

        st.markdown("""
        #### Python  
        IBM
        """)

        st.caption("IBM")


    with col4:

        st.image(
            "assets/certificacoes/pipeline_gcp.jfif",
            use_container_width=True
        )

        st.markdown("""
        #### Building Batch Data Pipelines on Google Cloud 
        """)

        st.caption("Google Cloud")     


with aba4:

    st.write("## Hobbies")

    st.write("""
    - Viajar
    - Futebol
    - Desenvolvimento de Games
    - Academia
    """)