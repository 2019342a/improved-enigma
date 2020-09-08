from django.contrib.admin.apps import AdminConfig


class SkorAdminConfig(AdminConfig):
    default_site = "config.admin.SkorAdmin"
