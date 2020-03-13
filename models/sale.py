from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    note = fields.Html(string='Terms and conditions', default=_default_note)
