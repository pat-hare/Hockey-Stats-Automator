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

def addRowToMetrics(team, home, away, fg, q1, q2, q3, q4):
    teamId = getTeamID(team)
    matchId = getMatchID(home, away)
    total25EFG = fg['25e']['L'] + fg['25e']['C'] + fg['25e']['R']
    total25EQ1 = q1['25e']['L'] + q1['25e']['C'] + q1['25e']['R']
    total25EQ2 = q2['25e']['L'] + q2['25e']['C'] + q2['25e']['R']
    total25EQ3 = q3['25e']['L'] + q3['25e']['C'] + q3['25e']['R']
    total25EQ4 = q4['25e']['L'] + q4['25e']['C'] + q4['25e']['R']
    totalCEFG = fg['ce']['1'] + fg['ce']['2'] + fg['ce']['3'] + fg['ce']['4'] + fg['ce']['5']
    totalCEQ1 = q1['ce']['1'] + q1['ce']['2'] + q1['ce']['3'] + q1['ce']['4'] + q1['ce']['5']
    totalCEQ2 = q2['ce']['1'] + q2['ce']['2'] + q2['ce']['3'] + q2['ce']['4'] + q2['ce']['5']
    totalCEQ3 = q3['ce']['1'] + q3['ce']['2'] + q3['ce']['3'] + q3['ce']['4'] + q3['ce']['5']
    totalCEQ4 = q4['ce']['1'] + q4['ce']['2'] + q4['ce']['3'] + q4['ce']['4'] + q4['ce']['5']

    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO metrics ([MatchID],[TeamID],[Goals],[Goals-Q1],[Goals-Q2],[Goals-Q3],[Goals-Q4],[Shots-FG],[Shots-Q1],[Shots-Q2],[Shots-Q3],[Shots-Q4],[GSO-FG],[GSO-Q1],[GSO-Q2],[GSO-Q3],[GSO-Q4],[25E-FG],[25E-L],[25E-C],[25E-R],[25E-Q1],[25E-Q2],[25E-Q3],[25E-Q4],[CE-FG],[CE-1],[CE-2],[CE-3],[CE-4],[CE-5],[CE-Q1],[CE-Q2],[CE-Q3],[CE-Q4],[OEff],[OEff-Q1],[OEff-Q2],[OEff-Q3],[OEff-Q4],[25Eff],[25Eff-Q1],[25Eff-Q2],[25Eff-Q3],[25Eff-Q4],[CEff],[CEff-Q1],[CEff-Q2],[CEff-Q3],[CEff-Q4],[DefAcc],[DefAcc-Q1],[DefAcc-Q2],[DefAcc-Q3],[DefAcc-Q4],[Poss-FG],[Poss-Q1],[Poss-Q2],[Poss-Q3],[Poss-Q4],[16s],[16sTo25E]) 
        
        VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')
    ''' % (matchId,teamId,fg['goals'],q1['goals'],q2['goals'],q3['goals'],q4['goals'],fg['shots'],q1['shots'],q2['shots'],q3['shots'],q4['shots'],fg['gso'],q1['gso'],q2['gso'],q3['gso'],q4['gso'],total25EFG,fg['25e']['L'],fg['25e']['C'],fg['25e']['R'],total25EQ1,total25EQ2,total25EQ3,total25EQ4,totalCEFG,fg['ce']['1'],fg['ce']['2'],fg['ce']['3'],fg['ce']['4'],fg['ce']['5'],totalCEQ1,totalCEQ2,totalCEQ3,totalCEQ4,fg['oEff'],q1['oEff'],q2['oEff'],q3['oEff'],q4['oEff'],fg['25Eff'],q1['25Eff'],q2['25Eff'],q3['25Eff'],q4['25Eff'],fg['ceEff'],q1['ceEff'],q2['ceEff'],q3['ceEff'],q4['ceEff'],0,0,0,0,0,fg['possession_time'],q1['possession_time'],q2['possession_time'],q3['possession_time'],q4['possession_time']))
   
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
