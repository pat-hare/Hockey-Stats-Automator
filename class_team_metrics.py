# store team data
from metrics_calc import basic_metrics_calc, pp_metrics_calc, calcMetrics

class TeamMetrics:
    def __init__(self, team):
        self.team = team
        self.metrics_fg = {}
        self.metrics_q1 = {}
        self.metrics_q2 = {}
        self.metrics_q3 = {}
        self.metrics_q4 = {}
        self.pp_metrics_fg = {}
        self.pp_metrics_q1 = {}
        self.pp_metrics_q2 = {}
        self.pp_metrics_q3 = {}
        self.pp_metrics_q4 = {}

        self.createMetrics()

    def createMetrics(self):
        self.metrics_fg = basic_metrics_calc(self.team.rows)
        self.metrics_q1 = basic_metrics_calc(self.team.rows_Q1)
        self.metrics_q2 = basic_metrics_calc(self.team.rows_Q2)
        self.metrics_q3 = basic_metrics_calc(self.team.rows_Q3)
        self.metrics_q4 = basic_metrics_calc(self.team.rows_Q4)
        
        self.pp_metrics_fg = pp_metrics_calc(self.team.pprows)
        self.pp_metrics_q1 = pp_metrics_calc(self.team.pprows_Q1)
        self.pp_metrics_q2 = pp_metrics_calc(self.team.pprows_Q2)
        self.pp_metrics_q3 = pp_metrics_calc(self.team.pprows_Q3)
        self.pp_metrics_q4 = pp_metrics_calc(self.team.pprows_Q4)

        self.metrics_fg, self.pp_metrics_fg = calcMetrics(self.metrics_fg, self.pp_metrics_fg)
        self.metrics_q1, self.pp_metrics_q1 = calcMetrics(self.metrics_q1, self.pp_metrics_q1)
        self.metrics_q2, self.pp_metrics_q2 = calcMetrics(self.metrics_q2, self.pp_metrics_q2)
        self.metrics_q3, self.pp_metrics_q3 = calcMetrics(self.metrics_q3, self.pp_metrics_q3)
        self.metrics_q4, self.pp_metrics_q4 = calcMetrics(self.metrics_q4, self.pp_metrics_q4)

