# -*- coding: utf-8 -*-
# Part of flectra. See LICENSE file for full copyright and licensing details.

from flectra import fields, models


class IrBranchCompanyMixin(models.AbstractModel):
    _name = "ir.branch.company.mixin"

    branch_id = fields.Many2one(
        'res.branch', 'Branch', ondelete="restrict",
        default=lambda self: self.env.user._get_default_branch())
    company_id = fields.Many2one(
        'res.company', 'Company', ondelete="restrict",
        default=lambda self: self.env.user.company_id)
