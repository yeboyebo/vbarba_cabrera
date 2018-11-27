
# @class_declaration vbarba_cabrera_almacenes #
class vbarba_cabrera_almacenes(new_oficial_almacenes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getFilters(self, name, template=None):
        return form.iface.getFilters(self, name, template)

