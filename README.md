## EDA
Este EDA tiene la finalidad de intentar entender el mercado laboral de Data Analyst y Data Scientist.

Para esta ocasión se ha determinado buscar el dataset a través de la red social LinkedIn, creando una base de datos para posteriormente analizarla y sacar las conclusiones.

Todo el código está escrito en `Python`, utilizando `notebooks` y `PyCharm CE`. También se han utilizado otras herramientas y librerías como `Streamlit` y `Selenium`.


### Etapas:

Se han definido 4 etapas diferenciadas:

1. **Web scraping**: para la recogida de datos se ha llevado a cabo la técnica de web scraping sobre LinkedIn con la librería de `Selenium` y utilizando como navegador `Chrome`. Hay dos notebooks documentados con las pruebas de como se ha llegado a la obtención. Y un tercero con la versión definitiva `WS_Linkedin`.

    En resumen, consiste en buscar el empleo deseado en la red social y ejecutar el código sobre cada página. Contando que cada página tiene como unos 25 puestos. En total se han recogido 800 vacantes de cada tipo de puesto.
    

2. **Limpieza de datos**: una vez obtenidos los datos, debido a que el *scraping* no era 100 % efectivo, hubo que limpiar los datos. Está documentado en el notebook `Data_cleaning`.

3. **Análisis**: a partir de esta etapa, se ha tratado de analizar los diferentes tipos de datos. Debido a que casi todos los datos son cualitativos, se han realizado `counts` por agrupaciones y análisis de palabras concretas. Están recogidas en el notebook `Data_cleaning`.
   
![Texto alternativo](main/pres_streamlit/data/graph_puesto_da.png)

4. **Presentación**: Por último, el desarrollo de la presentación se ha decidido hacerlo en `Streamlit`. Ya que ofrece una serie de características que se creía idóneo para la visualización del proyecto.

    4.1 Separación por pestañas: dividiendo el trabajo por secciones, haciéndolo más dinámico.
    
    4.2 Uso de mapa para representar las ubicaciones de los puestos de trabajo.
    
    4.3 Filtrado del dataframe para comprobar cualquier tipo de empresa, puesto ofertado, ubicación, nivel de experiencia o nº de solicitudes.

    4.4 Todo el código de *Streamlit* ha sido desarrollado en el IDE PyCharm CE.
    
Se puede acceder a la web a través de este enlace.

![Texto alternativo](data/mapa_streamlit.png)
