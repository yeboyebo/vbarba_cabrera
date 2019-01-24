
# @class_declaration vbarba_cabrera #
from YBLEGACY.constantes import *
from YBUTILS.viewREST import cacheController


class vbarba_cabrera(flfactalma):

    def vbarba_cabrera_iniciaValoresLabel(self, model=None, template=None, cursor=None, data=None):
        labels = {}
        fincaUsr = cacheController.getSessionVariable(ustr(u"fincaUsr_", qsatype.FLUtil.nameUser()))
        if template == 'stock':
            almacenes = []
            query = qsatype.FLSqlQuery()
            query.setTablesList(u"almacenes")
            query.setSelect(u"codalmacen")
            query.setFrom(u"almacenes")
            query.setWhere(ustr(u"codfinca = '", fincaUsr, u"'"))

            if query.exec_():
                while query.next():
                    almacenes.append(query.value("codalmacen"))

            stocksAlmacenes = ""
            for alma in almacenes:
                stocksAlmacenes += alma + ":"
                q = qsatype.FLSqlQuery()
                q.setTablesList(u"stocks")
                q.setSelect(u"sum(cantidad)")
                q.setFrom(u"stocks")
                q.setWhere(ustr(u"codalmacen IN ('", alma, u"') AND referencia = '", str(cursor.valueBuffer("referencia")), "'"))

                if q.exec_():
                    if q.next():
                        if(q.value(0)):
                            stocksAlmacenes += " " + str(int(q.value(0))) + "\n"

            almaStr = "', '".join(almacenes)
            totalStockFinca = ""
            q = qsatype.FLSqlQuery()
            q.setTablesList(u"stocks")
            q.setSelect(u"sum(cantidad)")
            q.setFrom(u"stocks")
            q.setWhere(ustr(u"codalmacen IN ('", almaStr, u"') AND referencia = '", str(cursor.valueBuffer("referencia")), "'"))

            if q.exec_():
                if q.next():
                    totalStockFinca = q.value(0)

            q = qsatype.FLSqlQuery()
            q.setTablesList(u"vb_fincas, articulosprov")
            q.setSelect(u"a.disponible")
            q.setFrom(u"vb_fincas f INNER JOIN articulosprov a ON f.codproveedor = a.codproveedor")
            q.setWhere(ustr(u"f.codfinca = ('", fincaUsr, u"') AND referencia = '", str(cursor.valueBuffer("referencia")), "'"))
            disponible = 'No'
            if q.exec_():
                if q.size() == 0:
                    disponible = 'No'
                elif q.next():
                    if q.value(0):
                        disponible = 'Sí'
                    else:
                        disponible = 'No'
            else:
                disponible = 'No'

            labels[u"totalStockFinca"] = totalStockFinca
            labels[u"stocksAlmacenes"] = stocksAlmacenes
            labels[u"disponibleProv"] = disponible
        if template == "stock" or template == "formRecord":
            tienefoto = 'No'
            if cursor.valueBuffer("tienefoto"):
                tienefoto = 'Sí'
            labels[u"tieneFoto"] = tienefoto
        labels[u"fincaActual"] = fincaUsr
        return labels

    def vbarba_cabrera_fieldartdisponible(self, model):
        fincaUsr = cacheController.getSessionVariable(ustr(u"fincaUsr_", qsatype.FLUtil.nameUser()))
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"vb_fincas, articulosprov")
        q.setSelect(u"a.disponible")
        q.setFrom(u"vb_fincas f INNER JOIN articulosprov a ON f.codproveedor = a.codproveedor")
        q.setWhere(ustr(u"f.codfinca = ('", fincaUsr, u"') AND referencia = '", model.referencia, "'"))

        if q.exec_():
            if q.size() == 0:
                return 'No'
            elif q.next():
                if q.value(0):
                    return 'Sí'
                else:
                    return 'No'
        else:
            print("error raro")

        return 'No'

    def vbarba_cabrera_getForeignFields(self, model, template=None):
        if template == 'articulosStock':
            return [
                {'verbose_name': 'artdisponible', 'func': 'fieldartdisponible'},
                {'verbose_name': 'rowColor', 'func': 'field_colorRow'}
            ]
        return []

    def vbarba_cabrera_field_colorRow(self, model):
        fincaUsr = cacheController.getSessionVariable(ustr(u"fincaUsr_", qsatype.FLUtil.nameUser()))
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"vb_fincas, articulosprov")
        q.setSelect(u"a.disponible")
        q.setFrom(u"vb_fincas f INNER JOIN articulosprov a ON f.codproveedor = a.codproveedor")
        q.setWhere(ustr(u"f.codfinca = ('", fincaUsr, u"') AND referencia = '", model.referencia, "'"))

        if q.exec_():
            if q.size() == 0:
                return None
            elif q.next():
                if q.value(0):
                    return "cInfo"
                else:
                    return None
        else:
            print("error raro")

        return None

    def vbarba_cabrera_vbarba_bChLabel(self, fN=None, cursor=None):
        labels = {}
        # if fN == u"totalStockFinca":
        #     labels[u"totalStockFinca"] = "2"
        return labels

    def vbarba_cabrera_initValidation(self, name, data):
        response = True
        if name == 'articulosStock':
            fincaUsr = cacheController.getSessionVariable(ustr(u"fincaUsr_", qsatype.FLUtil.nameUser()))
            if not fincaUsr:
                return False
            return response
        return response

    def vbarba_cabrera_cursorAccepted(self, cursor):
        return qsatype.FactoriaModulos.get('formRecordarticulos').iface.controlDatosModArticulosCursor(cursor)

    def vbarba_cabrera_dameCargaImagen(self, model):
        url = '/almacen/imagen/' + str(model.referencia)
        return url

    def vbarba_cabrera_dameUrlImagen(self, model):
        url = 'http://barnaplant.com/imagenes/disponible/' + str(model.referencia) + ".JPG"
        return url

    def vbarba_cabrera_dameTemplateStock(self, model):
        url = '/almacen/articulos/' + str(model.referencia) + '/stock'
        return url

    def vbarba_cabrera_getCodBarrasProv(self, model, oParam):
        data = []
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"articulos, articulosprov")
        q.setSelect(u"a.codbarras, a.descripcion, a.pvp, a.referencia")
        q.setFrom(u"articulos a LEFT JOIN articulosprov p ON a.referencia=p.referencia")
        q.setWhere(u"NOT obsoleto AND (UPPER(a.referencia) LIKE '%" + oParam['val'].upper() + "%' OR UPPER(a.descripcion) LIKE '%" + oParam['val'].upper() + "%' OR UPPER(a.codbarras) LIKE '%" + oParam['val'].upper() + "%' OR UPPER(p.codbarras) LIKE '%" + oParam['val'].upper() + "%') GROUP BY a.referencia ORDER BY LENGTH(a.referencia) LIMIT 7")

        if not q.exec_():
            print("Error inesperado")
            return []
        if q.size() > 100:
            print("sale por aqui")
            return []

        while q.next():
            descripcion = str(q.value(2)) + "€ " + q.value(1)
            data.append({"codbarras": q.value(0), "descripcion": descripcion, "pvp": q.value(2), "referencia": q.value(3)})

        return data

    def vbarba_cabrera_actualizarDisponible(self, model):
        fincaUsr = cacheController.getSessionVariable(ustr(u"fincaUsr_", qsatype.FLUtil.nameUser()))
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"vb_fincas")
        q.setSelect(u"codproveedor")
        q.setFrom(u"vb_fincas")
        q.setWhere(ustr(u"codfinca = ('", fincaUsr, u"')"))
        if q.exec_():
            if q.next():
                codprov = q.value(0)
                print("____", codprov)
                if not codprov:
                    response = {}
                    response['status'] = 1
                    response['msg'] = "No se encuentra proveedor asociado"
                    return response
            else:
                return False
        else:
            return False

        cursor = qsatype.FLSqlCursor("articulosprov")
        cursor.select(ustr(u"codproveedor = ('", codprov, u"') AND referencia = '", model.referencia, "'"))
        cursor.setModeAccess(cursor.Edit)
        cursor.refreshBuffer()
        if cursor.first():
            if cursor.valueBuffer("disponible"):
                cursor.setValueBuffer("disponible", False)
            else:
                cursor.setValueBuffer("disponible", True)
        else:
            q = qsatype.FLSqlQuery()
            q.setTablesList(u"ariculos")
            q.setSelect(u"pvp, codbarras")
            q.setFrom(u"articulos")
            q.setWhere(ustr(u"referencia = ('", model.referencia, u"')"))
            if q.exec_():
                if q.next():
                    pvpart = q.value(0)
                    codbarrasart = q.value(1)
                else:
                    return False
            else:
                return False
            cursor = qsatype.FLSqlCursor("articulosprov")
            cursor.setModeAccess(cursor.Insert)
            cursor.refreshBuffer()
            cursor.setValueBuffer("referencia", model.referencia)
            cursor.setActivatedBufferChanged(True)
            cursor.setValueBuffer("disponible", True)
            cursor.setValueBuffer("codproveedor", codprov)
            cursor.setValueBuffer("coste", pvpart)
            cursor.setValueBuffer("codbarras", codbarrasart)
            cursor.setActivatedBufferChanged(False)

        if not cursor.commitBuffer():
            return False

        return True

    def vbarba_cabrera_getFilters(self, model, name, template=None):
        return []

    def vbarba_cabrera_getDesc(self):
        desc = "descripcion"
        return desc

    def vbarba_cabrera_informes_getReferencia(self, model, oParam):
        data = []
        # print(oParam)
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"articulos, articulosprov")
        q.setSelect(u"a.codbarras, a.descripcion, a.pvp, a.referencia")
        q.setFrom(u"articulos a LEFT JOIN articulosprov p ON a.referencia=p.referencia")
        q.setWhere(u"UPPER(a.referencia) LIKE '%" + oParam['val'].upper() + "%' OR UPPER(a.descripcion) LIKE '%" + oParam['val'].upper() + "%' OR UPPER(a.codbarras) LIKE '%" + oParam['val'].upper() + "%' OR UPPER(p.codbarras) LIKE '%" + oParam['val'].upper() + "%' GROUP BY a.referencia ORDER BY LENGTH(a.referencia)")

        if not q.exec_():
            print("Error inesperado")
            return []
        if q.size() > 100:
            return []

        while q.next():
            descripcion = str(q.value(2)) + "€ " + q.value(1)
            data.append({"codbarras": q.value(0), "descripcion": descripcion, "pvp": q.value(2), "referencia": q.value(3), "refbusqueda": q.value(3)})

        return data

    def __init__(self, context=None):
        super().__init__(context)

    def getFilters(self, model, name, template=None):
        return self.ctx.vbarba_cabrera_getFilters(model, name, template)

    def iniciaValoresLabel(self, model=None, template=None, cursor=None, data=None):
        return self.ctx.vbarba_cabrera_iniciaValoresLabel(model, template, cursor, data)

    def vbarba_bChLabel(self, fN=None, cursor=None):
        return self.ctx.vbarba_cabrera_vbarba_bChLabel(fN, cursor)

    def initValidation(self, name, data):
        return self.ctx.vbarba_cabrera_initValidation(name, data)

    def cursorAccepted(self, cursor):
        return self.ctx.vbarba_cabrera_cursorAccepted(cursor)

    def dameCargaImagen(self, model):
        return self.ctx.vbarba_cabrera_dameCargaImagen(model)

    def dameUrlImagen(self, model):
        return self.ctx.vbarba_cabrera_dameUrlImagen(model)

    def dameTemplateStock(self, model):
        return self.ctx.vbarba_cabrera_dameTemplateStock(model)

    def getCodBarrasProv(self, model, oParam):
        return self.ctx.vbarba_cabrera_getCodBarrasProv(model, oParam)

    def actualizarDisponible(self, model):
        return self.ctx.vbarba_cabrera_actualizarDisponible(model)

    def getForeignFields(self, model, template=None):
            return self.ctx.vbarba_cabrera_getForeignFields(model, template)

    def fieldartdisponible(self, model):
            return self.ctx.vbarba_cabrera_fieldartdisponible(model)

    def field_colorRow(self, model):
        return self.ctx.vbarba_cabrera_field_colorRow(model)

    def getDesc(self):
        return self.ctx.vbarba_cabrera_getDesc()

    def getReferencia(self, model, oParam):
        return self.ctx.vbarba_cabrera_informes_getReferencia(model, oParam)

