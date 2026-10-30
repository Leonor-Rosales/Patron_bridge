from typing import TYPE_CHECKING

from .Notificacion import Notificacion

if TYPE_CHECKING:
    from ..contratos.Canal import Canal


class NotificacionConRespaldo(Notificacion):
    """Cambia permanentemente al respaldo si falla el canal principal."""

    def __init__(self, canal: "Canal", respaldo: "Canal") -> None:
        super().__init__(canal)
        self._respaldo = respaldo
        self._usando_respaldo = False

    def enviar(self, destinatario: str, texto: str) -> None:
        if self._usando_respaldo:
            self._canal.enviarMensaje(destinatario, texto)
            return

        try:
            self._canal.enviarMensaje(destinatario, texto)
        except ConnectionError:
            print("Canal no disponible, usando respaldo")
            self._canal = self._respaldo
            self._usando_respaldo = True
            self._canal.enviarMensaje(destinatario, texto)
