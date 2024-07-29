from django.contrib.auth import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'subcategory', 'price', 'description')
    list_filter = ('category', 'subcategory')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image')
    prepopulated_fields = {'slug': ('name',)}


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image', 'category')
    prepopulated_fields = {'slug': ('name',)}
