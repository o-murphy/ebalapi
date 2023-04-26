from py_eballistica_api.client.client import CrudApiClient
from py_eballistica_api.client import flags, types


class ApiClient(CrudApiClient):

    def login(self, username: str, password: str, **kwargs):
        result = self.session.request(
            flags.HttpMethod.POST, f'{self.base_url}/auth/', json={"username": username, "password": password}
        )

        if not result:
            return None
        auth_data = types.AuthData(**result.json())
        self.token = auth_data.token
        return auth_data


if __name__ == '__main__':
    client = ApiClient(
        base_url='127.0.0.1:8000/api', api_version=1,
        token='<token>',
        schema=flags.UrlSchema.HTTP,
    )

    # auth
    # print(client.login('<login>', '<pass>'))

    # res_instance = client.<resource_name>.get(5)
    # res_property = res_instance.<prop_name>
    # nested_res_instances = res_property.<nested_resource_name>.list()
