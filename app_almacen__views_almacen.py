
# @class_declaration vbarba_cabrera #
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

import shutil


class vbarba_cabrera(interna):
    FILE_UPLOAD_DIR = '/home/infosial/cabreraImg'
    # FILE_UPLOAD_DIR = '/home/juanma/cabreraImg'

    def vbarba_cabrera_uploadimage(self, request, param):

        _i = self.iface

        print(request.FILES['image'])
        _i.handle_uploaded_file(request.FILES['image'], param)
        # lftp -u infosialbnp,1nfosial -e 'mirror --reverse /home/juanma/pruebaImg infosial; bye' ftp.barnaplant.com
        # subprocess.call("lftp -e 'put -O infosial /home/infosial/cabreraImg/" + str(param) + ".jpg; bye' -u infosialbnp,1nfosial ftp.barnaplant.com", shell=True)
        # filename = request.POST['image']
        # print(filename)
        # return HttpResponse(renderers.JSONRenderer().render(dict()),content_type="application/json")
        # Informar el campo 'tienefoto'
        if not qsatype.FLUtil.execSql(u"UPDATE articulos set tienefoto = true WHERE referencia = '{}'".format(param)):
            raise ValueError("Error al actualizar el campo tienefoto")
            return False
        url = '/almacen/articulos/' + str(param)
        return HttpResponseRedirect(url)

    def vbarba_cabrera_imagen(self, request, param):
        print(param)
        return render(request, 'almacen/uploadimage.html', {"param": str(param)})

    def vbarba_cabrera_handle_uploaded_file(self, source, name):

        _i = self.iface

        filepath = _i.FILE_UPLOAD_DIR + '/' + name + '.JPG'
        # fd, filepath = tempfile.mkstemp(prefix=str(name), dir=FILE_UPLOAD_DIR, suffix=".jpg")
        print(filepath)
        with open(filepath, 'wb') as f:
            shutil.copyfileobj(source, f)
        return filepath

    def __init__(self, context=None):
        super().__init__(context)

    def uploadimage(self, request, param):
        return self.ctx.vbarba_cabrera_uploadimage(request, param)

    def imagen(self, request, param):
        return self.ctx.vbarba_cabrera_imagen(request, param)

    def handle_uploaded_file(self, source, name):
        return self.ctx.vbarba_cabrera_handle_uploaded_file(source, name)

