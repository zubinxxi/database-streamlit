import streamlit as st 
from views.alta_clientes import alta_clientes
from views.clientes import clientes

st.set_page_config(
    page_title="Clientes | Streamlit",
    page_icon="assets/favicon.ico",
    layout="wide"
)

tab1,tab2 = st.tabs(["Alta Clientes", "Mostrar Clientes"])

with tab1:
    alta_clientes()

with tab2:
    clientes()


#import os
#import mysql.connector
#from dotenv import load_dotenv


# Cargar las variables de entorno desde el archivo .env
#load_dotenv()

#def init_connector():
#    return mysql.connector.connect(
#        host=os.getenv("DB_HOST"),
#        port=os.getenv("DB_PORT"),
#        database=os.getenv("DB_NAME"),
#        user=os.getenv("DB_USER"),
#        password=os.getenv("DB_PASSWD"),
#    )

#con = init_connector()

#@st.cache_data()
#def run_query(query):
#    with con.cursor(dictionary=True) as cur:
#        cur.execute(query)
#        return cur.fetchall()
    
#sel_clientes=run_query("SELECT * FROM clientes")

#for cliente in sel_clientes:
#   st.write(cliente['cliente'])
