from py_eballistica_api.client.client import EBalApiClient
from py_eballistica_api.client import flags, types


class EBallisticaAPI(EBalApiClient):
    ...


if __name__ == '__main__':
    client = EBallisticaAPI(
        base_url='127.0.0.1:8000/api', api_version=1,
        token='50dbd59b4078e42dceb65d142debd89c52106a69',
        schema=flags.UrlSchema.HTTP,
    )
    bullets = client.bullets.get(5)
    d: types.DiameterInstance = bullets.diameter.get()
