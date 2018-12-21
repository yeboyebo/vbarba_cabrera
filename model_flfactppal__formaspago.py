
# @class_declaration vbarba_cabrera_formaspago #
class vbarba_cabrera_formaspago(flfactppal_formaspago, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getDesc():
        return form.iface.getDesc()

