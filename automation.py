# automation.py

def calcular_automacao(motores, temperatura, chuva, umidade, form_data):
    for nome, dados in motores.items():
        # Captura o modo de controlo enviado pelo formulário para este motor específico
        modo_ctrl = form_data.get(f"modo_{nome}", dados.get("modo_controle", "AUTO"))
        cmd_manual = form_data.get(f"cmd_{nome}", dados.get("comando_manual", "DESLIGADO"))
        
        dados["modo_controle"] = modo_ctrl
        dados["comando_manual"] = cmd_manual

        if modo_ctrl == "MANUAL":
            # Modo Manual: O operador manda diretamente
            dados["status"] = cmd_manual
            if cmd_manual == "LIGADO":
                dados["motivo"] = "Forçado Manualmente (LIGADO)"
                dados["corrente_A"] = 18.5
            else:
                dados["motivo"] = "Forçado Manualmente (DESLIGADO)"
                dados["corrente_A"] = 0.0
        else:
            # Modo Automático: Regras de Termometria e Segurança
            if chuva:
                dados["status"] = "DESLIGADO"
                dados["motivo"] = "Bloqueio de Segurança: Chuva Detectada"
                dados["corrente_A"] = 0.0
            elif temperatura > 24.0 and umidade < 70.0:
                dados["status"] = "LIGADO"
                dados["motivo"] = "Ciclo Ativo: Resfriamento (Auto)"
                dados["corrente_A"] = 18.5
            elif temperatura > 24.0 and umidade >= 70.0:
                dados["status"] = "DESLIGADO"
                dados["motivo"] = "Espera: Humidade Relativa Alta (>70%)"
                dados["corrente_A"] = 0.0
            else:
                dados["status"] = "DESLIGADO"
                dados["motivo"] = "Condições Estáveis (Massa Armazenada OK)"
                dados["corrente_A"] = 0.0
            
    return motores