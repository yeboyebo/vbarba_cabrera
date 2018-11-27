# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration vbarba_cabrera #
from YBLEGACY.constantes import *
from YBUTILS.viewREST import cacheController
from models.flfactalma.almacenes import almacenes


class vbarba_cabrera(interna):

    def vbarba_cabrera_getFilters(self, model, name, template=None):
        if name == 'almacenesUsuario':
            fincaUsr = cacheController.getSessionVariable(ustr(u"fincaUsr_", qsatype.FLUtil.nameUser()))
            aAlmacenes = []
            for almacen in almacenes.objects.filter(codfinca__exact=fincaUsr):
                aAlmacenes.append(almacen.codalmacen)
            return [{'criterio': 'codalmacen__in', 'valor': aAlmacenes}]

        return []

    def __init__(self, context=None):
        super(vbarba_cabrera, self).__init__(context)

    def getFilters(self, model, name, template=None):
        return self.ctx.vbarba_cabrera_getFilters(model, name, template)


# @class_declaration head #
class head(vbarba_cabrera):

    def __init__(self, context=None):
        super(head, self).__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super(ifaceCtx, self).__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
