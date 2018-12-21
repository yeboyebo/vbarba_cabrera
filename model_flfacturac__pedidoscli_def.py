
# @class_declaration vbarba_cabrera #


class vbarba_cabrera(flfacturac):

    def vbarba_cabrera_getForeignFields(self, model, template=None):
        if template == 'mastercarros':
            return [
                {'verbose_name': 'rowColor', 'func': 'field_masterColorRow'}
            ]
        elif template == 'articulosporcarro':
            return [
                {'verbose_name': 'rowColor', 'func': 'field_colorRow'},
                {'verbose_name': 'referenciaprov', 'func': 'fun_referenciaprov'}
            ]
        return []

    def vbarba_cabrera_fun_referenciaprov(self, model):
        where = u"referencia = UPPER('" + model["lineaspedidoscli.referencia"].upper() + "')"
        if model["lineaspedidoscli.codproveedor"]:
            where = where + " AND codproveedor = '" + str(model["lineaspedidoscli.codproveedor"]) + "'"
        else:
            return model["lineaspedidoscli.codproveedor"]
            where = where + " AND pordefecto = true"
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"articulosprov")
        q.setSelect(u"refproveedor")
        q.setFrom(u"articulosprov")
        q.setWhere(where)
        if not q.exec_():
            return ""

        if q.next():
            if not q.value(0):
                return model["lineaspedidoscli.codproveedor"]
            return q.value(0)

    def vbarba_cabrera_getFilters(self, model, name, template=None):
        return []

    def vbarba_cabrera_initValidation(self, name, data):
        response = True
        curPedido = qsatype.FLSqlCursor("pedidoscli")
        curPedido.setModeAccess(curPedido.Edit)
        curPedido.select(u"idpedido = '" + str(data['DATA']['idpedido']) + "'")
        curPedido.refreshBuffer()
        if curPedido.first():
            # if not curPedido.valueBuffer("numcarros"):
                # curPedido.setValueBuffer("numcarros", 1)
            if not curPedido.valueBuffer("numpisos"):
                curPedido.setValueBuffer("numpisos", 4)
            if not curPedido.commitBuffer():
                return False
        numcarros = qsatype.FLUtil.sqlSelect(u"montadospedido", u"numcarros", ustr(u"idpedido = '", str(curPedido.valueBuffer("idpedido")), u"' AND nummontado = '" + str(curPedido.valueBuffer("nummontados")) + "'"))
        if not numcarros:
            # nummontado = qsatype.FLUtil.sqlSelect(u"pedidoscli", u"nummontados", ustr(u"idpedido = ", data['DATA']['idpedido']))
            qsatype.FLUtil.sqlInsert(u"montadospedido", qsatype.Array([u"idpedido", u"numcarros", u"okcomercial", u"nummontado"]), qsatype.Array([data['DATA']['idpedido'], 1, False, curPedido.valueBuffer("nummontados")]))
            response = self.iface.creaLineasCarro(data['DATA']['idpedido'], 1, curPedido.valueBuffer("nummontados"))
        return response

    def vbarba_cabrera_creaLineasCarro(self, idpedido, numcarros, nummontado):
        aux = numcarros
        query = qsatype.FLSqlQuery()
        query.setTablesList(u"lineaspedidoscli")
        query.setSelect(u"idlinea")
        query.setFrom(u"lineaspedidoscli")
        query.setWhere(ustr(u"idpedido = '", idpedido, u"'"))
        if query.exec_():
            while query.next():
                aux = numcarros
                while aux > 0:
                    if not qsatype.FLUtil.sqlSelect(u"lineascarro", u"idlinea", ustr(u"idlineapedido = '", str(query.value(0)), u"' AND numcarro = '" + str(aux) + "' AND nummontado = '" + str(nummontado) + "'")):
                        qsatype.FLUtil.sqlInsert(u"lineascarro", qsatype.Array([u"idlineapedido", u"cantpiso1", u"cantpiso2", u"cantpiso3", u"cantpiso4", u"cantpiso5", u"cantpiso6", u"numcarro", u"nummontado"]), qsatype.Array([query.value(0), 0, 0, 0, 0, 0, 0, aux, nummontado]))
                    aux = aux - 1
        return True

    def vbarba_cabrera_iniciaValoresLabel(self, model, template=None):
        labels = {}
        labels["numPiso"] = 1
        labels["numCarro"] = 1
        numcarros = qsatype.FLUtil.sqlSelect(u"montadospedido", u"numcarros", ustr(u"idpedido = '", str(model.idpedido), u"' AND nummontado = '" + str(model.nummontados) + "'"))
        labels["totalCarros"] = numcarros or 1
        return labels

    def vbarba_cabrera_bChLabel(self, fN=None, cursor=None):
        labels = {}
        return labels

    def vbarba_cabrera_cambiarCantidad(self, model, oParam):
        return 1

    def vbarba_cabrera_queryGrid_articulosporcarro_initFilter(self):
        print("initfilter")
        initFilter = {}
        initFilter['where'] = u" AND lineascarro.numcarro = 1"
        initFilter['otros'] = {"numcarro": "1"}
        initFilter['filter'] = {"s_lineascarro.numcarro__exact": "1"}
        return initFilter

    def vbarba_cabrera_queryGrid_articulosporcarro(self, model):
        # usr = qsatype.FLUtil.nameUser()
        query = {}
        query["tablesList"] = u"lineaspedidoscli, lineascarro"
        query["select"] = u"lineascarro.idlinea, lineaspedidoscli.aliasprov, lineaspedidoscli.codproveedor, lineascarro.idlineapedido, lineaspedidoscli.cantidad, lineaspedidoscli.cantmontada, lineaspedidoscli.referencia, lineaspedidoscli.descripcion, lineascarro.cantpiso1, lineascarro.numcarro, lineascarro.cantpiso1, lineascarro.cantpiso2, lineascarro.cantpiso3, lineascarro.cantpiso4, lineascarro.cantpiso5, lineascarro.cantpiso6, lineascarro.cantpiso7, lineascarro.cantpiso8, lineascarro.cantpiso9, lineascarro.cantpiso10, lineascarro.cantpiso11, lineascarro.cantpiso12"
        query["from"] = u"lineaspedidoscli LEFT JOIN lineascarro ON lineaspedidoscli.idlinea = lineascarro.idlineapedido"
        query["where"] = u"lineaspedidoscli.idpedido = '" + str(model.idpedido) + "' AND lineascarro.nummontado = '" + str(model.nummontados) + "'"
        query["orderby"] = "lineaspedidoscli.idlinea"
        return query

    def vbarba_cabrera_drawPiso1(self, cursor):
        if cursor.valueBuffer("numpisos") and cursor.valueBuffer("numpisos") < 1:
            return "hidden"
        return None

    def vbarba_cabrera_drawPiso2(self, cursor):
        if cursor.valueBuffer("numpisos") and cursor.valueBuffer("numpisos") < 2:
            return "hidden"
        return None

    def vbarba_cabrera_drawPiso3(self, cursor):
        if cursor.valueBuffer("numpisos") and cursor.valueBuffer("numpisos") < 3:
            return "hidden"
        return None

    def vbarba_cabrera_drawPiso4(self, cursor):
        if cursor.valueBuffer("numpisos") and cursor.valueBuffer("numpisos") < 4:
            return "hidden"
        return None

    def vbarba_cabrera_drawPiso5(self, cursor):
        if cursor.valueBuffer("numpisos") and cursor.valueBuffer("numpisos") < 5:
            return "hidden"
        return None

    def vbarba_cabrera_drawPiso6(self, cursor):
        if cursor.valueBuffer("numpisos") and cursor.valueBuffer("numpisos") < 6:
            return "hidden"
        return None

    def vbarba_cabrera_drawPiso7(self, cursor):
        if cursor.valueBuffer("numpisos") and cursor.valueBuffer("numpisos") < 7:
            return "hidden"
        return None

    def vbarba_cabrera_drawPiso8(self, cursor):
        if cursor.valueBuffer("numpisos") and cursor.valueBuffer("numpisos") < 8:
            return "hidden"
        return None

    def vbarba_cabrera_drawPiso9(self, cursor):
        if cursor.valueBuffer("numpisos") and cursor.valueBuffer("numpisos") < 9:
            return "hidden"
        return None

    def vbarba_cabrera_drawPiso10(self, cursor):
        if cursor.valueBuffer("numpisos") and cursor.valueBuffer("numpisos") < 10:
            return "hidden"
        return None

    def vbarba_cabrera_drawPiso11(self, cursor):
        if cursor.valueBuffer("numpisos") and cursor.valueBuffer("numpisos") < 11:
            return "hidden"
        return None

    def vbarba_cabrera_drawPiso12(self, cursor):
        if cursor.valueBuffer("numpisos") and cursor.valueBuffer("numpisos") < 12:
            return "hidden"
        return None

    def vbarba_cabrera_field_colorRow(self, model):
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"lineaspedidoscli")
        q.setSelect(u"cantmontada, cantidad")
        q.setFrom(u"lineaspedidoscli")
        q.setWhere(ustr(u"idlinea = '", str(model['lineascarro.idlineapedido']), u"'"))
        if q.exec_():
            if q.next():
                cantmontada = q.value("cantmontada")
                cantidad = q.value("cantidad")
                if cantidad == cantmontada:
                    return "cSuccess"
                elif cantmontada == 0:
                    return "cWarning"
                elif cantmontada > 0 and cantmontada < cantidad:
                    return "cInfo"
                elif cantmontada > cantidad:
                    return "cDanger"
                else:
                    return None
        return "nulo"

    def vbarba_cabrera_field_masterColorRow(self, model):
        if model.servido == "Parcial":
            return "cInfo"
        return None

    def vbarba_cabrera_nuevoCarro(self, model, oParam, cursor):
        curMontadoPedido = qsatype.FLSqlCursor("montadospedido")
        curMontadoPedido.setModeAccess(curMontadoPedido.Edit)
        curMontadoPedido.select(u"idpedido = '" + str(cursor.valueBuffer("idpedido")) + "' AND nummontado = '" + str(cursor.valueBuffer("nummontados")) + "'")
        curMontadoPedido.refreshBuffer()
        if not curMontadoPedido.first():
            return False
        numcarros = curMontadoPedido.valueBuffer("numcarros") + 1
        curMontadoPedido.setValueBuffer("numcarros", numcarros)
        if not curMontadoPedido.commitBuffer():
            return False
        cursor.setValueBuffer("numcarros", numcarros)
        if not cursor.commitBuffer():
            return False
        # numcarros = qsatype.FLUtil.sqlSelect(u"montadospedido", u"numcarros", ustr(u"idpedido = '", str(cursor.valueBuffer("idpedido")), u"' AND nummontado = '" + str(cursor.valueBuffer("nummontados")) + "'"))
        # numcarros = numcarros + 1
        response = self.iface.creaLineasCarro(model.idpedido, numcarros, cursor.valueBuffer("nummontados"))
        return response

    def vbarba_cabrera_nuevoPiso(self, model, oParam, cursor):
        numpisos = cursor.valueBuffer("numpisos")
        if numpisos < 12:
            cursor.setValueBuffer("numpisos", numpisos + 1)
            if not cursor.commitBuffer():
                return False
        return True

    def vbarba_cabrera_dameCargaImagenCarro(self, model, oParam):
        url = '/facturacion/imagencarro/' + str(model.codigo) + "/" + str(oParam['numcarro'])
        return url

    def vbarba_cabrera_nuevoPedidoParcial(self, model, cursor):
        # Crear registros de lineascarro con nummontado + 1
        curPedido = qsatype.FLSqlCursor("pedidoscli")
        curPedido.setModeAccess(curPedido.Edit)
        curPedido.select(u"idpedido = '" + str(cursor.valueBuffer("idpedido")) + "'")
        curPedido.refreshBuffer()
        if curPedido.first():
            curPedido.setValueBuffer("numcarros", 1)
            curPedido.setValueBuffer("nummontados", int(curPedido.valueBuffer("nummontados")) + 1)
            if not curPedido.commitBuffer():
                return False
        return True

    def vbarba_cabrera_eliminarCarroActual(self, model, oParam):
        print("eliminar carroactual", oParam, model.idpedido)
        numcarros = qsatype.FLUtil.sqlSelect(u"montadospedido", u"numcarros", ustr(u"idpedido = '", str(model.idpedido), u"' AND nummontado = '" + str(model.nummontados) + "'"))
        print(numcarros)
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"lineaspedidoscli")
        q.setSelect(u"idlinea")
        q.setFrom(u"lineaspedidoscli")
        q.setWhere(ustr(u"idpedido = '", str(model.idpedido), u"'"))
        if q.exec_():
            while q.next():
                curLineaCarro = qsatype.FLSqlCursor(u"lineascarro")
                curLineaCarro.select(ustr(u"idlineapedido = '", q.value(0), u"'  AND numcarro = ", numcarros, " AND nummontado = ", model.nummontados, " "))
                if curLineaCarro.next():
                    curLineaCarro.setModeAccess(curLineaCarro.Del)
                    curLineaCarro.refreshBuffer()
                    if not curLineaCarro.commitBuffer():
                        return False

        if not qsatype.FLUtil.execSql(ustr(u"UPDATE montadospedido set numcarros = ", (int(numcarros) - 1), " WHERE nummontado = ", model.nummontados, " AND idpedido = ", model.idpedido)):
            return False
        if not qsatype.FLUtil.execSql(ustr(u"UPDATE pedidoscli set numcarros = ", (int(numcarros) - 1), " WHERE idpedido = ", model.idpedido)):
            return False
        return True

    def vbarba_cabrera_dameTemplateCarros(self, model):
        url = '/facturacion/pedidoscli/' + str(model.idpedido) + '/carros'
        return url

    def vbarba_cabrera_actObservacionesPedido(self, model, oParam):
        if not qsatype.FLUtil.execSql(ustr(u"UPDATE pedidoscli set observaciones = '", oParam['observaciones'], "' WHERE idpedido = ", model.idpedido)):
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

    def cambiarCantidad(self, model, oParam):
        return self.ctx.vbarba_cabrera_cambiarCantidad(model, oParam)

    def queryGrid_articulosporcarro(self, model):
        return self.ctx.vbarba_cabrera_queryGrid_articulosporcarro(model)

    def queryGrid_articulosporcarro_initFilter(self):
        return self.ctx.vbarba_cabrera_queryGrid_articulosporcarro_initFilter()

    def field_colorRow(self, model):
        return self.ctx.vbarba_cabrera_field_colorRow(model)

    def field_masterColorRow(self, model):
        return self.ctx.vbarba_cabrera_field_masterColorRow(model)

    def drawPiso1(self, cursor):
        return self.ctx.vbarba_cabrera_drawPiso1(cursor)

    def drawPiso2(self, cursor):
        return self.ctx.vbarba_cabrera_drawPiso2(cursor)

    def drawPiso3(self, cursor):
        return self.ctx.vbarba_cabrera_drawPiso3(cursor)

    def drawPiso4(self, cursor):
        return self.ctx.vbarba_cabrera_drawPiso4(cursor)

    def drawPiso5(self, cursor):
        return self.ctx.vbarba_cabrera_drawPiso5(cursor)

    def drawPiso6(self, cursor):
        return self.ctx.vbarba_cabrera_drawPiso6(cursor)

    def drawPiso7(self, cursor):
        return self.ctx.vbarba_cabrera_drawPiso7(cursor)

    def drawPiso8(self, cursor):
        return self.ctx.vbarba_cabrera_drawPiso8(cursor)

    def drawPiso9(self, cursor):
        return self.ctx.vbarba_cabrera_drawPiso9(cursor)

    def drawPiso10(self, cursor):
        return self.ctx.vbarba_cabrera_drawPiso10(cursor)

    def drawPiso11(self, cursor):
        return self.ctx.vbarba_cabrera_drawPiso11(cursor)

    def drawPiso12(self, cursor):
        return self.ctx.vbarba_cabrera_drawPiso12(cursor)

    def creaLineasCarro(self, idpedido, numcarros, nummontado):
        return self.ctx.vbarba_cabrera_creaLineasCarro(idpedido, numcarros, nummontado)

    def nuevoCarro(self, model, oParam, cursor):
        return self.ctx.vbarba_cabrera_nuevoCarro(model, oParam, cursor)

    def nuevoPiso(self, model, oParam, cursor):
        return self.ctx.vbarba_cabrera_nuevoPiso(model, oParam, cursor)

    def dameCargaImagenCarro(self, model, oParam):
        return self.ctx.vbarba_cabrera_dameCargaImagenCarro(model, oParam)

    def nuevoPedidoParcial(self, model, cursor):
        return self.ctx.vbarba_cabrera_nuevoPedidoParcial(model, cursor)

    def eliminarCarroActual(self, model, oParam):
        return self.ctx.vbarba_cabrera_eliminarCarroActual(model, oParam)

    def fun_referenciaprov(self, model):
        return self.ctx.vbarba_cabrera_fun_referenciaprov(model)

    def dameTemplateCarros(self, model):
        return self.ctx.vbarba_cabrera_dameTemplateCarros(model)

    def actObservacionesPedido(self, model, oParam):
        return self.ctx.vbarba_cabrera_actObservacionesPedido(model, oParam)

