# Imports from 3rd party libraries
import dash
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import seaborn as sns

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Movies - getting a bang for your buck
            Movie_monies provides potential revenue of bigger budget films, estimate the effects of any particular 
            
            feature on revenues. Adjust some features of an upcoming film production to see potential impacts on revenue.      
          
           

            """
        ),
        dcc.Link(dbc.Button('Make a Prediction Now!', color='primary'), href='/predictions')
    ],
    md=4,
)

df = pd.read_csv('https://raw.githubusercontent.com/peterger8y/Movie_money/main/df_x')
fig = px.scatter_matrix(df, dimensions=['duration', 'revenue', 'vote_count', 'year'])

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
