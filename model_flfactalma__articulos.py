
# @class_declaration vbarba_cabrera_articulos #
class vbarba_cabrera_articulos(flfactalma_articulos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getFilters(self, name, template=None):
        return form.iface.getFilters(self, name, template)

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def iniciaValoresLabel(self, fN=None, cursor=None, data=None):
        return form.iface.iniciaValoresLabel(self, fN, cursor)

    def vbarba_bChLabel(fN=None, cursor=None):
        return form.iface.vbarba_bChLabel(fN, cursor)

    def initValidation(name, data=None):
        return form.iface.initValidation(name, data)

    def cursorAccepted(cursor):
        return form.iface.cursorAccepted(cursor)

    @helpers.decoradores.accion()
    def dameCargaImagen(self):
        return form.iface.dameCargaImagen(self)

    @helpers.decoradores.accion()
    def dameUrlImagen(self):
        return form.iface.dameUrlImagen(self)

    @helpers.decoradores.accion()
    def dameTemplateStock(self):
        return form.iface.dameTemplateStock(self)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def getCodBarrasProv(self, oParam):
        return form.iface.getCodBarrasProv(self, oParam)

    @helpers.decoradores.accion()
    def actualizarDisponible(self):
        return form.iface.actualizarDisponible(self)

    def fieldartdisponible(self):
        return form.iface.fieldartdisponible(self)

    def field_colorRow(self):
        return form.iface.field_colorRow(self)

    def getDesc():
        return form.iface.getDesc()

    @helpers.decoradores.accion(aqparam=["oParam"])
    def getReferencia(self, oParam):
        return form.iface.getReferencia(self, oParam)

