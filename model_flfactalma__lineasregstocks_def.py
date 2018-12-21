
# @class_declaration vbarba_cabrera #
from YBUTILS.viewREST import cacheController
from models.flfactalma.stocks import stocks
from models.flfactalma.vb_ubicaciones import vb_ubicaciones


class vbarba_cabrera(flfactalma):

    def vbarba_cabrera_field_codubicacion(self, model):
        cstocks = stocks.objects.get(pk=model.idstock)
        if cstocks.vb_codubicacion:
            cubicaciones = vb_ubicaciones.objects.get(pk=cstocks.vb_codubicacion)
            ubicacion = cubicaciones.ubicacionlocal
            if ubicacion:
                return ubicacion
        return False

    def vbarba_cabrera_field_detalleubicacion(self, model):
        cstocks = stocks.objects.get(pk=model.idstock)
        detalleubicacion = cstocks.detalleubicacion
        if detalleubicacion:
            return detalleubicacion
        return False

    def vbarba_cabrera_field_colorRow(self, model):
        if model.field_codubicacion():
            return "cInfo"
        else:
            return False

    def vbarba_cabrera_getForeignFields(self, model, template):
        return [
            {'verbose_name': 'Ubicacion', 'func': 'field_codubicacion'},
            {'verbose_name': 'detalleubicacion', 'func': 'field_detalleubicacion'},
            {'verbose_name': 'rowColor', 'func': 'field_colorRow'}
        ]

    def vbarba_cabrera_getForeign(self, model, template):
        return [{'verbose_name': 'deotro', 'func': 'field_codubicacion'}]

    def __init__(self, context=None):
        super(vbarba_cabrera, self).__init__(context)

    def field_codubicacion(self, model):
        return self.ctx.vbarba_cabrera_field_codubicacion(model)

    def field_detalleubicacion(self, model):
        return self.ctx.vbarba_cabrera_field_detalleubicacion(model)

    def field_colorRow(self, model):
        return self.ctx.vbarba_cabrera_field_colorRow(model)

    def getForeignFields(self, model, template):
        return self.ctx.vbarba_cabrera_getForeignFields(model, template)

    def getForeign(self, model, template):
        return self.ctx.vbarba_cabrera_getForeign(model, template)

