# myapp.py

from random import random

from bokeh.layouts import column
from bokeh.models import Button, CustomJS, Select, Slider

from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc
import numpy as np
from modules import create_data



# create a plot and style its properties
p = figure(x_range=(0, 10), y_range=(0, 100), toolbar_location=None)
p.outline_line_color = None
p.grid.grid_line_color = None

x = np.arange(10)+1


def callback():
    y = create_data.power_func(x, select.value)
    p.line(x,y)


def callback_funk(attr, old, new):
    y = create_data.power_func(x, slider.value)
    p.line(x,y)
    
# add a button widget and configure with the call back
button = Button(label="Plot data")
button.on_click(callback)


select = Select(title="Option:", value="1", options=["1", "2", "3"])
select.js_on_change("value", CustomJS(code="""
    console.log('select: value=' + this.value, this.toString())
"""))

slider = Slider(start=0, end=10, value=1, step=.1, title="Stuff")
#slider.js_on_change("value", CustomJS(code="""
#    console.log('slider: value=' + this.value, this.toString())
#"""))
slider.on_change("value", callback_funk)

# put the button and plot in a layout and add to the document
curdoc().add_root(column(button, select, slider, p))





