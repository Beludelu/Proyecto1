from django.shortcuts import render
from AppCoder.models import Curso
from django.template import loader
from django.http import HttpResponse
from AppCoder.forms import Curso_form

def inicio(request):
        return render( request , "padre.html")

def ver_cursos(request):
        cursos = Curso.object.all() #comunicacion con la base de datos directo
        dicc = {"cursos":cursos}
        plantillas = loader.get_template("plantillas.html")
        documento = plantillas.render(dicc)
        return HttpResponse(documento) #aca me va a venir la plantilla renderizada con los datos

#def alta_curso(request, nombre , comision):
        curso = Curso(nombre=nombre , comision=comision)
        curso.save() #hace el registro y el .save() siempre lo guarda en la base de datos
        texto = f"Se guardo en el BD el Curso: {curso.nombre} Comision: {curso.comision}"
        return HttpResponse(texto) #aca estoy renderizando

#hasta aca pudimos hacer altas y lectura de datos

def profesores(request):
        return render( request , "profesores.html") #lo unico que esta haciendo aca es renderizarlo

def alumnos(request):
        return render( request , "alumnos.html")

def curso_formulario(request):
        if request.method == "POST":

            mi_formulario = Curso_form( request.POST )



            if mi_formulario.is_valid():
                datos = mi_formulario.cleaned_data

            curso = Curso( nombre=datos["nombre"] , comision=datos["comision"])
            curso.save()
            return render( request , "formulario.html")      
        return render( request , "formulario.html")

def buscar_curso(request):
       return render( request , "buscar_curso.html")

def buscar(request):
       if request.GET["nombre"]:
                nombre = request.GET["nombre"]
                cursos = Cursos.object.filter(nombre_icontains = nombre)
                return render( request , "resultado_busqueda.html" , {"Cursos": cursos})
       else:
              return HttpResponse("Campo vacio")