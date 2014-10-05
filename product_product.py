# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _


# Cette class permet : 
# - d'ajouter le moule à la class d'origine. 
# - de changer l'ordre de tri par défaut
# - d'ajouter une contrainte unique sur le code de l'article
# - de gérer la duplication de l'article
#class product_product(osv.osv):
#    _name = 'product.product'
#    _inherit = 'product.product'
#    _order='default_code'    
#    
#    #ATTENTION : Ne pas mettre d'accent dans le message
#    _sql_constraints = [('default_code_uniq','UNIQUE(default_code)', 'Ce code existe deja')]    
#    
#    _columns = {  
#        #ATTENTION : Pour que la relation many2one affiche le code du moule, le champ doit être nommé 'name' sinon il faut surcharger
#        #la méthode name_get
#        'mold': fields.many2one('is.mold', 'Moule', required=False, ondelete='cascade',
#            help="Sélectionnez un moule"),
#    }


#    def copy(self, cr, uid, id, default=None, context=None):
#        if not context:
#            context = {}
#        product = self.read(cr, uid, id, ['default_code'], context=context)
#        default.update({
#            'default_code': product['default_code'] + _(' (copy)'),
#        })
#        return super(product_product, self).copy(cr, uid, id, default=default,
#            context=context)

#product_product()

