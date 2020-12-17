

from bokeh.layouts import column, row
from bokeh.models import Button, CustomJS, Select, Slider, FactorRange
from bokeh.plotting import figure, curdoc
import numpy as np
from modules import update_plots, get_files, combine_data, read_thesportsdb
from bokeh.models.tools import HoverTool


p = figure(x_range=[], tools="hover", y_range=(0,3))
figures = [p]


df = read_thesportsdb.read_from_thesportsdb()
teams, round_nr = combine_data.combine_all(df)
team_list = list(teams.keys())


def callback_barplot():
    #dataframes = []
    #for team in teams:
    #    dataframes.append(get_files.read_file(f'data/teams/{team}.pkl'))
    #for team in teams:
    #    print(list(teams[team]['df']))
    update_plots.bar_plot_teams2(p, team_list, teams, figures, runde=round_nr)



button3 = Button(label="Se kommende modstandere")
button3.on_click(callback_barplot)



select = Select(title="Hold: (kan pt ikke plottes)", value=team_list[0], options=team_list)
select.js_on_change("value", CustomJS(code="""
    console.log('select: value=' + this.value, this.toString())
"""))


headers = ['Points', 'Opponent Points']
select2 = Select(title="Data: (kan pt ikke plottes)", value='Points', options=headers)
select2.js_on_change("value", CustomJS(code="""
    console.log('select: value=' + this.value, this.toString())
"""))



# put the button and plot in a layout and add to the document
curdoc().add_root(column(row(button3), row(select, select2), row(p)))