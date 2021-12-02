import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv("data/avocado.csv", index_col=0)
data = data.query("type == 'conventional' and region == 'albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Temp Analytics"),
        html.P(
            children="Temp"
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines"
                    }
                ],
                "layout": {"title": "Title_1"}
            }
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines"
                    }
                ],
                "layout": {"title": "Title_2"}
            }
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)