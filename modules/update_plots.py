from bokeh.transform import dodge
from bokeh.models import ColumnDataSource
from bokeh.models import Range1d
from bokeh.models.ranges import DataRange1d
import numpy as np
from bokeh.models.tools import HoverTool
from bokeh.plotting import figure   
import math


def bar_plot_teams(team_list, teams, runde, parameter):
    points1 = np.zeros(len(team_list))
    points2 = np.zeros(len(team_list))
    points3 = np.zeros(len(team_list))
    
    modstander1 = []
    modstander2 = []
    modstander3 = []
    
    for i, team in enumerate(teams):
        points1[i] = teams[team]['df'][parameter][runde+0]
        points2[i] = teams[team]['df'][parameter][runde+1]
        points3[i] = teams[team]['df'][parameter][runde+2]
        modstander1.append(teams[team]['df']['Opponent'][runde+0])
        modstander2.append(teams[team]['df']['Opponent'][runde+1])
        modstander3.append(teams[team]['df']['Opponent'][runde+2])
    
    points_mean = (points1 + points2 + points3)/3
    
    out_arr = np.argsort(points1)
    out_arr = np.argsort(points_mean)
    
    points1 = points1[out_arr]
    points2 = points2[out_arr]
    points3 = points3[out_arr]
    points_mean = points_mean[out_arr]
    
    team_list = list(np.array(team_list)[out_arr])
    modstander1 = list(np.array(modstander1)[out_arr])
    modstander2 = list(np.array(modstander2)[out_arr])
    modstander3 = list(np.array(modstander3)[out_arr])
    
    
    data = {'teams' : team_list,
            'runde1' : points1,
            'runde2' : points2,
            'runde3' : points3,
            'middel' : points_mean,
            'modstander1' : modstander1,
            'modstander2' : modstander2,
            'modstander3' : modstander3}
    
    source = ColumnDataSource(data=data)
    y_max = math.ceil(max(max(points1), max(points2), max(points3)))
    print(y_max)
    p = figure(x_range=[], tools="hover", y_range=(0,max(3,y_max)))
    p.x_range.factors = team_list

    p.vbar(x=dodge('teams', -0.30, range=p.x_range), top='runde1', width=0.15, source=source,
       color="#c9d9d3", legend_label=f"Pointgennemsnit for modstander i runde {runde+1}")
    
    p.vbar(x=dodge('teams', -0.1, range=p.x_range), top='runde2', width=0.15, source=source,
       color="#718dbf", legend_label=f"Pointgennemsnit for modstander i runde {runde+2}")
    
    p.vbar(x=dodge('teams', +0.1, range=p.x_range), top='runde3', width=0.15, source=source,
       color="#e84d60", legend_label=f"Pointgennemsnit for modstander i runde {runde+3}")
    
    p.vbar(x=dodge('teams', +0.3, range=p.x_range), top='middel', width=0.15, source=source,
       color="black", legend_label="Mean")
    
    p.add_tools(HoverTool(tooltips=[("Team", "@teams"), ("Modstander 1", "@modstander1"),("Modstander 2", "@modstander2"),("Modstander 3", "@modstander3")]))
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 0.5
    p.xgrid.grid_line_color = None
    
    p.legend.location = "top_left"
    return p