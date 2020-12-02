from django.db import models


# Create your models here.
# This is the model for Pokemon Types
class PokemonType(models.Model):
    pokemon_type_name = models.CharField(max_length=200)

    # Show pokemon Type
    def __str__(self):
        return self.pokemon_type_name


# This is the model for Pokemon Species
class PokemonSpecie(models.Model):
    pokemon_name = models.CharField(max_length=200)
    evolution_level = models.IntegerField(default='-', blank=True, null=True)
    next_evolution = models.ForeignKey('PokemonSpecie', on_delete=models.CASCADE, blank=True, null=True)
    pokemon_type = models.ManyToManyField(PokemonType, related_name='species')

    # Show the types of each pokemon
    def show_type(self):
        return list(self.pokemon_type.all())

    # Show pokemon name
    def __str__(self):
        return self.pokemon_name


# Pokemon Trainers model
class Trainer(models.Model):
    trainer_name = models.CharField(max_length=200)

    def __str__(self):
        return self.trainer_name


# This is the model for Pokemon and its trainers
class Pokemon(models.Model):
    pokemon_nickname = models.CharField(max_length=200)
    pokemon_specie = models.ForeignKey(PokemonSpecie, on_delete=models.CASCADE)
    pokemon_level = models.IntegerField(default=0)
    pokemon_trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    # This code is for the evolution of the pokemon
    def save(self, *args, **kwargs):
        pokemon_evolution_level = self.pokemon_specie.evolution_level
        if pokemon_evolution_level is not None:
            if self.pokemon_level >= pokemon_evolution_level:
                self.pokemon_specie = self.pokemon_specie.next_evolution
        else:
            self.pokemon_specie = self.pokemon_specie
        super(Pokemon, self).save(*args, **kwargs)

    # Show pokemon nicknames
    def __str__(self):
        return self.pokemon_nickname
