from bokeh.transform import dodge
from bokeh.models import ColumnDataSource
from bokeh.models import Range1d
from bokeh.models.ranges import DataRange1d
import numpy as np
from bokeh.models.tools import HoverTool

    
    
def bar_plot_teams(p, teams, dataframes, figures, runde):
    points1 = np.zeros(len(teams))
    points2 = np.zeros(len(teams))
    points3 = np.zeros(len(teams))
    
    modstander1 = []
    modstander2 = []
    modstander3 = []
    
    for i, team in enumerate(dataframes):
        points1[i] = team['df']['Modstander Point'][runde+0]
        points2[i] = team['df']['Modstander Point'][runde+1]
        points3[i] = team['df']['Modstander Point'][runde+2]
        modstander1.append(team['df']['Modstander'][runde+0])
        modstander2.append(team['df']['Modstander'][runde+1])
        modstander3.append(team['df']['Modstander'][runde+2])
    
    points_mean = (points1 + points2 + points3)/3
    
    out_arr = np.argsort(points1)
    
    points1 = points1[out_arr]
    points2 = points2[out_arr]
    points3 = points3[out_arr]
    points_mean = points_mean[out_arr]
    
    teams = list(np.array(teams)[out_arr])
    modstander1 = list(np.array(modstander1)[out_arr])
    modstander2 = list(np.array(modstander2)[out_arr])
    modstander3 = list(np.array(modstander3)[out_arr])

    
    data = {'teams' : teams,
            'runde1' : points1,
            'runde2' : points2,
            'runde3' : points3,
            'middel' : points_mean,
            'modstander1' : modstander1,
            'modstander2' : modstander2,
            'modstander3' : modstander3}
    
    source = ColumnDataSource(data=data)

    
    p.x_range.factors = teams

    p.vbar(x=dodge('teams', -0.30, range=p.x_range), top='runde1', width=0.15, source=source,
       color="#c9d9d3", legend_label="Pointgennemsnit for modstander i næste runde")
    
    p.vbar(x=dodge('teams', -0.1, range=p.x_range), top='runde2', width=0.15, source=source,
       color="#718dbf", legend_label="Pointgennemsnit for modstander om to runder")
    
    p.vbar(x=dodge('teams', +0.1, range=p.x_range), top='runde3', width=0.15, source=source,
       color="#e84d60", legend_label="Pointgennemsnit for modstander om tre runder")
    
    p.vbar(x=dodge('teams', +0.3, range=p.x_range), top='middel', width=0.15, source=source,
       color="black", legend_label="Mean")
    
    p.add_tools(HoverTool(tooltips=[("Team", "@teams"), ("Modstander 1", "@modstander1"),("Modstander 2", "@modstander2"),("Modstander 3", "@modstander3")]))
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 0.5
    p.xgrid.grid_line_color = None
    
    
def bar_plot_teams2(p, teams, dataframes, figures, runde):
    points1 = np.zeros(len(teams))
    points2 = np.zeros(len(teams))
    points3 = np.zeros(len(teams))
    
    modstander1 = []
    modstander2 = []
    modstander3 = []
    
    for i, team in enumerate(dataframes):
        print(list(team['df']))
        points1[i] = team['df']['Opponent avg points'][runde+0]
        points2[i] = team['df']['Opponent avg points'][runde+1]
        points3[i] = team['df']['Opponent avg points'][runde+2]
        modstander1.append(team['df']['Opponent'][runde+0])
        modstander2.append(team['df']['Opponent'][runde+1])
        modstander3.append(team['df']['Opponent'][runde+2])
    
    points_mean = (points1 + points2 + points3)/3
    
    out_arr = np.argsort(points1)
    
    points1 = points1[out_arr]
    points2 = points2[out_arr]
    points3 = points3[out_arr]
    points_mean = points_mean[out_arr]
    
    teams = list(np.array(teams)[out_arr])
    modstander1 = list(np.array(modstander1)[out_arr])
    modstander2 = list(np.array(modstander2)[out_arr])
    modstander3 = list(np.array(modstander3)[out_arr])

    
    data = {'teams' : teams,
            'runde1' : points1,
            'runde2' : points2,
            'runde3' : points3,
            'middel' : points_mean,
            'modstander1' : modstander1,
            'modstander2' : modstander2,
            'modstander3' : modstander3}
    
    source = ColumnDataSource(data=data)

    
    p.x_range.factors = teams

    p.vbar(x=dodge('teams', -0.30, range=p.x_range), top='runde1', width=0.15, source=source,
       color="#c9d9d3", legend_label="Pointgennemsnit for modstander i næste runde")
    
    p.vbar(x=dodge('teams', -0.1, range=p.x_range), top='runde2', width=0.15, source=source,
       color="#718dbf", legend_label="Pointgennemsnit for modstander om to runder")
    
    p.vbar(x=dodge('teams', +0.1, range=p.x_range), top='runde3', width=0.15, source=source,
       color="#e84d60", legend_label="Pointgennemsnit for modstander om tre runder")
    
    p.vbar(x=dodge('teams', +0.3, range=p.x_range), top='middel', width=0.15, source=source,
       color="black", legend_label="Mean")
    
    p.add_tools(HoverTool(tooltips=[("Team", "@teams"), ("Modstander 1", "@modstander1"),("Modstander 2", "@modstander2"),("Modstander 3", "@modstander3")]))
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 0.5
    p.xgrid.grid_line_color = None
    
    
