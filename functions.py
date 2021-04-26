import streamlit as st
from PIL import Image


def config_page():
    st.set_page_config(page_title='Data Analyst & Scientist research', page_icon=':electric_plug:',
                       layout="wide",
                       initial_sidebar_state="auto")


csv_path = 'data/map_jobs2.csv'


def home():

    st.markdown('<div align=center></div>\n',
                unsafe_allow_html=True)

    st.text("")

    img = Image.open('data/big_data.jpg')
    st.image(img, use_column_width='auto')

    st.markdown('''\n
        ### Este EDA tiene la finalidad de intentar entender el mercado laboral de Data Analyst\
         y Data Scientist.
        Para esta ocasión se ha determinado buscar el dataset a través de la red social LinkedIn,\
        creando una base de datos para posteriormente analizarla y sacar las conclusiones.
         
        Se divide en tres pestañas:\n
        - **Principal**: presentación del proyecto.\n
        - **Gráficos**: análisis del dato exploratorio.\n
        - **Filtros**: comprobación de la tabla de datos para la búsqueda de información.
                ''')

    with st.beta_expander('Basado en los roles Data Analyst y Data Scientist.'):
        img_job_types = Image.open('data/job_types.png')
        st.image(img_job_types, use_column_width='auto')


def filtros(df_jobs):

    check_puesto = st.sidebar.checkbox('¿Quieres filtrar por tipo del puesto?')
    puesto = df_jobs['Tipo puesto'].unique().tolist()
    filtro_puesto = st.sidebar.selectbox('Selecciona el tipo del puesto', puesto)

    check_emp = st.sidebar.checkbox('¿Quieres filtrar por empresa?')
    emp = df_jobs['Nombre empresa'].unique().tolist()
    filtro_emp = st.sidebar.selectbox('Selecciona la empresa', emp)

    check_ubic = st.sidebar.checkbox('¿Quieres filtrar por ubicación?')
    ubic = df_jobs['Ubicación'].unique().tolist()
    filtro_ubic = st.sidebar.selectbox('Selecciona la ubicación del puesto', ubic)

    check_exp = st.sidebar.checkbox('¿Quieres filtrar por nivel de  experiencia?')
    exp = df_jobs['Nivel experiencia'].unique().tolist()
    filtro_exp = st.sidebar.selectbox('Selecciona la ubicación del puesto', exp)

    check_solicitudes = st.sidebar.checkbox('¿Filtrado por número de solicitudes?')
    max_carg = df_jobs['Nº Solicitudes'].max()
    n_posibles = range(max_carg + 1)
    filtro_solicitudes = st.sidebar.select_slider('Selecciona el nº máximo de solicitudes.',
                                                  n_posibles, value=max_carg)

    if check_puesto:
        df_jobs = df_jobs.loc[df_jobs['Tipo puesto'] == filtro_puesto, :]

    if check_emp:
        df_jobs = df_jobs.loc[df_jobs['Nombre empresa'] == filtro_emp, :]

    if check_ubic:
        df_jobs = df_jobs.loc[df_jobs['Ubicación'] == filtro_ubic, :]

    if check_exp:
        df_jobs = df_jobs.loc[df_jobs['Nº Solicitudes'] == filtro_exp, :]

    if check_solicitudes:
        mask2 = df_jobs['Nº Solicitudes'] <= filtro_solicitudes
        df_jobs = df_jobs[mask2]
    st.write(df_jobs)

    if df_jobs.shape[0] == 0:
        st.warning('No existen empresas')
        st.stop()
