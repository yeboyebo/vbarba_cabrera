
# @class_declaration vbarba_cabrera_divisas #
class vbarba_cabrera_divisas(flfactppal_divisas, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getDesc():
        return form.iface.getDesc()

