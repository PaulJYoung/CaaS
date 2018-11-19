from django.contrib import admin

# from .models import Material
from .models import Material, AWS, Azure, Google, ContactUs, Lists, UpdateText

@admin.register(Material, AWS, Azure, Google, ContactUs, Lists, UpdateText)

class DefaultAdmin(admin.ModelAdmin):
	pass
#myModels = [models.SiteCategories, models.Entities]

#admin.site.register(SiteCategories, Entities)
#admin.site.register(myModels)

# Register your models here.
