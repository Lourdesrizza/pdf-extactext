"""Excepciones personalizadas del dominio."""


class DomainException(Exception):
    """Excepción base para errores de dominio."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class NotFoundException(DomainException):
    """Recurso no encontrado."""

    def __init__(self, resource_name: str, resource_id: str) -> None:
        message = f"{resource_name} con ID '{resource_id}' no encontrado"
        super().__init__(message)


class ValidationException(DomainException):
    """Error de validación de datos."""

    def __init__(self, field: str, message: str) -> None:
        self.field = field
        super().__init__(message)
