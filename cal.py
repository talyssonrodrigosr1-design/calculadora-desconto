import streamlit as st
st.title("Calculadora de Descontos")
preco_original=st.number_input("Digite o Valor do Serviço")
porgetagem=st.number_input("Digite a porgetagem do produto")
if st.button("Calcular"):
   valor_desconto= preco_original*(porgetagem/100)
   valor_final=preco_original-valor_desconto
   st.write(f'Meu amor o Valor pra cobrar do cliente é:{valor_final:.2f}')
