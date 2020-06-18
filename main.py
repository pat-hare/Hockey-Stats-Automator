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
draw.text((488, 173),"1",(0,0,0),font=font)
draw.text((628, 425),"1",(0,0,0),font=font)
draw.text((902, 530),"1",(0,0,0),font=font)
draw.text((1175, 430),"1",(0,0,0),font=font)
draw.text((1320, 173),"1",(0,0,0),font=font)

font = ImageFont.truetype("OpenSans-Semibold.ttf", 45)
draw.text((478, 800),"1",(0,0,0),font=font)
draw.text((902, 800),"1",(0,0,0),font=font)
draw.text((1325, 800),"1",(0,0,0),font=font)

img.save('sample-out.png')

# print(home_basic_metrics)
# print(away_basic_metrics)