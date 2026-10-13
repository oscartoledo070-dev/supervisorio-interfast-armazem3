# config.py

MOTORES_INICIAIS = {
    f"Motor {i}": {
        "id": i,
        "modo_controle": "AUTO",     # "AUTO" ou "MANUAL"
        "comando_manual": "LIGADO",  # "LIGADO" ou "DESLIGADO" quando estiver em manual
        "status": "DESLIGADO",
        "motivo": "Sistema Inicializado",
        "corrente_A": 0.0
    } for i in range(1, 7)
}