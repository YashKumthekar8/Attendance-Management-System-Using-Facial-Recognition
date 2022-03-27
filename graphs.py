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

#Function for plotting the scatter plot
def ScatterPlot(dataFrame,xlabel,ylabel,type):
    fig = px.scatter(dataFrame, x=xlabel, y=ylabel, color=type, symbol=type)
    fig.show()
    return fig.to_html()



#calling the scatter plot function
# df = px.data.iris()
# ScatterPlot(df,"sepal_width","sepal_length","species")

''''
date       time t1 t2  t3   t4
  29          8-9  1  0    0    0
31         9-10  1 0    1    0 
'''


# time_slot=["8-9","9-10","10-11","11-12"]
# date=["29","31","1","2"]
# present_table=[]
# present_table.append([1,0,0,0])
# present_table.append([1,0,1,0])
# present_table.append([1,0,0,1])
# present_table.append([1,1,1,1])

# df=[]
LineGraph([1,2,3,4],[3,5,6,7],"tp","yellow","Example")