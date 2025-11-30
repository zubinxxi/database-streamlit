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
        
    item = ClientesModel.getClienteById(id) if id else ClientesModel()

    with st.container(border=True):
        c1, c2, c3 = st.columns(3)
        cliente = c1.text_input("Cliente:", autocomplete="off", key="cliente", value=item.cliente )
        tel = c2.text_input("Tel:", autocomplete="off", key="tel", value=item.tel)
        fecha = c3.date_input("Fecha:", key="fecha", value=item.fecha)
        proyecto = st.text_area("Proyecto", key="proyecto", value=item.proyecto)

        def guardar():
            if cliente:
                #consulta
                ClientesModel.create(cliente, tel, proyecto, fecha)
                ssf.cliente = ""
                ssf.tel = ""
                ssf.proyecto = ""
                ssf.fecha = date.today()
                st.toast("Guardo correctamente")
            else:
                st.warning("Escribe el nombre del cliente")
                
        def editar():
            ClientesModel.update(id, cliente, tel, proyecto, fecha)
            ssf.id = ""
            st.toast("Actualizo correctamente")

        def eliminar():
            ClientesModel.delete(id)
            ssf.id = ""
            st.toast("Elimino correctamente")

        def cancelar():
            ssf.id = ""
        
        if id:
            #Editar
            b1,b2,b3,b4 = st.columns([1,1,1,5])
            b1.button("Editar", on_click=editar)
            b2.button("Cancelar", on_click=cancelar)
            toggle = b3.toggle("Eliminar")
            if toggle:
                b4.button("Eliminar", on_click=eliminar, type="primary")
        else:
            #Guardar
            st.button("Guardar", on_click=guardar)
