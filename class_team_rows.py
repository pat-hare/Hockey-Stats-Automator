# store team rows

class TeamRows:
    def __init__(self, teamName, rows, pprows, goals, EoQ1, EoQ2, EoQ3):
        self.teamName = teamName
        self.goals = goals
        self.EoQ1 = EoQ1
        self.EoQ2 = EoQ2
        self.EoQ3 = EoQ3
        self.rows = rows
        self.rows_Q1 = []
        self.rows_Q2 = []
        self.rows_Q3 = []
        self.rows_Q4 = []
        self.pprows = pprows
        self.pprows_Q1 = []
        self.pprows_Q2 = []
        self.pprows_Q3 = []
        self.pprows_Q4 = []

        self.breakdown_rows()

    def breakdown_rows(self):
        for row in self.rows:
            if row['end'] < EoQ1:
                self.rows_Q1.append(row)
            elif row['end'] < EoQ2 and row['end'] >= EoQ1:
                self.rows_Q2.append(row)
            elif row['end'] < EoQ3 and row['end'] >= EoQ2:
                self.rows_Q3.append(row)
            elif row['end'] >= EoQ3:
                self.rows_Q4.append(row)

        for row in self.pprows:
            if row['end'] < EoQ1:
                self.pprows_Q1.append(row)
            elif row['end'] < EoQ2 and row['end'] >= EoQ1:
                self.pprows_Q2.append(row)
            elif row['end'] < EoQ3 and row['end'] >= EoQ2:
                self.pprows_Q3.append(row)
            elif row['end'] >= EoQ3:
                self.pprows_Q4.append(row)