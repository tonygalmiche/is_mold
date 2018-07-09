# -*- coding: utf-8 -*-

from openerp import models,fields,api
from openerp.tools.translate import _
import datetime


class is_mold(models.Model):
    _name='is.mold'
    _order='name'    #Ordre de tri par defaut des listes
    _sql_constraints = [('name_uniq','UNIQUE(name)', 'Ce moule existe deja')] #ATTENTION : Ne pas mettre d'accent dans le message

    name             = fields.Char("N°Moule",size=40,required=True, select=True)
    designation      = fields.Char("Désignation")
    project          = fields.Many2one('is.mold.project', 'Projet')
    client_id        = fields.Many2one('res.partner', 'Client'        , store=True, compute='_compute')
    chef_projet_id   = fields.Many2one('res.users'  , 'Chef de projet', store=True, compute='_compute')
    dossierf_id      = fields.Many2one('is.dossierf', 'Dossier F')
    nb_empreintes    = fields.Char("Nb empreintes", help="Nombre d'empreintes du moule (Exemple : 1+1)")
    moule_a_version  = fields.Selection([('oui', u'Oui'),('non', u'Non')], "Moule à version")
    lieu_changement  = fields.Selection([('sur_presse', u'sur presse'),('en_mecanique', u'en mécanique')], "Lieu de changement")
    temps_changement = fields.Float("Temps de changement de la version (H)")
    date_creation    = fields.Date("Date de création")
    date_fin         = fields.Date("Date de fin")
    mouliste_id      = fields.Many2one('res.partner', 'Mouliste')
    carcasse         = fields.Char("Carcasse")
    emplacement      = fields.Char("Emplacement")
    type_dateur      = fields.Selection([
        ('dateur_grille', u'dateur à grille'),
        ('dateur_laiton', u'dateur laiton'),
        ('dateur_fleche', u'dateur à fleche')], "Type de dateur")
    date_peremption  = fields.Date("Date de péremption")
    qt_dans_moule    = fields.Integer("Quantité dans le moule")
    diametre_laiton  = fields.Selection([
            ('d3' , u'Ø3'),
            ('d4' , u'Ø4'),
            ('d5' , u'Ø5'),
            ('d6' , u'Ø6'),
            ('d8' , u'Ø8'),
            ('d10', u'Ø10'),
            ('d12', u'Ø12'),
        ], "Diamètre dateur laiton")
    diametre_fleche  = fields.Selection([
            ('d4' , u'Ø4'),
            ('d5' , u'Ø5'),
            ('d6' , u'Ø6'),
            ('d8' , u'Ø8'),
            ('d10', u'Ø10'),
            ('d12', u'Ø12'),
            ('d14', u'Ø14'),
            ('d16', u'Ø16'),
            ('d18', u'Ø18'),
            ('d20', u'Ø20'),
        ], "Diamètre dateur fleche")


#    def _date_creation():
#        now = datetime.date.today()         # Date du jour
#        return now.strftime('%Y-%m-%d')     # Formatage

    _defaults = {
        'date_creation': lambda *a: fields.datetime.now(),
    }


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
        return super(is_mold, self).copy(cr, uid, id, default=default,
            context=context)


    @api.multi
    def action_acceder_moule(self):
        for obj in self:
            return {
                'name': "Moule",
                'view_mode': 'form',
                'view_type': 'form',
                'res_model': 'is.mold',
                'type': 'ir.actions.act_window',
                'res_id': obj.id,
                'domain': '[]',
            }


