
# @class_declaration vbarba_cabrera #
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from YBLEGACY.constantes import ustr
import shutil

class vbarba_cabrera(interna):
    FILE_UPLOAD_DIR = '/mnt/carros/CABRERA'
    # FILE_UPLOAD_DIR = '/var/www/images'

    # def vbarba_cabrera_uploadimagencarro(self, request, pedido, carro):

    #     _i = self.iface
    #     nummontados = qsatype.FLUtil.sqlSelect(u"pedidoscli", u"nummontados", ustr(u"idpedido = '", str(pedido), u"'"))
    #     if not nummontados:
    #         nummontados = 0
    #     name = str(pedido) + "__" + str(carro) + "_M" + str(nummontados)
    #     _i.handle_uploaded_file(request.FILES['imagencarro'], name)
    #     # lftp -u infosialbnp,1nfosial -e 'mirror --reverse /home/juanma/pruebaImg infosial; bye' ftp.barnaplant.com
    #     # subprocess.call("lftp -e 'put -O infosial /home/infosial/cabreraImg/" + str(pedido) + ".jpg; bye' -u infosialbnp,1nfosial ftp.barnaplant.com", shell=True)
    #     # filename = request.POST['image']
    #     # print(filename)
    #     # return HttpResponse(renderers.JSONRenderer().render(dict()),content_type="application/json")
    #     url = '/facturacion/pedidoscli/' + str(pedido)
    #     return HttpResponseRedirect(url)
    def vbarba_cabrera_uploadimagencarro(self, request, pedido, carro):
        _i = self.iface
        nummontados = qsatype.FLUtil.sqlSelect(u"pedidoscli", u"nummontados", ustr(u"codigo = '", str(pedido), u"'"))
        if not nummontados:
            nummontados = 0
        name = str(pedido) + "__" + str(carro) + "_M" + str(nummontados)
        _i.handle_uploaded_file(request.FILES['imagencarro'], name)
        # lftp -u infosialbnp,1nfosial -e 'mirror --reverse /home/juanma/pruebaImg infosial; bye' ftp.barnaplant.com
        # subprocess.call("lftp -e 'put -O infosial /home/infosial/cabreraImg/" + str(pedido) + ".jpg; bye' -u infosialbnp,1nfosial ftp.barnaplant.com", shell=True)
        # filename = request.POST['image']
        # print(filename)
        # return HttpResponse(renderers.JSONRenderer().render(dict()),content_type="application/json")
        url = '/facturacion/pedidoscli/' + str(pedido)
        url = '/facturacion/imagencarro/' + str(pedido) + "/" + str(carro)
        return HttpResponseRedirect(url)

    def vbarba_cabrera_imagencarro(self, request, pedido, carro):
        print(pedido)
        return render(request, 'facturacion/uploadimagencarro.html', {"pedido": str(pedido), "carro": str(carro)})

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

    def uploadimagencarro(self, request, pedido, carro):
        return self.ctx.vbarba_cabrera_uploadimagencarro(request, pedido, carro)

    def imagencarro(self, request, pedido, carro):
        return self.ctx.vbarba_cabrera_imagencarro(request, pedido, carro)

    def handle_uploaded_file(self, source, name):
        return self.ctx.vbarba_cabrera_handle_uploaded_file(source, name)

