import streamlit as st
import functions as ft
import pandas as pd
import graphs as gph
from PIL import Image

ft.config_page()

st.title('Data Analyst & Scientist job market research')

df_jobs = pd.read_csv(ft.csv_path)

menu = st.sidebar.selectbox('Seleccionar menú:', ('Principal', 'Gráficos', 'Filtros'))
if menu == 'Principal':
    ft.home()

if menu == 'Gráficos':
    with st.beta_expander('Ver mapa de puestos por ciudad y tipo:'):

        st.markdown('''#### En el mapa se indica con puntos rojos las ubicaciones en las que existen\
                    puestos de Data Analyst y Data Scientist.''')

        st.map(df_jobs)

        st.markdown('''#### Teniendo en cuenta todos los puestos analizados, la gran mayoría se\
                    se concentran en las dos capitales más importantes.''')

        graph_npuestos_ciudad = gph.graph_npuestos_ciudad(gph.df)
        st.plotly_chart(graph_npuestos_ciudad)

    with st.beta_expander('Ver gráfico de palabras descritas en el puesto:'):
        st.markdown('''#### Las palabras de mayor tamaño, son las que más se utilizan\
                    a la hora de describir los puestos de trabajo.''')

        st.text("")

        st.markdown('#### Palabras que contienen Data Analyst')
        img_puesto_da = Image.open('data/graph_puesto_da.png')
        st.image(img_puesto_da, use_column_width='auto')

        st.markdown('#### Palabras que contienen Data Scientist')
        img_puesto_ds = Image.open('data/graph_puesto_ds.png')
        st.image(img_puesto_ds, use_column_width='auto')

    with st.beta_expander('Ver gráfico de: Nº publicaciones activas'):

        st.markdown('''#### Se pretende analizar cuantos días dura un puesto activo.\n'
                    Los resultados son muy parecidos para ambos puestos.''')

        graph_dias_da = gph.graph_dias_da(gph.df)
        st.plotly_chart(graph_dias_da)

        graph_dias_ds = gph.graph_dias_ds(gph.df)
        st.plotly_chart(graph_dias_ds)

    with st.beta_expander('Ver gráfico de: Nº solicitudes por empresa'):

        st.markdown('''#### Análisis del top 10 de empresas por número de solicitudes.
                    ''')

        graph_nsolicitudes = gph.graph_nsolicitudes(gph.df)
        st.plotly_chart(graph_nsolicitudes)

    with st.beta_expander('Ver gráfico de: Experiencia solicitada'):

        st.markdown('''#### Análisis de la experiencia solicitada por las empresas\
                    diferenciada por tipo de puesto.''')

        graph_nexp = gph.graph_nexp(gph.df)
        st.plotly_chart(graph_nexp)

    with st.beta_expander('Ver gráfico de: Tipo de jornada'):

        st.markdown('''#### Análisis del tipo de jornada del puesto.\
                    ''')

        graph_jornada = gph.graph_jornada(gph.df)
        st.plotly_chart(graph_jornada)

    with st.beta_expander('Ver gráfico de palabras en las descripciones:'):
        st.markdown('''#### Las palabras de mayor tamaño, son las que más se utilizan\
                    en las descripciones de las funciones.''')

        st.text("")

        st.markdown('#### Palabras de las descripciones Data Analyst')
        img_desc_da = Image.open('data/graph_desc_da.png')
        st.image(img_desc_da, use_column_width='auto')

        st.markdown('#### Palabras de las descripciones Data Scientist')
        img_desc_ds = Image.open('data/graph_desc_ds.png')
        st.image(img_desc_ds, use_column_width='auto')

if menu == 'Filtros':
    ft.filtros(df_jobs)
