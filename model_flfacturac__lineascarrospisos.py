# @class_declaration interna_lineascarrospisos #
from YBUTILS.viewREST import helpers
from models.flfacturac import models as modelos
import importlib


class interna_lineascarrospisos(modelos.mtd_lineascarrospisos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration vbarba_cabrera_lineascarrospisos #
class vbarba_cabrera_lineascarrospisos(interna_lineascarrospisos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lineascarrospisos #
class lineascarrospisos(vbarba_cabrera_lineascarrospisos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.lineascarrospisos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
