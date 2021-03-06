
# @class_declaration vbarba_cabrera #
from YBLEGACY.constantes import *


class vbarba_cabrera(flfactppal):

    def vbarba_cabrera_getCodproveedor(self, model, oParam):
        data = []
        # print(oParam)
        referencia = oParam['referencia']
        if referencia:
            q = qsatype.FLSqlQuery()
            # q.setTablesList(u"proveedores, articulosprov")
            # q.setSelect("proveedores.codproveedor, proveedores.nombre")
            # q.setFrom("proveedores INNER JOIN articulosprov ON proveedores.codproveedor = articulosprov.codproveedor")
            # q.setWhere(ustr(u"articulosprov.referencia = '", referencia, u"' AND UPPER(proveedores.nombre) LIKE UPPER('%", str(oParam['val']), u"%')"))

            # 22-02-2019 , Pedido de Jordi para que puede seleccionar cualquier proveedor
            q.setTablesList(u"proveedores")
            q.setSelect("codproveedor, nombre")
            q.setFrom("proveedores")
            q.setWhere(ustr(u"UPPER(proveedores.nombre) LIKE UPPER('%", str(oParam['val']), u"%')"))
            if not q.exec_():
                print("Error inesperado")
                return []

            while q.next():
                data.append({"codproveedor": str(q.value(0)), "nombre": str(q.value(1))})
        # print("getCodproveedor__Fin-data:", data)

        return data

    def __init__(self, context=None):
        super().__init__(context)

    def getCodproveedor(self, model, oParam):
        return self.ctx.vbarba_cabrera_getCodproveedor(model, oParam)

