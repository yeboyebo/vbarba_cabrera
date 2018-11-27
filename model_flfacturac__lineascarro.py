# @class_declaration interna_lineascarro #
from YBUTILS.viewREST import helpers
from models.flfacturac import models as factmodels
import importlib


class interna_lineascarro(factmodels.mtd_lineascarro, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration vbarba_cabrera_lineascarro #
class vbarba_cabrera_lineascarro(interna_lineascarro, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getForeignFields(self, template=None):
        return form.iface.getForeignFields(self, template)

    def getFilters(self, name, template=None):
        return form.iface.getFilters(self, name, template)

    def initValidation(name, data):
        return form.iface.initValidation(name, data)

    def iniciaValoresLabel(self, template=None, cursor=None, data=None):
        return form.iface.iniciaValoresLabel(self, template, cursor)

    def bChLabel(fN=None, cursor=None):
        return form.iface.bChLabel(fN, cursor)

    @helpers.decoradores.accion(aqparam=["oParam", "cursor"])
    def editarCantPiso(self, oParam, cursor):
        return form.iface.editarCantPiso(self, oParam, cursor)


# @class_declaration lineascarro #
class lineascarro(vbarba_cabrera_lineascarro, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


definitions = importlib.import_module("models.flfacturac.lineascarro_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
