
# @class_declaration vbarba_cabrera_proveedores #
class vbarba_cabrera_proveedores(oficial_proveedores, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    @helpers.decoradores.accion(aqparam=["oParam"])
    def getCodproveedor(self, oParam):
        return form.iface.getCodproveedor(self, oParam)

