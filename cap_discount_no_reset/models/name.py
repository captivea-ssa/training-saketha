# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.

from odoo import fields, models,api


class DiscountModify(SaleOrderLine):
    #@api.depends('state', 'price_reduce', 'product_id', 'untaxed_amount_invoiced', 'qty_delivered','discount')
    #def _onchange_discount(self):
     #   self.discount = discount
    @api.onchange('product_id', 'price_unit', 'product_uom', 'product_uom_qty', 'tax_id')
    def _onchange_discount(self):
        if self.product_id and self.product_uom_qty>0
            self.discount = 25
        
        
                
