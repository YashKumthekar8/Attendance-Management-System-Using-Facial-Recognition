import folium
from chart_studio import plotly
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


#Line Graph
def  LineGraph(datax,datay,name,color,title):
    totalcases = go.Figure()
    totalcases.add_trace(go.Scatter(x=datax, y=datay, mode='markers',marker_symbol="x",
            name=name,connectgaps=True,line_color=color,fill='tozeroy',
                marker=dict(
            color='purple',
            size=10,
            line=dict(
                color='MediumPurple',
                width=2
            )
        )))

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
            showgrid=True,
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
    totalcases.show() 
    return totalcases.to_html()


#function for plotting the bar graph
def BarGraph(data,label,color):
    fig = go.Figure(go.Bar(
                y=data,
                x=label,
                orientation='v',
        marker=dict(
        color=color,
        line=dict(color=color, width=3)
    )))
    
    return fig.to_html()

'''
Example of calling function BarGraph([1,2,3,100,-1],["A","B","C","D","E"],"violet")    
'''
def SeparateXY(df):
    x=[]
    y=[]
    for ind in df.index:
      for name in df.columns:
          if df[name][ind]==1:
              x.append(df["date"][ind])
              y.append(name)
    return x,y



#Function for plotting the scatter plot
def ScatterPlot(df):
    x_axis,y_axis=SeparateXY(df)
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=x_axis,y=y_axis,mode="markers",marker_symbol="x"))
    fig.update_xaxes(type='category')
    fig.update_yaxes(type='category')    
    fig.update_traces(marker_size=15)

    fig.show()
    return fig.to_html()

data=[['27-03',1,0,0,1],['28-03',1,0,1,1],['29-03',1,1,1,1],['30-03',0,0,1,1]]
df=pd.DataFrame(data,columns=["date","8-9","9-10","10-11","11-12"])

ScatterPlot(df)
