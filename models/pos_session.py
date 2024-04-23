# -*- coding: utf-8 -*-
from odoo import models


class PosSession(models.Model):
    """POS session """
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        """ Included New Field In POS"""
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('spanish_name')
        return result

    # def _pos_ui_models_to_load(self):
    #     res = super()._pos_ui_models_to_load()
    #     res.append('students.registration')
    #     return res
