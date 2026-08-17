import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="LH Nautical — Dashboard Analítico",
    layout="wide"
)

st.title("LH Nautical — Análise de Dados")

aba0, aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "Análise Geral",
    "Visão Geral",
    "Intervalo de Datas",
    "Clientes de Elite",
    "Pior Dia de Vendas",
    "Previsão de Demanda",
    "Recomendação de Produtos"
])


with aba0:
    st.markdown("---")

    st.markdown("""
    ###  Resumo das principais análises

    - **Estoque:** 100% dos registros de `stock_levels` estão sem ponto de reposição (`reorder_point`) definido — ausência de processo estruturado de reabastecimento
    - **Coletes x Âncoras:** o desequilíbrio relatado pela Diretoria não se confirma no snapshot atual de estoque (médias praticamente iguais); possivelmente um problema sazonal, não estrutural
    - **Pior dia de vendas:** Domingo é o 2º pior dia (não o melhor, como o estagiário concluiu) — ver aba "Pior Dia de Vendas"
    - **Previsão de demanda:** baseline de média móvel tem MAE de ~19 unidades para a Bússola de Bordo 702 — ver aba "Previsão de Demanda"
    - **Clientes de elite:** identificados 10 clientes com alto ticket médio e diversidade de compra em até 14 categorias — ver aba "Clientes de Elite"
    """)

    st.markdown("---")

    st.caption("""
    Esta aba ("Análise Geral") apresenta achados de uma exploração adicional dos dados 
    (tabelas `stock_levels`, `product_variants` e `products`), complementar às 7 questões 
    formais do desafio, realizada para investigar diretamente o cenário relatado pela 
    Diretoria sobre gestão de estoque.
    """)

    st.metric(
        "Registros de Estoque com Ponto de Reposição Definido",
        "0%",
        delta="6.054 de 6.054 registros sem reorder_point",
        delta_color="inverse"
    )

    st.markdown("""
    **Achado:** A tabela de níveis de estoque não possui, em nenhum
    registro, um ponto de reposição (`reorder_point`) definido.

    Isso indica que a empresa não possui um processo sistemático de
    alerta para reposição de estoque, o que pode contribuir para
    episódios como a ruptura do estoque de Coletes Salva-Vidas
    mencionada pela Diretoria.

    **Recomendação:** implementar pontos de reposição por produto,
    baseados no histórico de vendas e no lead time dos fornecedores.
    """)

    st.markdown("""
    **Verificação do cenário relatado (Coletes Salva-Vidas x Âncoras):**

    Ao comparar o estoque atual desses dois produtos citados pela Diretoria, não foi identificada 
    uma assimetria evidente: Coletes Salva-Vidas somam 556 unidades em estoque (média de ~15,9 
    por variante), enquanto Âncoras somam 601 unidades (média de ~15,4 por variante), ou seja,  números 
    muito próximos entre si.

    Isso sugere que o desequilíbrio relatado pode ter 
    sido pontual, associado a um período específico (o verão mencionado no cenário), e não se 
    reflete no snapshot atual de estoque disponível na base de dados. A ausência de `reorder_point` 
    definido (achado anterior) permanece como a causa estrutural mais provável para esse tipo de 
    episódio, independentemente do estoque momentâneo de cada item.
    """)


with aba1:
    st.header("Visão Geral dos Dados")

    dados_q1 = pd.read_csv("resultados_quest_streamlit/q1_visao_geral.csv")

    st.dataframe(dados_q1, use_container_width=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total de Pedidos", "50.000")
    col2.metric("Data Mínima", "2020-01-01")
    col3.metric("Data Máxima", "2026-12-31")


with aba2:
    st.header("Intervalo de Datas")

    dados_q1_2 = pd.read_csv("resultados_quest_streamlit/q1_intervalo_datas.csv")

    st.dataframe(dados_q1_2, use_container_width=True)

    st.markdown("""
    O intervalo de valores apresentado pode indicar uma distribuição
    assimétrica dos dados, especialmente caso os valores mínimo e
    máximo estejam muito distantes da média.

    **Observação:** essa diferença, por si só, não confirma a presença
    de outliers. É necessário utilizar métodos estatísticos, como o
    intervalo interquartil (IQR), para identificá-los com maior
    segurança.
    """)


with aba3:
    st.header("Clientes de Elite")

    dados_q4 = pd.read_csv("resultados_quest_streamlit/q4_clientes_elite.csv")

    st.dataframe(dados_q4, use_container_width=True)


with aba4:
    st.header("Pior Dia de Vendas")

    dados_q5 = pd.read_csv("resultados_quest_streamlit/q5_pior_dia.csv")

    st.dataframe(dados_q5, use_container_width=True)

    st.metric(
        "Média de vendas aos Domingos",
        "R$ 157.616",
        delta="-96,8% vs. estimativa inicial (R$ 5.000)",
        delta_color="inverse"
    )


with aba5:
    st.header("Previsão de Demanda")

    dados_q6 = pd.read_csv("resultados_quest_streamlit/q6_previsao.csv")

    st.subheader("Valores reais x valores previstos")
    st.dataframe(dados_q6, use_container_width=True)

    dados_mae = pd.read_csv("dados/q6_mae.csv")

    st.subheader("Erro Médio Absoluto (MAE)")
    st.dataframe(dados_mae, use_container_width=True)

    st.subheader("Comparação entre valores reais e previstos")
    st.line_chart(
        dados_q6.set_index("mes")[["valor_real", "valor_previsto"]]
    )


with aba6:
    st.header("Recomendação de Produtos")

    dados_q7 = pd.read_csv("resultados_quest_streamlit/q7_recomendacao.csv")

    st.dataframe(dados_q7, use_container_width=True)