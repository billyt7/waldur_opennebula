from waldur_core.core import WaldurExtension


class OpenNebulaExtension(WaldurExtension):
    class Settings:
        WALDUR_OPENNEBULA = {
            'BASIC_MODE': False,
        }

    @staticmethod
    def get_public_settings():
        return ['BASIC_MODE']

    @staticmethod
    def django_app():
        return 'waldur_opennebula'

    @staticmethod
    def rest_urls():
        from .urls import register_in

        return register_in
