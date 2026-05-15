# Lista de eventos suspeitos
suspeitas = [
    "Failed password",
    "authentication failure",
    "sudo failed"
]

# Abre o arquivo de log
with open("sample.log", "r") as arquivo:

    # Lê linha por linha
    for linha in arquivo:

        # Verifica cada evento suspeito
        for palavra in suspeitas:

            # Se encontrar evento suspeito
            if palavra in linha:

                print("[ALERTA] Evento suspeito detectado:")
                print(linha)
