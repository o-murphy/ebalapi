from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response


from rest_framework import serializers

from ebalapi_service.models import Diameter


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('pk', )



class GetTokenAuthentication(TokenAuthentication):

    def authenticate(self, request: Request):
        query_params = request.query_params.dict()
        query_params.update(**request.data)

        token = query_params.get('token')
        if not token:
            return None
        if len(token) == 1:
            msg = 'Invalid token parameter. No credentials provided.'
            raise AuthenticationFailed(msg)

        return self.authenticate_credentials(token)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)  # objects: QuerySet
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class AuthView(generics.RetrieveAPIView):
    authentication_classes = [
        # SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
        GetTokenAuthentication
    ]
    permission_classes = [IsAuthenticated]

    serializer_class = TokenSerializer

    def get(self, request: Request, *args, **kwargs):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
            # 'sid': str(request.session._SessionBase__session_key)
        }
        return Response(content)
