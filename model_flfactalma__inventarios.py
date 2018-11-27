
# @class_declaration vbarba_cabrera_inventarios #
class vbarba_cabrera_inventarios(new_oficial_inventarios, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getServerData(self, name):
        return form.iface.getServerData(self, name)

    def getForeignFields(self):
        return form.iface.getForeignFields(self)

    def getFilters(self, name, template):
        return form.iface.getFilters(self, name, template)

    def initValidation(self, name, data):
        return form.iface.initValidation(self, name, data)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def nuevaLinea(self, oParam):
        return form.iface.nuevaLinea(self, oParam)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def establecerFinca(self, oParam):
        return form.iface.establecerFinca(self, oParam)

