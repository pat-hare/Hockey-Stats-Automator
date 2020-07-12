import json
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from metrics_calc import basic_metrics_calc, pp_metrics_calc, calcMetrics
from chart_creator import createBasicChart, createTimeSeriesChart, createPossessionTimeScoreChart

_home_rows_fg = []
_home_rows_q1 = []
_home_rows_q2 = []
_home_rows_q3 = []
_home_rows_q4 = []

_away_rows_fg = []
_away_rows_q1 = []
_away_rows_q2 = []
_away_rows_q3 = []
_away_rows_q4 = []

_home_pprows_fg = []
_home_pprows_q1 = []
_home_pprows_q2 = []
_home_pprows_q3 = []
_home_pprows_q4 = []

_away_pprows_fg = []
_away_pprows_q1 = []
_away_pprows_q2 = []
_away_pprows_q3 = []
_away_pprows_q4 = []

home_goals = 0
away_goals = 0


with open('WIM v OGHC.json') as json_file:
    data = json.load(json_file)
    for r in data['rows']:
        if r['name'] == 'OGHC':
            _home_rows_fg = r['highlights']
        elif r['name'] == 'OGHC Goal':
            home_goals = len(r['highlights'])
        elif r['name'] == 'OGHC PP':
            _home_pprows = r['highlights']
        elif r['name'] == 'WIM':
            _away_rows_fg = r['highlights']
        elif r['name'] == 'WIM Goal':
            away_goals = len(r['highlights'])
        elif r['name'] == 'WIM PP':
            _away_pprows = r['highlights']

for row in _home_rows_fg:
    if row['end'] < 1114:
        _home_rows_q1.append(row)
    elif row['end'] < 2264 and row['end'] >= 1114:
        _home_rows_q2.append(row)
    elif row['end'] < 3430 and row['end'] >= 2264:
        _home_rows_q3.append(row)
    elif row['end'] >= 3430:
        _home_rows_q4.append(row)

for row in _away_rows_fg:
    if row['end'] < 1114:
        _away_rows_q1.append(row)
    elif row['end'] < 2264 and row['end'] >= 1114:
        _away_rows_q2.append(row)
    elif row['end'] < 3430 and row['end'] >= 2264:
        _away_rows_q3.append(row)
    elif row['end'] >= 3430:
        _away_rows_q4.append(row)

for row in _home_pprows_fg:
    if row['end'] < 1114:
        _home_pprows_q1.append(row)
    elif row['end'] < 2264 and row['end'] >= 1114:
        _home_pprows_q2.append(row)
    elif row['end'] < 3430 and row['end'] >= 2264:
        _home_pprows_q3.append(row)
    elif row['end'] >= 3430:
        _home_pprows_q4.append(row)

for row in _away_pprows_fg:
    if row['end'] < 1114:
        _away_pprows_q1.append(row)
    elif row['end'] < 2264 and row['end'] >= 1114:
        _away_pprows_q2.append(row)
    elif row['end'] < 3430 and row['end'] >= 2264:
        _away_pprows_q3.append(row)
    elif row['end'] >= 3430:
        _away_pprows_q4.append(row)

# create full game metrics
home_basic_metrics = basic_metrics_calc(_home_rows_fg, home_goals)
away_basic_metrics = basic_metrics_calc(_away_rows_fg, away_goals)
home_pp_metrics = pp_metrics_calc(_home_pprows_fg)
away_pp_metrics = pp_metrics_calc(_away_pprows_fg)
home_basic_metrics, away_basic_metrics, home_pp_metrics, away_pp_metrics = calcMetrics(home_basic_metrics, away_basic_metrics, home_pp_metrics, away_pp_metrics)

# create quarter metrics
# Q1
home_basic_metrics_q1 = basic_metrics_calc(_home_rows_q1, 0)
away_basic_metrics_q1 = basic_metrics_calc(_away_rows_q1, 0)
home_pp_metrics_q1 = pp_metrics_calc(_home_pprows_q1)
away_pp_metrics_q1 = pp_metrics_calc(_away_pprows_q1)
home_basic_metrics_q1, away_basic_metrics_q1, home_pp_metrics_q1, away_pp_metrics_q1 = calcMetrics(home_basic_metrics_q1, away_basic_metrics_q1, home_pp_metrics_q1, away_pp_metrics_q1)

# Q2
home_basic_metrics_q2 = basic_metrics_calc(_home_rows_q2, 0)
away_basic_metrics_q2 = basic_metrics_calc(_away_rows_q2, 0)
home_pp_metrics_q2 = pp_metrics_calc(_home_pprows_q2)
away_pp_metrics_q2 = pp_metrics_calc(_away_pprows_q2)
home_basic_metrics_q2, away_basic_metrics_q2, home_pp_metrics_q2, away_pp_metrics_q2 = calcMetrics(home_basic_metrics_q2, away_basic_metrics_q2, home_pp_metrics_q2, away_pp_metrics_q2)

# Q3
home_basic_metrics_q3 = basic_metrics_calc(_home_rows_q3, 0)
away_basic_metrics_q3 = basic_metrics_calc(_away_rows_q3, 0)
home_pp_metrics_q3 = pp_metrics_calc(_home_pprows_q3)
away_pp_metrics_q3 = pp_metrics_calc(_away_pprows_q3)
home_basic_metrics_q3, away_basic_metrics_q3, home_pp_metrics_q3, away_pp_metrics_q3 = calcMetrics(home_basic_metrics_q3, away_basic_metrics_q3, home_pp_metrics_q3, away_pp_metrics_q3)

# Q4
home_basic_metrics_q4 = basic_metrics_calc(_home_rows_q4, 0)
away_basic_metrics_q4 = basic_metrics_calc(_away_rows_q4, 0)
home_pp_metrics_q4 = pp_metrics_calc(_home_pprows_q4)
away_pp_metrics_q4 = pp_metrics_calc(_away_pprows_q4)
home_basic_metrics_q4, away_basic_metrics_q4, home_pp_metrics_q4, away_pp_metrics_q4 = calcMetrics(home_basic_metrics_q4, away_basic_metrics_q4, home_pp_metrics_q4, away_pp_metrics_q4)


# create full game charts
basic_chart_fg = createBasicChart(home_basic_metrics, away_basic_metrics, 'Full Game', 'fg-basic')
time_series_chart_fg = createTimeSeriesChart(_home_rows_fg, _away_rows_fg, 'Full Game Outlet Efficiency', 'fg-oeff')
home_possession_chart_fg = createPossessionTimeScoreChart(_home_rows_fg, 'Home Full Game Possession Outcomes', 'h-fg-pout')
away_possession_chart_fg = createPossessionTimeScoreChart(_away_rows_fg, 'Away Full Game Possession Outcomes', 'a-fg-pout')

basic_chart_q1 = createBasicChart(home_basic_metrics_q1, away_basic_metrics_q1, '1st Quarter', 'q1-basic')
time_series_chart_q1 = createTimeSeriesChart(_home_rows_q1, _away_rows_q1, '1st Quarter Outlet Efficiency', 'q1-oeff')
home_possession_chart_q1 = createPossessionTimeScoreChart(_home_rows_q1, 'Home 1st Quarter Possession Outcomes', 'h-q1-pout')
away_possession_chart_q1 = createPossessionTimeScoreChart(_away_rows_q1, 'Away 1st Quarter Possession Outcomes', 'a-q1-pout')

basic_chart_q2 = createBasicChart(home_basic_metrics_q2, away_basic_metrics_q2, '2nd Quarter', 'q2-basic')
time_series_chart_q2 = createTimeSeriesChart(_home_rows_q2, _away_rows_q2, '2nd Quarter Outlet Efficiency', 'q2-oeff')
home_possession_chart_q2 = createPossessionTimeScoreChart(_home_rows_q2, 'Home 2nd Quarter Possession Outcomes', 'h-q2-pout')
away_possession_chart_q2 = createPossessionTimeScoreChart(_away_rows_q2, 'Away 2nd Quarter Possession Outcomes', 'a-q2-pout')

basic_chart_q3 = createBasicChart(home_basic_metrics_q3, away_basic_metrics_q3, '3rd Quarter', 'q3-basic')
time_series_chart_q3 = createTimeSeriesChart(_home_rows_q3, _away_rows_q3, '3rd Quarter Outlet Efficiency', 'q3-oeff')
home_possession_chart_q3 = createPossessionTimeScoreChart(_home_rows_q3, 'Home 3rd Quarter Possession Outcomes', 'h-q3-pout')
away_possession_chart_q3 = createPossessionTimeScoreChart(_away_rows_q3, 'Away 2rd Quarter Possession Outcomes', 'a-q3-pout')

basic_chart_q4 = createBasicChart(home_basic_metrics_q4, away_basic_metrics_q4, '4th Quarter', 'q4-basic')
time_series_chart_q4 = createTimeSeriesChart(_home_rows_q4, _away_rows_q4, '4th Quarter Outlet Efficiency', 'q4-oeff')
home_possession_chart_q4 = createPossessionTimeScoreChart(_home_rows_q4, 'Home 4th Quarter Possession Outcomes', 'h-q4-pout')
away_possession_chart_q4 = createPossessionTimeScoreChart(_away_rows_q4, 'Away 4th Quarter Possession Outcomes', 'a-q4-pout')

# plt.show()

img = Image.open("HockeyCircle.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("OpenSans-Semibold.ttf", 25)
# CE1
draw.text((418, 81),"1",(255,255,255),font=font)
draw.text((418, 122),"1",(255,255,255),font=font)
draw.text((418, 163),"1",(255,255,255),font=font)
draw.text((418, 204),"1",(255,255,255),font=font)
draw.text((418, 245),"1",(255,255,255),font=font)
draw.text((418, 286),"1",(255,255,255),font=font)

# CE2
draw.text((575, 461),"1",(255,255,255),font=font)
draw.text((575, 502),"1",(255,255,255),font=font)
draw.text((575, 543),"1",(255,255,255),font=font)
draw.text((575, 584),"1",(255,255,255),font=font)
draw.text((575, 625),"1",(255,255,255),font=font)
draw.text((575, 666),"1",(255,255,255),font=font)

# CE3
draw.text((875, 631),"1",(255,255,255),font=font)
draw.text((875, 672),"1",(255,255,255),font=font)
draw.text((875, 713),"1",(255,255,255),font=font)
draw.text((968, 631),"1",(255,255,255),font=font)
draw.text((968, 672),"1",(255,255,255),font=font)
draw.text((968, 713),"1",(255,255,255),font=font)

# CE4
draw.text((1292, 462),"1",(255,255,255),font=font)
draw.text((1292, 503),"1",(255,255,255),font=font)
draw.text((1292, 544),"1",(255,255,255),font=font)
draw.text((1292, 585),"1",(255,255,255),font=font)
draw.text((1292, 626),"1",(255,255,255),font=font)
draw.text((1292, 667),"1",(255,255,255),font=font)

# CE5
draw.text((1440, 81),"1",(255,255,255),font=font)
draw.text((1440, 122),"1",(255,255,255),font=font)
draw.text((1440, 164),"1",(255,255,255),font=font)
draw.text((1440, 205),"1",(255,255,255),font=font)
draw.text((1440, 246),"1",(255,255,255),font=font)
draw.text((1440, 287),"1",(255,255,255),font=font)

# arrows
font = ImageFont.truetype("OpenSans-Semibold.ttf", 35)
draw.text((488, 173),str(home_basic_metrics['ce']['1']),(0,0,0),font=font)
draw.text((628, 425),str(home_basic_metrics['ce']['2']),(0,0,0),font=font)
draw.text((902, 530),str(home_basic_metrics['ce']['3']),(0,0,0),font=font)
draw.text((1175, 430),str(home_basic_metrics['ce']['4']),(0,0,0),font=font)
draw.text((1320, 173),str(home_basic_metrics['ce']['5']),(0,0,0),font=font)

font = ImageFont.truetype("OpenSans-Semibold.ttf", 45)
draw.text((466, 800),str(home_basic_metrics['25e']['L']),(0,0,0),font=font)
draw.text((886, 800),str(home_basic_metrics['25e']['C']),(0,0,0),font=font)
draw.text((1308, 800),str(home_basic_metrics['25e']['R']),(0,0,0),font=font)

img.save('sample-out.png')

# print(home_basic_metrics)
# print(away_basic_metrics)