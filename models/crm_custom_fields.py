# -*- coding: utf-8 -*-

from datetime import datetime, date, time
from openerp import api, fields, models

class CrmCustomFields(models.Model):
  _inherit = "crm.lead"

  neuro_fecha_de_cita  = fields.Date('Fecha de Cita')
  neuro_seguimiento    = fields.Char(string="Número de seguimiento")
  neuro_canal          = fields.Selection(selection=[('formulario','Formulario'),('telefono', 'Teléfono'),('email', 'Email'),('facebook', 'Facebook'),('linkedin', 'Linkedin')], string ='Canal',  help="Canal por el cual llegó la oportunidad")
  neuro_origen         = fields.Many2one(comodel_name = 'neuro.origen', string ='Origen',  help="Origen de la oportunidad")
  neuro_evento         = fields.Many2one(comodel_name = 'neuro.evento', string ='Evento')
  neuro_servicios      = fields.Many2many('neuro.servicios')
  neuro_productos      = fields.Many2many('neuro.productos')
  tengo = fields.Char()

  def on_change_price(self,cr,uid,ids,tengo,context=None):
  #Calculate the total
    fuente=self.pool.get('crm.tracking.source').browse(cr, uid, tengo, context).name
    res = {'value': {'tengo': fuente}}
    #Return the values to update it in the view.
    return res


class neuroServicios(models.Model):
	_name = 'neuro.servicios'
	name  = fields.Char('Servicios', required=True)

class neuroProductos(models.Model):
    _name = 'neuro.productos'
    name  = fields.Char('Productos', required=True)

class neuroEvento(models.Model):
    _name = 'neuro.evento'
    name  = fields.Char('evento', required=True)

class neuroOrigen(models.Model):
	_name = 'neuro.origen'
	name  = fields.Char('Origen', required=True)





#crm_custom_fields()
