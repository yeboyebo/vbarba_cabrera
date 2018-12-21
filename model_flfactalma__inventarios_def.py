
# @class_declaration vbarba_cabrera #
from YBUTILS.viewREST import cacheController
from models.flfactalma import flfactalma_def


class vbarba_cabrera(flfactalma):

    def vbarba_cabrera_getServerData(self, model, name):
        return []

    def vbarba_cabrera_getForeignFields(self, model):
        return []

    def vbarba_cabrera_getFilters(self, model, name, template):
        return []

    def vbarba_cabrera_initValidation(self, name, data):
        response = True

        if name == 'inventariosAlmacen':
            fincaUsr = cacheController.getSessionVariable(ustr(u"fincaUsr_", qsatype.FLUtil.nameUser()))
            if not fincaUsr:
                return False
            return response

        return response

    def vbarba_cabrera_nuevaLinea(self, model, oParam):
        aux = flfactalma_def.iface.nuevaLineaRegStock(model.codinventario, model.codalmacen, oParam['codbarras'], oParam['cantidad'])
        return aux

    def vbarba_cabrera_establecerFinca(self, model, oParam):
        codFinca = oParam['codfinca']
        print("User: ", qsatype.FLUtil.nameUser())
        cacheController.setSessionVariable(ustr(u"fincaUsr_", qsatype.FLUtil.nameUser()), codFinca)
        resul = {}
        resul['status'] = True
        resul['url'] = "/almacen/articulos/custom/articulosStock"
        return resul

    def __init__(self, context=None):
        super(vbarba_cabrera, self).__init__(context)

    def getServerData(self, model, name):
        return self.ctx.vbarba_cabrera_getServerData(model, name)

    def getForeignFields(self, model):
        return self.ctx.vbarba_cabrera_getForeignFields(model)

    def getFilters(self, model, name, template):
        return self.ctx.vbarba_cabrera_getFilters(model, name, template)

    def initValidation(self, name, data):
        return self.ctx.vbarba_cabrera_initValidation(name, data)

    def nuevaLinea(self, model, oParam):
        return self.ctx.vbarba_cabrera_nuevaLinea(model, oParam)

    def establecerFinca(self, model, oParam):
        return self.ctx.vbarba_cabrera_establecerFinca(model, oParam)

