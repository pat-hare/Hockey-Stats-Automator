import pandas as pd
import matplotlib.pyplot as plt

def setColours(team):
    if team == 'BEE':
        return 'black'
    elif team == 'BMU':
        return 'midnightblue'
    elif team == 'EG':
        return 'darkblue'
    elif team == 'HWHC':
        return 'cornflowerblue'
    elif team == 'HOL':
        return 'red'
    elif team == 'OGHC':
        return 'maroon'
    elif team == 'REA':
        return 'lightsteelblue'
    elif team == 'SUR':
        return 'darkgreen'
    elif team == 'UOD':
        return 'purple'
    elif team == 'UOE':
        return 'darkgreen'
    elif team == 'WIM':
        return 'midnightblue'
    elif team == 'TED':
        return 'pink'

def createBasicChart(home, away, home_goals, away_goals):
    homeCol = setColours(home.team.teamName)
    awayCol = setColours(away.team.teamName)
    homeTotalCE = home.metrics_fg['ce']['1']['total'] + home.metrics_fg['ce']['2']['total'] + home.metrics_fg['ce']['3']['total'] + home.metrics_fg['ce']['4']['total'] + home.metrics_fg['ce']['5']['total']
    awayTotalCE = away.metrics_fg['ce']['1']['total'] + away.metrics_fg['ce']['2']['total'] + away.metrics_fg['ce']['3']['total'] + away.metrics_fg['ce']['4']['total'] + away.metrics_fg['ce']['5']['total']
    homeTotalPPCE = home.pp_metrics_fg['ce']['1']['total'] + home.pp_metrics_fg['ce']['2']['total'] + home.pp_metrics_fg['ce']['3']['total'] + home.pp_metrics_fg['ce']['4']['total'] + home.pp_metrics_fg['ce']['5']['total']
    awayTotalPPCE = away.pp_metrics_fg['ce']['1']['total'] + away.pp_metrics_fg['ce']['2']['total'] + away.pp_metrics_fg['ce']['3']['total'] + away.pp_metrics_fg['ce']['4']['total'] + away.pp_metrics_fg['ce']['5']['total']

    df = pd.DataFrame(
        {
            home.team.teamName: [
                homeTotalCE + homeTotalPPCE,
                sum(home.metrics_fg['25e'].values()),
                home.metrics_fg['pc_win'] + home.pp_metrics_fg['pc_win'],
                home.metrics_fg['gso'] + home.pp_metrics_fg['gso'],
                home.metrics_fg['shots'] + home.pp_metrics_fg['shots'],
                home_goals,
            ],
            away.team.teamName: [
                awayTotalCE + awayTotalPPCE,
                sum(away.metrics_fg['25e'].values()),
                away.metrics_fg['pc_win'] + away.pp_metrics_fg['pc_win'],
                away.metrics_fg['gso'] + away.pp_metrics_fg['gso'],
                away.metrics_fg['shots'] + away.pp_metrics_fg['shots'],
                away_goals,
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
    stacked_data = stacked_data.plot.barh(stacked=True, color=[homeCol, awayCol])
    stacked_data.axes.xaxis.set_visible(False)
    plt.gca().legend(loc='upper center', bbox_to_anchor=(0.5,-0.05), ncol=2)

    plt.text(x=1,y=4.9, s=home_goals, size=12, color='white')
    plt.text(x=1,y=3.9, s=(home.metrics_fg['shots'] + home.pp_metrics_fg['shots']), size=12, color='white')
    plt.text(x=1,y=2.9, s=(home.metrics_fg['gso'] + home.pp_metrics_fg['gso']), size=12, color='white')
    plt.text(x=1,y=1.9, s=(home.metrics_fg['pc_win'] + home.pp_metrics_fg['pc_win']), size=12, color='white')
    plt.text(x=1,y=0.9, s=sum(home.metrics_fg['25e'].values()), size=12, color='white')
    plt.text(x=1,y=-0.1, s=(homeTotalCE + homeTotalPPCE), size=12, color='white')

    plt.text(x=95,y=4.9, s=away_goals, size=12, color='white')
    plt.text(x=95,y=3.9, s=(away.metrics_fg['shots'] + away.pp_metrics_fg['shots']), size=12, color='white')
    plt.text(x=95,y=2.9, s=(away.metrics_fg['gso'] + away.pp_metrics_fg['gso']), size=12, color='white')
    plt.text(x=95,y=1.9, s=(away.metrics_fg['pc_win'] + away.pp_metrics_fg['pc_win']), size=12, color='white')
    plt.text(x=95,y=0.9, s=sum(away.metrics_fg['25e'].values()), size=12, color='white')
    plt.text(x=95,y=-0.1, s=(awayTotalCE + awayTotalPPCE), size=12, color='white')

    plt.title(home.team.teamName + " v " + away.team.teamName)
    plt.savefig('./assets_output/' + home.team.teamName + ' v ' + away.team.teamName, bbox_inches='tight')

    return stacked_data

def createTimeSeriesChart(home, away, home_rows, away_rows, title, filename):
    homeCol = setColours(home)
    awayCol = setColours(away)

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
            score += 5
        if {'name':'Shot On Target'} in row['events']:
            score += 6
        if {'name':'PC Win'} in row['events']:
            score += 6
        if {'name':'Shot Off Target'} in row['events']:
            score += 4
        if {'name':'PP Win'} in row['events']:
            score += 2
        if {'name':'Foul Won'} in row['events']:
            score += 1
        if {'name':'Lost'} in row['events']:
            score -= 1
        if {'name':'Out of Play'} in row['events']:
            score -= 0.5

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
        if {'name':'Shot On Target'} in row['events']:
            score += 6
        if {'name':'PC Win'} in row['events']:
            score += 6
        if {'name':'Shot Off Target'} in row['events']:
            score += 4
        if {'name':'PP Win'} in row['events']:
            score += 2
        if {'name':'Foul Won'} in row['events']:
            score += 1
        if {'name':'Lost'} in row['events']:
            score -= 1
        if {'name':'Out of Play'} in row['events']:
            score -= 0.5

        away_times.append(time)
        away_chart_scores.append(score)


    hdf = pd.DataFrame({'time': home_times, home + ' scores': home_chart_scores})
    hdf['time'] = hdf['time'].div(60).round(2)
    hdf = hdf.set_index('time')
    hdf = hdf.cumsum()

    adf = pd.DataFrame({'time': away_times, away + ' scores': away_chart_scores})
    adf['time'] = adf['time'].div(60).round(2)
    adf = adf.set_index('time')
    adf = adf.cumsum()

    bigdata = hdf.append(adf)

    bigdata.plot.line(color=[homeCol, awayCol])
    plt.title(title)
    plt.savefig('./assets_output/' + filename, bbox_inches='tight')

    return bigdata

def createPossessionTimeScoreChart(team, rows, title, filename):
    teamCol = setColours(team)

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
            score += 5
        if {'name':'Shot On Target'} in row['events']:
            score += 6
        if {'name':'PC Win'} in row['events']:
            score += 6
        if {'name':'Shot Off Target'} in row['events']:
            score += 4
        if {'name':'PP Win'} in row['events']:
            score += 2
        if {'name':'Foul Won'} in row['events']:
            score += 1
        if {'name':'Lost'} in row['events']:
            score -= 1
        if {'name':'Out of Play'} in row['events']:
            score -= 0.5

        scores.append((time,score))

    scores.sort()

    df = pd.DataFrame(scores,columns=['time','score'])
    df = df.set_index('time')
    df.plot.bar(color=teamCol)

    plt.title(title)
    plt.tick_params(axis='x', which='major', labelsize=9)
    plt.savefig('./assets_output/' + filename, bbox_inches='tight')    
