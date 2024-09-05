import random

agentsTotal = ["Astra", "Breach", "Brimstone", "Chamber", "Clove", "Cypher", "Deadlock", "Fade", "Gekko", "Harbor", "Iso", 
               "Jett", "KAYO", "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Vyse", "Yoru"]

agentes_sorteados = []

def agente_sorteado(exclusao):
    agentes_filtrados = [agente for agente in agentsTotal if agente not in exclusao and agente not in agentes_sorteados]
    
    if not agentes_filtrados:
        return "Não há agentes disponíveis para sorteio."
    
    sorteado = random.choice(agentes_filtrados)
    
    agentes_sorteados.append(sorteado)
    
    return sorteado

print(f'ccen : {agente_sorteado([])}')
print(f'Lori : {agente_sorteado(["Astra", "Breach", "Chamber", "Cypher", "Deadlock", "Fade", "Harbor", "KAYO", "Neon", "Omen", "Reyna"])}')
print(f'Guto : {agente_sorteado(["Astra", "Cypher", "Omen", "Yoru"])}')
