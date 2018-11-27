
# @class_declaration vbarba_cabrera_lineasregstocks #
class vbarba_cabrera_lineasregstocks(oficial_lineasregstocks, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def field_codubicacion(self):
        return form.iface.field_codubicacion(self)

    def field_detalleubicacion(self):
        return form.iface.field_detalleubicacion(self)

    def field_colorRow(self):
        return form.iface.field_colorRow(self)

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def getForeign(self, template):
        return form.iface.getForeign(self, template)

