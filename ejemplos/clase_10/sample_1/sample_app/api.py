from ninja import NinjaAPI, Schema
from django.contrib.auth import authenticate
from django.http import HttpRequest
from .utils import generar_token, validar_token, JWTAuth

api = NinjaAPI(
    title="API de Ejemplo",
    version="1.0.0",
    description="Esta es una API de ejemplo", 
)
auth = JWTAuth()


class AuthRequest(Schema):
    username: str
    password: str


@api.post("/token", tags=["Auth"])
def obtener_token(request: HttpRequest, data: AuthRequest):
    user = authenticate(username=data.username, password=data.password)
    if not user:
        return { "error": "Credenciales inválidas" }
    token = generar_token(user)
    return { "token": token }


@api.get("/public", tags=["Public"])
def datos_publicos(request):
    return { "mensaje": "Bienvenido a la zona pública" }


@api.get("/private", auth=auth, tags=["Private"])
def datos_protegidos(request):
    return { "mensaje": f"Bienvenido, {request.auth.username}" }

