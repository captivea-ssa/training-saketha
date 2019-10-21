# coding: utf-8
# Part of CAPTIVEA. Odoo 12 EE.

from odoo import fields, models,api


class Sale_Order_Line_custom(models.Model):
    _name = 'sale.order.line.custom'
    _inherit = 'sale.order.line'
    customdiscount = fields.Boolean(string = 'Custom Discount class')

    @api.model
    @api.onchange('product_id', 'price_unit', 'product_uom', 'product_uom_qty', 'tax_id')
    def _onchange_discount(self)
        res = super(Sale_Order_Line_custom, self)._onchange_discount()
        self['discount'] = 55.0
        self['customdiscount'] = true
        print('did the custom class execute {}', self['customdiscount'])
        return res
