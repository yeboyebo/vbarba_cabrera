
# @class_declaration vbarba_cabrera #
from YBLEGACY.constantes import *
from YBUTILS.viewREST import cacheController


class vbarba_cabrera(interna):

    def vbarba_cabrera_afterCommit_lineaspedidoscli(self, curLinea=None):
        _i = self.iface
        if not qsatype.FactoriaModulos.get('flfacturac').iface.afterCommit_lineaspedidoscli(curLinea):
            return False
        if not _i.comprobarMontadoPedido(curLinea):
            return False
        return True

    def vbarba_cabrera_afterCommit_lineascarro(self, curLinea=None):
        _i = self.iface
        if not _i.actualizaMontadoLineaPedido(curLinea):
            return False
        return True

    def vbarba_cabrera_afterCommit_pedidoscli(self, curPedido=None):
        _i = self.iface
        if not qsatype.FactoriaModulos.get('flfacturac').iface.afterCommit_pedidoscli(curPedido):
            return False
        return True

    def vbarba_cabrera_beforeCommit_pedidoscli(self, curPedido=None):
        _i = self.iface
        if not qsatype.FactoriaModulos.get('flfacturac').iface.beforeCommit_pedidoscli(curPedido):
            return False
        return True

    def vbarba_cabrera_comprobarMontadoPedido(self, curLinea):
        print("?????????????")
        cursor = qsatype.FLSqlCursor("pedidoscli")
        cursor.select(ustr("idpedido = '", curLinea.valueBuffer("idpedido"), "'"))
        cursor.setModeAccess(cursor.Edit)
        cursor.refreshBuffer()
        if cursor.first():
            q = qsatype.FLSqlQuery()
            q.setTablesList(u"lineaspedidoscli")
            q.setSelect(u"sum(cantidad), sum(cantmontada)")
            q.setFrom(u"lineaspedidoscli")
            q.setWhere(ustr(u"idpedido = '", curLinea.valueBuffer("idpedido"), "'"))
            if q.exec_():
                if q.next():
                    totalCantidad = q.value(0)
                    totalCantMontada = q.value(1)
                    if not totalCantidad or totalCantidad == u"undefined":
                        totalCantidad = 0
                    if not totalCantMontada or totalCantMontada == u"undefined":
                        totalCantMontada = 0
                    # if(q.value(0) == q.value(1)):
                    if totalCantidad == totalCantMontada:
                        cursor.setValueBuffer("montado", 'Si')
                    elif totalCantMontada > 0:
                        cursor.setValueBuffer("montado", 'Parcial')
                    else:
                        cursor.setValueBuffer("montado", 'No')
                    if not cursor.commitBuffer():
                        return False
        return True

    def vbarba_cabrera_actualizaMontadoLineaPedido(self, curLinea=None):
        cursor = qsatype.FLSqlCursor("lineaspedidoscli")
        cursor.select(ustr("idlinea = '", curLinea.valueBuffer("idlineapedido"), "'"))
        cursor.setModeAccess(cursor.Edit)
        cursor.refreshBuffer()
        if cursor.first():
            q = qsatype.FLSqlQuery()
            q.setTablesList(u"lineascarro")
            q.setSelect(u"sum(cantpiso1 + cantpiso2 + cantpiso3 + cantpiso4 + cantpiso5 + cantpiso6 + cantpiso7 + cantpiso8 + cantpiso9 + cantpiso10 + cantpiso11 + cantpiso12)")
            q.setFrom(u"lineascarro")
            q.setWhere(ustr(u"idlineapedido = '", curLinea.valueBuffer("idlineapedido"), "'"))

            if q.exec_():
                if q.next():
                    # No permitir que se introduzca mas de la esperada
                    # if(float(q.value(0)) > cursor.valueBuffer("cantidad")):
                    #     return False
                    # if not qsatype.FLUtil.execSql(ustr(u"UPDATE lineaspedidoscli set cantmontada = ", q.value(0), " WHERE idpedido = ", curLinea.valueBuffer("idlineapedido"))):
                    #     return False
                    cursor.setValueBuffer("cantmontada", q.value(0))
                    if not cursor.commitBuffer():
                        return False

        return True

    def vbarba_cabrera_bufferCommited_lineaspedidoscli(self, curLinea=None):
        # _i = self.iface
        curPedido = qsatype.FLSqlCursor(u"pedidoscli")
        curPedido.select(ustr(u"idpedido = ", curLinea.valueBuffer(u"idpedido")))
        if not curPedido.first():
            return False
        curPedido.setModeAccess(curPedido.Edit)
        curPedido.refreshBuffer()
        if not qsatype.FactoriaModulos.get('formRecordpedidoscli').iface.calcularTotalesCursor(curPedido):
            return False
        if not curPedido.commitBuffer():
            return False
        return True

    def __init__(self, context=None):
        super(vbarba_cabrera, self).__init__(context)

    def afterCommit_lineascarro(self, curLinea=None):
        return self.ctx.vbarba_cabrera_afterCommit_lineascarro(curLinea)

    def afterCommit_lineaspedidoscli(self, curLinea=None):
        return self.ctx.vbarba_cabrera_afterCommit_lineaspedidoscli(curLinea)

    def afterCommit_pedidoscli(self, curPedido=None):
        return self.ctx.vbarba_cabrera_afterCommit_pedidoscli(curPedido)

    def beforeCommit_pedidoscli(self, curPedido=None):
        return self.ctx.vbarba_cabrera_beforeCommit_pedidoscli(curPedido)

    def actualizaMontadoLineaPedido(self, curLinea):
        return self.ctx.vbarba_cabrera_actualizaMontadoLineaPedido(curLinea)

    def comprobarMontadoPedido(self, curLinea):
        return self.ctx.vbarba_cabrera_comprobarMontadoPedido(curLinea)

    def bufferCommited_lineaspedidoscli(self, curLinea=None):
        return self.ctx.vbarba_cabrera_bufferCommited_lineaspedidoscli(curLinea)

