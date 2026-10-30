from .Notificacion import Notificacion


class NotificacionUrgente(Notificacion):
    def enviar(self, destinatario: str, texto: str) -> None:
        self._canal.enviarMensaje(destinatario, f"URGENTE: {texto}")
