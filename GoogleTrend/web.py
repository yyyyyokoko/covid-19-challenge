import pandas as pd
import os
import plotly.graph_objs as go
import plotly.express as px
from copy import deepcopy
from plotly.subplots import make_subplots
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Step 1. Launch the application
app = dash.Dash()


app.layout = html.Div([
    html.Iframe(src = "https://public.flourish.studio/visualisation/2211837/", width="100%", height = "800" )
])


if __name__ == "__main__":
    app.run_server(debug=True, port=3004)

