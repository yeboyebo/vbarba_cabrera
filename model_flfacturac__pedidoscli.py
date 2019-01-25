
# @class_declaration vbarba_cabrera_pedidoscli #
class vbarba_cabrera_pedidoscli(flfacturac_pedidoscli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def queryGrid_articulosporcarro(self):
        return form.iface.queryGrid_articulosporcarro(self)

    def queryGrid_articulosporcarro_initFilter(model=None):
        return form.iface.queryGrid_articulosporcarro_initFilter()

    def field_colorRow(cursor):
        return form.iface.field_colorRow(cursor)

    def field_masterColorRow(cursor):
        return form.iface.field_masterColorRow(cursor)

    def drawPiso1(cursor):
        return form.iface.drawPiso1(cursor)

    def drawPiso2(cursor):
        return form.iface.drawPiso2(cursor)

    def drawPiso3(cursor):
        return form.iface.drawPiso3(cursor)

    def drawPiso4(cursor):
        return form.iface.drawPiso4(cursor)

    def drawPiso5(cursor):
        return form.iface.drawPiso5(cursor)

    def drawPiso6(cursor):
        return form.iface.drawPiso6(cursor)

    def drawPiso7(cursor):
        return form.iface.drawPiso7(cursor)

    def drawPiso8(cursor):
        return form.iface.drawPiso8(cursor)

    def drawPiso9(cursor):
        return form.iface.drawPiso9(cursor)

    def drawPiso10(cursor):
        return form.iface.drawPiso10(cursor)

    def drawPiso11(cursor):
        return form.iface.drawPiso11(cursor)

    def drawPiso12(cursor):
        return form.iface.drawPiso12(cursor)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def editarCantPiso(self, oParam):
        return form.iface.editarCantPiso(self, oParam)

    @helpers.decoradores.accion(aqparam=["oParam", "cursor"])
    def nuevoCarro(self, oParam, cursor):
        return form.iface.nuevoCarro(self, oParam, cursor)

    @helpers.decoradores.accion(aqparam=["oParam", "cursor"])
    def nuevoPiso(self, oParam, cursor):
        return form.iface.nuevoPiso(self, oParam, cursor)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def dameCargaImagenCarro(self, oParam):
        return form.iface.dameCargaImagenCarro(self, oParam)

    @helpers.decoradores.accion(aqparam=["cursor"])
    def nuevoPedidoParcial(self, cursor):
        return form.iface.nuevoPedidoParcial(self, cursor)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def eliminarCarroActual(self, oParam):
        return form.iface.eliminarCarroActual(self, oParam)

    def fun_referenciaprov(self):
        return form.iface.fun_referenciaprov(self)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def actObservacionesPedido(self, oParam):
        return form.iface.actObservacionesPedido(self, oParam)

    @helpers.decoradores.accion()
    def dameTemplateCarros(self):
        return form.iface.dameTemplateCarros(self)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def generarPedido_clicked(self, oParam):
        return form.iface.generarPedido_clicked(self, oParam)

    def dameEmailsProveedorer(self, codProveedor):
        return form.iface.dameEmailsProveedorer(self, codProveedor)

    def generarReport(self, aProveedor):
        return form.iface.generarReport(self, aProveedor)

    def enviarReport(self, aProveedor, filepath):
        return form.iface.enviarReport(self, aProveedor, filepath)

    def datosConfigMail(self):
        return form.iface.datosConfigMail(self)

