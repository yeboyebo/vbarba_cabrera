
# @class_declaration vbarba_cabrera_clientes #
class vbarba_cabrera_clientes(new_oficial_clientes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getDesc():
        return form.iface.getDesc()

    @helpers.decoradores.accion(aqparam=["oParam"])
    def getCliente(self, oParam):
        return form.iface.getCliente(self, oParam)

