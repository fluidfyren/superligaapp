

from bokeh.layouts import column, row
from bokeh.models import Button, CustomJS, Select, Slider
from bokeh.plotting import figure, curdoc
import numpy as np
from modules import update_plots, get_files
from bokeh.models.tools import HoverTool


# create a plot and style its properties
p = figure(x_range=(0, 22), y_range=(0, 10), toolbar_location=None, sizing_mode="scale_width")
p.outline_line_color = None
p.grid.grid_line_color = None

p2 = figure(x_range=(0, 22), y_range=(0, 10), toolbar_location=None, sizing_mode="scale_width")

lines_p = []
max_value_p = []

lines_p2 = []
max_value_p2 = []

def callback():
    df = get_files.read_file(f'data/teams/{select.value}.pkl')
    l = p.line(df['df']['Runde'],df['df'][select2.value], 
        legend_label=f'{select.value} - {select2.value}', 
        line_color=df['color'], line_width=5)
    lines_p.append(l)
    max_value_p.append(max(df['df'][select2.value]))
    p.y_range.end = max(max_value_p)

    

def callback2():
    df = get_files.read_file(f'data/teams/{select.value}.pkl')
    p.line(df['df']['Runde'],df['df']['Cum Points'])
    p.y_range.end = max(df['df']['Cum Points'])
    

def callback_all():
    for team in teams:
        df = get_files.read_file(f'my_app/data/teams/{team}.pkl')
        l = p2.line(df['df']['Runde'],df['df'][select2.value], 
            legend_label=f'{team}', 
            line_color=df['color'], line_width=5)
        lines_p2.append(l)
        max_value_p2.append(max(df['df'][select2.value]))
        p2.y_range.end = max(max_value_p2)


def callback_all2():
    runde = 10
    for team in teams:
        df = get_files.read_file(f'data/teams/{team}.pkl')
        l = p2.line(df['df']['Runde'][runde:],df['df']['Modstander Point'][runde:].expanding().mean(), 
            legend_label=f'{team}', 
            line_color=df['color'], line_width=5, name=team)
        lines_p2.append(l)
        max_value_p2.append(max(df['df']['Modstander Point'].expanding().mean()))
        
        hover1 = HoverTool(names=[team])
        hover1.tooltips = [(f'Hold', f'{team}')]


        p2.add_tools(hover1)
        
    p2.y_range.end = max(max_value_p2)
    p2.x_range.start = runde+1
        
        
        
# add a button widget and configure with the call back
button = Button(label="Plot data")
button.on_click(callback)


button2 = Button(label="Plot points")
button2.on_click(callback2)

button3 = Button(label="Plot All Teams")
button3.on_click(callback_all2)

teams = get_files.get_file_list('data/teams')
select = Select(title="Hold:", value=teams[0], options=teams)
select.js_on_change("value", CustomJS(code="""
    console.log('select: value=' + this.value, this.toString())
"""))


headers = ['Points', 'Cum Points', 'Mean Points', 'Running Mean Points', 
           'Modstander Point', 'Modstander Form']
select2 = Select(title="Data:", value='Points', options=headers)
select2.js_on_change("value", CustomJS(code="""
    console.log('select: value=' + this.value, this.toString())
"""))



# put the button and plot in a layout and add to the document
curdoc().add_root(column(row(button, button2, button3), row(select, select2), row(p, p2)))