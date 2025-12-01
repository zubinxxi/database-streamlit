import streamlit as st
from datetime import date
from models.clientes_model import ClientesModel


def form_clientes(id):
    ssf = st.session_state
    #if "id" not in ssf:
     #   ssf.id = ""
    #    ssf.cliente = ""
    #    ssf.tel = ""
    #    ssf.proyecto = ""
    #    ssf.fecha = ""

    # 1. Cargar el objeto cliente (item)
    # Usamos el ID pasado como argumento, no el ID de la sesión de estado  
    item = ClientesModel.getClienteById(id) if id else ClientesModel()

    # Si el item no existe (p. ej., ID inválido), inicializar un objeto vacío.
    if id and not item.id: 
         st.warning(f"No se encontró el cliente con ID: {id}. Volviendo al modo inserción.")
         id = None
         item = ClientesModel()
         # Asegurarse de limpiar el ID de edición en el ssf (ver punto 4.1)

    # 2. *** SOLUCIÓN CLAVE: Forzar la actualización del Session State ***
    # Forzamos los valores del objeto 'item' a las claves del ssf antes de que se dibujen los inputs.
    if id:
        # Modo Edición: Usar los valores cargados
        st.subheader(f"📝 Editar Cliente (ID: {id})")
        ssf.cliente = item.cliente
        ssf.tel = item.tel
        ssf.proyecto = item.proyecto
        ssf.fecha = item.fecha if isinstance(item.fecha, date) else date.today()
    else:
        # Modo Inserción: Reiniciar el estado
        st.subheader("➕ Agregar Cliente")
        # Es buena práctica limpiar las keys de los inputs para evitar que se rellenen con datos viejos
        ssf.id = ""
        ssf.cliente = ""
        ssf.tel = ""
        ssf.proyecto = ""
        ssf.fecha = date.today()
        item.id = ""
        item.cliente = ""
        item.tel = ""
        item.proyecto = ""
        item.fecha = date.today()
        #if id in ssf.id: ssf.id = ""
        #if 'cliente' in ssf: ssf.cliente = ""
        #if 'tel' in ssf: ssf.tel = ""
        #if 'proyecto' in ssf: ssf.proyecto = ""        
        #if 'fecha' in ssf: ssf.fecha = date.today()
        #item.fecha = date.today() # Establecer fecha por defecto para la inserción

    # 3. Dibujar el Formulario (Los inputs ahora leerán los valores actualizados de ssf)
    with st.container(border=True):
        c1, c2, c3 = st.columns(3)

        # Aunque usamos 'value=item.atributo', el valor correcto ya está forzado en ssf
        cliente = c1.text_input("Cliente:", autocomplete=None, value=item.cliente )
        tel = c2.text_input("Tel:", autocomplete=None, value=item.tel)
        fecha = c3.date_input("Fecha:", value=item.fecha)
        proyecto = st.text_area("Proyecto", value=item.proyecto)

        # 4. Lógica de Guardar/Actualizar
        def guardar():
            if cliente:
                #consulta
                ClientesModel.create(cliente, tel, proyecto, fecha)
                ssf.current_edit_id = None
                ssf.id = ""
                ssf.cliente = ""
                ssf.tel = ""
                ssf.proyecto = ""
                ssf.fecha = date.today()
                st.toast("Guardo correctamente", icon="✅")
               
            else:
                st.warning("Escribe el nombre del cliente", icon="⚠️")
                
        def editar():
            ClientesModel.update(id, cliente, tel, proyecto, fecha)
            st.toast("Actualizo correctamente", icon="✅")
            ssf.id = ""
            ssf.current_edit_id = None
            

        def eliminar():
            ClientesModel.delete(id)
            st.toast("Elimino correctamente", icon="✅")
            ssf.id = ""
            ssf.current_edit_id = None
            

        def cancelar():
            ssf.id = ""
            ssf.current_edit_id = None
            
        
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
