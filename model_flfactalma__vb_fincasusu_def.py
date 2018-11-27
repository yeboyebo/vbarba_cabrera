# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration vbarba_cabrera #
from YBLEGACY.constantes import *


class vbarba_cabrera(interna):

    def vbarba_cabrera_initValidation(self, name, data=None):
        response = True
        return response

    def vbarba_cabrera_iniciaValoresLabel(self, model=None, template=None, cursor=None):
        labels = {}
        return labels

    def vbarba_cabrera_bChLabel(self, fN=None, cursor=None):
        labels = {}
        return labels

    def vbarba_cabrera_getFilters(self, model, name, template=None):
        filters = []
        return filters

    def vbarba_cabrera_getForeignFields(self, model, template=None):
        fields = []
        return fields

    def vbarba_cabrera_getDesc(self):
        desc = None
        return desc

    def __init__(self, context=None):
        super(vbarba_cabrera, self).__init__(context)

    def initValidation(self, name, data=None):
        return self.ctx.vbarba_cabrera_initValidation(name, data=None)

    def iniciaValoresLabel(self, model=None, template=None, cursor=None):
        return self.ctx.vbarba_cabrera_iniciaValoresLabel(model, template, cursor)

    def bChLabel(self, fN=None, cursor=None):
        return self.ctx.vbarba_cabrera_bChLabel(fN, cursor)

    def getFilters(self, model, name, template=None):
        return self.ctx.vbarba_cabrera_getFilters(model, name, template)

    def getForeignFields(self, model, template=None):
        return self.ctx.vbarba_cabrera_getForeignFields(model, template)

    def getDesc(self):
        return self.ctx.vbarba_cabrera_getDesc()


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
