# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration vbarba_cabrera #
from YBLEGACY.constantes import *


class vbarba_cabrera(interna):

    def vbarba_cabrera_getForeignFields(self, model, template=None):
        return []

    def vbarba_cabrera_getFilters(self, model, name, template=None):
        return []

    def vbarba_cabrera_initValidation(self, name, data):
        response = True
        return response

    def vbarba_cabrera_iniciaValoresLabel(self, model, template=None):
        labels = {}
        return labels

    def vbarba_cabrera_bChLabel(self, fN=None, cursor=None):
        labels = {}
        return labels

    def vbarba_cabrera_editarCantPiso(self, model, oParam, cursorLinea):
        print(oParam)
        val = None
        piso = None

        for p in oParam:
            if p.split(".")[1].startswith("cantpiso"):
                val = oParam[p]
                piso = p.split(".")[1]

        if not val or not piso:
            return False

        # print("referencia", qsatype.FLUtil.sqlSelect(u"lineaspedidoscli", u"referencia", ustr(u"idlinea = '", model.idlineapedido, u"'")))
        # print("numcarro", cursorLinea.valueBuffer("numcarro"))
        # print("idlineapedido", cursorLinea.valueBuffer("idlineapedido"))
        cursorLinea.setValueBuffer(piso, val)
        if not cursorLinea.commitBuffer():
            return False
        return True

    def __init__(self, context=None):
        super(vbarba_cabrera, self).__init__(context)

    def getForeignFields(self, model, template=None):
        return self.ctx.vbarba_cabrera_getForeignFields(model, template)

    def getFilters(self, model, name, template=None):
        return self.ctx.vbarba_cabrera_getFilters(model, name, template)

    def initValidation(self, name, data):
        return self.ctx.vbarba_cabrera_initValidation(name, data)

    def iniciaValoresLabel(self, model=None, template=None, cursor=None):
        return self.ctx.vbarba_cabrera_iniciaValoresLabel(model, template)

    def bChLabel(self, fN=None, cursor=None):
        return self.ctx.vbarba_cabrera_bChLabel(fN, cursor)

    def editarCantPiso(self, model, oParam, cursor):
        return self.ctx.vbarba_cabrera_editarCantPiso(model, oParam, cursor)

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
