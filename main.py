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
from class_team_rows import TeamRows
from class_team_metrics import TeamMetrics

_home_rows_fg = []
_home_pprows_fg = []
_away_rows_fg = []
_away_pprows_fg = []

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

home_rows = TeamRows(home,_home_rows_fg,_home_pprows_fg,home_goals,EoQ1,EoQ2,EoQ3)
away_rows = TeamRows(away,_away_rows_fg,_away_pprows_fg,away_goals,EoQ1,EoQ2,EoQ3)

# create full game metrics
home_team_metrics = TeamMetrics(home_rows)
away_team_metrics = TeamMetrics(away_rows)

# add metrics to database
addRowToMetrics(home, home, away, home_team_metrics)
addRowToMetrics(away, home, away, away_team_metrics)

# create full game charts
basic_chart_fg = createBasicChart(home_team_metrics, away_team_metrics)
time_series_chart_fg = createTimeSeriesChart(home, away, home_rows.rows, away_rows.rows, 'Full Game Outlet Efficiency', 'fg-oeff')

# create quarter charts
time_series_chart_q1 = createTimeSeriesChart(home, away, home_rows.rows_Q1, away_rows.rows_Q1, '1st Quarter Outlet Efficiency', 'q1-oeff')
time_series_chart_q2 = createTimeSeriesChart(home, away, home_rows.rows_Q2, away_rows.rows_Q2, '2nd Quarter Outlet Efficiency', 'q2-oeff')
time_series_chart_q3 = createTimeSeriesChart(home, away, home_rows.rows_Q3, away_rows.rows_Q3, '3rd Quarter Outlet Efficiency', 'q3-oeff')
time_series_chart_q4 = createTimeSeriesChart(home, away, home_rows.rows_Q4, away_rows.rows_Q4, '4th Quarter Outlet Efficiency', 'q4-oeff')

# create circle entry pictures
createCircleEntryImage(home_team_metrics.metrics_fg, home)
createCircleEntryImage(away_team_metrics.metrics_fg, away)

# create turnover chart
createSeasonTurnoverImage()
