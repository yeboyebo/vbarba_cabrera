# @class_declaration interna_vb_ubicaciones #
from YBUTILS.viewREST import helpers
from models.flfactalma import models as almamodels
import importlib


class interna_vb_ubicaciones(almamodels.mtd_vb_ubicaciones, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration vbarba_cabrera_vb_ubicaciones #
class vbarba_cabrera_vb_ubicaciones(interna_vb_ubicaciones, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getFilters(self, name, template=None):
        return form.iface.getFilters(self, name, template)


# @class_declaration vb_ubicaciones #
class vb_ubicaciones(vbarba_cabrera_vb_ubicaciones, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactalma.vb_ubicaciones_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
