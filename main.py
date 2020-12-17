

from bokeh.layouts import column, row
from bokeh.models import Button, CustomJS, Select, Slider, FactorRange
from bokeh.plotting import figure, curdoc
import numpy as np
from modules import update_plots, get_files, combine_data, read_thesportsdb
from bokeh.models.tools import HoverTool
from bokeh.layouts import layout

p = figure()


def callback_barplot():
    p = figure(x_range=[], tools="hover", y_range=(0,3))
    league = read_thesportsdb.leagues[select.value]
    df = read_thesportsdb.read_from_thesportsdb(league)
    teams, round_nr = combine_data.combine_all(df)
    team_list = list(teams.keys())
    if select2.value == 'Opponent Points':
        update_plots.bar_plot_teams2(p, team_list, teams, runde=round_nr)
    elif select2.value == 'Opponent Shape':
        update_plots.bar_plot_teams_shape(p, team_list, teams, runde=round_nr)
    layout.children[0].children[2] = p


button3 = Button(label="See coming matches")
button3.on_click(callback_barplot)


leagues = list(read_thesportsdb.leagues)
select = Select(title="Vælg Liga", value=leagues[0], options=leagues)
select.js_on_change("value", CustomJS(code="""
    console.log('select: value=' + this.value, this.toString())
"""))


headers = ['Opponent Points', 'Opponent Shape']
select2 = Select(title="Data", value=headers[0], options=headers)
select2.js_on_change("value", CustomJS(code="""
    console.log('select: value=' + this.value, this.toString())
"""))



# put the button and plot in a layout and add to the document
layout = layout(column(row(button3), row(select, select2), row(p)))
curdoc().add_root(layout)