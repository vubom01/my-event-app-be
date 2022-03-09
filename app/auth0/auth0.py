import jwt

from app.core.config import settings


class Auth0Service:
    def __init__(self):
        jwks_url = f'https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json'
        self.jwks_client = jwt.PyJWKClient(jwks_url)

    def verify(self, token):
        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(token).key
        except jwt.exceptions.PyJWKClientError as error:
            return {"status": "error", "msg": error.__str__()}
        except jwt.exceptions.DecodeError as error:
            return {"status": "error", "msg": error.__str__()}
        try:
            payload = jwt.decode(
                token,
                signing_key,
                algorithms=settings.AUTH0_ALGO,
                audience=settings.AUTH0_AUDIENCE,
                issuer=settings.AUTH0_BASE_URL,
            )
        except Exception as e:
            return {"status": "error", "message": str(e)}

        return payload
