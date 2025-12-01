import streamlit as st 
from models.clientes_model import ClientesModel
from components.form_clientes import form_clientes

def alta_clientes():

    ss = st.session_state
    if "clientes" not in ss:
        ss.clientes = []

    if "id" not in ss:
        ss.id = ""

    #def getId(id):
    #    ss.id = id
    # Obtener el ID de edición (será None si no se ha pulsado el botón)
    edit_id = ss.get('current_edit_id', None)    

    _, col, _=st.columns([1,3,1])
    with col:
        st.title("Alta de Cliente")
        form_clientes(edit_id)

    

    # Fila de titulos de columnas
    with st.container(border=True):
        ccc1,ccc2,ccc3,ccc4,ccc5,ccc6 = st.columns(6)
        ccc1.write("ID",)
        ccc2.write("CLIENTE")
        ccc3.write("TELÉFONO")
        ccc4.write("PROYECTO")
        ccc5.write("FECHA")
        ccc6.write("ACCIONES")
    
    ss.clientes = ClientesModel.get_all()

    if ss.clientes:
        for cliente in ss.clientes:
            with st.container(border=True):
                cc1, cc2, cc3, cc4, cc5, cc6 = st.columns(6)
                cc1.write(f"{cliente.id}")
                cc2.write(cliente.cliente)
                cc3.write(cliente.tel)
                cc4.write(cliente.proyecto)
                cc5.write(cliente.fecha)
                #cc6.button("Editar / Eliminar", key=f"edit_{cliente.id}", icon=":material/edit:", on_click=getId, args=(cliente.id,))
                with cc6:
                    if st.button("Editar / Eliminar", key=f"edit_{cliente.id}", icon=":material/edit:", help="Editar o eliminar registro" ):
                        st.session_state.current_edit_id = cliente.id
                        st.rerun()
                    
    else:
        st.caption("No hay clientes registrados en la base de datos")
    