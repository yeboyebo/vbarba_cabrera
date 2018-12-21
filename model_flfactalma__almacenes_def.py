
# @class_declaration vbarba_cabrera #
from YBLEGACY.constantes import *
from YBUTILS.viewREST import cacheController
# Quitar cuando se arregle el caso de vbarba_cabrera_getFilters
from models.flfactalma.almacenes import almacenes


class vbarba_cabrera(flfactalma):

    def vbarba_cabrera_getFilters(self, model, name, template=None):
        if name == 'almacenesUsuario':
            fincaUsr = cacheController.getSessionVariable(ustr(u"fincaUsr_", qsatype.FLUtil.nameUser()))
            aAlmacenes = []
            for almacen in almacenes.objects.filter(codfinca__exact=fincaUsr):
                aAlmacenes.append(almacen.codalmacen)
            return [{'criterio': 'codalmacen__in', 'valor': aAlmacenes}]

        return []

    def vbarba_cabrera_getDesc(self):
        desc = "nombre"
        return desc

    def __init__(self, context=None):
        super().__init__(context)

    def getFilters(self, model, name, template=None):
        return self.ctx.vbarba_cabrera_getFilters(model, name, template)

    def getDesc(self):
        return self.ctx.vbarba_cabrera_getDesc()

