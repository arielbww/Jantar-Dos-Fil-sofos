import time

# --- CONFIGURAÇÃO INICIAL ---
NUM_FILOSOFOS = 5
PENSANDO = "PENSANDO"
FAMINTO  = "FAMINTO "
COMENDO  = "COMENDO "

# Criamos os 5 filósofos
filosofos = []
for i in range(NUM_FILOSOFOS):
    filosofos.append({
        "id": i, 
        "estado": PENSANDO, 
        "tempo": (i + 1) * 2 # Tempos diferentes para iniciarem em momentos distintos
    })

# Criamos os 5 talheres. 
# "Livre" significa que está na mesa. Se for pego, guardará o nome do Filósofo (ex: "F1")
talheres = ["Livre", "Livre", "Livre", "Livre", "Livre"]

print("=== Início do Jantar dos Filósofos com Talheres ===")

rodada = 1
while True:
    print(f"\n--- Rodada {rodada} ---")
    
    # 1. TENTATIVA DE COMER (Alocação de Recursos)
    for f in filosofos:
        if f["estado"] == FAMINTO:
            # Identificando quais são os talheres deste filósofo
            # O da esquerda tem o mesmo número dele. O da direita é o próximo (fazendo a volta na mesa).
            talher_esq = f["id"]
            talher_dir = (f["id"] + 1) % NUM_FILOSOFOS
            
            # Ele só pega se OS DOIS estiverem livres! (Isso evita que o sistema trave)
            if talheres[talher_esq] == "Livre" and talheres[talher_dir] == "Livre":
                # Pega os talheres (registra o ID do filósofo neles)
                talheres[talher_esq] = f"F{f['id']}"
                talheres[talher_dir] = f"F{f['id']}"
                
                f["estado"] = COMENDO
                f["tempo"] = 4 # Ele vai passar 4 rodadas comendo

    # 2. MOSTRAR O STATUS DA MESA NA TELA
    for f in filosofos:
        if f["estado"] == COMENDO:
            esq = f["id"]
            dir = (f["id"] + 1) % NUM_FILOSOFOS
            print(f"Filósofo {f['id']} [{f['estado']}] -> Segurando talheres {esq} e {dir}")
        else:
            print(f"Filósofo {f['id']} [{f['estado']}]")
            
    # Mostra exatamente como está a lista de talheres agora
    print(f"Mesa (Talheres 0 a 4): {talheres}")

    # 3. PASSAGEM DO TEMPO
    time.sleep(4) # Aguarda 4 segundo
    rodada += 1
    
    # 4. ATUALIZAR TEMPOS E LIBERAR TALHERES
    for f in filosofos:
        f["tempo"] -= 1
        
        if f["tempo"] <= 0:
            if f["estado"] == COMENDO:
                # Terminou de comer, devolve os talheres para a mesa!
                talher_esq = f["id"]
                talher_dir = (f["id"] + 1) % NUM_FILOSOFOS
                talheres[talher_esq] = "Livre"
                talheres[talher_dir] = "Livre"
                
                f["estado"] = PENSANDO
                f["tempo"] = 5 # Ficará 5 rodadas pensando
                
            elif f["estado"] == PENSANDO:
                f["estado"] = FAMINTO
                # Fica faminto com tempo 0, apenas esperando a lógica da etapa 1 liberar os talheres
