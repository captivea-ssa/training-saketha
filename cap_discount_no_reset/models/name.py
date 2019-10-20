# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.

from odoo import fields, models,api


class Sale_Order_Line(models.Model):
    _inherit = 'sale.order.line'
    @api.model
    @api.onchange('product_id', 'price_unit', 'product_uom', 'product_uom_qty', 'tax_id')
    def _onchange_discount(self)
        #record = super(Sale_Order_Line, self)._onchange_discount()
        self['discount'] =55.0
        return self   
        
        
                
