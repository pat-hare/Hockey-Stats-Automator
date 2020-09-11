import pyodbc
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP;"
                      "Database=db_hockey;"
                      "Trusted_Connection=yes;")

def getTeamID(team):
    teamId = 0

    cursor = conn.cursor()
    cursor.execute("SELECT TeamID FROM teams WHERE TeamName = '" + team + "'")
    for row in cursor:
        teamId = row[0]

    return teamId

def getMatchID(home, away):
    homeId = 0
    awayId = 0
    matchId = 0

    cursor = conn.cursor()
    cursor.execute("SELECT TeamID FROM teams WHERE TeamName = '" + home + "'")
    for row in cursor:
        homeId = row[0]

    cursor.execute("SELECT TeamID FROM teams WHERE TeamName = '" + away + "'")
    for row in cursor:
        awayId = row[0]

    cursor.execute("SELECT MatchID FROM fixtures WHERE Home = '" + str(homeId) + "' AND Away = '" + str(awayId) + "'")

    for row in cursor:
        matchId = row[0]

    return matchId

def getSeasonTurnovers():
    data = {
        '1.0': {},
        '1.1': {},
        '1.2': {},
        '1.3': {},
        '2.0': {},
        '2.1': {},
        '2.2': {},
        '2.3': {},
        '3.0': {},
        '3.1': {},
        '3.2': {},
        '3.3': {},
        '4.0': {},
        '4.1': {},
        '4.2': {},
        '4.3': {},
    }
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM turnovers")
    for row in cursor:
        zone = row[1]
        if 'PositiveWins' not in data[zone]:
            data[zone]['PositiveWins']: row[3]
        else:
            data[zone]['PositiveWins'] += row[3]
        
        if 'TotalWins' not in data[zone]:
            data[zone]['TotalWins']: row[2]
        else:
            data[zone]['TotalWins'] += row[2]
        
        if 'GSOs' not in data[zone]:
            data[zone]['GSOs']: row[4]
        else:
            data[zone]['GSOs'] += row[4]

    return data

def getSeasonPCShots():
    data = {
        'for': {},
        'against': {}
    }

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pc_shot_map")
    for row in cursor:
        zone = row[2]
        if row[1] == 6:
            if zone not in data['for']:
                data['for'][zone]: {
                    'total': 0,
                    'saved': 0,
                    'blocked': 0,
                    'conceded': 0
                }
            
            data['for'][zone]['total'] += 1

            if row[3] == 1 and row[4] == 0 and row[5] == 0:
                data['for'][zone]['conceded'] += 1
            elif row[4] == 1:
                data['for'][zone]['saved'] += 1
            elif row[5] == 1:
                data['for'][zone]['blocked'] += 1
        else:
            if zone not in data['against']:
                data['against'][zone]: {
                    'total': 0,
                    'saved': 0,
                    'blocked': 0,
                    'conceded': 0
                }
            
            data['against'][zone]['total'] += 1

            if row[3] == 1 and row[4] == 0 and row[5] == 0:
                data['against'][zone]['conceded'] += 1
            elif row[4] == 1:
                data['against'][zone]['saved'] += 1
            elif row[5] == 1:
                data['against'][zone]['blocked'] += 1
    
    return data

def getSeasonMetricsAverage():
    data = {
        '16sTo25E': 0,
        '25EToCE': 0,
        'CEToGSO': 0,
        'GSOToGoal': 0,
        'DeepDToCE': 0,
        'DeepDToGSO': 0,
        'DeepDToGoal': 0,
    }
    cursor = conn.cursor()

    cursor.execute('''
        SELECT 
            AVG([16sTo25E]) AS [16sTo25E],
            (AVG([CE-FG])/AVG([25E-FG])) AS [25EToCE],
            (AVG([GSO-FG])/AVG([CE-FG])) AS [CEToGSO],
            (AVG([Goals])/AVG([GSO-FG])) AS [GSOToGoal]
        FROM [db_hockey].[dbo].[metrics]
        WHERE TeamID = 6
    ''')
    for row in cursor:
        data['16sTo25E'] = row[0]
        data['25EToCE'] = row[1]
        data['CEToGSO'] = row[2]
        data['GSOToGoal'] = row[3]

    cursor.execute('''
        SELECT 
            ([CE]/[PP_Count]) AS [DeepDToCE],
            ([GSO]/[PP_Count]) AS [DeepDToGSO],
            ([Goals]/[PP_Count]) AS [DeepDToGoal]
        FROM [db_hockey].[dbo].[pp_metrics]
        WHERE TeamID = 6
    ''')
    for row in cursor:
        data['DeepDToCE'] = row[0]
        data['DeepDToGSO'] = row[1]
        data['DeepDToGoal'] = row[2]

    return data

def getMetricsFromLastGame(team):
    teamID = getTeamID(team)
    data = {
        '16sTo25E': 0,
        '25EToCE': 0,
        'CEToGSO': 0,
        'GSOToGoal': 0,
        'DeepDToCE': 0,
        'DeepDToGSO': 0,
        'DeepDToGoal': 0,
    }
    cursor = conn.cursor()

    cursor.execute('''
        SELECT 
            AVG([16sTo25E]) AS [16sTo25E],
            (AVG([CE-FG])/AVG([25E-FG])) AS [25EToCE],
            (AVG([GSO-FG])/AVG([CE-FG])) AS [CEToGSO],
            (AVG([Goals])/AVG([GSO-FG])) AS [GSOToGoal]
        FROM [db_hockey].[dbo].[metrics]
        WHERE TeamID = %s
    ''' % (teamID))
    for row in cursor:
        data['16sTo25E'] = row[0]
        data['25EToCE'] = row[1]
        data['CEToGSO'] = row[2]
        data['GSOToGoal'] = row[3]

    cursor.execute('''
        SELECT 
            ([CE]/[PP_Count]) AS [DeepDToCE],
            ([GSO]/[PP_Count]) AS [DeepDToGSO],
            ([Goals]/[PP_Count]) AS [DeepDToGoal]
        FROM [db_hockey].[dbo].[pp_metrics]
        WHERE TeamID = %s
    ''' % (teamID))
    for row in cursor:
        data['DeepDToCE'] = row[0]
        data['DeepDToGSO'] = row[1]
        data['DeepDToGoal'] = row[2]

    return data

def addRowToMetrics(team, home, away, metrics):
    teamId = getTeamID(team)
    matchId = getMatchID(home, away)
    total25EFG = metrics.metrics_fg['25e']['L'] + metrics.metrics_fg['25e']['C'] + metrics.metrics_fg['25e']['R']
    total25EQ1 = metrics.metrics_q1['25e']['L'] + metrics.metrics_q1['25e']['C'] + metrics.metrics_q1['25e']['R']
    total25EQ2 = metrics.metrics_q2['25e']['L'] + metrics.metrics_q2['25e']['C'] + metrics.metrics_q2['25e']['R']
    total25EQ3 = metrics.metrics_q3['25e']['L'] + metrics.metrics_q3['25e']['C'] + metrics.metrics_q3['25e']['R']
    total25EQ4 = metrics.metrics_q4['25e']['L'] + metrics.metrics_q4['25e']['C'] + metrics.metrics_q4['25e']['R']
    totalCEFG = metrics.metrics_fg['ce']['1']['total'] + metrics.metrics_fg['ce']['2']['total'] + metrics.metrics_fg['ce']['3']['total'] + metrics.metrics_fg['ce']['4']['total'] + metrics.metrics_fg['ce']['5']['total']
    totalCEQ1 = metrics.metrics_q1['ce']['1']['total'] + metrics.metrics_q1['ce']['2']['total'] + metrics.metrics_q1['ce']['3']['total'] + metrics.metrics_q1['ce']['4']['total'] + metrics.metrics_q1['ce']['5']['total']
    totalCEQ2 = metrics.metrics_q2['ce']['1']['total'] + metrics.metrics_q2['ce']['2']['total'] + metrics.metrics_q2['ce']['3']['total'] + metrics.metrics_q2['ce']['4']['total'] + metrics.metrics_q2['ce']['5']['total']
    totalCEQ3 = metrics.metrics_q3['ce']['1']['total'] + metrics.metrics_q3['ce']['2']['total'] + metrics.metrics_q3['ce']['3']['total'] + metrics.metrics_q3['ce']['4']['total'] + metrics.metrics_q3['ce']['5']['total']
    totalCEQ4 = metrics.metrics_q4['ce']['1']['total'] + metrics.metrics_q4['ce']['2']['total'] + metrics.metrics_q4['ce']['3']['total'] + metrics.metrics_q4['ce']['4']['total'] + metrics.metrics_q4['ce']['5']['total']

    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO metrics ([MatchID],[TeamID],[Goals],[Goals-Q1],[Goals-Q2],[Goals-Q3],[Goals-Q4],[Shots-FG],[Shots-Q1],[Shots-Q2],[Shots-Q3],[Shots-Q4],[GSO-FG],[GSO-Q1],[GSO-Q2],[GSO-Q3],[GSO-Q4],[25E-FG],[25E-L],[25E-C],[25E-R],[25E-Q1],[25E-Q2],[25E-Q3],[25E-Q4],[CE-FG],[CE-1],[CE-2],[CE-3],[CE-4],[CE-5],[CE-Q1],[CE-Q2],[CE-Q3],[CE-Q4],[OEff],[OEff-Q1],[OEff-Q2],[OEff-Q3],[OEff-Q4],[25Eff],[25Eff-Q1],[25Eff-Q2],[25Eff-Q3],[25Eff-Q4],[CEff],[CEff-Q1],[CEff-Q2],[CEff-Q3],[CEff-Q4],[DefAcc],[DefAcc-Q1],[DefAcc-Q2],[DefAcc-Q3],[DefAcc-Q4],[Poss-FG],[Poss-Q1],[Poss-Q2],[Poss-Q3],[Poss-Q4],[16s],[16sTo25E]) 
        
        VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')
    ''' % (matchId,teamId,metrics.metrics_fg['goals'],metrics.metrics_q1['goals'],metrics.metrics_q2['goals'],metrics.metrics_q3['goals'],metrics.metrics_q4['goals'],metrics.metrics_fg['shots'],metrics.metrics_q1['shots'],metrics.metrics_q2['shots'],metrics.metrics_q3['shots'],metrics.metrics_q4['shots'],metrics.metrics_fg['gso'],metrics.metrics_q1['gso'],metrics.metrics_q2['gso'],metrics.metrics_q3['gso'],metrics.metrics_q4['gso'],total25EFG,metrics.metrics_fg['25e']['L'],metrics.metrics_fg['25e']['C'],metrics.metrics_fg['25e']['R'],total25EQ1,total25EQ2,total25EQ3,total25EQ4,totalCEFG,metrics.metrics_fg['ce']['1'],metrics.metrics_fg['ce']['2'],metrics.metrics_fg['ce']['3'],metrics.metrics_fg['ce']['4'],metrics.metrics_fg['ce']['5'],totalCEQ1,totalCEQ2,totalCEQ3,totalCEQ4,metrics.metrics_fg['oEff'],metrics.metrics_q1['oEff'],metrics.metrics_q2['oEff'],metrics.metrics_q3['oEff'],metrics.metrics_q4['oEff'],metrics.metrics_fg['25Eff'],metrics.metrics_q1['25Eff'],metrics.metrics_q2['25Eff'],metrics.metrics_q3['25Eff'],metrics.metrics_q4['25Eff'],metrics.metrics_fg['ceEff'],metrics.metrics_q1['ceEff'],metrics.metrics_q2['ceEff'],metrics.metrics_q3['ceEff'],metrics.metrics_q4['ceEff'],0,0,0,0,0,metrics.metrics_fg['possession_time'],metrics.metrics_q1['possession_time'],metrics.metrics_q2['possession_time'],metrics.metrics_q3['possession_time'],metrics.metrics_q4['possession_time'],0,0))
   
    conn.commit()

def addTurnovers(data):
    cursor = conn.cursor()
    for row in data:
        cursor.execute('''
            INSERT INTO turnovers ([MatchID],[ZoneID],[TotalWins],[PositiveWins])

            VALUES ('%s','%s','%s','%s')
        ''' % (row[0],row[1],row[2],row[3]))
    
    conn.commit()

def addPPMetrics(data):
    cursor = conn.cursor()
    for row in data:
        cursor.execute('''
            INSERT INTO pp_metrics ([MatchID],[TeamID],[PP_Count],[CE],[GSO],[Goals])

            VALUES ('%s','%s','%s','%s','%s','%s')
        ''' % (row[0],row[1],row[2],row[3],row[4],row[5]))
    
    conn.commit()

def addPCShots(data):
    cursor = conn.cursor()
    for row in data:
        if len(row) == 4:
            cursor.execute('''
                INSERT INTO pc_shot_map ([MatchID],[TeamID],[ZoneID],[OnTarget])

                VALUES ('%s','%s','%s','%s')
            ''' % (row[0],row[1],row[2],row[3]))
        else:
            cursor.execute('''
                INSERT INTO pc_shot_map ([MatchID],[TeamID],[ZoneID],[OnTarget],[Saved],[Blocked])

                VALUES ('%s','%s','%s','%s','%s','%s')
            ''' % (row[0],row[1],row[2],row[3],row[4],row[5]))
    
    conn.commit()

def addShots(data):
    cursor = conn.cursor()
    for row in data:
        cursor.execute('''
            INSERT INTO shot_map ([MatchID],[TeamID],[CircleEntry],[ShotZone],[OnTarget],[TypeOfShot],[PlayerID])

            VALUES ('%s','%s','%s','%s','%s','%s','%s')
        ''' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

    conn.commit()

def addPlayerData(data):
    cursor = conn.cursor()
    for row in data:
        cursor.execute('''
                INSERT INTO player_scores ([MatchID],[PlayerID],[EfficiencyScore])

                VALUES ('%s','%s','%s')
            ''' % (row[0],row[1],row[2],row[3]))
    
    conn.commit()
