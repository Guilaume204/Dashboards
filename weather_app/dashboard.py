import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State


from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)

def create_plots():
	df = pd.read_csv('../data/weather_15_days.csv', skiprows=11, sep=';')

	df['startime'] = df.Year.astype(str) + \
	'-' +df.Month.astype(str) + \
	'-' +df.Day.astype(str) + \
	' ' +df.Hour.astype(str)+ \
	':' +df.Minute.astype(str)

	df.startime = df.startime.astype('datetime64[ns]')

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
	return plots




app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Cape Town weather'),
    html.Div(children='', id='discription'),
    dcc.Graph(id='Graph1',figure={'data': create_plots()}),

    dcc.Input(
    placeholder='Enter a value...',
    type='text',
    id='textbox',
    value=''),

    dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}],
    values=['MTL', 'SF'],
    id='checklist'), 
 
    html.Button('Submit', id='btnSubmit'),])

@app.callback(
    Output('discription', 'children'),
    [Input('btnSubmit', 'n_clicks')],
     [State('checklist', 'values'),State('textbox', 'value')])
def update_output(n_clicks, values, value):
	if n_clicks != None:
		return('hallo '+str(n_clicks) + ' '+','.join(values) + ' '+value)
	else:
		return('Dash: A web application framework for Python.')




if __name__ == '__main__':
     app.run_server(port=9984, host='127.0.0.1')

