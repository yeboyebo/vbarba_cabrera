
# @class_declaration vbarba_cabrera_agentes #
class vbarba_cabrera_agentes(new_oficial_agentes, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getDesc():
        return form.iface.getDesc()

