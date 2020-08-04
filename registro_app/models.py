from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class Brigada(models.Model):
    nombre = models.CharField(max_length=255)
    jefe = models.ForeignKey(Persona, on_delete=models.CASCADE)
    integrantes = models.ManyToManyField(
        Persona, verbose_name='lista de integrantes', related_name='integrantes')

    def __str__(self):
        return self.nombre


class Especialidad(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Objeto(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Zona(models.Model):
    nombre = models.CharField(max_length=255)
    objetos = models.ManyToManyField(Objeto, verbose_name="lista de objetos")

    def __str__(self):
        return self.nombre


class Obra(models.Model):

    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Convenio(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.codigo


class MesEnCurso(models.Model):

    class Mes(models.IntegerChoices):
        Enero = 1
        Febrero = 2
        Marzo = 3
        Abril = 4
        Mayo = 5
        Junio = 6
        Julio = 7
        Agosto = 8
        Septiembre = 9
        Octubre = 10
        Noviembre = 11
        Diciembre = 12

    mes = models.IntegerField(choices=Mes.choices, default=-1)
    anno = models.IntegerField()
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.mes) + '/' + str(self.anno)


class QSE(models.Model):
    nro = models.IntegerField(unique=True, blank=True)
    # especialidad
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    # convenio
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE)
    # actividad
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    # brigada
    brigada = models.ForeignKey(Brigada, on_delete=models.CASCADE)
    # zona
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    # objeto
    objeto = models.ForeignKey(Objeto, on_delete=models.CASCADE)
    # clasificacion
    clasificacion = models.CharField(max_length=10, default='FAC')
    # mes_en_curso
    mes_en_curso = models.ForeignKey(MesEnCurso, on_delete=models.CASCADE)

    fecha = models.DateField()
    aprobacion = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)
