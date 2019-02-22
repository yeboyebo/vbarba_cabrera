from AQNEXT.celery import app
from YBLEGACY import qsatype
from YBUTILS import globalValues
from YBUTILS import DbRouter
from YBLEGACY.constantes import *
from YBUTILS.viewREST import fileAttachment
from YBUTILS import notifications


globalValues.registrarmodulos()


@app.task
def prueba(param):
    print(param)


@app.task
def enviomail(aCodProv):
    indice = 0
    while indice < len(aCodProv):
        emailProveedor = dameEmailsProveedorer(aCodProv[indice]["codproveedor"])
        aCodProv[indice]['emailproveedor'] = emailProveedor
        filepath = generarReport(aCodProv[indice])
        enviarReport(aCodProv[indice], filepath)
        indice += 1


@app.task
def dameEmailsProveedorer(codProveedor):
    listaEmails = ""
    emailPrincipal = qsatype.FLUtil.sqlSelect(u"proveedores", u"email", ustr(u"codproveedor = '", codProveedor, u"'"))

    q = qsatype.FLSqlQuery()
    q.setTablesList("contactosproveedores,crm_contactos")
    q.setFrom("contactosproveedores INNER JOIN crm_contactos ON contactosproveedores.codcontacto = crm_contactos.codcontacto")
    q.setSelect("crm_contactos.email,crm_contactos.nombre")
    q.setWhere("contactosproveedores.codproveedor = '" + codProveedor + "' AND (crm_contactos.email <> '' AND crm_contactos.email IS NOT NULL)")
    if not q.exec_():
        if emailPrincipal and emailPrincipal != "":
            listaEmails = emailPrincipal
        return listaEmails
    if q.size() > 1:
        while q.next():
            listaEmails += q.value(0) + ","
        listaEmails = listaEmails[:len(listaEmails) - 1]
        return listaEmails
    else:
        return emailPrincipal


@app.task
def generarReport(aProveedor):
    report = {}
    nombreBD = qsatype.FLUtil.nameBD()
    report['reportName'] = "vb_pedidosprov"
    if nombreBD == u"cabrera":
        report['reportName'] = "vb_pedidosprov"
    elif nombreBD == u"cash":
        report['reportName'] = "vb_cash_pedidosprov"
    elif nombreBD == u"barnaplant":
        report['reportName'] = "vb_bnp_pedidosprov"
    report['params'] = {}
    report['params']['WHERE'] = "pedidosprov.codigo = '" + str(aProveedor['codigo']) + u"'"
    filename = "Pedido_" + str(aProveedor['codigo'])
    filepath = fileAttachment.saveJReport(filename, report['reportName'], report["params"], "/tmp")
    print("generarReport___FIN")
    return filepath


@app.task
def enviarReport(aProveedor, filepath):
    asunto = qsatype.FactoriaModulos.get('flfacturac').iface.valorDefecto(u"asuntoemail")
    cuerpo = qsatype.FactoriaModulos.get('flfacturac').iface.valorDefecto(u"cuerpoemail")
    if not asunto:
        asunto = ""
    if not cuerpo:
        cuerpo = ""
    oDM = {}
    oDM = datosConfigMail()
    # connection = notifications.get_connection("smtp.gmail.com", "todos.yeboyebo@gmail.com", "555zapato", "465", "SSL")
    connection = notifications.get_connection(oDM["hostcorreosaliente"], oDM["usuariosmtp"], oDM["passwordsmtp"], oDM["puertosmtp"], oDM["tipocxsmtp"])
    response = notifications.sendMail(connection, oDM["usuariosmtp"], asunto, cuerpo, [aProveedor['emailproveedor']], filepath)
    print("enviarReport___FIN___response: ", response)
    return response


@app.task
def datosConfigMail():
    oDM = {}
    q = qsatype.FLSqlQuery()
    q.setSelect("hostcorreosaliente, puertosmtp, tipocxsmtp, tipoautsmtp, usuariosmtp, passwordsmtp")
    q.setFrom(u"factppal_general")
    q.setWhere(u"1 = 1")
    print("Consulta_: ", q.sql())
    if not q.exec_():
        return False
    if q.first():
        oDM["hostcorreosaliente"] = q.value("hostcorreosaliente")
        oDM["puertosmtp"] = q.value("puertosmtp")
        oDM["tipocxsmtp"] = q.value("tipocxsmtp")
        oDM["tipoautsmtp"] = q.value("tipoautsmtp")
        oDM["usuariosmtp"] = q.value("usuariosmtp")
        oDM["passwordsmtp"] = q.value("passwordsmtp")
    print("datosConfigMail___FIN")
    return oDM
