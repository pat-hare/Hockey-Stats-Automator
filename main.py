import json
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from metrics_calc import basic_metrics_calc, pp_metrics_calc, calcMetrics
from chart_creator import createBasicChart, createTimeSeriesChart, createPossessionTimeScoreChart

_home_rows = []
_away_rows = []
_home_pprows = []
_away_pprows = []
home_goals = 0
away_goals = 0

with open('OGHC v REA.json') as json_file:
    data = json.load(json_file)
    for r in data['rows']:
        if r['name'] == 'OGHC':
            _home_rows = r['highlights']
        elif r['name'] == 'OGHC Goal':
            home_goals = len(r['highlights'])
        elif r['name'] == 'OGHC PP':
            _home_pprows = r['highlights']
        elif r['name'] == 'REA':
            _away_rows = r['highlights']
        elif r['name'] == 'REA Goal':
            away_goals = len(r['highlights'])
        elif r['name'] == 'REA PP':
            _away_pprows = r['highlights']

home_basic_metrics = basic_metrics_calc(_home_rows, home_goals)
away_basic_metrics = basic_metrics_calc(_away_rows, away_goals)

home_pp_metrics = pp_metrics_calc(_home_pprows)
away_pp_metrics = pp_metrics_calc(_away_pprows)


home_basic_metrics, away_basic_metrics, home_pp_metrics, away_pp_metrics = calcMetrics(home_basic_metrics, away_basic_metrics, home_pp_metrics, away_pp_metrics)

basic_chart = createBasicChart(home_basic_metrics, away_basic_metrics)

time_series_chart = createTimeSeriesChart(_home_rows, _away_rows)

home_possession_chart = createPossessionTimeScoreChart(_home_rows)

away_possession_chart = createPossessionTimeScoreChart(_away_rows)


plt.show()

img = Image.open("HockeyCircle.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("OpenSans-Semibold.ttf", 16)
draw.text((0, 0),"Sample Text",(0,0,0),font=font)
img.save('sample-out.png')

# print(home_basic_metrics)
# print(away_basic_metrics)