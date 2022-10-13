from requests import Response
import json


class AuthenticationError(Exception):
    """Se genera cuando la clave de API proporcionada no es válida"""
    pass


class InvalidQueryError(Exception):
    """Se genera cuando no se encuentra un parámetro de consulta"""
    pass


def check_response(r: Response):
    if r.status_code == 401:
        raise AuthenticationError(r.text)
    elif r.status_code == 404:
        raise InvalidQueryError(r.text)
    elif r.status_code == 400:
        raise InvalidQueryError(r.text)
    try:
        return r.json()
    except json.decoder.JSONDecodeError:
        return r
