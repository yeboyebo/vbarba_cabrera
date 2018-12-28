
# @class_declaration vbarba_cabrera_almacenes #
class vbarba_cabrera_almacenes(flfactalma_almacenes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getFilters(self, name, template=None):
        return form.iface.getFilters(self, name, template)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def almacenesUsuario(self, oParam):
        return form.iface.almacenesUsuario(self, oParam)

