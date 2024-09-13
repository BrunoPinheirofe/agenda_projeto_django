from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact) 
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','phone','email',) #configura os campos que seram exibidos na area administrativa
    
    ordering = '-id', #ordena pelo id de forma decrescente
    
    
    list_filter = 'created_date', #cria um filtro com base na data e hora
    search_fields = 'first_name','id','last_name', # modo de pesquisa
    list_per_page = 10 #configura quantos dados por pagina serão exibidos
    
    list_max_show_all = 1000 # o maximo de dados que podem ser exibidos
    #list_editable = 'firt_name', 'last_name',
    list_display_links = 'first_name',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= 'category_name',
 
    