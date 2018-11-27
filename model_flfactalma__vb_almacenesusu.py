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


# @class_declaration vb_almacenesusu #
class vb_almacenesusu(vbarba_cabrera_vb_almacenesusu, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


definitions = importlib.import_module("models.flfactalma.vb_almacenesusu_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
