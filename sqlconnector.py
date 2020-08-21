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
        INSERT INTO metrics ([MatchID],[TeamID],[Goals],[Goals-Q1],[Goals-Q2],[Goals-Q3],[Goals-Q4],[Shots-FG],[Shots-Q1],[Shots-Q2],[Shots-Q3],[Shots-Q4],[GSO-FG],[GSO-Q1],[GSO-Q2],[GSO-Q3],[GSO-Q4],[25E-FG],[25E-L],[25E-C],[25E-R],[25E-Q1],[25E-Q2],[25E-Q3],[25E-Q4],[CE-FG],[CE-1],[CE-2],[CE-3],[CE-4],[CE-5],[CE-Q1],[CE-Q2],[CE-Q3],[CE-Q4],[OEff],[OEff-Q1],[OEff-Q2],[OEff-Q3],[OEff-Q4],[25Eff],[25Eff-Q1],[25Eff-Q2],[25Eff-Q3],[25Eff-Q4],[CEff],[CEff-Q1],[CEff-Q2],[CEff-Q3],[CEff-Q4],[DefAcc],[DefAcc-Q1],[DefAcc-Q2],[DefAcc-Q3],[DefAcc-Q4],[Poss-FG],[Poss-Q1],[Poss-Q2],[Poss-Q3],[Poss-Q4]) 
        
        VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')
    ''' % (matchId,teamId,fg['goals'],q1['goals'],q2['goals'],q3['goals'],q4['goals'],fg['shots'],q1['shots'],q2['shots'],q3['shots'],q4['shots'],fg['gso'],q1['gso'],q2['gso'],q3['gso'],q4['gso'],total25EFG,fg['25e']['L'],fg['25e']['C'],fg['25e']['R'],total25EQ1,total25EQ2,total25EQ3,total25EQ4,totalCEFG,fg['ce']['1'],fg['ce']['2'],fg['ce']['3'],fg['ce']['4'],fg['ce']['5'],totalCEQ1,totalCEQ2,totalCEQ3,totalCEQ4,fg['oEff'],q1['oEff'],q2['oEff'],q3['oEff'],q4['oEff'],fg['25Eff'],q1['25Eff'],q2['25Eff'],q3['25Eff'],q4['25Eff'],fg['ceEff'],q1['ceEff'],q2['ceEff'],q3['ceEff'],q4['ceEff'],0,0,0,0,0,fg['possession_time'],q1['possession_time'],q2['possession_time'],q3['possession_time'],q4['possession_time']))
   

    conn.commit()
