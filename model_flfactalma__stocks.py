
# @class_declaration vbarba_cabrera_stocks #
class vbarba_cabrera_stocks(flfactalma_stocks, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    @helpers.decoradores.accion(aqparam=["oParam"])
    def cambiarUbicacion(self, oParam):
        return form.iface.cambiarUbicacion(self, oParam)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def altaStock(self, oParam):
        return form.iface.altaStock(self, oParam)

    @helpers.decoradores.accion(aqparam=["oParam", "cursor"])
    def nuevaLineaRegStock(self, oParam, cursor):
        return form.iface.nuevaLineaRegStock(self, oParam, cursor)

    @helpers.decoradores.accion(aqparam=["oParam", "cursor"])
    def sumaCantidadLineaRegStock(self, oParam, cursor):
        return form.iface.sumaCantidadLineaRegStock(self, oParam, cursor)

    def vbarba_bChLabel(fN=None, cursor=None):
        return form.iface.vbarba_bChLabel(fN, cursor)

    def field_codubicacion(self):
        return form.iface.field_codubicacion(self)

    def field_sumacantidad(self):
        return form.iface.field_sumacantidad(self)

    def field_nombreAlmacen(self):
        return form.iface.field_nombreAlmacen(self)

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def getFilters(self, name, template):
        return form.iface.getFilters(self, name, template)

    def initValidation(self, name, data):
        return form.iface.initValidation(self, name, data)

    @helpers.decoradores.accion()
    def prueba(self):
        return form.iface.prueba(self)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def cambiarDetalleUbicacion(self, oParam):
        return form.iface.cambiarDetalleUbicacion(self, oParam)

