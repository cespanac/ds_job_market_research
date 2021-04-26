import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots

import plotly.graph_objs as go


df = pd.read_csv('data/info_data_job_market_research.csv')


def graph_npuestos_ciudad(df):
    df_ub_da = df[df['Tipo puesto'] == 'Data Analyst']
    df_ub_da = df_ub_da['Ubicación'].copy()
    df_ub_da_top = df_ub_da.value_counts()[:6]
    df_ub_da_other = df_ub_da.value_counts()[7:].count()
    df_ub_da_other = pd.Series([df_ub_da_other], index=['Otras ciudades'])
    df_ub_da_ok = df_ub_da_top.append(df_ub_da_other)
    df_ub_da_ok.rename('Data Analyst', inplace=True)
    df_ub_da_ok = pd.DataFrame(df_ub_da_ok)

    df_ub_ds = df[df['Tipo puesto'] == 'Data Scientist']
    df_ub_ds = df_ub_ds['Ubicación'].copy()
    df_ub_ds_top = df_ub_ds.value_counts()[:6]
    df_ub_ds_other = df_ub_ds.value_counts()[7:].count()
    df_ub_ds_other = pd.Series([df_ub_ds_other], index=['Otras ciudades'])
    df_ub_ds_ok = df_ub_ds_top.append(df_ub_ds_other)
    df_ub_ds_ok.rename('Data Scientist', inplace=True)
    df_ub_ds_ok = pd.DataFrame(df_ub_ds_ok)

    result = pd.concat([df_ub_da_ok, df_ub_ds_ok], axis=1)

    result.sort_values(by=['Data Analyst'], ascending=False)

    labels = list(result.index)

    graph_npuestos_ciudad = go.Figure()
    graph_npuestos_ciudad.add_trace(go.Bar(
        x=labels,
        y=result['Data Analyst'],
        name='Data Analyst',
        marker_color='green'
    ))
    graph_npuestos_ciudad.add_trace(go.Bar(
        x=labels,
        y=result['Data Scientist'],
        name='Data Scientist',
        marker_color='rgba(48,45,255)'
    ))

    graph_npuestos_ciudad.update_layout(barmode='group', xaxis_tickangle=-45, template="plotly_white")

    return graph_npuestos_ciudad


def graph_dias_da(df):
    diasact_da = df[df['Tipo puesto'] == 'Data Analyst']

    diasact_da = diasact_da['Días activos'].copy()

    lista_dias = ['segundo', 'segundos', 'minuto', 'minutos', 'hora', 'horas', 'día', 'días']

    for i in lista_dias:
        diasact_da[diasact_da.str.contains(i)] = '03-08-21'

    diasact_da[diasact_da.str.contains(' 1 semana')] = '03-01-21'
    diasact_da[diasact_da.str.contains(' 2 semanas')] = '02-22-21'
    diasact_da[diasact_da.str.contains(' 3 semanas')] = '02-15-21'
    diasact_da[diasact_da.str.contains(' 4 semanas')] = '02-08-21'
    diasact_da[diasact_da.str.contains(' 1 mes')] = '02-01-21'
    diasact_da[diasact_da.str.contains(' 2 meses')] = '01-25-21'
    diasact_da[diasact_da.str.contains(' 3 meses')] = '01-18-21'
    diasact_da[diasact_da.str.contains(' 4 meses')] = '01-11-21'
    diasact_da[diasact_da.str.contains(' 5 meses')] = '01-04-21'

    diasact_da = diasact_da.value_counts()

    diasact_da.drop('no_data', inplace=True)

    df_diasact_da = pd.DataFrame(diasact_da)

    df_diasact_da.reset_index(inplace=True)

    df_diasact_da.rename(columns={'index': 'Fechas'}, inplace=True)

    df_diasact_da['Fechas'] = pd.to_datetime(df_diasact_da['Fechas'])

    df_diasact_da.sort_values('Fechas', ascending=True, inplace=True)

    graph_dias_da = px.bar(df_diasact_da, x='Fechas', y='Días activos',
                 template="presentation",
                 labels={'Fechas': 'Semanas',
                         'Días activos': 'Nº puestos activos'})

    graph_dias_da.update_traces(marker=dict(color='green'))
    graph_dias_da.update_layout(title_text='Nº publicaciones activas D. Analyst por semanas')
    graph_dias_da['layout']['xaxis']['autorange'] = "reversed"

    return graph_dias_da

def graph_dias_ds(df):
    diasact_ds = df[df['Tipo puesto'] == 'Data Analyst']

    diasact_ds = diasact_ds['Días activos'].copy()

    lista_dias = ['segundo', 'segundos', 'minuto', 'minutos', 'hora', 'horas', 'día', 'días']

    for i in lista_dias:
        diasact_ds[diasact_ds.str.contains(i)] = '03-08-21'

    diasact_ds[diasact_ds.str.contains(' 1 semana')] = '03-01-21'
    diasact_ds[diasact_ds.str.contains(' 2 semanas')] = '02-22-21'
    diasact_ds[diasact_ds.str.contains(' 3 semanas')] = '02-15-21'
    diasact_ds[diasact_ds.str.contains(' 4 semanas')] = '02-08-21'
    diasact_ds[diasact_ds.str.contains(' 1 mes')] = '02-01-21'
    diasact_ds[diasact_ds.str.contains(' 2 meses')] = '01-25-21'
    diasact_ds[diasact_ds.str.contains(' 3 meses')] = '01-18-21'
    diasact_ds[diasact_ds.str.contains(' 4 meses')] = '01-11-21'
    diasact_ds[diasact_ds.str.contains(' 5 meses')] = '01-04-21'

    diasact_ds = diasact_ds.value_counts()

    diasact_ds.drop('no_data', inplace=True)

    df_diasact_ds = pd.DataFrame(diasact_ds)

    df_diasact_ds.reset_index(inplace=True)

    df_diasact_ds.rename(columns={'index': 'Fechas'}, inplace=True)

    df_diasact_ds['Fechas'] = pd.to_datetime(df_diasact_ds['Fechas'])

    df_diasact_ds.sort_values('Fechas', ascending=True, inplace=True)

    graph_dias_ds = px.bar(df_diasact_ds, x='Fechas', y='Días activos',
                 template="presentation",
                 labels={'Fechas': 'Semanas',
                         'Días activos': 'Nº puestos activos'})

    graph_dias_ds.update_traces(marker=dict(color='rgba(48,45,255)'))
    graph_dias_ds.update_layout(title_text='Nº publicaciones activas D. Scientist por semanas')
    graph_dias_ds['layout']['xaxis']['autorange'] = "reversed"

    return graph_dias_ds

def graph_nsolicitudes(df):
    sol_da = df[df['Tipo puesto'] == 'Data Analyst']
    sol_ds = df[df['Tipo puesto'] == 'Data Scientist']

    mask_sol_da = sol_da.groupby(['Nombre empresa'])['Nº Solicitudes'].sum()
    mask_sol_da = mask_sol_da.sort_values(ascending=False)[:10]
    mask_sol_da = pd.DataFrame(mask_sol_da)
    mask_sol_da.reset_index(inplace=True)

    mask_sol_ds = sol_ds.groupby(['Nombre empresa'])['Nº Solicitudes'].sum()
    mask_sol_ds = mask_sol_ds.sort_values(ascending=False)[:10]
    mask_sol_ds = pd.DataFrame(mask_sol_ds)
    mask_sol_ds.reset_index(inplace=True)

    graph_nsolicitudes = go.Figure(data=[
        go.Bar(name='Data Analysis', x=mask_sol_da['Nº Solicitudes'],
               y=mask_sol_da['Nombre empresa'], orientation='h'),
        go.Bar(name='Data Scientist', x=mask_sol_ds['Nº Solicitudes'],
               y=mask_sol_ds['Nombre empresa'], orientation='h')
    ])

    graph_nsolicitudes.update_layout(barmode='group', xaxis_tickangle=-45,
                                     template="plotly_white"
                                     )

    return graph_nsolicitudes


def graph_nexp(df):
    nexp_da = df[df['Tipo puesto'] == 'Data Analyst']
    nexp_da = nexp_da['Nivel experiencia'].value_counts()
    nexp_da = pd.DataFrame(nexp_da)
    nexp_da.drop('no_data', inplace=True)

    nexp_ds = df[df['Tipo puesto'] == 'Data Analyst']
    nexp_ds = nexp_ds['Nivel experiencia'].value_counts()
    nexp_ds = pd.DataFrame(nexp_ds)

    labels1 = list(nexp_da.index)
    labels2 = list(nexp_ds.index)

    graph_nexp = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])

    graph_nexp.add_trace(go.Pie(labels=labels1, values=nexp_da['Nivel experiencia']),
                  1, 1)

    graph_nexp.add_trace(go.Pie(labels=labels2, values=nexp_ds['Nivel experiencia']),
                  1, 2)

    graph_nexp.update_traces(hole=.4, hoverinfo="label+percent+name")

    graph_nexp.update_layout(
        annotations=[dict(text='DA', x=0.18, y=0.5, font_size=20, showarrow=False),
                     dict(text='DS', x=0.82, y=0.5, font_size=20, showarrow=False)])
    graph_nexp['layout']['yaxis']['autorange'] = "reversed"

    return graph_nexp


def graph_jornada(df):
    jornada_da = df[df['Tipo puesto'] == 'Data Analyst']
    jornada_da = jornada_da['Tipo jornada'].value_counts()
    jornada_da = pd.DataFrame(jornada_da)

    jornada_ds = df[df['Tipo puesto'] == 'Data Scientist']
    jornada_ds = jornada_ds['Tipo jornada'].value_counts()
    jornada_ds = pd.DataFrame(jornada_ds)
    jornada_ds.drop('no_data', inplace=True)

    labels1 = list(jornada_da.index)
    labels2 = list(jornada_ds.index)

    graph_jornada = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])

    graph_jornada.add_trace(go.Pie(labels=labels1, values=jornada_da['Tipo jornada']),
                            1, 1)

    graph_jornada.add_trace(go.Pie(labels=labels2, values=jornada_ds['Tipo jornada']),
                            1, 2)

    graph_jornada.update_traces(hole=.4, hoverinfo="label+percent+name")

    graph_jornada.update_layout(
        title_text="Tipo jornada por puesto",

        annotations=[dict(text='DA', x=0.18, y=0.5, font_size=20, showarrow=False),
                     dict(text='DS', x=0.82, y=0.5, font_size=20, showarrow=False)])
    return graph_jornada
