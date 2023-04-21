import requests


from api_client.types import UrlSchema, HttpMethod


class RelatedResource:
    def __init__(self, instance: 'ResourceInstance', name: str):
        self.instance = instance
        self.resource = Resource(instance.resource.api_client, name)

    def __repr__(self):
        return f"<RelatedResource: {self.resource.name.capitalize()} for {self.instance}>"

    def get(self) -> 'ResourceInstance':

        resource_id = self.instance.__getattribute__(f'{self.resource.name}_id')
        response = self.resource.api_client.request(
            HttpMethod.GET, f"{self.resource.url()}{resource_id}"
        )
        return self.resource.from_dict(response)

    def list(self, **extra_params) -> list['ResourceInstance']:
        response = self.resource.api_client.request(
            HttpMethod.GET,
            f"{self.resource.url()}?{self.instance.resource.name}={self.instance.id}",
            **extra_params
        )
        return [self.resource.from_dict(item) for item in response]

    # def create(self, **extra_params) -> 'ResourceInstance':
    #     extra_params[self.instance.name + "_id"] = self.instance.id
    #     response = self.resource.api_client.request(HttpMethod.POST, self.resource.url(), json=extra_params)
    #     return self.resource.from_dict(response)


class ResourceInstance:
    def __init__(self, resource: 'Resource', data: dict):
        self.resource = resource
        self.id = data["id"]
        self.__dict__.update(data)

    def __repr__(self):
        return f"<ResourceInstance: {self.resource.name.capitalize()}, id: {self.id}>"

    # def update(self, data: dict):
    #     updated_data = self.resource.update(self.id, data)
    #     self.__dict__.update(updated_data.__dict__)

    # def delete(self, id: int) -> bool:
    #     response = self.api_client.request(HttpMethod.DELETE, self.url(id))
    #     return response.status_code == 204

    # def related(self, name):
    #     return RelatedResource(self, name)

    def __getattr__(self, name) -> 'RelatedResource':
        return RelatedResource(self, name)


class Resource:
    def __init__(self, api_client: 'CrudApiClient', name: str):
        self.api_client = api_client
        self.name = name

    def __repr__(self):
        return f"<Resource: {self.name.capitalize()}>"

    def url(self, id: int = None):
        url = f"{self.api_client.base_url}/{self.name}/"
        if id is not None:
            url += f"{id}/"
        return url

    def list(self, **extra_params) -> list['ResourceInstance']:
        response = self.api_client.request(HttpMethod.GET, self.url(), **extra_params)
        return [self.from_dict(item) for item in response]

    def get(self, id: int) -> 'ResourceInstance':
        response = self.api_client.request(HttpMethod.GET, self.url(id))
        return self.from_dict(response)

    def create(self, data: dict) -> 'ResourceInstance':
        response = self.api_client.request(HttpMethod.POST, self.url(), json=data)
        return self.from_dict(response)

    def update(self, id: int, data: dict) -> 'ResourceInstance':
        response = self.api_client.request(HttpMethod.PUT, self.url(id), json=data)
        return self.from_dict(response)

    def delete(self, id: int) -> bool:
        response = self.api_client.request(HttpMethod.DELETE, self.url(id))
        return response.status_code == 204

    def from_dict(self, data: dict) -> 'ResourceInstance':
        return ResourceInstance(self, data)


class CrudApiClient:
    def __init__(self, base_url: str,
                 api_version: int,
                 token: str = None,
                 schema: UrlSchema = UrlSchema.HTTP,
                 **extra_params):
        self.token = token

        self.default_params = {'token': self.token}
        self.default_params.update(extra_params)
        self.base_url = f"{schema}{base_url}/v{api_version}"
        self.session = requests.Session()

    def __getattr__(self, name):
        return Resource(self, name)

    def request(self, method: HttpMethod, url: str, **extra_params) -> dict:
        params = self.default_params.copy()
        params.update(extra_params)
        print(url)
        response = self.session.request(method, url, params=params)
        response.raise_for_status()
        return response.json()


if __name__ == '__main__':
    client = CrudApiClient(
        base_url='127.0.0.1:8000/api', api_version=1,
        token='50dbd59b4078e42dceb65d142debd89c52106a69',
        schema=UrlSchema.HTTP,
    )

    bullet = client.bullet.list(id=5)

    print(bullet)
