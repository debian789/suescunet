suescunet
=========

Administrar archivos de código fuente desde una aplicación web hecha con Django 

El proyecto consisten en poder ingresar códigos fuentes, proyectos, diagramas, sitios web, los cuales ayuden al aprendizaje y retención de información, he notado que cuando se esta iniciando en desarrollo tener códigos de referencia ayuda bastante, buscar códigos en internet es sencillo lo complejo es cuando encuentras uno que satisface tu necesidad lo modificas para adaptarlo mejor y queda en unos de los proyectos que realízate, y quieras desarrollar algún producto que implemente ese código que desarrollaste y tengas que buscar las pagina donde los tomaste o buscar en el el proyecto donde lo implémentate, la idea de este software es ayudar en esa gestión, almacenar y gestionar  ese código fuente que tanto te demórate en desarrollar que satisface una necesidad especifica. 


Instalación 

Ejecutar los siguentes comandos en consola 

pip install -r requirements.txt

python manage.py syncdb 

python manage.py runserver



ingresar a la url http://127.0.0.1:8000/ falta la pagina de inicio estan habilitadas las urls 

http://127.0.0.1:8000/admin
http://127.0.0.1:8000/codigos
http://127.0.0.1:8000/galeria 


al ingresar por primera vez al sitio web  es necesario ingresar al panel de administración  http://127.0.0.1:8000/admin en la sección de "Elementos_Comunes"  e ingresar los datos:
  - En "lenguaje"  ingresar los lenguajes de programación que crea necesarios, Ejemplo: python, java, javascript, en minusculas 
  - En "Sistema Operativos" ingresar los que considere necesarios, Ejemplo: Linux, Mac, Qnx, Android, Windows



los campos de los formularios no se encuentran validados así que tener cuidado al ingresar los datos especialmente cuando piden urls. 

Se han aplicados los conceptos aprendidos en Mejorando.la en los cursos de frontend y backend 


