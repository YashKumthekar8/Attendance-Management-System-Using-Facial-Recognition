import folium
from chart_studio import plotly
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
#Line Graph
def  LineGraph(datax,datay,name,color,title):
    totalcases = go.Figure()
    totalcases.add_trace(go.Scatter(x=datax, y=datay, mode='lines',
            name=name,connectgaps=True,line_color=color,fill='tozeroy'))

    totalcases.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='black',
            linewidth=3,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=True,
            showline=True,
            showticklabels=True,
        ),
        
        autosize=False,
        showlegend=False,
        plot_bgcolor='white',
        
        title=title,
        title_x=0.5,
        title_font_size=23
    )
     
    return totalcases.to_html()


#function for plotting the bar graph