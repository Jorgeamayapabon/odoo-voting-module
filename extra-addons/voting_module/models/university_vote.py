from odoo import models, fields


class UniversityVotes(models.Model):
    _name = 'university.votes'
    _description = 'Votes'

    student_id = fields.Many2one('res.partner', domain=[('is_student', '=', True)], string="Student", required=True)
    voting_process_id = fields.Many2one('university.voting_process', string="Voting process", required=True)
    candidate_id = fields.Many2one('res.partner', domain=[('is_candidate', '=', True)], string="Candidate", required=True)

    _sql_constraints = [
        ('unique_vote_per_student', 'unique(student_id, voting_process_id)', "Each student can only vote once in each process.")
    ]
