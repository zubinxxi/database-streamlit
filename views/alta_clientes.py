import streamlit as st 
from models.clientes_model import ClientesModel
from components.form_clientes import form_clientes

def alta_clientes():
    

    ss = st.session_state
    if "clientes" not in ss:
        ss.clientes = []

    if "id" not in ss:
        ss.id=""

    _,col,_=st.columns([1,3,1])
    with col:
        st.title("Alta de Cliente")
        form_clientes(ss.id)

    ss.clientes = ClientesModel.get_all()

    if ss.clientes:
        for cliente in ss.clientes:
            with st.container(border=True):
                cc1,cc2,cc3,cc4,cc5,cc6 = st.columns(6)
                with cc1:
                    st.write(f"{cliente.id}")
                with cc2:
                    st.write(f"{cliente.cliente}")
                with cc3:
                    st.write(f"{cliente.tel}")
                with cc4:
                    st.write(f"{cliente.proyecto}")
                with cc5:
                    st.write(f"{cliente.fecha}")
                with cc6:
                    cl1,cl2,_ = st.columns([1,1,3])
                    cl1.button("", key=f"delete_{cliente.id}", icon=":material/delete:", type="primary")
                    cl2.button("", key=f"edit_{cliente.id}", icon=":material/edit:")
    else:
        st.write("No hay clientes registrados")
    