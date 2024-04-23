# -*- coding: utf-8 -*-
from odoo import fields, models


class Product(models.Model):
    """Spanish Name Field For POS"""
    _inherit = 'product.product'

    spanish_name = fields.Char()
