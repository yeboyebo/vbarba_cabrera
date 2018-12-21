# @class_declaration interna_montadospedido #
from YBUTILS.viewREST import helpers
from models.flfacturac import models as modelos
import importlib


class interna_montadospedido(modelos.mtd_montadospedido, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration vbarba_cabrera_montadospedido #
class vbarba_cabrera_montadospedido(interna_montadospedido, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration montadospedido #
class montadospedido(vbarba_cabrera_montadospedido, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.montadospedido_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
