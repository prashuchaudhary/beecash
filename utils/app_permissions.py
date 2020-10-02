from django.contrib.auth.management import create_permissions


def create_required_permissions_for_app(app_label, apps):
    app_config = apps.get_app_config(app_label=app_label)
    app_config.models_module = True
    create_permissions(app_config, apps=apps, verbosity=0)
    app_config.models_module = None
