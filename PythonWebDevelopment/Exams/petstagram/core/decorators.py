from django.shortcuts import redirect


def can_like(model_class):
    def decorator(view_func):
        def wrapper(request, pet_id, *args, **kwargs):
            model_obj = model_class.objects.get(pk=pet_id)

            if model_obj.user.id != request.user.id:
                return view_func(request, pet_id, *args, **kwargs)
            return redirect('redirect:login')

        return wrapper

    return decorator


def can_delete_or_edit(model_class):
    def decorator(view_func):
        def wrapper(request, pet_id, *args, **kwargs):
            model_obj = model_class.objects.get(pk=pet_id)

            if model_obj.user.id == request.user.id:
                return view_func(request, pet_id, *args, **kwargs)
            return redirect('redirect:login')

        return wrapper

    return decorator
