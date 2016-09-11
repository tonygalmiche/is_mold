# -*- coding: utf-8 -*-

from openerp import models,fields,api
from openerp.tools.translate import _


class is_dossierf(models.Model):
    _name='is.dossierf'
    _order='name'    #Ordre de tri par defaut des listes
    _sql_constraints = [('name_uniq','UNIQUE(name)', u'Ce Dossier F existe déjà !')] 

    name            = fields.Char("N°Dossier",size=20,required=True, select=True)
    designation     = fields.Char("Désignation")
    project         = fields.Many2one('is.mold.project', 'Projet')
    client_id       = fields.Many2one('res.partner', 'Client'        , store=True, compute='_compute')
    chef_projet_id  = fields.Many2one('res.users'  , 'Chef de projet', store=True, compute='_compute')
    mold_ids        = fields.One2many('is.mold', 'dossierf_id', u"Moules")


    @api.depends('project','project.client_id','project.chef_projet_id')
    def _compute(self):
        for obj in self:
            if obj.project:
                obj.client_id      = obj.project.client_id
                obj.chef_projet_id = obj.project.chef_projet_id


    def copy(self, cr, uid, id, default=None, context=None):
        if not context:
            context = {}
        mold = self.read(cr, uid, id, ['name'], context=context)
        default.update({
            'name': mold['name'] + _(' (copy)'),
        })
        return super(is_mold, self).copy(cr, uid, id, default=default, context=context)



