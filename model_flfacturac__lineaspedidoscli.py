
# @class_declaration vbarba_cabrera_lineaspedidoscli #
class vbarba_cabrera_lineaspedidoscli(oficial_lineaspedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def field_colorRow(self):
        return form.iface.field_colorRow(self)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def asociarTotal(self, oParam):
        return form.iface.asociarTotal(self, oParam)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def asociarParcial(self, oParam):
        return form.iface.asociarParcial(self, oParam)

