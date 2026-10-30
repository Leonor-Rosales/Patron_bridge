from ..contratos.Canal import Canal


class CanalSMS(Canal):
    def enviarMensaje(self, destinatario: str, texto: str) -> None:
        print(f"SMS a {destinatario}: {texto}")
