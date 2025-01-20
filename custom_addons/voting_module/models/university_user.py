from odoo import models, fields


class UniversityPerson(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(string="Student")
    is_candidate = fields.Boolean(string="Candidate")
    carrera = fields.Char(string="Career")
    sede_id = fields.Many2one('university.sede', string="Sede")

    _sql_constraints = [
        ('unique_identification', 'unique(vat)', "El número de identificación debe ser único."),
    ]
