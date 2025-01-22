from odoo import models, fields


class UniversitySede(models.Model):
    _name = 'university.sede'
    _description = 'University Sede'

    name = fields.Char(string="Name", required=True)
    country = fields.Many2one('res.country', string="Country")
    timezone = fields.Selection(
        [
            ('GMT-5', 'GMT-5'),
            ('GMT-4', 'GMT-4'),
            ('GMT-3', 'GMT-3'),
        ],
        string="Timezone",
        required=True
    )
