import streamlit as st 
from datetime import date
from models.clientes_model import ClientesModel


def form_clientes(id):
    ssf = st.session_state
    if "id" not in ssf:
        ssf.id = id
        ssf.cliente = ""
        ssf.tel = ""
        ssf.proyecto = ""
        ssf.fecha = ""
        #ssf.fecha = date.today()

    item = ClientesModel.getClienteById(ssf.id) if ssf.id else ClientesModel()
    print(item.cliente)

    with st.container(border=True):
        c1,c2,c3 = st.columns(3)
        cliente = c1.text_input("Cliente:", autocomplete="off", key="cliente", value=item.cliente)
        tel = c2.text_input("Teléfono:", autocomplete="off", key="tel", value=item.tel)
        fecha = c3.date_input("Fecha:", key="fecha", value=item.fecha)
        proyecto = st.text_area("Proyecto:", key="proyecto", value=item.proyecto) 
        
        def guardar():
            if cliente:
                #consulta
                ClientesModel.create(cliente, tel, proyecto, fecha)
                ssf.id = ""
                ssf.cliente = ""
                ssf.tel = ""
                ssf.proyecto = ""
                ssf.fecha = date.today()
                st.toast("Cliente guardado", icon="✅")
            else:
                st.warning("Escribe el nombre del cliente")

        if id:
            #Editar
            print()
        else:
            #Guardar
            st.button("Guardar", on_click=guardar)
