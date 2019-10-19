# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.

from odoo import fields, models,api


class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    def onchange_discount(self)
        #values = super(SaleOrderLineCustom, self).onchange_discount()
        values.discount =55
        return values   
        
                
