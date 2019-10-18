# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.

from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    @api.depends('state', 'price_reduce', 'product_id', 'untaxed_amount_invoiced', 'qty_delivered','discount')
    def _onchange_discount(self):
        self.discount = discount
        
                
