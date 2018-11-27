
/** @delete_class new_oficial */

# @class_declaration vbarba_cabrera #
from YBLEGACY.constantes import *
from YBUTILS.viewREST import cacheController


class vbarba_cabrera(interna):

    def vbarba_cabrera_nuevaLineaRegStockInventario(self, codinventario, codalmacen, barcode, cantidad):
        # 8400001316513
        cantidad = parseFloat(cantidad)
        resul = {}
        hoy = qsatype.Date()

        pvp = 0
        descripcion = ""
        referencia = ""
        idstock = ""

        query = qsatype.FLSqlQuery()
        query.setTablesList(u"articulos")
        query.setSelect(u"referencia, descripcion, pvp")
        query.setFrom(u"articulos")
        query.setWhere(ustr(u"codbarras = '", barcode, u"'"))

        if query.exec_():
            if query.next():
                referencia = query.value(0)
                descripcion = query.value(1)
                pvp = query.value(2)
            else:
                resul['status'] = -1
                resul['msg'] = "No existe referencia asociada al código de barras"
                resul['param'] = barcode
                return resul
        else:
            resul['status'] = -1
            resul['msg'] = "Error al obtener la referencia asociada al código de barras"
            resul['param'] = barcode
            return resul

        query = qsatype.FLSqlQuery()
        query.setTablesList(u"stocks")
        query.setSelect(u"idstock")
        query.setFrom(u"stocks")
        query.setWhere(ustr(u"codalmacen = '", codalmacen, u"' AND referencia= '", referencia, u"'"))

        if query.exec_():
            if query.next():
                idstock = query.value(0)
            else:
                oArticulo = {}
                oArticulo['referencia'] = referencia
                idstock = qsatype.FactoriaModulos.get('flfactalma').iface.crearStock(codalmacen, oArticulo)

        else:
            resul['status'] = -1
            resul['msg'] = "Error al obtener el stocks asociada a la referencia"
            resul['param'] = referencia
            return resul

        curLRS = qsatype.FLSqlCursor(u"lineasregstocks")
        curLRS.select(ustr(u"codinventario = '", codinventario, u"' AND referencia = '", referencia, "'"))
        if curLRS.first():
            curLRS.setModeAccess(curLRS.Edit)
            curLRS.refreshBuffer()
            cantidad = cantidad + curLRS.valueBuffer(u"cantidadfin")
            curLRS.setValueBuffer("cantidadfin", cantidad)
        else:
            curLRS.setModeAccess(curLRS.Insert)
            curLRS.refreshBuffer()
            curLRS.setValueBuffer("desarticulo", descripcion)
            curLRS.setValueBuffer("referencia", referencia)
            curLRS.setValueBuffer("barcode", barcode)
            curLRS.setValueBuffer("pvp", pvp)
            curLRS.setValueBuffer("cantidadfin", cantidad)
            curLRS.setValueBuffer("idstock", idstock)
            curLRS.setValueBuffer("codinventario", codinventario)
            curLRS.setValueBuffer("hora", hoy.time())
            curLRS.setValueBuffer("fecha", hoy.date())
            curLRS.setValueBuffer("sincronizado", False)
            curLRS.setValueBuffer("cantidadini", 0)
            curLRS.setValueBuffer("ptecalculo", True)

        if not curLRS.commitBuffer():
            resul['status'] = -1
            resul['msg'] = "Error al crear la linea de regularizacion de stock"
            resul['param'] = referencia
            return resul

        resul['status'] = 0
        resul['msg'] = "OK"

        return True

    def vbarba_cabrera_nuevaLineaRegStock(self, idstock, referencia, cantidadini, cantidadfin):
        # 8400001316513
        cantidadini = parseFloat(cantidadini)
        resul = {}
        hoy = qsatype.Date()

        descripcion = ""

        query = qsatype.FLSqlQuery()
        query.setTablesList(u"articulos")
        query.setSelect(u"descripcion")
        query.setFrom(u"articulos")
        query.setWhere(ustr(u"referencia = '", referencia, u"'"))

        if query.exec_():
            if query.next():
                descripcion = query.value(0).encode("utf-8")
            else:
                resul['status'] = -1
                resul['msg'] = "No existe articulo asociada a la referencia"
                resul['param'] = referencia
                return resul
        else:
            resul['status'] = -1
            resul['msg'] = "Error al obtener el articulo asociado a la referencia"
            resul['param'] = referencia
            return resul

        curLRS = qsatype.FLSqlCursor(u"lineasregstocks")

        curLRS.setModeAccess(curLRS.Insert)
        curLRS.refreshBuffer()
        curLRS.setValueBuffer("desarticulo", descripcion)
        curLRS.setValueBuffer("referencia", referencia)
        curLRS.setValueBuffer("cantidadfin", cantidadfin)
        curLRS.setValueBuffer("idstock", idstock)
        curLRS.setValueBuffer("hora", hoy.time())
        curLRS.setValueBuffer("fecha", hoy.date())
        curLRS.setValueBuffer("sincronizado", False)
        curLRS.setValueBuffer("cantidadini", cantidadini)
        curLRS.setValueBuffer("ptecalculo", True)

        if not curLRS.commitBuffer():
            resul['status'] = -1
            resul['msg'] = "Error al crear la linea de regularizacion de stock"
            resul['param'] = referencia
            return resul

        resul['status'] = 0
        resul['msg'] = "OK"

        return True

    def vbarba_cabrera_cambiaUbicacionStocks(self, model, ubicacion, detalleubicacion):
        resul = {}
        curS = qsatype.FLSqlCursor(u"stocks")
        curS.select(ustr(u"idstock = '", model.idstock, "'"))
        if curS.first():
            curS.setModeAccess(curS.Edit)
            curS.refreshBuffer()
            curS.setValueBuffer("vb_codubicacion", ubicacion)
            curS.setValueBuffer("detalleubicacion", detalleubicacion)
        else:
            resul['status'] = -1
            resul['msg'] = "Error no se encuentra la linea de stocks"
            resul['param'] = model.idstock
            return resul

        if not curS.commitBuffer():
            resul['status'] = -1
            resul['msg'] = "Error al cambiar la ubicacion de stock"
            resul['param'] = model.idstock
            return resul

        resul['status'] = 0
        resul['msg'] = "OK"
        return resul

    def __init__(self, context=None):
        super(vbarba_cabrera, self).__init__(context)

    def cambiaUbicacionStocks(self, model, ubicacion, detalleubicacion):
        return self.ctx.vbarba_cabrera_cambiaUbicacionStocks(model, ubicacion, detalleubicacion)

    def nuevaLineaRegStockInventario(self, codinventario, codalmacen, barcode, cantidad):
        return self.ctx.vbarba_cabrera_nuevaLineaRegStockInventario(codinventario, codalmacen, barcode, cantidad)

    def nuevaLineaRegStock(self, idstock, referencia, cantidadini, cantidadfin):
        return self.ctx.vbarba_cabrera_nuevaLineaRegStock(idstock, referencia, cantidadini, cantidadfin)

