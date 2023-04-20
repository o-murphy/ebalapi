from typing import Iterable


class AbstractEBalAPIObject(object):

    def __init__(self, api_client: 'EBalAPI', **kwargs):
        self.__api_client = api_client
        for key, val in kwargs.items():
            self.__setattr__(key, val)

    def __getattr__(self, action):
        """
        Enable the calling of eBallistica API methods through Python method calls
        of the same name.
        """
        if action == '__api_client':
            return self.__api_client
        elif hasattr(self, f'{action}_url'):
            return self.__call(action)
        elif hasattr(self, action):
            return super(AbstractEBalAPIObject, self).__getattribute__(action)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{action}'")

    def json(self):
        output: dict = {k: v for k, v in self.__dict__.items() if type(v) in [int, float, str]}
        # output.pop('_AbstractEBalAPIObject__api_client')
        return output

    def __dir__(self) -> Iterable[str]:

        output: Iterable = super(AbstractEBalAPIObject, self).__dir__()
        output += [key.replace('_url', '') for key in self.__dict__.keys() if key.endswith('_url')]
        return set(output)

    def __call(self, action):
        response = self.__api_client.request(
            action, url=self.__getattribute__(f'{action}_url'),
            params={'token': self.__api_client.token}
        )

        response.update({'action': action})

        # return response
        return self.__api_client.parse(response)
