from odoo import models, fields


class VotingImportWizard(models.TransientModel):
    _name = 'university.voting_import_wizard'
    _description = 'Import Voting Processes'

    file = fields.Binary(string="File")
    template = fields.Binary(string="Template", readonly=True, default=lambda self: self._default_template())

    def _default_template(self):
        return b"id,name,start_date,end_date,candidates\n"

    def action_import(self):
        # Import logic goes here
        pass
