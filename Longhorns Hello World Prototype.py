# Hello world prototype for the second semester of the Software Engineering course.
# Longhorns
# Spring 2022

from requests import request
import json
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

# Get the data from the API
r = request(url = 'http://augur.chaoss.io/api/unstable/repos/25205/closed-issues-count', method = 'get')
e = r.json()
df = pd.DataFrame(e)

# Create the graph
reponame = df['repo_name'][0]
df['date'] = pd.to_datetime(df.date, format='%Y-%m-%d %H:%M:%S')

fig = go.Figure([go.Histogram(x=df['date'], y=df['closed_count'])])
fig.update_layout(title_text="Issues Closed <br>Count of how many issues closed for repo \"" + reponame + "\"")
fig.update_xaxes(title_text="Date")
fig.update_yaxes(title_text="Closed Issues Count")
fig.show()