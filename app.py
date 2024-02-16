# Importando as bibliotecas necessárias
import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo o arquivo CSV
car_data = pd.read_csv('vehicles.csv')


# Criando o cabeçalho
st.header('Análise de Dados de Veículos')

# Criando um botão para o histograma
hist_button = st.button('Criar histograma')

# Se o botão do histograma for clicado
if hist_button:
    # Escrevendo uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # Criando um histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Exibindo um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Criando um botão para o gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

# Se o botão do gráfico de dispersão for clicado
if scatter_button:
    # Escrevendo uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # Criando um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # Exibindo um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)