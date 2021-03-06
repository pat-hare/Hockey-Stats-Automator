def basic_metrics_calc(rows):
    basic_metrics = {
        'possession_time': 0,
        '16s': 0,
        '16sTo25E': 0,
        'goals': 0,
        'gso': 0,
        'shots': 0,
        'pc_win': 0,
        'pp_win': 0,
        'lost': 0,
        'ce': {
            '1': {
                'total': 0,
                'goals': 0,
                'pc_win': 0,
                'gso': 0,
                'pp_win': 0,
                'retain': 0,
                'lost': 0
            },
            '2': {
                'total': 0,
                'goals': 0,
                'pc_win': 0,
                'gso': 0,
                'pp_win': 0,
                'retain': 0,
                'lost': 0
            },
            '3': {
                'total': 0,
                'goals': 0,
                'pc_win': 0,
                'gso': 0,
                'pp_win': 0,
                'retain': 0,
                'lost': 0
            },
            '4': {
                'total': 0,
                'goals': 0,
                'pc_win': 0,
                'gso': 0,
                'pp_win': 0,
                'retain': 0,
                'lost': 0
            },
            '5': {
                'total': 0,
                'goals': 0,
                'pc_win': 0,
                'gso': 0,
                'pp_win': 0,
                'retain': 0,
                'lost': 0
            },
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
        # row is not called 16s it is TEAM 16
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
            basic_metrics['ce']['1']['total'] += 1
            if {'name':'Goal'} in row['events']:
                basic_metrics['ce']['1']['goals'] += 1
            elif {'name':'PC Win'} in row['events']:
                basic_metrics['ce']['1']['pc_win'] += 1
            elif {'name':'GSO'} in row['events']:
                basic_metrics['ce']['1']['gso'] += 1
            elif {'name':'PP Win'} in row['events']:
                basic_metrics['ce']['1']['pp_win'] += 1
            elif {'name':'PP Win '} in row['events']:
                basic_metrics['ce']['1']['pp_win'] += 1
            elif {'name':'Lost'} in row['events']:
                basic_metrics['ce']['1']['lost'] += 1
            elif {'name':'Out of Play'} in row['events']:
                basic_metrics['ce']['1']['lost'] += 1
            elif {'name':'Foul Won'} in row['events']:
                basic_metrics['ce']['1']['lost'] += 1
            elif {'name':'Foul Lost'} in row['events']:
                basic_metrics['ce']['1']['lost'] += 1
        elif {'name':'CE 2'} in row['events']:
            basic_metrics['ce']['2']['total'] += 1
            if {'name':'Goal'} in row['events']:
                basic_metrics['ce']['2']['goals'] += 1
            elif {'name':'PC Win'} in row['events']:
                basic_metrics['ce']['2']['pc_win'] += 1
            elif {'name':'GSO'} in row['events']:
                basic_metrics['ce']['2']['gso'] += 1
            elif {'name':'PP Win'} in row['events']:
                basic_metrics['ce']['2']['pp_win'] += 1
            elif {'name':'PP Win '} in row['events']:
                basic_metrics['ce']['2']['pp_win'] += 1
            elif {'name':'Lost'} in row['events']:
                basic_metrics['ce']['2']['lost'] += 1
            elif {'name':'Out of Play'} in row['events']:
                basic_metrics['ce']['2']['lost'] += 1
            elif {'name':'Foul Won'} in row['events']:
                basic_metrics['ce']['2']['lost'] += 1
            elif {'name':'Foul Lost'} in row['events']:
                basic_metrics['ce']['2']['lost'] += 1
        elif {'name':'CE 3'} in row['events']:
            basic_metrics['ce']['3']['total'] += 1
            if {'name':'Goal'} in row['events']:
                basic_metrics['ce']['3']['goals'] += 1
            elif {'name':'PC Win'} in row['events']:
                basic_metrics['ce']['3']['pc_win'] += 1
            elif {'name':'GSO'} in row['events']:
                basic_metrics['ce']['3']['gso'] += 1
            elif {'name':'PP Win'} in row['events']:
                basic_metrics['ce']['3']['pp_win'] += 1
            elif {'name':'PP Win '} in row['events']:
                basic_metrics['ce']['3']['pp_win'] += 1
            elif {'name':'Lost'} in row['events']:
                basic_metrics['ce']['3']['lost'] += 1
            elif {'name':'Out of Play'} in row['events']:
                basic_metrics['ce']['3']['lost'] += 1
            elif {'name':'Foul Won'} in row['events']:
                basic_metrics['ce']['3']['lost'] += 1
            elif {'name':'Foul Lost'} in row['events']:
                basic_metrics['ce']['3']['lost'] += 1
        elif {'name':'CE 4'} in row['events']:
            basic_metrics['ce']['4']['total'] += 1
            if {'name':'Goal'} in row['events']:
                basic_metrics['ce']['4']['goals'] += 1
            elif {'name':'PC Win'} in row['events']:
                basic_metrics['ce']['4']['pc_win'] += 1
            elif {'name':'GSO'} in row['events']:
                basic_metrics['ce']['4']['gso'] += 1
            elif {'name':'PP Win'} in row['events']:
                basic_metrics['ce']['4']['pp_win'] += 1
            elif {'name':'PP Win '} in row['events']:
                basic_metrics['ce']['4']['pp_win'] += 1
            elif {'name':'Lost'} in row['events']:
                basic_metrics['ce']['4']['lost'] += 1
            elif {'name':'Out of Play'} in row['events']:
                basic_metrics['ce']['4']['lost'] += 1
            elif {'name':'Foul Won'} in row['events']:
                basic_metrics['ce']['4']['lost'] += 1
            elif {'name':'Foul Lost'} in row['events']:
                basic_metrics['ce']['4']['lost'] += 1
        elif {'name':'CE 5'} in row['events']:
            basic_metrics['ce']['5']['total'] += 1
            if {'name':'Goal'} in row['events']:
                basic_metrics['ce']['5']['goals'] += 1
            elif {'name':'PC Win'} in row['events']:
                basic_metrics['ce']['5']['pc_win'] += 1
            elif {'name':'GSO'} in row['events']:
                basic_metrics['ce']['5']['gso'] += 1
            elif {'name':'PP Win'} in row['events']:
                basic_metrics['ce']['5']['pp_win'] += 1
            elif {'name':'PP Win '} in row['events']:
                basic_metrics['ce']['5']['pp_win'] += 1
            elif {'name':'Lost'} in row['events']:
                basic_metrics['ce']['5']['lost'] += 1
            elif {'name':'Out of Play'} in row['events']:
                basic_metrics['ce']['5']['lost'] += 1
            elif {'name':'Foul Won'} in row['events']:
                basic_metrics['ce']['5']['lost'] += 1
            elif {'name':'Foul Lost'} in row['events']:
                basic_metrics['ce']['5']['lost'] += 1
        
        if {'name':'GSO'} in row['events']:
            basic_metrics['gso'] += 1
        if {'name':'Shot On Target'} in row['events']:
            basic_metrics['shots'] += 1
        if {'name':'Saved'} in row['events']:
            basic_metrics['shots'] += 1
        if {'name':'Shot Off Target'} in row['events']:
            basic_metrics['shots'] += 1
        if {'name':'PC Win'} in row['events']:
            basic_metrics['pc_win'] += 1
        if {'name':'PP Win'} in row['events']:
            basic_metrics['pp_win'] += 1
        if {'name':'PP Win '} in row['events']:
            basic_metrics['pp_win'] += 1
        if {'name':'Foul Lost'} in row['events']:
            basic_metrics['lost'] += 1
        if {'name':'Foul Won'} in row['events']:
            basic_metrics['lost'] += 1
        if {'name':'Out of Play'} in row['events']:
            basic_metrics['lost'] += 1
        if {'name':'Goal'} in row['events']:
            basic_metrics['goals'] += 1

    return basic_metrics

def pp_metrics_calc(rows):
    pp_metrics = {
        'total': 0,
        'ce': {
            '1': {
                'total': 0,
                'goals': 0,
                'pc_win': 0,
                'gso': 0,
                'pp_win': 0,
                'retain': 0,
                'lost': 0
            },
            '2': {
                'total': 0,
                'goals': 0,
                'pc_win': 0,
                'gso': 0,
                'pp_win': 0,
                'retain': 0,
                'lost': 0
            },
            '3': {
                'total': 0,
                'goals': 0,
                'pc_win': 0,
                'gso': 0,
                'pp_win': 0,
                'retain': 0,
                'lost': 0
            },
            '4': {
                'total': 0,
                'goals': 0,
                'pc_win': 0,
                'gso': 0,
                'pp_win': 0,
                'retain': 0,
                'lost': 0
            },
            '5': {
                'total': 0,
                'goals': 0,
                'pc_win': 0,
                'gso': 0,
                'pp_win': 0,
                'retain': 0,
                'lost': 0
            },
        },
        'gso': 0,
        'shots': 0,
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
            pp_metrics['ce']['1']['total'] += 1
            if {'name':'Goal'} in row['events']:
                pp_metrics['ce']['1']['goals'] += 1
            elif {'name':'PC Win'} in row['events']:
                pp_metrics['ce']['1']['pc_win'] += 1
            elif {'name':'GSO'} in row['events']:
                pp_metrics['ce']['1']['gso'] += 1
            elif {'name':'PP Win'} in row['events']:
                pp_metrics['ce']['1']['pp_win'] += 1
            elif {'name':'PP Win '} in row['events']:
                pp_metrics['ce']['1']['pp_win'] += 1
            elif {'name':'Lost'} in row['events']:
                pp_metrics['ce']['1']['lost'] += 1
            elif {'name':'Out of Play'} in row['events']:
                pp_metrics['ce']['1']['lost'] += 1
            elif {'name':'Foul Won'} in row['events']:
                pp_metrics['ce']['1']['lost'] += 1
            elif {'name':'Foul Lost'} in row['events']:
                pp_metrics['ce']['1']['lost'] += 1
        elif {'name':'CE 2'} in row['events']:
            pp_metrics['ce']['2']['total'] += 1
            if {'name':'Goal'} in row['events']:
                pp_metrics['ce']['2']['goals'] += 1
            elif {'name':'PC Win'} in row['events']:
                pp_metrics['ce']['2']['pc_win'] += 1
            elif {'name':'GSO'} in row['events']:
                pp_metrics['ce']['2']['gso'] += 1
            elif {'name':'PP Win'} in row['events']:
                pp_metrics['ce']['2']['pp_win'] += 1
            elif {'name':'PP Win '} in row['events']:
                pp_metrics['ce']['2']['pp_win'] += 1
            elif {'name':'Lost'} in row['events']:
                pp_metrics['ce']['2']['lost'] += 1
            elif {'name':'Out of Play'} in row['events']:
                pp_metrics['ce']['2']['lost'] += 1
            elif {'name':'Foul Won'} in row['events']:
                pp_metrics['ce']['2']['lost'] += 1
            elif {'name':'Foul Lost'} in row['events']:
                pp_metrics['ce']['2']['lost'] += 1
        elif {'name':'CE 3'} in row['events']:
            pp_metrics['ce']['3']['total'] += 1
            if {'name':'Goal'} in row['events']:
                pp_metrics['ce']['3']['goals'] += 1
            elif {'name':'PC Win'} in row['events']:
                pp_metrics['ce']['3']['pc_win'] += 1
            elif {'name':'GSO'} in row['events']:
                pp_metrics['ce']['3']['gso'] += 1
            elif {'name':'PP Win'} in row['events']:
                pp_metrics['ce']['3']['pp_win'] += 1
            elif {'name':'PP Win '} in row['events']:
                pp_metrics['ce']['3']['pp_win'] += 1
            elif {'name':'Lost'} in row['events']:
                pp_metrics['ce']['3']['lost'] += 1
            elif {'name':'Out of Play'} in row['events']:
                pp_metrics['ce']['3']['lost'] += 1
            elif {'name':'Foul Won'} in row['events']:
                pp_metrics['ce']['3']['lost'] += 1
            elif {'name':'Foul Lost'} in row['events']:
                pp_metrics['ce']['3']['lost'] += 1
        elif {'name':'CE 4'} in row['events']:
            pp_metrics['ce']['4']['total'] += 1
            if {'name':'Goal'} in row['events']:
                pp_metrics['ce']['4']['goals'] += 1
            elif {'name':'PC Win'} in row['events']:
                pp_metrics['ce']['4']['pc_win'] += 1
            elif {'name':'GSO'} in row['events']:
                pp_metrics['ce']['4']['gso'] += 1
            elif {'name':'PP Win'} in row['events']:
                pp_metrics['ce']['4']['pp_win'] += 1
            elif {'name':'PP Win '} in row['events']:
                pp_metrics['ce']['4']['pp_win'] += 1
            elif {'name':'Lost'} in row['events']:
                pp_metrics['ce']['4']['lost'] += 1
            elif {'name':'Out of Play'} in row['events']:
                pp_metrics['ce']['4']['lost'] += 1
            elif {'name':'Foul Won'} in row['events']:
                pp_metrics['ce']['4']['lost'] += 1
            elif {'name':'Foul Lost'} in row['events']:
                pp_metrics['ce']['4']['lost'] += 1
        elif {'name':'CE 5'} in row['events']:
            pp_metrics['ce']['5']['total'] += 1
            if {'name':'Goal'} in row['events']:
                pp_metrics['ce']['5']['goals'] += 1
            elif {'name':'PC Win'} in row['events']:
                pp_metrics['ce']['5']['pc_win'] += 1
            elif {'name':'GSO'} in row['events']:
                pp_metrics['ce']['5']['gso'] += 1
            elif {'name':'PP Win'} in row['events']:
                pp_metrics['ce']['5']['pp_win'] += 1
            elif {'name':'PP Win '} in row['events']:
                pp_metrics['ce']['5']['pp_win'] += 1
            elif {'name':'Lost'} in row['events']:
                pp_metrics['ce']['5']['lost'] += 1
            elif {'name':'Out of Play'} in row['events']:
                pp_metrics['ce']['5']['lost'] += 1
            elif {'name':'Foul Won'} in row['events']:
                pp_metrics['ce']['5']['lost'] += 1
            elif {'name':'Foul Lost'} in row['events']:
                pp_metrics['ce']['5']['lost'] += 1
        
        if {'name':'GSO'} in row['events']:
            pp_metrics['gso'] += 1
        if {'name':'Shot On Target'} in row['events']:
            pp_metrics['shots'] += 1
        if {'name':'Saved'} in row['events']:
            pp_metrics['shots'] += 1
        if {'name':'Shot Off Target'} in row['events']:
            pp_metrics['shots'] += 1
        if {'name':'PC Win'} in row['events']:
            pp_metrics['pc_win'] += 1
        if {'name':'PP Win '} in row['events']:
            pp_metrics['pp_win'] += 1
        if {'name':'PP Win'} in row['events']:
            pp_metrics['pp_win'] += 1
        if {'name':'Lost'} in row['events']:
            pp_metrics['lost'] += 1
        if {'name':'Foul Lost'} in row['events']:
            pp_metrics['lost'] += 1
        if {'name':'Foul Won'} in row['events']:
            pp_metrics['lost'] += 1
        if {'name':'Out of Play'} in row['events']:
            pp_metrics['lost'] += 1
        if {'name':'Goal'} in row['events']:
            pp_metrics['goals'] += 1

    return pp_metrics

def calcMetrics(metrics, pp_metrics):
    totalCE = metrics['ce']['1']['total'] + metrics['ce']['2']['total'] + metrics['ce']['3']['total'] + metrics['ce']['4']['total'] + metrics['ce']['5']['total']
    totalPPCE =  pp_metrics['ce']['1']['total'] + pp_metrics['ce']['2']['total'] + pp_metrics['ce']['3']['total'] + pp_metrics['ce']['4']['total'] + pp_metrics['ce']['5']['total']
    if pp_metrics['total'] == 0:
        pp_metrics['PPp'] = 0
        pp_metrics['PPs'] = 0
        pp_metrics['PPf'] = 0
    else:
        pp_metrics['PPp'] = round((totalPPCE + pp_metrics['gso'] + pp_metrics['pc_win'] + pp_metrics['goals']) / pp_metrics['total'], 2)
        pp_metrics['PPs'] = round((pp_metrics['gso'] + pp_metrics['pc_win'] + pp_metrics['goals']) / pp_metrics['total'], 2)
        pp_metrics['PPf'] = round(pp_metrics['lost'] / pp_metrics['total'], 2)

    metrics['oEff'] = (metrics['pp_win'] + pp_metrics['pp_win']) * 2 + (sum(metrics['25e'].values())) * 2 + (totalCE + totalPPCE) * 4 + (metrics['gso'] + pp_metrics['gso']) * 6 + (metrics['pc_win'] + pp_metrics['pc_win']) * 6 + (metrics['goals'] + pp_metrics['goals']) * 10 - metrics['lost'] - pp_metrics['lost']

    metrics['25Eff'] = (metrics['pp_win'] + pp_metrics['pp_win']) + (totalCE + totalPPCE) * 3 + (metrics['gso'] + pp_metrics['gso']) * 6 + (metrics['pc_win'] + pp_metrics['pc_win']) * 6 + (metrics['goals'] + pp_metrics['goals']) * 10 - metrics['lost'] - pp_metrics['lost']

    metrics['ceEff'] = (metrics['gso'] + pp_metrics['gso']) * 6 + (metrics['pc_win'] + pp_metrics['pc_win']) * 6 + (metrics['goals'] + pp_metrics['goals']) * 10 - ((metrics['lost'] + pp_metrics['lost']) * 2)

    return (metrics, pp_metrics)
