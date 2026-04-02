import streamlit as st

# 1. Base de datos de prueba (Simulada)
# En el futuro, esto estará en un archivo o base de datos real.
usuarios = {
    "moto01": {
        "nombre": "Emanuel Masuelli",
        "sangre": "O+",
        "alergias": "La pala",
        "contacto": "264-1234567",
        "parentesco": "Madre (María)"
    },
    "moto02": {
        "nombre": "Sofía García",
        "sangre": "O-",
        "alergias": "Ninguna",
        "contacto": "264-7654321",
        "parentesco": "Hermano (Luis)"
    }
}

# 2. Configuración de la página
st.set_page_config(page_title="Ficha Médica de Emergencia", page_icon="🚑")

# 3. Capturar el ID desde la URL (ej: ?id=moto01)
query_params = st.query_params
user_id = query_params.get("id")

# 4. Lógica de visualización
if user_id in usuarios:
    datos = usuarios[user_id]
    
    st.error("🚨 INFORMACIÓN DE EMERGENCIA")
    st.header(f"Titular: {datos['nombre']}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Grupo Sanguíneo", datos['sangre'])
    with col2:
        st.write("**Alergias:**")
        st.warning(datos['alergias'])
    
    st.divider()
    
    st.subheader("Contacto de Emergencia")
    st.write(f"📞 {datos['parentesco']}: {datos['contacto']}")
    
    # Botón que simula una llamada (funciona en móviles)
    st.link_button(f"LLAMAR A {datos['parentesco'].upper()}", f"tel:{datos['contacto']}")

else:
    st.title("Bienvenido")
    st.write("Escanee un código QR válido para ver la información de emergencia.")
    st.info("Si sos el dueño, recordá que tu ID debe estar activo.")