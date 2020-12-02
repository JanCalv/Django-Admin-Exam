from django.contrib import admin
from .models import PokemonType, PokemonSpecie, Pokemon, Trainer


# Register your models here.

# Show fields for PokemonSpecie Model
class PokemonSpecieAdmin(admin.ModelAdmin):
    filter_horizontal = ('pokemon_type',)
    list_display = ('pokemon_name', 'evolution_level', 'next_evolution', 'show_type',)


# Show fields for Pokemon Model
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('pokemon_nickname', 'pokemon_specie', 'pokemon_level', 'pokemon_trainer')


admin.site.register(PokemonType)
admin.site.register(PokemonSpecie, PokemonSpecieAdmin)
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Trainer)
