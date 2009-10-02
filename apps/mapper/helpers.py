def get_app(application_id):
    try:
        application = Application.objects.get(title = application_id)
    except Application.DoesNotExist:
        application = get_object_or_404(Application, id = application_id)
    return application