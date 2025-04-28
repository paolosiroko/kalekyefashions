from .models import Category

def categories(request):
    return {
        'categories': Category.objects.filter(is_active=True, parent=None).prefetch_related('subcategories').order_by('title')
    }
