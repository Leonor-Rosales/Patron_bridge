from abc import ABC, abstractmethod


class Canal(ABC):
    """Contrato común para los canales de envío del patrón Bridge."""

    @abstractmethod
    def enviarMensaje(self, destinatario: str, texto: str) -> None:
        """Envía el mensaje o lanza ConnectionError si no está disponible."""
