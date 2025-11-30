import streamlit as st 
from models.clientes_model import ClientesModel
from components.form_clientes import form_clientes

def alta_clientes():
    

    ss = st.session_state
    if "clientes" not in ss:
        ss.clientes = []

    if "id" not in ss:
        ss.id = ""

    def getId(id):
        ss.id = id
        

    _,col,_=st.columns([1,3,1])
    with col:
        st.title("Alta de Cliente")
        form_clientes(ss.id)

    

    # Fila de titulos de columnas
    with st.container(border=True):
        ccc1,ccc2,ccc3,ccc4,ccc5,ccc6 = st.columns(6)
        ccc1.write("ID",)
        ccc2.write("Cliente")
        ccc3.write("Teléfono")
        ccc4.write("Proyecto")
        ccc5.write("Fecha")
        ccc6.write("Acciones")
    
    ss.clientes = ClientesModel.get_all()

    if ss.clientes:
        for cliente in ss.clientes:
            with st.container(border=True):
                cc1,cc2,cc3,cc4,cc5,cc6 = st.columns(6)
                cc1.write(f"{cliente.id}")
                cc2.write(f"{cliente.cliente}")
                cc3.write(f"{cliente.tel}")
                cc4.write(f"{cliente.proyecto}")
                cc5.write(f"{cliente.fecha}")
                cc6.button("Editar/Eliminar", key=f"edit_{cliente.id}", icon=":material/edit:", on_click=getId, args=(cliente.id,))
                #with cc6:
                    #cl1,cl2,_ = st.columns([1,1,3])
                    #cl1.button("", key=f"edit_{cliente.id}", icon=":material/edit:", on_click=getId, args=(cliente.id,))
                    #cl2.button("", key=f"delete_{cliente.id}", icon=":material/delete:", type="primary")
                    
    else:
        st.caption("No hay clientes registrados en la base de datos")
    