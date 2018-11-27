
# @class_declaration vbarba_cabrera #
from YBLEGACY.constantes import *


class vbarba_cabrera(oficial):

    def vbarba_cabrera_getDesc(self):
        desc = "descripcion"
        return desc

    def __init__(self, context=None):
        super(vbarba_cabrera, self).__init__(context)

    def getDesc(self):
        return self.ctx.vbarba_cabrera_getDesc()

