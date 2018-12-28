
# @class_declaration vbarba_cabrera #
from YBUTILS.viewREST import cacheController
from models.flfactalma import flfactalma_def
from models.flfactalma.stocks import stocks
from models.flfactalma.almacenes import almacenes
from models.flfactalma.vb_ubicaciones import vb_ubicaciones


class vbarba_cabrera(flfactalma):

    def vbarba_cabrera_cambiarUbicacion(self, model, oParam):
        if not oParam:
            ubicacion = model.vb_codubicacion
            detalleubicacion = model.detalleubicacion
            ubicacionlocal = None
            if ubicacion:
                ubicacionlocal = vb_ubicaciones.objects.get(pk=model.vb_codubicacion)
                ubicacionlocal = ubicacionlocal.ubicacionlocal
            if not detalleubicacion:
                detalleubicacion = ""
            # print({"ubicacion": ubicacion, "detalleubicacion": detalleubicacion, "ubicacionlocal": ubicacionlocal})
            response = {}
            response['status'] = -1
            response['data'] = {
                "codubicacion": ubicacion,
                "detalleubicacion": detalleubicacion,
                "ubicacionlocal": ubicacionlocal,
                "codalmacen": model.codalmacen
            }
            if not detalleubicacion:
                response['data'] = {
                    "ubicacion": ubicacion,
                    "codalmacen": model.codalmacen
                }

            response['params'] = {
                "codubicacion": {
                    "prefix": "stocks",
                    "modelName": "codubicacion",
                    "desc_name": "Ubicacion",
                    "verbose_name": "Ubicacion",
                    "tipo": 5,
                    "rel": "vb_ubicaciones",
                    "aplic": "almacen",
                    "key": "codubicacion",
                    "desc": "ubicacionlocal",
                    "filtro": ["codalmacen"],
                    "showpk": False,
                    "null": True
                },
                "field_detalleubicacion": {
                    "tipo": 3,
                    "required": True,
                    "verbose_name": "detalleubicacion",
                    "key": "detalleubicacion",
                    "null": True
                }
            }
            return response
        else:
            flfactalma_def.iface.cambiaUbicacionStocks(model, oParam['codubicacion'], oParam['detalleubicacion'])
            return True
        return True

    def vbarba_cabrera_altaStock(self, model, oParam):
        return True

    def vbarba_cabrera_nuevaLineaRegStock(self, model, oParam, cursor):
        # aux = flfactalma_def.iface.nuevaLineaRegStock(model.idstock, model.referencia, model.cantidad, oParam['cantidad'])
        aux = flfactalma_def.iface.nuevaLineaRegStock(cursor.valueBuffer("idstock"), cursor.valueBuffer("referencia"), cursor.valueBuffer("cantidad"), oParam['cantidad'])
        return aux

    def vbarba_cabrera_sumaCantidadLineaRegStock(self, model, oParam, cursor):
        cant = parseFloat(oParam['sumacantidad']) + cursor.valueBuffer("cantidad")
        aux = flfactalma_def.iface.nuevaLineaRegStock(cursor.valueBuffer("idstock"), cursor.valueBuffer("referencia"), cursor.valueBuffer("cantidad"), cant)
        return aux

    def vbarba_cabrera_iniciaValoresLabel(self, model=None, template=None, cursor=None):
        labels = {}
        labels[u"fincaActual"] = cacheController.getSessionVariable(ustr(u"fincaUsr_", qsatype.FLUtil.nameUser()))
        return labels

    def vbarba_cabrera_vbarba_bChLabel(self, fN=None, cursor=None):
        labels = {}
        return labels

    def vbarba_cabrera_field_codubicacion(self, model):
        cstocks = stocks.objects.get(pk=model.idstock)
        if cstocks.vb_codubicacion:
            try:
                cubicaciones = vb_ubicaciones.objects.get(pk=cstocks.vb_codubicacion)
                ubicacion = cubicaciones.ubicacionlocal
                if ubicacion:
                    return ubicacion
            except Exception:
                return False
        return False

    def vbarba_cabrera_field_sumacantidad(self, model):
        return 0

    def vbarba_cabrera_field_nombreAlmacen(self, model):
        # almacen = almacenes.objects.get(pk=model.codalmacen)
        almacen = model.codalmacen
        return almacen.nombre

    def vbarba_cabrera_getForeignFields(self, model, template):
        return [
            {'verbose_name': 'ubicacionlocal', 'func': 'field_codubicacion'},
            {'verbose_name': 'sumacantidad', 'func': 'field_sumacantidad'},
            {'verbose_name': 'nombreAlmacen', 'func': 'field_nombreAlmacen'}
        ]

    def vbarba_cabrera_getFilters(self, model, name, template):
        if name == 'fincaUsuario':
            fincaUsr = cacheController.getSessionVariable(ustr(u"fincaUsr_", qsatype.FLUtil.nameUser()))
            aAlmacenes = []
            for almacen in almacenes.objects.filter(codfinca__exact=fincaUsr):
                aAlmacenes.append(almacen.codalmacen)

            return [{'criterio': 'codalmacen__in', 'valor': aAlmacenes}]

        return []

    def vbarba_cabrera_initValidation(self, model, name, data):
        response = True

        if name == 'inventariosAlmacen':
            fincaUsr = cacheController.getSessionVariable(ustr(u"fincaUsr_", qsatype.FLUtil.nameUser()))
            if not fincaUsr:
                return False
            return response

        return response

    def vbarba_cabrera_prueba(self, model):
        print(model.pk)
        return True

    def vbarba_cabrera_cambiarDetalleUbicacion(self, model, oParam):
        flfactalma_def.iface.cambiaUbicacionStocks(model, model.vb_codubicacion, oParam['detalleubicacion'])
        return True

    def __init__(self, context=None):
        super().__init__(context)

    def cambiarUbicacion(self, model, oParam):
        return self.ctx.vbarba_cabrera_cambiarUbicacion(model, oParam)

    def altaStock(self, model, oParam):
        return self.ctx.vbarba_cabrera_altaStock(model, oParam)

    def nuevaLineaRegStock(self, model, oParam, cursor):
        return self.ctx.vbarba_cabrera_nuevaLineaRegStock(model, oParam, cursor)

    def sumaCantidadLineaRegStock(self, model, oParam, cursor):
        return self.ctx.vbarba_cabrera_sumaCantidadLineaRegStock(model, oParam, cursor)

    def iniciaValoresLabel(self, model=None, template=None, cursor=None):
        return self.ctx.vbarba_cabrera_iniciaValoresLabel(model, template, cursor)

    def vbarba_bChLabel(self, fN=None, cursor=None):
        return self.ctx.vbarba_cabrera_vbarba_bChLabel(fN, cursor)

    def field_codubicacion(self, model):
        return self.ctx.vbarba_cabrera_field_codubicacion(model)

    def field_sumacantidad(self, model):
        return self.ctx.vbarba_cabrera_field_sumacantidad(model)

    def field_nombreAlmacen(self, model):
        return self.ctx.vbarba_cabrera_field_nombreAlmacen(model)

    def getForeignFields(self, model, template):
        return self.ctx.vbarba_cabrera_getForeignFields(model, template)

    def getFilters(self, model, name, template):
        return self.ctx.vbarba_cabrera_getFilters(model, name, template)

    def initValidation(self, model, name, data):
        return self.ctx.vbarba_cabrera_initValidation(model, name, data)

    def prueba(self, model):
        return self.ctx.vbarba_cabrera_prueba(model)

    def cambiarDetalleUbicacion(self, model, oParam):
        return self.ctx.vbarba_cabrera_cambiarDetalleUbicacion(model, oParam)

