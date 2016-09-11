# -*- coding: utf-8 -*-

from openerp import models,fields,api
from openerp.tools.translate import _


class is_mold_project(models.Model):
    _name='is.mold.project'
    _order='name'    #Ordre de tri par defaut des listes
    _sql_constraints = [('name_uniq','UNIQUE(name)', 'Ce projet existe déjà')]

    name           = fields.Char("Code",size=20,required=True, select=True)
    client_id      = fields.Many2one('res.partner', 'Client')
    chef_projet_id = fields.Many2one('res.users', 'Chef de projet')
    mold_ids       = fields.One2many('is.mold', 'project', u"Moules")


    def copy(self, cr, uid, id, default=None, context=None):
        if not context:
            context = {}

        project = self.read(cr, uid, id, ['name'], context=context)
        default.update({
            'name': project['name'] + _(' (copy)'),
        })
        return super(is_mold_project, self).copy(cr, uid, id, default=default,
            context=context)


