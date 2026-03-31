from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product

admin.site.site_header = mark_safe(
    '''
    <style>
        :root {
            --primary: #3e2a1c !important;
            --header-bg: #3e2a1c !important;
            --header-color: #b8860b !important;
            --link-color: #8b4513 !important;
        }
        #header, .module h2, .panel h2, header { 
            background: #3e2a1c !important; 
            color: #b8860b !important;
        }
        div#header #branding h1, div#header #branding h1 a { 
            color: #b8860b !important; 
        }
        .breadcrumbs, .breadcrumbs a { 
            background: #5c4033 !important; 
            color: #f5e6be !important; 
        }
        input[type=submit], .button, .submit-row input {
            background: #3e2a1c !important;
            color: #b8860b !important;
            border: 1px solid #b8860b !important;
        }
        body, #content {
            background-color: #fdfaf5 !important;
        }
        .module h2 {
            background: #3e2a1c !important;
            color: #b8860b !important;
        }
        a:link, a:visited {
            color: #8b4513 !important;
        }
    </style>
    <span style="color: #b8860b; font-family: Georgia; font-weight: bold;">The Gilded Thread Boutique</span>
    '''
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')