def my_model_context_processor(request):
    from .models import About
    about = About.objects.get(id=1)  # یا هر روش دیگری برای دریافت مدل

    return {'title': about}