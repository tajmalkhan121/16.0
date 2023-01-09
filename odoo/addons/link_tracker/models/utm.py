# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class UtmCampaign(models.Model):
    _inherit = ['utm.campaign']
    _description = 'UTM Campaign'

    click_count = fields.Integer(string="Number of clicks generated by the campaign", compute="_compute_clicks_count")

    def _compute_clicks_count(self):
        click_data = self.env['link.tracker.click']._read_group(
            [('campaign_id', 'in', self.ids)],
            ['campaign_id'], ['campaign_id'])

        mapped_data = {datum['campaign_id'][0]: datum['campaign_id_count'] for datum in click_data}

        for campaign in self:
            campaign.click_count = mapped_data.get(campaign.id, 0)