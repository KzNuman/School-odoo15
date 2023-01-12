from odoo import api, fields, models, _

class Section(models.Model):
    _name = 'school.section'
    _description = 'section'
    id = fields.Integer('Section Id')
    name = fields.Char('Section Name', reqired=True)
    code = fields.Char('Code')
