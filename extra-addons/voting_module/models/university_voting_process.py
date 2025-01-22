from odoo import models, fields


class UniversityVotingProcess(models.Model):
    _name = 'university.voting_process'
    _description = 'Voting Process'

    name = fields.Char(string="Description", required=True)
    start_date = fields.Datetime(string="Start", required=True)
    end_date = fields.Datetime(string="End", required=True)
    candidates = fields.Many2many('res.partner', domain=[('is_candidate', '=', True)], string="Candidates")
    votes = fields.One2many('university.votes', 'voting_process_id', string="Votes")
    state = fields.Selection(
        [('draft', 'Draft'), ('in_progress', 'In progress'), ('closed', 'Closed')],
        default='draft',
        string="State",
    )

    def action_start_voting(self):
        self.state = 'in_progress'

    def action_close_voting(self):
        self.state = 'closed'
