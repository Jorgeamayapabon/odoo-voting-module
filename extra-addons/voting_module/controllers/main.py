from odoo import http
from odoo.http import request

class UniversityVotingController(http.Controller):
    @http.route('/vote', type='http', auth='public', methods=['POST'], csrf=True)
    def submit_vote(self, **post):
        candidate_id = int(post.get('candidate_id'))
        student_id = request.env.user.partner_id.id
        voting_process = request.env['university.voting_process'].search([('state', '=', 'in_progress')], limit=1)

        if not voting_process:
            return request.render('university_voting.student_voting_page', {'error': "No hay votaciones activas."})

        try:
            request.env['university.votes'].create({
                'student_id': student_id,
                'voting_process_id': voting_process.id,
                'candidate_id': candidate_id
            })
        except Exception as e:
            return request.render('university_voting.student_voting_page', {'error': str(e)})

        return request.redirect('/thank_you')

    @http.route('/thank_you', type='http', auth='public', website=True)
    def thank_you(self):
        return "<h1>Gracias por tu voto!</h1>"
    