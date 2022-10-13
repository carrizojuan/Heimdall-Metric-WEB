from .client import ConsoleClient


API_KEY = ""


def test_console_client():
    # inicializar cliente
    client = ConsoleClient(api_key=API_KEY)

    # lista de dispositivos
    devices = client.get_devices()

    # buscar dispositivo por app key, app eui, dev eui
    single_device = client.get_device_by_details(devices[0].app_eui, devices[0].app_key, devices[0].dev_eui)
    assert devices[0].__dict__ == single_device.__dict__

    # buscar dispositivo por uuid
    uuid_device = client.get_device_by_uuid(devices[0].id)
    assert devices[0].__dict__ == uuid_device.__dict__

    # obtener eventos del dispositivo
    events = client.get_device_events(devices[5].id)

    # obtener integraciones de dispositivo
    integration_events = client.get_device_integration_events(devices[5].id)

    # crear dispositivo
    created_device = client.create_device(name='python-client-test-device',
                                          app_key='850AFDC6F1CF2397D3FEAB8C1850E6E1',
                                          app_eui='B21C36EBBDC0D75F',
                                          dev_eui='ABA47D469E1021AF')

    # lista de etiquetas
    labels = client.get_labels()

    # crear etiqueta
    created_label = client.create_label('python-client-test-label')

    # buscar etiquetas por id
    queried_label = client.search_for_label(created_label.id)
    assert created_label.id == queried_label.id

    # agregar etiqueta a dispositivo
    add_label_result = client.add_device_label(created_device.id, created_label.id)
    assert add_label_result is True

    # eliminar etiqueta de dispositivo
    remove_label_result = client.remove_device_label(created_device.id, created_label.id)
    assert remove_label_result is True

    # eliminar dispositivo
    deleted_device_result = client.delete_device(created_device.id)
    assert deleted_device_result is True

    # eliminar etiqueta
    deleted_label_result = client.delete_label(created_label.id)
    assert deleted_label_result is True
