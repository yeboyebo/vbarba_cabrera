# @class_declaration interna_vb_fincasusu #
from YBUTILS.viewREST import helpers
from models.flfactalma import models as modelos
import importlib


class interna_vb_fincasusu(modelos.mtd_vb_fincasusu, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration vbarba_cabrera_vb_fincasusu #
class vbarba_cabrera_vb_fincasusu(interna_vb_fincasusu, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def initValidation(name, data=None):
        return form.iface.initValidation(name, data)

    def iniciaValoresLabel(self, template=None, cursor=None, data=None):
        return form.iface.iniciaValoresLabel(self, template, cursor)

    def bChLabel(fN=None, cursor=None):
        return form.iface.bChLabel(fN, cursor)

    def getFilters(self, name, template=None):
        return form.iface.getFilters(self, name, template)

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def getDesc():
        return form.iface.getDesc()


# @class_declaration vb_fincasusu #
class vb_fincasusu(vbarba_cabrera_vb_fincasusu, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


definitions = importlib.import_module("models.flfactalma.vb_fincasusu_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
