import json
import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

_home_rows = []
_away_rows = []
_home_pprows = []
_away_pprows = []
home_basic_metrics = {
    'possession_time': 0,
    'goals': 0,
    'gso': 0,
    'shots': 0,
    'pc_win': 0,
    'pp_win': 0,
    'lost': 0,
    'ce': {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
    },
    '25e': {
        'L': 0,
        'C': 0,
        'R': 0,
    },
    'xG': 0,
    'xS': 0,
    'xPCG': 0,
    'xPC': 0,
    'oEff': 0,
    '25Eff': 0,
    'ceEff': 0 }
home_pp_metrics = {
    'total': 0,
    'forwards': 0,
    'backwards': 0,
    'ce': 0,
    'gso': 0,
    'pc_win': 0,
    'goals': 0,
    'lost': 0,
    'pp_win': 0,
    'PPp': 0,
    'PPs': 0,
    'PPf': 0 }
away_basic_metrics = {
    'possession_time': 0,
    'goals': 0,
    'gso': 0,
    'shots': 0,
    'pc_win': 0,
    'pp_win': 0,
    'lost': 0,
    'ce': {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
    },
    '25e': {
        'L': 0,
        'C': 0,
        'R': 0,
    },
    'xG': 0,
    'xS': 0,
    'xPCG': 0,
    'xPC': 0 }
away_pp_metrics = {
    'total': 0,
    'forwards': 0,
    'backwards': 0,
    'ce': 0,
    'gso': 0,
    'pc_win': 0,
    'goals': 0,
    'lost': 0,
    'pp_win': 0,
    'PPp': 0,
    'PPs': 0,
    'PPf': 0 }

home_scores = []
away_scores = []

with open('OGHC v REA.json') as json_file:
    data = json.load(json_file)
    for r in data['rows']:
        if r['name'] == 'OGHC':
            _home_rows = r['highlights']
        elif r['name'] == 'OGHC Goal':
            home_basic_metrics['goals'] = len(r['highlights'])
        elif r['name'] == 'OGHC PP':
            _home_pprows = r['highlights']
        elif r['name'] == 'REA':
            _away_rows = r['highlights']
        elif r['name'] == 'REA Goal':
            away_basic_metrics['goals'] = len(r['highlights'])
        elif r['name'] == 'REA PP':
            _away_pprows = r['highlights']

# traverse rows to add data to metrics
for row in _home_rows:
    if {'name':'25 Entry (L)'} in row['events']:
        home_basic_metrics['25e']['L'] += 1
    elif {'name':'25 Entry (C)'} in row['events']:
        home_basic_metrics['25e']['C'] += 1
    elif {'name':'25 Entry (R)'} in row['events']:
        home_basic_metrics['25e']['R'] += 1
    
    if {'name':'CE 1'} in row['events']:
        home_basic_metrics['ce']['1'] += 1
    elif {'name':'CE 2'} in row['events']:
        home_basic_metrics['ce']['2'] += 1
    elif {'name':'CE 3'} in row['events']:
        home_basic_metrics['ce']['3'] += 1
    elif {'name':'CE 4'} in row['events']:
        home_basic_metrics['ce']['4'] += 1
    elif {'name':'CE 5'} in row['events']:
        home_basic_metrics['ce']['5'] += 1
    
    if {'name':'GSO'} in row['events']:
        home_basic_metrics['gso'] += 1
    if {'name':'Shot'} in row['events']:
        home_basic_metrics['shots'] += 1
    if {'name':'PC Win'} in row['events']:
        home_basic_metrics['pc_win'] += 1
    if {'name':'PP Win'} in row['events']:
        home_basic_metrics['pp_win'] += 1
    if {'name':'Lost'} in row['events']:
        home_basic_metrics['lost'] += 1
for row in _home_pprows:
    home_pp_metrics['total'] += 1
    
    if {'name':'CE 1'} in row['events']:
        home_pp_metrics['ce'] += 1
    elif {'name':'CE 2'} in row['events']:
        home_pp_metrics['ce'] += 1
    elif {'name':'CE 3'} in row['events']:
        home_pp_metrics['ce'] += 1
    elif {'name':'CE 4'} in row['events']:
        home_pp_metrics['ce'] += 1
    elif {'name':'CE 5'} in row['events']:
        home_pp_metrics['ce'] += 1
    
    if {'name':'GSO'} in row['events']:
        home_pp_metrics['gso'] += 1
    if {'name':'PC Win'} in row['events']:
        home_pp_metrics['pc_win'] += 1
    if {'name':'PP Win '} in row['events']:
        home_pp_metrics['pp_win'] += 1
    if {'name':'PP Win'} in row['events']:
        home_pp_metrics['pp_win'] += 1
    if {'name':'Lost'} in row['events']:
        home_pp_metrics['lost'] += 1
    if {'name':'Foul Won'} in row['events']:
        home_pp_metrics['lost'] += 1
    if {'name':'End of Phase'} in row['events']:
        home_pp_metrics['lost'] += 1
    if {'name':'Goal'} in row['events']:
        home_pp_metrics['goal'] += 1
        home_pp_metrics['gso'] += 1

# traverse rows to add data to metrics
for row in _away_rows:
    if {'name':'25 Entry (L)'} in row['events']:
        away_basic_metrics['25e']['L'] += 1
    elif {'name':'25 Entry (C)'} in row['events']:
        away_basic_metrics['25e']['C'] += 1
    elif {'name':'25 Entry (R)'} in row['events']:
        away_basic_metrics['25e']['R'] += 1
    
    if {'name':'CE 1'} in row['events']:
        away_basic_metrics['ce']['1'] += 1
    elif {'name':'CE 2'} in row['events']:
        away_basic_metrics['ce']['2'] += 1
    elif {'name':'CE 3'} in row['events']:
        away_basic_metrics['ce']['3'] += 1
    elif {'name':'CE 4'} in row['events']:
        away_basic_metrics['ce']['4'] += 1
    elif {'name':'CE 5'} in row['events']:
        away_basic_metrics['ce']['5'] += 1
    
    if {'name':'GSO'} in row['events']:
        away_basic_metrics['gso'] += 1
    if {'name':'Shot'} in row['events']:
        away_basic_metrics['shots'] += 1
    if {'name':'PC Win'} in row['events']:
        away_basic_metrics['pc_win'] += 1
    if {'name':'PP Win'} in row['events']:
        away_basic_metrics['pp_win'] += 1
    if {'name':'Lost'} in row['events']:
        away_basic_metrics['lost'] += 1
for row in _away_pprows:
    away_pp_metrics['total'] += 1
    
    if {'name':'CE 1'} in row['events']:
        away_pp_metrics['ce'] += 1
    elif {'name':'CE 2'} in row['events']:
        away_pp_metrics['ce'] += 1
    elif {'name':'CE 3'} in row['events']:
        away_pp_metrics['ce'] += 1
    elif {'name':'CE 4'} in row['events']:
        away_pp_metrics['ce'] += 1
    elif {'name':'CE 5'} in row['events']:
        away_pp_metrics['ce'] += 1
    
    if {'name':'GSO'} in row['events']:
        away_pp_metrics['gso'] += 1
    if {'name':'PC Win'} in row['events']:
        away_pp_metrics['pc_win'] += 1
    if {'name':'PP Win '} in row['events']:
        away_pp_metrics['pp_win'] += 1
    if {'name':'PP Win'} in row['events']:
        away_pp_metrics['pp_win'] += 1
    if {'name':'Lost'} in row['events']:
        away_pp_metrics['lost'] += 1
    if {'name':'Foul Won'} in row['events']:
        away_pp_metrics['lost'] += 1
    if {'name':'End of Phase'} in row['events']:
        away_pp_metrics['lost'] += 1
    if {'name':'Goal'} in row['events']:
        away_pp_metrics['goal'] += 1
        away_pp_metrics['gso'] += 1

# traverse rows to add time/score data
for row in _home_rows:
    time = row['end'] - row['start']
    time = round(time, 1)

    score = 0

    if {'name':'25 Entry (L)'} in row['events']:
        score += 2
    elif {'name':'25 Entry (C)'} in row['events']:
        score += 2
    elif {'name':'25 Entry (R)'} in row['events']:
        score += 2
    
    if {'name':'CE 1'} in row['events']:
        score += 4
    elif {'name':'CE 2'} in row['events']:
        score += 4
    elif {'name':'CE 3'} in row['events']:
        score += 4
    elif {'name':'CE 4'} in row['events']:
        score += 4
    elif {'name':'CE 5'} in row['events']:
        score += 4
    
    if {'name':'GSO'} in row['events']:
        score += 6
    if {'name':'Shot'} in row['events']:
        score += 6
    if {'name':'PC Win'} in row['events']:
        score += 6
    if {'name':'PP Win'} in row['events']:
        score += 2
    if {'name':'Lost'} in row['events']:
        score -= 1

    home_scores.append((time,score))
for row in _away_rows:
    time = row['end'] - row['start']
    time = round(time, 1)

    score = 0

    if {'name':'25 Entry (L)'} in row['events']:
        score += 2
    elif {'name':'25 Entry (C)'} in row['events']:
        score += 2
    elif {'name':'25 Entry (R)'} in row['events']:
        score += 2
    
    if {'name':'CE 1'} in row['events']:
        score += 4
    elif {'name':'CE 2'} in row['events']:
        score += 4
    elif {'name':'CE 3'} in row['events']:
        score += 4
    elif {'name':'CE 4'} in row['events']:
        score += 4
    elif {'name':'CE 5'} in row['events']:
        score += 4
    
    if {'name':'GSO'} in row['events']:
        score += 6
    if {'name':'Shot'} in row['events']:
        score += 6
    if {'name':'PC Win'} in row['events']:
        score += 6
    if {'name':'PP Win'} in row['events']:
        score += 2
    if {'name':'Lost'} in row['events']:
        score -= 1

    away_scores.append((time,score))
home_scores.sort()
away_scores.sort()

# calculating PP metrics
def calcMetrics():
    home_pp_metrics['PPp'] = round((home_pp_metrics['ce'] + home_pp_metrics['gso'] + home_pp_metrics['pc_win'] + home_pp_metrics['goals']) / home_pp_metrics['total'], 2)
    home_pp_metrics['PPs'] = round((home_pp_metrics['gso'] + home_pp_metrics['pc_win'] + home_pp_metrics['goals']) / home_pp_metrics['total'], 2)
    home_pp_metrics['PPf'] = round(home_pp_metrics['lost'] / home_pp_metrics['total'], 2)

    away_pp_metrics['PPp'] = round((away_pp_metrics['ce'] + away_pp_metrics['gso'] + away_pp_metrics['pc_win'] + away_pp_metrics['goals']) / away_pp_metrics['total'], 2)
    away_pp_metrics['PPs'] = round((away_pp_metrics['gso'] + away_pp_metrics['pc_win'] + away_pp_metrics['goals']) / away_pp_metrics['total'], 2)
    away_pp_metrics['PPf'] = round(away_pp_metrics['lost'] / away_pp_metrics['total'], 2)

    home_basic_metrics['oEff'] = (home_basic_metrics['pp_win'] + home_pp_metrics['pp_win']) * 2 + (sum(home_basic_metrics['25e'].values())) * 2 + (sum(home_basic_metrics['ce'].values()) + home_pp_metrics['ce']) * 4 + (home_basic_metrics['gso'] + home_pp_metrics['gso']) * 6 + (home_basic_metrics['pc_win'] + home_pp_metrics['pc_win']) * 6 + (home_basic_metrics['goals'] + home_pp_metrics['goals']) * 10 - home_basic_metrics['lost'] - home_pp_metrics['lost']

    away_basic_metrics['oEff'] = (away_basic_metrics['pp_win'] + away_pp_metrics['pp_win']) * 2 + (sum(away_basic_metrics['25e'].values())) * 2 + (sum(away_basic_metrics['ce'].values()) + away_pp_metrics['ce']) * 4 + (away_basic_metrics['gso'] + away_pp_metrics['gso']) * 6 + (away_basic_metrics['pc_win'] + away_pp_metrics['pc_win']) * 6 + (away_basic_metrics['goals'] + away_pp_metrics['goals']) * 10 - away_basic_metrics['lost'] - away_pp_metrics['lost']

    home_basic_metrics['25Eff'] = (home_basic_metrics['pp_win'] + home_pp_metrics['pp_win']) + (sum(home_basic_metrics['ce'].values()) + home_pp_metrics['ce']) * 3 + (home_basic_metrics['gso'] + home_pp_metrics['gso']) * 6 + (home_basic_metrics['pc_win'] + home_pp_metrics['pc_win']) * 6 + (home_basic_metrics['goals'] + home_pp_metrics['goals']) * 10 - home_basic_metrics['lost'] - home_pp_metrics['lost']

    away_basic_metrics['25Eff'] = (away_basic_metrics['pp_win'] + away_pp_metrics['pp_win']) + (sum(away_basic_metrics['ce'].values()) + away_pp_metrics['ce']) * 3 + (away_basic_metrics['gso'] + away_pp_metrics['gso']) * 6 + (away_basic_metrics['pc_win'] + away_pp_metrics['pc_win']) * 6 + (away_basic_metrics['goals'] + away_pp_metrics['goals']) * 10 - away_basic_metrics['lost'] - away_pp_metrics['lost']

    home_basic_metrics['ceEff'] = (home_basic_metrics['gso'] + home_pp_metrics['gso']) * 6 + (home_basic_metrics['pc_win'] + home_pp_metrics['pc_win']) * 6 + (home_basic_metrics['goals'] + home_pp_metrics['goals']) * 10 - ((home_basic_metrics['lost'] + home_pp_metrics['lost']) * 2)

    away_basic_metrics['ceEff'] = (away_basic_metrics['gso'] + away_pp_metrics['gso']) * 6 + (away_basic_metrics['pc_win'] + away_pp_metrics['pc_win']) * 6 + (away_basic_metrics['goals'] + away_pp_metrics['goals']) * 10 - ((away_basic_metrics['lost'] + away_pp_metrics['lost']) * 2)

calcMetrics()

def createBasicChart(home_data, away_data):
    df = pd.DataFrame(
        {
            'OGHC': [
                sum(home_data['ce'].values()),
                sum(home_data['25e'].values()),
                home_data['pc_win'],
                home_data['gso'],
                home_data['shots'],
                home_data['goals'],
            ],
            'Reading': [
                sum(away_data['ce'].values()),
                sum(away_data['25e'].values()),
                away_data['pc_win'],
                away_data['gso'],
                away_data['shots'],
                away_data['goals'],
            ],
        }, 
        index = [
            'Circle Entries',
            '25 Entries',
            'PC Wins',
            'GSO',
            'Shots',
            'Goals',
        ]
    )

    stacked_data = df.apply(lambda x: x*100/sum(x), axis=1)
    stacked_data = stacked_data.plot.barh(stacked=True)
    stacked_data.axes.xaxis.set_visible(False)
    plt.gca().legend(loc='upper center', bbox_to_anchor=(0.5,-0.05), ncol=2)

    plt.text(x=1,y=4.9, s=home_data['goals'], size=12, color='white')
    plt.text(x=1,y=3.9, s=home_data['shots'], size=12, color='white')
    plt.text(x=1,y=2.9, s=home_data['gso'], size=12, color='white')
    plt.text(x=1,y=1.9, s=home_data['pc_win'], size=12, color='white')
    plt.text(x=1,y=0.9, s=sum(home_data['25e'].values()), size=12, color='white')
    plt.text(x=1,y=-0.1, s=sum(home_data['ce'].values()), size=12, color='white')

    plt.text(x=95,y=4.9, s=away_data['goals'], size=12, color='white')
    plt.text(x=95,y=3.9, s=away_data['shots'], size=12, color='white')
    plt.text(x=95,y=2.9, s=away_data['gso'], size=12, color='white')
    plt.text(x=95,y=1.9, s=away_data['pc_win'], size=12, color='white')
    plt.text(x=95,y=0.9, s=sum(away_data['25e'].values()), size=12, color='white')
    plt.text(x=95,y=-0.1, s=sum(away_data['ce'].values()), size=12, color='white')

    return stacked_data

basic_chart = createBasicChart(home_basic_metrics, away_basic_metrics)

plt.show()

img = Image.open("HockeyCircle.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("OpenSans-Semibold.ttf", 16)
draw.text((0, 0),"Sample Text",(0,0,0),font=font)
img.save('sample-out.png')

print(home_basic_metrics)
print(away_basic_metrics)