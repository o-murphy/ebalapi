from api_client.client import EBalApiClient, UrlSchema, DiameterInstance


class EBallisticaAPI(EBalApiClient):
    ...


if __name__ == '__main__':
    client = EBallisticaAPI(
        base_url='127.0.0.1:8000/api', api_version=1,
        token='50dbd59b4078e42dceb65d142debd89c52106a69',
        schema=UrlSchema.HTTP,
    )

    diameter = client.caliber.get(5).rifle
    # print(diameter.rifle.get())

    cal = client.caliber.get(5)
    print(diameter)

