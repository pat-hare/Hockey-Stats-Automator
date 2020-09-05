def basic_metrics_calc(rows, goals):
    basic_metrics = {
        'possession_time': 0,
        '16s': 0,
        '16sTo25E': 0,
        'goals': goals,
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
        'ceEff': 0 
    }

    for row in rows:
        if {'name':'16s'} in row['events']:
            basic_metrics['16s'] += 1
            if {'name':'25 Entry (L)'} in row['events']:
                basic_metrics['16sTo25E'] += 1
            elif {'name':'25 Entry (C)'} in row['events']:
                basic_metrics['16sTo25E'] += 1
            elif {'name':'25 Entry (R)'} in row['events']:
                basic_metrics['16sTo25E'] += 1

        if {'name':'25 Entry (L)'} in row['events']:
            basic_metrics['25e']['L'] += 1
        elif {'name':'25 Entry (C)'} in row['events']:
            basic_metrics['25e']['C'] += 1
        elif {'name':'25 Entry (R)'} in row['events']:
            basic_metrics['25e']['R'] += 1
        
        if {'name':'CE 1'} in row['events']:
            basic_metrics['ce']['1'] += 1
        elif {'name':'CE 2'} in row['events']:
            basic_metrics['ce']['2'] += 1
        elif {'name':'CE 3'} in row['events']:
            basic_metrics['ce']['3'] += 1
        elif {'name':'CE 4'} in row['events']:
            basic_metrics['ce']['4'] += 1
        elif {'name':'CE 5'} in row['events']:
            basic_metrics['ce']['5'] += 1
        
        if {'name':'GSO'} in row['events']:
            basic_metrics['gso'] += 1
        if {'name':'Shot On Target'} in row['events']:
            basic_metrics['shots'] += 1
        if {'name':'Shot Off Target'} in row['events']:
            basic_metrics['shots'] += 1
        if {'name':'PC Win'} in row['events']:
            basic_metrics['pc_win'] += 1
        if {'name':'PP Win'} in row['events']:
            basic_metrics['pp_win'] += 1
        if {'name':'Lost'} in row['events']:
            basic_metrics['lost'] += 1

    return basic_metrics

def pp_metrics_calc(rows):
    pp_metrics = {
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
        'PPf': 0
    }

    for row in rows:
        pp_metrics['total'] += 1
        
        if {'name':'CE 1'} in row['events']:
            pp_metrics['ce'] += 1
        elif {'name':'CE 2'} in row['events']:
            pp_metrics['ce'] += 1
        elif {'name':'CE 3'} in row['events']:
            pp_metrics['ce'] += 1
        elif {'name':'CE 4'} in row['events']:
            pp_metrics['ce'] += 1
        elif {'name':'CE 5'} in row['events']:
            pp_metrics['ce'] += 1
        
        if {'name':'GSO'} in row['events']:
            pp_metrics['gso'] += 1
        if {'name':'PC Win'} in row['events']:
            pp_metrics['pc_win'] += 1
        if {'name':'PP Win '} in row['events']:
            pp_metrics['pp_win'] += 1
        if {'name':'PP Win'} in row['events']:
            pp_metrics['pp_win'] += 1
        if {'name':'Lost'} in row['events']:
            pp_metrics['lost'] += 1
        if {'name':'Foul Won'} in row['events']:
            pp_metrics['lost'] += 1
        if {'name':'End of Phase'} in row['events']:
            pp_metrics['lost'] += 1
        if {'name':'Goal'} in row['events']:
            pp_metrics['goal'] += 1
            pp_metrics['gso'] += 1

    return pp_metrics

def calcMetrics(home_basic_metrics, away_basic_metrics, home_pp_metrics, away_pp_metrics):
    if home_pp_metrics['total'] == 0:
        home_pp_metrics['PPp'] = 0
        home_pp_metrics['PPs'] = 0
        home_pp_metrics['PPf'] = 0
    else:
        home_pp_metrics['PPp'] = round((home_pp_metrics['ce'] + home_pp_metrics['gso'] + home_pp_metrics['pc_win'] + home_pp_metrics['goals']) / home_pp_metrics['total'], 2)
        home_pp_metrics['PPs'] = round((home_pp_metrics['gso'] + home_pp_metrics['pc_win'] + home_pp_metrics['goals']) / home_pp_metrics['total'], 2)
        home_pp_metrics['PPf'] = round(home_pp_metrics['lost'] / home_pp_metrics['total'], 2)

    if away_pp_metrics['total'] == 0:
        away_pp_metrics['PPp'] = 0
        away_pp_metrics['PPs'] = 0
        away_pp_metrics['PPf'] = 0
    else:
        away_pp_metrics['PPp'] = round((away_pp_metrics['ce'] + away_pp_metrics['gso'] + away_pp_metrics['pc_win'] + away_pp_metrics['goals']) / away_pp_metrics['total'], 2)
        away_pp_metrics['PPs'] = round((away_pp_metrics['gso'] + away_pp_metrics['pc_win'] + away_pp_metrics['goals']) / away_pp_metrics['total'], 2)
        away_pp_metrics['PPf'] = round(away_pp_metrics['lost'] / away_pp_metrics['total'], 2)

    home_basic_metrics['oEff'] = (home_basic_metrics['pp_win'] + home_pp_metrics['pp_win']) * 2 + (sum(home_basic_metrics['25e'].values())) * 2 + (sum(home_basic_metrics['ce'].values()) + home_pp_metrics['ce']) * 4 + (home_basic_metrics['gso'] + home_pp_metrics['gso']) * 6 + (home_basic_metrics['pc_win'] + home_pp_metrics['pc_win']) * 6 + (home_basic_metrics['goals'] + home_pp_metrics['goals']) * 10 - home_basic_metrics['lost'] - home_pp_metrics['lost']

    away_basic_metrics['oEff'] = (away_basic_metrics['pp_win'] + away_pp_metrics['pp_win']) * 2 + (sum(away_basic_metrics['25e'].values())) * 2 + (sum(away_basic_metrics['ce'].values()) + away_pp_metrics['ce']) * 4 + (away_basic_metrics['gso'] + away_pp_metrics['gso']) * 6 + (away_basic_metrics['pc_win'] + away_pp_metrics['pc_win']) * 6 + (away_basic_metrics['goals'] + away_pp_metrics['goals']) * 10 - away_basic_metrics['lost'] - away_pp_metrics['lost']

    home_basic_metrics['25Eff'] = (home_basic_metrics['pp_win'] + home_pp_metrics['pp_win']) + (sum(home_basic_metrics['ce'].values()) + home_pp_metrics['ce']) * 3 + (home_basic_metrics['gso'] + home_pp_metrics['gso']) * 6 + (home_basic_metrics['pc_win'] + home_pp_metrics['pc_win']) * 6 + (home_basic_metrics['goals'] + home_pp_metrics['goals']) * 10 - home_basic_metrics['lost'] - home_pp_metrics['lost']

    away_basic_metrics['25Eff'] = (away_basic_metrics['pp_win'] + away_pp_metrics['pp_win']) + (sum(away_basic_metrics['ce'].values()) + away_pp_metrics['ce']) * 3 + (away_basic_metrics['gso'] + away_pp_metrics['gso']) * 6 + (away_basic_metrics['pc_win'] + away_pp_metrics['pc_win']) * 6 + (away_basic_metrics['goals'] + away_pp_metrics['goals']) * 10 - away_basic_metrics['lost'] - away_pp_metrics['lost']

    home_basic_metrics['ceEff'] = (home_basic_metrics['gso'] + home_pp_metrics['gso']) * 6 + (home_basic_metrics['pc_win'] + home_pp_metrics['pc_win']) * 6 + (home_basic_metrics['goals'] + home_pp_metrics['goals']) * 10 - ((home_basic_metrics['lost'] + home_pp_metrics['lost']) * 2)

    away_basic_metrics['ceEff'] = (away_basic_metrics['gso'] + away_pp_metrics['gso']) * 6 + (away_basic_metrics['pc_win'] + away_pp_metrics['pc_win']) * 6 + (away_basic_metrics['goals'] + away_pp_metrics['goals']) * 10 - ((away_basic_metrics['lost'] + away_pp_metrics['lost']) * 2)

    return (home_basic_metrics, away_basic_metrics, home_pp_metrics, away_pp_metrics)
