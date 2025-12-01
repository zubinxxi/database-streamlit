import streamlit as st
from models.clientes_model import ClientesModel
import pandas as pd

def clientes():
    st.title("Mostrar Clientes")

    ss = st.session_state
    if "df_clientes" not in ss:
        ss.df_clientes = []

    clientes = ClientesModel.get_all_dataframe()
    ss.df_clientes = pd.DataFrame(clientes)
    ss.df_clientes["Eliminar"] = False
    data = st.data_editor(ss.df_clientes, hide_index=True, width="stretch")

    rc1, rc2, _ = st.columns([1,1,12])
    with rc1:
        if st.button("Editar", icon=":material/edit:"):
            for index, row in data.iterrows():
                ClientesModel.update(
                    id = row["id"],
                    cliente = row["cliente"],
                    tel = row["tel"],
                    proyecto = row["proyecto"],
                    fecha = row["fecha"],
                )
            st.toast("Cliente editado correctamente", icon="✅")
    with rc2:
        @st.dialog("Eliminar registros")
        def delete():
            st.error("Deseas eliminar los registros?")
            if st.button("Aceptar"):
                rows_to_delete = data[data["Eliminar"]]
                if not rows_to_delete.empty:
                    for _, row in rows_to_delete.iterrows():
                        ClientesModel.delete(row["id"])
                    st.toast("Registros eliminados correctamente", icon="✅")
                    ss.df_clientes = ClientesModel.get_all_dataframe()
                    st.rerun()
                else:
                    st.warning("No se seleccionaron registros para eliminar")


        if st.button("Eliminar", icon=":material/delete:", type="primary"):
            delete()