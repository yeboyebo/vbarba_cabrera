# @class_declaration interna #
from YBLEGACY import qsatype
from YBLEGACY.constantes import *
from YBUTILS.viewREST import viewsets


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration vbarba_cabrera #
class vbarba_cabrera(interna):

    def vbarba_cabrera_formRecordlineaspedidoscli(self, fN, dict, prefix, pk):
        print("????", fN)
        if fN == "referencia":
            querydict = {}
            querydict["p_l"] = 50
            querydict["p_c"] = 1
            querydict["s_referencia__exact"] = dict["data"]["referencia"]
            # print(querydict)
            # print(prefix)
            # TODO no calcula PCount
            a, dataprov, b, c = viewsets.YBMIXINCTXtemplate.cargaDatosQuery("articulosprov", querydict)
            dict["rel"] = dataprov
        elif fN == "actProveedor":
            codproveedor = qsatype.FLUtil.sqlSelect(u"articulosprov", u"codproveedor", ustr(u"id = '", dict["otros"]["inputVal"], u"'"))
            print(codproveedor)
            dict["datachange"] = {}
            dict["datachange"]["codproveedor"] = codproveedor
            pass
        # print(dict)
        return dict

    def __init__(self, context=None):
        super(vbarba_cabrera, self).__init__(context)

    def formRecordlineaspedidoscli(self, fN, dict, prefix, pk):
        return self.vbarba_cabrera_formRecordlineaspedidoscli(fN, dict, prefix, pk)


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
