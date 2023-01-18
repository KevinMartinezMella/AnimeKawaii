from django.db import models

class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=150)

class Anime(models.Model):
    nombreAnime = models.CharField(max_length=255)
    descripcionAnime = models.TextField()
    numeroEpisodios = models.IntegerField(null=True, blank=True)
    imagenAnime = models.CharField(max_length=255)
    fechaEstreno = models.DateField()
    fechaTermino = models.DateField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)

class CategoriaAnime(models.Model):
    idAnime = models.ForeignKey(Anime, on_delete =models.PROTECT)
    idCategoria = models.ForeignKey(Categoria, on_delete =models.PROTECT)

class Episodio(models.Model):
    numeroEpisodio = models.IntegerField()
    urlEpisodio = models.CharField(max_length=500)
    idAnime = models.ForeignKey(Anime, on_delete=models.PROTECT)

