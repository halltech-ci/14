from odoo import models, fields, api
#from datetime import date 

class bulletin(models.Model):
      _inherit = "hr.employee"
        
      hiring_date=fields.Date(string="Date Embauche", required=True, default=fields.Date.today ,store=True)
      #seniority=fields.Integer(string="Anciennete",compute='_convert',store=True)
      hiring_end=fields.Date(string="Date de Fin", required=True, default=fields.Date.today,store=True)
      matricule=fields.Char(string="Matricule",store=True)
      n_cnps=fields.Char(string="N° CNPS",store=True)
      n_part=fields.Char(string="Nombre de Part",store=True)
    
    
    #@api.depends('hiring_date')
    #def _calcul(self):
        #date=date.today()
        #Seniority=hiring_date - date
             