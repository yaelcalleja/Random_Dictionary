from semillas import ArrayNombres as n
from semillas import ArrayApellidos as a
from semillas import CarrerasCUGdl as c
from semillas import MateriasSemestre1 as m1
from semillas import MateriasSemestre2 as m2
from semillas import MateriasSemestre3 as m3
from semillas import TuplaSemestres as s
import random

# Cree un programa que genere de forma aleatoria y utilizando
# la informacion semilla del archivo "semilla.py" la estructura de codigo
# mencionada en el archivo estructura.py

# Utilice la informacion de clases anteriores.
# La funcion que estructure la informacion,
# debe de regresar un arreglo llamado AspirantesLista

# Generador de codigo de estudiante


def generador_codigo(codigo=[2, 2]):
    if len(codigo) > 8:
        for ent in codigo:
            str(ent)
        return codigo
    else:
        codigo.append(random.randint(1, 9))
        generador_codigo()
    return codigo

# Randomizador de las claves de los diccionario.


def randomizador(diccionario):
    listaDeClaves = list(diccionario)
    key = random.choice(listaDeClaves)
    return key


# Selector de materias dependiendo del semestre

def calificaciones_de_materias(s, materias={}):
    if s == 1:
        for m in m1:
            materias[m] = random.randint(0, 100)
    elif s == 2:
        for m in m2:
            materias[m] = random.randint(0, 100)
    elif s == 3:
        for m in m3:
            materias[m] = random.randint(0, 100)
    else:
        print("No existen materias para este semestre")
    return materias

# Sumador de los valores del dicc para el promedio


def sumador(lista):
    if not lista:
        return 0
    else:
        x = lista.pop()
        listanuaeva = sumador(lista)
        return x + listanuaeva


# Logica principal


def aspirantes_generador(numeroAspirantes, AspirantesLista=[]):
    for i in range(numeroAspirantes):
        semes = random.randint(0, 2)
        sem = s[semes]
        estudiante = {
            'codigo': generador_codigo(),
            'nombre': n[random.randint(0, 4)],
            'apellidoP': a[random.randint(0, 4)],
            'apellidoM': a[random.randint(0, 4)],
            'promedioEP': sumador(list(calificaciones_de_materias(sem).values()))/len(list(calificaciones_de_materias(sem).values())),
            'carrera': randomizador(c),
            'semestre': s[semes],
            'activo': True,
            'calificaciones': calificaciones_de_materias(sem)
        }
        AspirantesLista.append(estudiante)
    return AspirantesLista


print(aspirantes_generador(3))
