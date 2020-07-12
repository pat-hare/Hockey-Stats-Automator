import pandas as pd
import matplotlib.pyplot as plt

def createBasicChart(home_data, away_data, title, filename):
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
            'Wimbledon': [
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

    plt.title(title)
    plt.savefig(filename, bbox_inches='tight')

    return stacked_data

def createTimeSeriesChart(home_rows, away_rows, title, filename):
    home_times = []
    away_times = []
    home_chart_scores = []
    away_chart_scores = []

    for row in home_rows:
        time = row['end']
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

        home_times.append(time)
        home_chart_scores.append(score)

    for row in away_rows:
        time = row['end']
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

        away_times.append(time)
        away_chart_scores.append(score)


    hdf = pd.DataFrame({'time': home_times, 'home scores': home_chart_scores})
    hdf['time'] = hdf['time'].div(60).round(2)
    hdf = hdf.set_index('time')
    hdf = hdf.cumsum()

    adf = pd.DataFrame({'time': away_times, 'away scores': away_chart_scores})
    adf['time'] = adf['time'].div(60).round(2)
    adf = adf.set_index('time')
    adf = adf.cumsum()

    bigdata = hdf.append(adf)

    bigdata.plot.line()
    plt.title(title)
    plt.savefig(filename, bbox_inches='tight')

    return bigdata

def createPossessionTimeScoreChart(rows, title, filename):
    scores = []

    for row in rows:
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

        scores.append((time,score))

    scores.sort()

    df = pd.DataFrame(scores,columns=['time','score'])
    df = df.set_index('time')
    df.plot.bar()

    plt.title(title)
    plt.savefig(filename, bbox_inches='tight')    
