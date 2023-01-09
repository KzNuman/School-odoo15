from odoo import api, fields, models, _

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'teacher'
    name = fields.Char('Teacher Name', reqired=True)
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    birth_date = fields.Date('Date of Birth')
    gender = fields.Selection('Gender', [('M','Male'), ('F','Female')])