from .api_calls import *


class ConsoleClient:
    """Cliente HTTP para interactuar con la API de Helium Console.
    Helium Console expone una API HTTP con puntos finales para administrar dispositivos y etiquetas.
    Inicialice el cliente con esta clase ConsoleClient.
    Consulte los documentos de la API de la consola (https://docs.helium.com/api/console/)
    Atributos:
        api_key: la clave API para su cuenta de Helium Console.
    """

    def __init__(self, api_key: str):
        """Inicializar la cliente con una clave API"""
        self.api_key = api_key

    def get_devices(self):
        """Enumere todos los dispositivos en su cuenta"""
        return get_devices(self.api_key)

    def get_device_by_details(self, app_eui: str, app_key: str, dev_eui: str):
        """Busque un dispositivo por su AppEui, AppKey y DevEui"""
        return get_device_by_details(self.api_key, app_eui, app_key, dev_eui)

    def get_device_by_uuid(self, device_id: str):
        """Buscar un dispositivo por su UUID"""
        return get_device_by_uuid(self.api_key, device_id)

    def get_device_events(self, device_id: str):
        """Obtenga hasta 100 eventos recientes de un dispositivo"""
        return get_device_events(self.api_key, device_id)

    def get_device_integration_events(self, device_id: str):
        """Obtenga hasta 10 eventos de integración recientes desde un dispositivo"""
        return get_device_integration_events(self.api_key, device_id)

    def create_device(self, name: str, app_eui: str, app_key: str, dev_eui: str):
        """Cree un nuevo dispositivo. El estado puede estar 'Pendiente' durante unos minutos
        ACTUALMENTE SE ENCUENTRA DESACTIVADO POR HELIUM, HAY QUE HACERLO DESDE LA PLATAFORMA"""
        return create_device(self.api_key, name, app_eui, app_key, dev_eui)

    def delete_device(self, device_id: str):
        """Eliminar un dispositivo. Devuelve True si tiene éxito"""
        return delete_device(self.api_key, device_id)

    def get_labels(self):
        """Enumera todas las etiquetas en su cuenta"""
        return get_labels(self.api_key)

    def create_label(self, name: str):
        """Crea una nueva etiqueta"""
        return create_label(self.api_key, name)

    def search_for_label(self, label_id: str):
        """Buscar una etiqueta por su id"""
        return search_for_label(self.api_key, label_id)

    def add_device_label(self, device_id: str, label_id: str):
        """Adjuntar una etiqueta a un dispositivo (por UUID)"""
        return add_device_label(self.api_key, device_id, label_id)

    def remove_device_label(self, device_id: str, label_id: str):
        """Desasociar una etiqueta de un dispositivo"""
        return remove_device_label(self.api_key, device_id, label_id)

    def delete_label(self, label_id: str):
        """Eliminar una etiqueta por id"""
        return delete_label(self.api_key, label_id)

    def get_data_credits_balance(self):
        """Obtenemos el balance de créditos de una organización"""
        return get_data_credits_balance(self.api_key)

    def create_mqtt_integration(self, name: str, type: str, endpoint: str, uplink_topic: str, downlink_topic: str):
        """Cree una nueva integración de dispositivo por mqtt"""
        return create_mqtt_integration(self.api_key, name, type, endpoint, uplink_topic, downlink_topic)

    def update_device_active_status(self, active: str, device_id: str):
        """ Actualizar estado de dispositivo"""
        return update_device_active_status(self.api_key, active, device_id)
