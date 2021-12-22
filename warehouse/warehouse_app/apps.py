""" Add configuration storage module"""

from django.apps import AppConfig



class WarehouseAppConfig(AppConfig):
    """ Warehouse - app confiration class"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'warehouse_app'
