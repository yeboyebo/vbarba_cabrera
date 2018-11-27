
# @class_declaration vbarba_cabrera #
from YBLEGACY.constantes import *


class vbarba_cabrera(oficial):

    def vbarba_cabrera_getDesc(self):
        desc = "nombre"
        return desc

    def vbarba_cabrera_getCliente(self, model, oParam):
        data = []
        q = qsatype.FLSqlQuery()
        q.setTablesList(u"clientes, crm_contactos")
        # q.setSelect(u"c.nombre, c.codcliente")
        # q.setFrom(u"crm_contactos cc LEFT OUTER JOIN contactosclientes ci ON cc.codcontacto = ci.codcontacto INNER JOIN clientes c ON ci.codcliente=c.codcliente")
        # q.setWhere(u"UPPER(c.nombre) LIKE '%" + oParam['val'].upper() + "%' OR UPPER(c.codcliente) LIKE '%" + oParam['val'].upper() + "%' OR UPPER(cc.nif) LIKE '%" + oParam['val'].upper() + "%'")
        q.setSelect("nombre, codcliente")
        q.setFrom("clientes")
        q.setWhere("UPPER(nombre) LIKE '%" + oParam['val'].upper() + "%' OR UPPER(codcliente) LIKE '%" + oParam['val'].upper() + "%' OR UPPER(cifnif) LIKE '%" + oParam['val'].upper() + "%' OR codcliente in (SELECT cc.codcliente FROM contactosclientes cc INNER JOIN crm_contactos cr ON cc.codcontacto = cr.codcontacto WHERE UPPER(cr.nif) LIKE '%" + oParam['val'].upper() + "%')")

        if not q.exec_():
            print("Error inesperado")
            return []
        if q.size() > 200:
            return []

        while q.next():
            data.append({"nombre": q.value(0), "codcliente": q.value(1)})

        return data

    def __init__(self, context=None):
        super(vbarba_cabrera, self).__init__(context)

    def getDesc(self):
        return self.ctx.vbarba_cabrera_getDesc()

    def getCliente(self, model, oParam):
        return self.ctx.vbarba_cabrera_getCliente(model, oParam)

