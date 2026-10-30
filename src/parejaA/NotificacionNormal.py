from .Notificacion import Notificacion


class NotificacionNormal(Notificacion):
    def enviar(self, destinatario: str, texto: str) -> None:
        self._canal.enviarMensaje(destinatario, texto)
