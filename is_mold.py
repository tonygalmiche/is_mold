# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _

class is_mold(osv.osv):
    _name='is.mold'
    _order='name'    #Ordre de tri par defaut des listes
    _sql_constraints = [('name_uniq','UNIQUE(name)', 'Ce moule existe deja')] #ATTENTION : Ne pas mettre d'accent dans le message


    #ATTENTION : Pour que la relation many2one affiche le code du moule, le champ doit être nommé 'name' sinon il faut surcharger la méthode name_get
    _columns={
        'name':fields.char("Code",size=20,required=True, select=True),
        'project': fields.many2one('is.mold.project', 'Projet', required=False, ondelete='cascade', help="Sélectionnez un projet"),
    }

    def copy(self, cr, uid, id, default=None, context=None):
        if not context:
            context = {}

        mold = self.read(cr, uid, id, ['name'], context=context)
        default.update({
            'name': mold['name'] + _(' (copy)'),
        })
        return super(is_mold, self).copy(cr, uid, id, default=default,
            context=context)
is_mold()

