# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from flectra import fields, models


class IrBranchCompanyMixin(models.AbstractModel):
    _name = "ir.branch.company.mixin"

    branch_id = fields.Many2one(
        'res.branch', 'Branch', ondelete="restrict",
        default=lambda self: self.env.user.default_branch_id)
    company_id = fields.Many2one(
        'res.company', 'Company', ondelete="restrict",
        default=lambda self: self.env.user.company_id)
