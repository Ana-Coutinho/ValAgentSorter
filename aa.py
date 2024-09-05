import random

agentsTotal = ["Astra","Breach","Brimstone","Chamber","Clove","Cypher","Deadlock","Fade","Gekko","Harbor","Iso","Jett","KAYO","Killjoy","Neon","Omen","Phoenix","Raze","Reyna","Sage", "Skye","Sova","Viper","Vyse","Yoru"]

def agente_sorteado():
    return random.choice(agentsTotal)

print(f'ccen : {agente_sorteado()}')
print(f'Lori : {agente_sorteado()}')
