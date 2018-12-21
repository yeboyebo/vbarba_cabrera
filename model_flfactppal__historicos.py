# @class_declaration interna_historicos #
from YBUTILS.viewREST import helpers
from models.flfactppal import models as modelos
import importlib


class interna_historicos(modelos.mtd_historicos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration vbarba_cabrera_historicos #
class vbarba_cabrera_historicos(interna_historicos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration historicos #
class historicos(vbarba_cabrera_historicos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.historicos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
