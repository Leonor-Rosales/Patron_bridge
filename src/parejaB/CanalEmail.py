from ..contratos.Canal import Canal


class CanalEmail(Canal):
    def enviarMensaje(self, destinatario: str, texto: str) -> None:
        print(f"EMAIL a {destinatario}: {texto}")
