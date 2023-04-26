from dataclasses import dataclass

from .flags import HttpMethod


class AbstractRelatedResource:
    def __init__(self, instance: 'ResourceInstance', name: str):
        self.instance = instance
        self.resource = Resource(instance.resource.api_client, name)

    def __repr__(self):
        return f"<RelatedResource: {self.resource.name.capitalize()} for {self.instance}>"


class RelatedList(AbstractRelatedResource):
    def list(self, **extra_params) -> list['ResourceInstance']:
        response = self.resource.api_client.request(
            HttpMethod.GET,
            f"{self.resource.url()}?{self.instance.resource.name}={self.instance.id}",
            json=extra_params
        )
        return [self.resource.from_dict(item) for item in response]


class RelatedRetrieve(AbstractRelatedResource):
    def get(self, **extra_params) -> 'ResourceInstance':
        resource_id = self.instance.__getattribute__(f'{self.resource.name}_id')
        response = self.resource.api_client.request(
            HttpMethod.GET,
            f"{self.resource.url()}{resource_id}",
            json=extra_params
        )
        return self.resource.from_dict(response)


class RelatedResource(RelatedList, RelatedRetrieve):
    ...


class ResourceInstance:

    def __init__(self, resource: 'Resource', data: dict):
        self.resource = resource
        self.id = data['id']

        self.__dict__.update(data)

    def __repr__(self):
        return f"<ResourceInstance: {self.resource.name.capitalize()}, id: {self.id}>"

    def update(self, **extra_params) -> 'ResourceInstance':
        response = self.resource.update(self.id, **extra_params)
        return response

    def delete(self, **extra_params) -> dict:
        response = self.resource.delete(self.id, **extra_params)
        return response

    def __getattribute__(self, name):
        try:
            if object.__getattribute__(self, f'{name}_url'):

                return RelatedResource(self, name)
            raise AttributeError(f'{self.__repr__()} has no attribute {name}')
        except AttributeError:
            try:
                return super(ResourceInstance, self).__getattribute__(name)
            except AttributeError as err:
                raise AttributeError(f'{self.__repr__()} has no attribute {err.name}')

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
        response = self.api_client.request(
            HttpMethod.GET,
            self.url(),
            **extra_params
        )
        return [self.from_dict(item) for item in response]

    def get(self, id: int) -> 'ResourceInstance':
        response = self.api_client.request(HttpMethod.GET, self.url(id))
        return self.from_dict(response)

    def create(self, **extra_params) -> 'ResourceInstance':
        response = self.api_client.request(HttpMethod.POST, self.url(), data=extra_params)
        return self.from_dict(response)

    def update(self, id: int, **extra_params) -> 'ResourceInstance':
        response = self.api_client.request(HttpMethod.PATCH, self.url(id), data=extra_params)
        return self.from_dict(response)

    def delete(self, id: int, **extra_params) -> dict:
        response = self.api_client.request(HttpMethod.DELETE, self.url(id), data=extra_params)
        return response

    def from_dict(self, data: dict) -> 'ResourceInstance':
        return ResourceInstance(self, data)
