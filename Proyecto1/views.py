from django.http import HttpResponse
from django.template import Template, Context

def test_template(request):
    datos = {"nombre":"Pepe" , "notas":[3,6,10,5,8,5,4]}
    plantilla = loader.get_template("template.html")
    documento = plantilla
    return HttpResponse(documento)



def test_template(request):

    pass

    mi_html = open("C:/Python - Coder/Clase 18/Proyecto1/Proyecto1/Plantillas/template.html")


    plantilla = Template( mi_html.read() )

    mi_html.close()

    mi_contexto = Context({"nombre":"Pepe" , "notas":[3,6,10,5,8,5,4]})

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)
