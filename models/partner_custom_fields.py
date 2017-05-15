# -*- coding: utf-8 -*-
from openerp import api, fields, models
# Aqui se importan los paquetes que necesites, en orden alfabético
#
# El nombre de la clase en notación CamelCase.
# La clases que se usan para extender los modelos, son modelos en sí mismos, por tanto heredan de models.Model
# En la version anterior de la API se usaba osv.osv.
#

class PartnerCustomFields(models.Model):
  _inherit = "res.partner"

  neuro_domicilio_fiscal  = fields.Char(string="Domicilio Fiscal", help="Domicilio Fiscal de la empresa")
  neuro_rfc               = fields.Char(string="RFC", help="RFC de la empresa")
  neuro_razon_social      = fields.Char(string="Razón Social", help="Razón Social de la empresa")
  neuro_especialidad      = fields.Many2many('neuro.especialidad')

  class neuroEspecialidad (models.Model):
    _name = 'neuro.especialidad'
    name  = fields.Char('Especialidad', required=True)