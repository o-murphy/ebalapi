from api_client.client.client import EBalApiClient
from api_client.client import flags, types


class EBallisticaAPI(EBalApiClient):
    ...


if __name__ == '__main__':
    client = EBallisticaAPI(
        base_url='127.0.0.1:8000/api', api_version=1,
        token='50dbd59b4078e42dceb65d142debd89c52106a69',
        schema=flags.UrlSchema.HTTP,
    )
    bullets = client.bullets.get(5)
    d = bullets.diameter

    d = d.get()