import pandas as pd
import plotly.graph_objs as go
import plotly.plotly as py
def linear_graph(link_to_file, title, filename, range_file):
    py.sign_in('federico123579', 'tmp58hnp2w')
    # Import data from csv
    df = pd.read_csv(link_to_file)
    data = []
    for count, val in enumerate(range_file):
        data.append(go.Scatter(
            x = df['Date'],
            y = df[val['name']],
            mode = 'lines+markers',
            name = val['name']
        ))
    layout = go.Layout(title=title)
    fig = go.Figure(data=data, layout=layout)

    # Plot data in the notebook
    py.plot(fig, filename=filename)
def polynomial_graph(link_to_file, title, filename, range_file):
    py.sign_in('federico123579', 'tmp58hnp2w')
    # Import data from csv
    df = pd.read_csv(link_to_file)
    data = []
    for count, val in enumerate(range_file):
        data.append(go.Scatter(
            x = df['Date'],
            y = df[val['name']],
            mode = 'lines+markers',
            name = val['name']
        ))
    layout = go.Layout(title=title)
    fig = go.Figure(data=data, layout=layout)

    # Plot data in the notebook
    py.plot(fig, filename=filename)
