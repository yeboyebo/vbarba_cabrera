# @class_declaration interna_vb_almacenesusu #
from YBUTILS.viewREST import helpers
from models.flfactalma import models as modelos
import importlib


class interna_vb_almacenesusu(modelos.mtd_vb_almacenesusu, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration vbarba_cabrera_vb_almacenesusu #
class vbarba_cabrera_vb_almacenesusu(interna_vb_almacenesusu, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration vb_almacenesusu #
class vb_almacenesusu(vbarba_cabrera_vb_almacenesusu, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.vb_almacenesusu_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
