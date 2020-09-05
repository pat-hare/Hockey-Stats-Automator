import json
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from metrics_calc import basic_metrics_calc, pp_metrics_calc, calcMetrics
from chart_creator import createBasicChart, createTimeSeriesChart, createPossessionTimeScoreChart
from sqlconnector import addRowToMetrics
from image_creator import createCircleEntryImage, createSeasonTurnoverImage

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

inputFilename = input('Filename: ')
home = input('home: ')
away = input('away: ')

EoQ1 = int(input('end of Q1: '))
EoQ2 = int(input('end of Q2: '))
EoQ3 = int(input('end of Q3: '))

with open(inputFilename) as json_file:
    data = json.load(json_file)
    for r in data['rows']:
        if r['name'] == home:
            _home_rows_fg = r['highlights']
        elif r['name'] == home + ' Goal':
            home_goals = len(r['highlights'])
        elif r['name'] == home + ' PP':
            _home_pprows = r['highlights']
        elif r['name'] == away:
            _away_rows_fg = r['highlights']
        elif r['name'] == away + ' Goal':
            away_goals = len(r['highlights'])
        elif r['name'] == away + ' PP':
            _away_pprows = r['highlights']

for row in _home_rows_fg:
    if row['end'] < EoQ1:
        _home_rows_q1.append(row)
    elif row['end'] < EoQ2 and row['end'] >= EoQ1:
        _home_rows_q2.append(row)
    elif row['end'] < EoQ3 and row['end'] >= EoQ2:
        _home_rows_q3.append(row)
    elif row['end'] >= EoQ3:
        _home_rows_q4.append(row)

for row in _away_rows_fg:
    if row['end'] < EoQ1:
        _away_rows_q1.append(row)
    elif row['end'] < EoQ2 and row['end'] >= EoQ1:
        _away_rows_q2.append(row)
    elif row['end'] < EoQ3 and row['end'] >= EoQ2:
        _away_rows_q3.append(row)
    elif row['end'] >= EoQ3:
        _away_rows_q4.append(row)

for row in _home_pprows_fg:
    if row['end'] < EoQ1:
        _home_pprows_q1.append(row)
    elif row['end'] < EoQ2 and row['end'] >= EoQ1:
        _home_pprows_q2.append(row)
    elif row['end'] < EoQ3 and row['end'] >= EoQ2:
        _home_pprows_q3.append(row)
    elif row['end'] >= EoQ3:
        _home_pprows_q4.append(row)

for row in _away_pprows_fg:
    if row['end'] < EoQ1:
        _away_pprows_q1.append(row)
    elif row['end'] < EoQ2 and row['end'] >= EoQ1:
        _away_pprows_q2.append(row)
    elif row['end'] < EoQ3 and row['end'] >= EoQ2:
        _away_pprows_q3.append(row)
    elif row['end'] >= EoQ3:
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

# add metrics to database
addRowToMetrics(home, home, away, home_basic_metrics, home_basic_metrics_q1, home_basic_metrics_q2,home_basic_metrics_q3, home_basic_metrics_q4)

addRowToMetrics(away, home, away, away_basic_metrics, away_basic_metrics_q1, away_basic_metrics_q2,away_basic_metrics_q3, away_basic_metrics_q4)

# create full game charts
basic_chart_fg = createBasicChart(home, away, home_basic_metrics, away_basic_metrics, 'Full Game', 'fg-basic')
time_series_chart_fg = createTimeSeriesChart(home, away, _home_rows_fg, _away_rows_fg, 'Full Game Outlet Efficiency', 'fg-oeff')
powerplay_chart_fg = createTimeSeriesChart(home, away, _home_pprows_fg, _away_pprows_fg, 'Full Game PowerPlay Efficiency', 'fg-ppeff')
# home_possession_chart_fg = createPossessionTimeScoreChart(home, _home_rows_fg, home + ' Full Game Possession Outcomes', 'h-fg-pout')
# away_possession_chart_fg = createPossessionTimeScoreChart(away, _away_rows_fg, away + ' Full Game Possession Outcomes', 'a-fg-pout')

# create quarter charts
basic_chart_q1 = createBasicChart(home, away, home_basic_metrics_q1, away_basic_metrics_q1, '1st Quarter', 'q1-basic')
time_series_chart_q1 = createTimeSeriesChart(home, away, _home_rows_q1, _away_rows_q1, '1st Quarter Outlet Efficiency', 'q1-oeff')
# home_possession_chart_q1 = createPossessionTimeScoreChart(home, _home_rows_q1, home + ' 1st Quarter Possession Outcomes', 'h-q1-pout')
# away_possession_chart_q1 = createPossessionTimeScoreChart(away, _away_rows_q1, away + ' 1st Quarter Possession Outcomes', 'a-q1-pout')

basic_chart_q2 = createBasicChart(home, away, home_basic_metrics_q2, away_basic_metrics_q2, '2nd Quarter', 'q2-basic')
time_series_chart_q2 = createTimeSeriesChart(home, away, _home_rows_q2, _away_rows_q2, '2nd Quarter Outlet Efficiency', 'q2-oeff')
# home_possession_chart_q2 = createPossessionTimeScoreChart(home, _home_rows_q2, home + ' 2nd Quarter Possession Outcomes', 'h-q2-pout')
# away_possession_chart_q2 = createPossessionTimeScoreChart(away, _away_rows_q2, away + ' 2nd Quarter Possession Outcomes', 'a-q2-pout')

basic_chart_q3 = createBasicChart(home, away, home_basic_metrics_q3, away_basic_metrics_q3, '3rd Quarter', 'q3-basic')
time_series_chart_q3 = createTimeSeriesChart(home, away, _home_rows_q3, _away_rows_q3, '3rd Quarter Outlet Efficiency', 'q3-oeff')
# home_possession_chart_q3 = createPossessionTimeScoreChart(home, _home_rows_q3, home + ' 3rd Quarter Possession Outcomes', 'h-q3-pout')
# away_possession_chart_q3 = createPossessionTimeScoreChart(away, _away_rows_q3, away + ' 3rd Quarter Possession Outcomes', 'a-q3-pout')

basic_chart_q4 = createBasicChart(home, away, home_basic_metrics_q4, away_basic_metrics_q4, '4th Quarter', 'q4-basic')
time_series_chart_q4 = createTimeSeriesChart(home, away, _home_rows_q4, _away_rows_q4, '4th Quarter Outlet Efficiency', 'q4-oeff')
# home_possession_chart_q4 = createPossessionTimeScoreChart(home, _home_rows_q4, home + ' 4th Quarter Possession Outcomes', 'h-q4-pout')
# away_possession_chart_q4 = createPossessionTimeScoreChart(away, _away_rows_q4, away + ' 4th Quarter Possession Outcomes', 'a-q4-pout')

# create circle entry pictures
createCircleEntryImage(home_basic_metrics, home)
createCircleEntryImage(away_basic_metrics, away)

# create turnover chart
createSeasonTurnoverImage()
