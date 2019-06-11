import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html


from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)
df = pd.read_csv('../data/weather_15_days.csv', skiprows=11, sep=';')

df['startime'] = df.Year.astype(str) + \
'-' +df.Month.astype(str) + \
'-' +df.Day.astype(str) + \
' ' +df.Hour.astype(str)+ \
':' +df.Minute.astype(str)

df.startime = df.startime.astype('datetime64[ns]')
df.columnsdf.columns

plots = []
for measurement in ['Temperature  [2 m above gnd]', 'Relative Humidity  [2 m above gnd]',
       'Mean Sea Level Pressure  [MSL]',
       'Total Precipitation (high resolution)  [sfc]',
       'Total Cloud Cover  [sfc]', 'Sunshine Duration  [sfc]',
       'Shortwave Radiation  [sfc]', 'Wind Speed  [10 m above gnd]',
       'Wind Direction  [10 m above gnd]']:
    plots.append({'x':df.startime,
               'y':df[measurement],
               'name':measurement})



app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Cape Town weather'),
    html.Div(children='Dash: A web application framework for Python.'),
    dcc.Graph(id='Graph1',figure={'data': plots})
])

if __name__ == '__main__':
    app.run_server(port=9977, host='10.0.0.107')

