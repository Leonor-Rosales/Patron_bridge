from ..contratos.Canal import Canal


class CanalWhatsApp(Canal):
    def __init__(self, disponible: bool) -> None:
        self.disponible = disponible

    def enviarMensaje(self, destinatario: str, texto: str) -> None:
        if not self.disponible:
            raise ConnectionError("El servicio de WhatsApp no está disponible")
        print(f"WHATSAPP a {destinatario}: {texto}")
