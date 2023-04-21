from api_client.types import CrudApiClient, UrlSchema


class EBalAPI(CrudApiClient):
    ...


if __name__ == '__main__':
    client = EBalAPI(
        base_url='127.0.0.1:8000/api', api_version=1,
        token='50dbd59b4078e42dceb65d142debd89c52106a69',
        schema=UrlSchema.HTTP,
    )

    print(client.bullet.get(5))
