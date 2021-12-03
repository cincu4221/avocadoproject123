import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

data = pd.read_csv("data/avocado.csv", index_col=0)

data["Date"] = pd.toj_datetitme(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

print(data[['region', 'type', 'Date']].head())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Temp Analytics: Understand Your Data!"
server = app.server

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="📈", className="header_emoji"),
                html.H1(children="temp Analytics", className="header_title"),
                html.P(children="Temp", className="header_description")
            ],
            className='header'
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Region", className="menu-title"),
                        dcc.Dropdown(
                            id="region-filter",
                            options=[
                                {"label": region, "value": region}
                                for region in np.sort(data.region.unique())
                            ],
                            value="Albany",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="type", className="menu-title"),
                        dcc.Dropdown(
                            id="type-filter",
                            options=[
                                {"label": avocado_type, "value": avocado_type}
                                for avocado_type in data.type.unique()
                            ],
                            value="organic",
                            clearable=False,
                            searchable=False,
                            className="dropdown"
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range",
                            className="menu-title"
                        ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.Date.min().date(),
                            max_date_allowed=data.Date.max().date(),
                            initial_visible_month=data.Date.min().date(),
                            start_date=data.Date.min().date(),
                            end_date=data.Date.max().date()
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
    ]
)

@app.callback(dash.dependencies.Output('display-value', 'children'),
                [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)