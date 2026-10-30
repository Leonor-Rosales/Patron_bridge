from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..contratos.Canal import Canal


class Notificacion(ABC):
    """Abstracción que delega el envío a un canal intercambiable.

    El canal debe ofrecer enviarMensaje(destinatario, texto) y lanzar
    ConnectionError cuando no esté disponible.
    """

    def __init__(self, canal: "Canal") -> None:
        self._canal = canal

    @abstractmethod
    def enviar(self, destinatario: str, texto: str) -> None:
        """Envía una notificación utilizando el canal asociado."""
