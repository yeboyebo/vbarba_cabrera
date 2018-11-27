
# @class_declaration vbarba_cabrera #

class vbarba_cabrera(new_oficial):

    def vbarba_cabrera_getForeignFields(self, model, template):
        print("_____", template)
        if template == 'formRecord':
            return [
                {'verbose_name': 'rowColor', 'func': 'field_colorRow'}
            ]
        return []

    def vbarba_cabrera_field_colorRow(self, model):
        cantidad = model.cantidad or 0
        cantmontada = model.cantmontada or 0
        if cantidad == cantmontada:
            return "cSuccess"
        elif cantmontada == 0:
            return "cDanger"
        elif cantmontada > 0 and cantmontada < cantidad:
            return "cInfo"
        else:
            return None

    def vbarba_cabrera_asociarTotal(self, model, oParam):
        numCarro = oParam['numCarro'] or 1
        numPiso = oParam['numPiso'] or 1
        cantmontada = model.cantmontada or 0
        cursorLinea = qsatype.FLSqlCursor("lineascarrospisos")
        cursorLinea.setModeAccess(cursorLinea.Edit)
        cursorLinea.select(ustr(u"idlineapedido = '" + str(model.idlinea) + "' AND numcarro = '", str(numCarro), "' AND numpiso = '" + str(numPiso) + "'"))
        cursorLinea.refreshBuffer()
        if cursorLinea.first():
            if model.cantidad == model.cantmontada:
                return True
            else:
                cursorLinea.setValueBuffer("cantidad", model.cantidad - cantmontada + cursorLinea.valueBuffer("cantidad"))
            if not cursorLinea.commitBuffer():
                return False
            return True
        else:
            cursor = qsatype.FLSqlCursor("lineascarrospisos")
            cursor.setModeAccess(cursor.Insert)
            cursor.refreshBuffer()
            cursor.setValueBuffer("idlineapedido", model.idlinea)
            cursor.setValueBuffer("cantidad", model.cantidad - cantmontada)
            cursor.setValueBuffer("numcarro", int(numCarro))
            cursor.setValueBuffer("numpiso", int(numPiso))
            if not cursor.commitBuffer():
                return False
        return True

    def vbarba_cabrera_asociarParcial(self, model, oParam):
        if "numCarro" in oParam:
            numCarro = oParam['numCarro'] or 1
        else:
            numCarro = 1
        if "numPiso" in oParam:
            numPiso = oParam['numPiso'] or 1
        else:
            numPiso = 1
        cantmontada = model.cantmontada or 0
        cantidad = int(oParam['cantidad'])
        if(model.cantidad - cantmontada >= cantidad):
            cursorLinea = qsatype.FLSqlCursor("lineascarrospisos")
            cursorLinea.setModeAccess(cursorLinea.Edit)
            cursorLinea.select(ustr(u"idlineapedido = '" + str(model.idlinea) + "' AND numcarro = '", str(numCarro), "' AND numpiso = '" + str(numPiso) + "'"))
            cursorLinea.refreshBuffer()
            if cursorLinea.first():
                cursorLinea.setValueBuffer("cantidad", cantidad)
                if not cursorLinea.commitBuffer():
                    return False
            else:
                cursor = qsatype.FLSqlCursor("lineascarrospisos")
                cursor.setModeAccess(cursor.Insert)
                cursor.refreshBuffer()
                cursor.setValueBuffer("idlineapedido", model.idlinea)
                cursor.setValueBuffer("cantidad", cantidad)
                cursor.setValueBuffer("numcarro", int(numCarro))
                cursor.setValueBuffer("numpiso", int(numPiso))
                if not cursor.commitBuffer():
                    return False
            return True
        response = {}
        response['status'] = 1
        response['msg'] = "Cantidad incorrecta"
        return response

    def __init__(self, context=None):
        super(vbarba_cabrera, self).__init__(context)

    def getForeignFields(self, model, template):
        return self.ctx.vbarba_cabrera_getForeignFields(model, template)

    def field_colorRow(self, model):
        return self.ctx.vbarba_cabrera_field_colorRow(model)

    def asociarTotal(self, model, oParam):
        return self.ctx.vbarba_cabrera_asociarTotal(model, oParam)

    def asociarParcial(self, model, oParam):
        return self.ctx.vbarba_cabrera_asociarParcial(model, oParam)

