
# @class_declaration vbarba_cabrera #
from YBUTILS import notifications
from YBUTILS.viewREST import fileAttachment


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

    def vbarba_cabrera_iniciaValoresLabel(self, model=None, template=None, cursor=None, data=None):
        labels = {}
        if template == "master" or template == "mastercarros":
            return labels

        labels["numPiso"] = 1
        labels["numCarro"] = 1
        numcarros = 0
        numcarros = qsatype.FLUtil.sqlSelect(u"montadospedido", u"numcarros", ustr(u"idpedido = '", str(cursor.valueBuffer("idpedido")), u"' AND nummontado = '" + str(cursor.valueBuffer("nummontados")) + "'"))
        labels["totalCarros"] = numcarros or 1
        return labels

    def vbarba_cabrera_bChLabel(self, fN=None, cursor=None):
        labels = {}
        return labels

    def vbarba_cabrera_cambiarCantidad(self, model, oParam):
        return 1

    def vbarba_cabrera_queryGrid_articulosporcarro_initFilter(self):
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
        numcarros = qsatype.FLUtil.sqlSelect(u"montadospedido", u"numcarros", ustr(u"idpedido = '", str(model.idpedido), u"' AND nummontado = '" + str(model.nummontados) + "'"))
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

    def vbarba_cabrera_generarPedido_clicked(self, model, oParam):
        _i = self.iface
        aChecked = []
        aChecked = oParam['selecteds'].split(u",")
        aLineasPedCli = {}
        aAsociados = []
        aNoEmail = []
        aFalloGenerar = []
        aFalloEnviar = []
        response = {}
        response['status'] = 1
        if not aChecked[0]:
            response['msg'] = "Deberías seleccionar por lo menos un pedido"
            return response
        for idpedido in aChecked:
            codigo = qsatype.FLUtil.sqlSelect(u"pedidoscli", u"codigo", ustr(u"idpedido = ", idpedido, u" AND pedido <> 'No'"))
            if codigo:
                aAsociados.append(codigo)
        if aAsociados:
            response["status"] = 2
            if len(aAsociados) > 1:
                response["confirm"] = "Los pedidos (%s) que ha seleccionado ya están asociados a provedor." % (", ".join(aAsociados))
            else:
                response["confirm"] = "El pedido (%s) que ha seleccionado ya está asociado a provedor." % (", ".join(aAsociados))
            response["close"] = True
            return response
        aChecked = str(aChecked)[1: -1]
        aChecked = str(aChecked)
        aLineasPedCli = qsatype.FactoriaModulos.get('formpedidosprov').iface.crearArray(aChecked)
        if not aLineasPedCli:
            response['status'] = 2
            response['confirm'] = "Info: No hay ninguna linea del pedido(s) asociada a proveedor."
            response["close"] = True
            return response
        # msgEnviados = ""
        # msgNoEnviados = ""
        msgCab = ""
        indice = 0
        contNoCrearPedidoProv = 0
        contEmailProveedor = 0
        contGenerados = 0
        contEnviados = 0
        nuevoPed = None
        emailProveedor = ""
        codProveedor = None
        while indice < len(aLineasPedCli):
            aProveedor = {}
            try:
                nuevoPed = qsatype.FactoriaModulos.get('formpedidosprov').iface.crearPedidoProvCli(indice, False, aLineasPedCli)
            except Exception as e:
                response = {}
                response['status'] = 1
                response['msg'] = "Error: No se ha creado el pedido." + e
                return response
            if not nuevoPed:
                contNoCrearPedidoProv += 1
            codProveedor = qsatype.FLUtil.sqlSelect(u"pedidosprov", u"codproveedor", ustr(u"codigo = '", str(nuevoPed), u"'"))
            emailProveedor = _i.dameEmailsProveedorer(codProveedor)
            if emailProveedor and emailProveedor != "":
                aProveedor['codigo'] = nuevoPed
                aProveedor['codproveedor'] = codProveedor
                aProveedor['emailproveedor'] = emailProveedor
                filepath = _i.generarReport(aProveedor)
                if filepath:
                    contGenerados += 1
                    if _i.enviarReport(aProveedor, filepath):
                        contEnviados += 1
                    else:
                        aFalloEnviar.append(nuevoPed)
                else:
                    aFalloGenerar.append(nuevoPed)
                contEmailProveedor += 1
            else:
                aNoEmail.append(nuevoPed)
            indice += 1
        if contNoCrearPedidoProv > 0:
            msgCab = "Hay " + str(contNoCrearPedidoProv) + " pedidos de proveedor  que no se han generado."
        if indice == contEnviados:
            msgCab += "Se han generado " + str(indice) + " pedidos de proveedor."
        else:
            if indice > contEmailProveedor:
                msgCab += "Hay pedidos de proveedor que no se han podido enviar por no haber contacto asociado (%s). Revise los pedidos y envielos desde AbanQ.\n" % (", ".join(aNoEmail))
            if contEmailProveedor > contGenerados:
                msgCab += "Hay pedidos de proveedor para los que no se ha podido generar el informe (%s). Revise los pedidos y genera los informes desde AbanQ.\n" % (", ".join(aFalloGenerar))
            if contGenerados > contEnviados:
                msgCab += "Hay pedidos de proveedor que no se han podido enviar (%s). Revise los pedidos y envielos desde AbanQ." % (", ".join(aFalloEnviar))
        response["status"] = 2
        response["confirm"] = msgCab
        response["close"] = True
        return response

    def vbarba_cabrera_dameEmailsProveedorer(self, codProveedor):
        listaEmails = ""
        emailPrincipal = qsatype.FLUtil.sqlSelect(u"proveedores", u"email", ustr(u"codproveedor = '", codProveedor, u"'"))

        q = qsatype.FLSqlQuery()
        q.setTablesList("contactosproveedores,crm_contactos")
        q.setFrom("contactosproveedores INNER JOIN crm_contactos ON contactosproveedores.codcontacto = crm_contactos.codcontacto")
        q.setSelect("crm_contactos.email,crm_contactos.nombre")
        q.setWhere("contactosproveedores.codproveedor = '" + codProveedor + "' AND (crm_contactos.email <> '' AND crm_contactos.email IS NOT NULL)")
        if not q.exec_():
            if emailPrincipal and emailPrincipal != "":
                listaEmails = emailPrincipal
            return listaEmails
        if q.size() > 1:
            while q.next():
                listaEmails += q.value(0) + ","
            listaEmails = listaEmails[:len(listaEmails) - 1]
            return listaEmails
        else:
            return emailPrincipal

    def vbarba_cabrera_generarReport(self, aProveedor):
        report = {}
        nombreBD = qsatype.FLUtil.nameBD()
        report['reportName'] = "vb_pedidosprov"
        if nombreBD == u"cabrera":
            report['reportName'] = "vb_pedidosprov"
        elif nombreBD == u"cash":
            report['reportName'] = "vb_cash_pedidosprov"
        elif nombreBD == u"barnaplant":
            report['reportName'] = "vb_bnp_pedidosprov"
        report['reportName'] = "vb_pedidosprov"
        print("Nombre informe: ", report['reportName'])
        report['params'] = {}
        report['params']['WHERE'] = "pedidosprov.codigo = '" + str(aProveedor['codigo']) + u"'"
        filename = "Pedido_" + str(aProveedor['codigo'])
        filepath = fileAttachment.saveJReport(filename, report['reportName'], report["params"], "/tmp")
        return filepath

    def vbarba_cabrera_enviarReport(self, aProveedor, filepath):
        _i = self.iface
        asunto = qsatype.FactoriaModulos.get('flfacturac').iface.valorDefecto(u"asuntoemail")
        cuerpo = qsatype.FactoriaModulos.get('flfacturac').iface.valorDefecto(u"cuerpoemail")
        if not asunto:
            asunto = ""
        if not cuerpo:
            cuerpo = ""
        oDM = {}
        oDM = _i.datosConfigMail()
        # connection = notifications.get_connection("smtp.gmail.com", "todos.yeboyebo@gmail.com", "555zapato", "465", "SSL")
        connection = notifications.get_connection(oDM["hostcorreosaliente"], oDM["usuariosmtp"], oDM["passwordsmtp"], oDM["puertosmtp"], oDM["tipocxsmtp"])
        response = notifications.sendMail(connection, oDM["usuariosmtp"], asunto, cuerpo, [aProveedor['emailproveedor']], filepath)
        return response

    def vbarba_cabrera_datosConfigMail(self):
        oDM = {}
        q = qsatype.FLSqlQuery()
        q.setSelect("hostcorreosaliente, puertosmtp, tipocxsmtp, tipoautsmtp, usuariosmtp, passwordsmtp")
        q.setFrom(u"factppal_general")
        q.setWhere(u"1 = 1")
        print("Consulta_: ", q.sql())
        if not q.exec_():
            return False
        if q.first():
            oDM["hostcorreosaliente"] = q.value("hostcorreosaliente")
            oDM["puertosmtp"] = q.value("puertosmtp")
            oDM["tipocxsmtp"] = q.value("tipocxsmtp")
            oDM["tipoautsmtp"] = q.value("tipoautsmtp")
            oDM["usuariosmtp"] = q.value("usuariosmtp")
            oDM["passwordsmtp"] = q.value("passwordsmtp")
        return oDM

    def __init__(self, context=None):
        super().__init__(context)

    def getForeignFields(self, model, template=None):
        return self.ctx.vbarba_cabrera_getForeignFields(model, template)

    def getFilters(self, model, name, template=None):
        return self.ctx.vbarba_cabrera_getFilters(model, name, template)

    def initValidation(self, name, data):
        return self.ctx.vbarba_cabrera_initValidation(name, data)

    def iniciaValoresLabel(self, model=None, template=None, cursor=None, data=None):
        return self.ctx.vbarba_cabrera_iniciaValoresLabel(model, template, cursor, data)

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

    def generarPedido_clicked(self, model, oParam):
        return self.ctx.vbarba_cabrera_generarPedido_clicked(model, oParam)

    def dameEmailsProveedorer(self, codProveedor):
        return self.ctx.vbarba_cabrera_dameEmailsProveedorer(codProveedor)

    def generarReport(self, aProveedor):
        return self.ctx.vbarba_cabrera_generarReport(aProveedor)

    def enviarReport(self, aProveedor, filepath):
        return self.ctx.vbarba_cabrera_enviarReport(aProveedor, filepath)

    def datosConfigMail(self, ):
        return self.ctx.vbarba_cabrera_datosConfigMail()

