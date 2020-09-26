import pandas as pd

def createInDepthTable(home, away):
    data = {
        '': [
            '16s to 25E',
            '25E to CE',
            'CE to GSO',
            'GSO to Goal',
            'CA to GSO/PC Win',
            'Deep Def. to CE',
            'Deep Def. to GSO',
            'Deep Def. to Goal',
            'Deep Def. Turnover to 25E',
        ],
        home.team.teamName: [],
        away.team.teamName: [],
        'Season': [0,0,0,0,0,0,0,0,0],
        'Last Game': [0,0,0,0,0,0,0,0,0]
    }

    homeTotalCE = home.metrics_fg['ce']['1']['total'] + home.metrics_fg['ce']['2']['total'] + home.metrics_fg['ce']['3']['total'] + home.metrics_fg['ce']['4']['total'] + home.metrics_fg['ce']['5']['total']
    awayTotalCE = away.metrics_fg['ce']['1']['total'] + away.metrics_fg['ce']['2']['total'] + away.metrics_fg['ce']['3']['total'] + away.metrics_fg['ce']['4']['total'] + away.metrics_fg['ce']['5']['total']
    homeTotalPPCE = home.pp_metrics_fg['ce']['1']['total'] + home.pp_metrics_fg['ce']['2']['total'] + home.pp_metrics_fg['ce']['3']['total'] + home.pp_metrics_fg['ce']['4']['total'] + home.pp_metrics_fg['ce']['5']['total']
    awayTotalPPCE = away.pp_metrics_fg['ce']['1']['total'] + away.pp_metrics_fg['ce']['2']['total'] + away.pp_metrics_fg['ce']['3']['total'] + away.pp_metrics_fg['ce']['4']['total'] + away.pp_metrics_fg['ce']['5']['total']

    data[home.team.teamName].append(home.metrics_fg['16sTo25E'])
    data[home.team.teamName].append(str((round((homeTotalCE/sum(home.metrics_fg['25e'].values())),2))*100) + '%')
    data[home.team.teamName].append(str((round((home.metrics_fg['gso']/homeTotalCE),2))*100) + '%')
    data[home.team.teamName].append(str((round((home.metrics_fg['goals']/home.metrics_fg['gso']),2))*100) + '%')
    data[home.team.teamName].append(0)
    data[home.team.teamName].append(homeTotalPPCE/home.pp_metrics_fg['total'])
    data[home.team.teamName].append(home.pp_metrics_fg['gso']/home.pp_metrics_fg['total'])
    data[home.team.teamName].append(home.pp_metrics_fg['goals']/home.pp_metrics_fg['total'])
    data[home.team.teamName].append(0)

    data[away.team.teamName].append(away.metrics_fg['16sTo25E'])
    data[away.team.teamName].append(str((round((awayTotalCE/sum(away.metrics_fg['25e'].values())),2))*100) + '%')
    data[away.team.teamName].append(str((round((away.metrics_fg['gso']/awayTotalCE),2))*100) + '%')
    data[away.team.teamName].append(str((round((away.metrics_fg['goals']/away.metrics_fg['gso']),2))*100) + '%')
    data[away.team.teamName].append(0)
    data[away.team.teamName].append(awayTotalPPCE/away.pp_metrics_fg['total'])
    data[away.team.teamName].append(away.pp_metrics_fg['gso']/away.pp_metrics_fg['total'])
    data[away.team.teamName].append(away.pp_metrics_fg['goals']/away.pp_metrics_fg['total'])
    data[away.team.teamName].append(0)

    df = pd.DataFrame(data)

    df.to_csv('detailed-analysis.csv')
