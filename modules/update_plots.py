from bokeh.transform import dodge
from bokeh.models import ColumnDataSource
from bokeh.models import Range1d, LegendItem, Legend
from bokeh.models.ranges import DataRange1d
import numpy as np
from bokeh.models.tools import HoverTool
from bokeh.plotting import figure   
import math
from bokeh.models.callbacks import CustomJS
from bokeh.models.annotations import Title


def bar_plot_teams2(team_list, teams, runde, parameter):
    p2 = figure(x_range=(1,runde), y_range=(0,runde*3))
    data1 = {'round':teams[team_list[0]]['df']['Round'],
             'x':teams[team_list[0]]['df']['Round'], 
             'y':teams[team_list[0]]['df']['Round']}
    
    for team in teams:
        data1[team] = teams[team]['df']['Total Points']
    sourceline = ColumnDataSource(data1)
    
    
    line1 = p2.line(x='x', y='y', source=sourceline, color="#c9d9d3", line_width=4)
    line2 = p2.line(x='x', y='y', source=sourceline, color="#718dbf", line_width=4)
    line3 = p2.line(x='x', y='y', source=sourceline, color="#e84d60", line_width=4)
    
    legend = Legend(items=[('', [line1]),
                           ('', [line2]),
                           ('', [line3]),
                           ], location="top_left")
    
    p2.add_layout(legend)
    
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
    
    
 
    
    p = figure(x_range=[], title=f'{parameter}', y_range=(0,max(3,y_max)))
    
    
    p.x_range.factors = team_list

    bar1 = p.vbar(x=dodge('teams', -0.30, range=p.x_range), top='runde1', width=0.15, source=source,
       color="#c9d9d3", legend_label=f"{parameter} in round {runde+1}")
    
    bar2 =  p.vbar(x=dodge('teams', -0.1, range=p.x_range), top='runde2', width=0.15, source=source,
       color="#718dbf", legend_label=f"{parameter} in round {runde+2}")
    
    bar3 = p.vbar(x=dodge('teams', +0.1, range=p.x_range), top='runde3', width=0.15, source=source,
       color="#e84d60", legend_label=f"{parameter} in round {runde+3}")
    
    bar4 = p.vbar(x=dodge('teams', +0.3, range=p.x_range), top='middel', width=0.15, source=source,
       color="black", legend_label=f"Mean of {parameter} in round {runde+1}, {runde+2} and {runde+3}")
    
    
    callback = CustomJS(args=dict(title=p2.title, data=source, dataline=sourceline, plotline1=line1, 
                                  plotline2=line2, plotline3=line3, legend=legend), code="""
        var a = cb_data.index.indices;
        var a2 = cb_data;
        console.log(a2)
        if (a.length > 0) {
                var b = a[0];
                var team = data.attributes.data.teams[b];
                var point = data.attributes.data.runde1[b]
                console.log(point);
                title.text = team;
                
                
                var modstander1 = data.attributes.data.modstander1[b];
                var modstander2 = data.attributes.data.modstander2[b];
                var modstander3 = data.attributes.data.modstander3[b];
                
                console.log(legend.items[0].label.value);
                plotline1.attributes.glyph.y.field = modstander1
                plotline2.attributes.glyph.y.field = modstander2
                plotline3.attributes.glyph.y.field = modstander3
                plotline3.attributes.glyph.legend_label = "hov"
                plotline1.change.emit();
                plotline2.change.emit();
                plotline3.change.emit();
                dataline.change.emit();
                legend.items[0].label.value = modstander1
                legend.items[1].label.value = modstander2
                legend.items[2].label.value = modstander3
        }
    """)
    
    
    p.add_tools(HoverTool(tooltips=[("Team", "@teams"), ("Modstander 1", "@modstander1 @runde1"),
                                    ("Modstander 2", "@modstander2 @runde2"),
                                    ("Modstander 3", "@modstander3 @runde3")], callback=callback, 
                          renderers=[bar1, bar2, bar3, bar4]))
    
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 0.5
    p.xgrid.grid_line_color = None
    
    p.legend.location = "top_left"
    
    return p, p2