eventos = {}

proximo_id_evento = 1

INFO_SISTEMA = ("v1.0.2", -8.0578, -34.8824) 



def menu_principal():
    
    print(f" --- Gerenciador do Eventos Festa Ao Redor Do Mundo (Versão: {INFO_SISTEMA[0]}) ---")
    print("1. Adicionar Novo Evento")
    print("2. Listar Todos os Eventos")
    print("3. Detalhar Evento e Inscrições")
    print("4. Inscrever Participante em Evento")
    print("5. Sair")
    
    escolha = input("Escolha uma opção: ")
    return escolha

def adicionar_evento():
    
    global proximo_id_evento
    
    
    nome = input("Nome do Evento: ")
    data = input("Data (AAAA-MM-DD): ")
    vagas = int(input("Número de Vagas: "))
    
   
    habilidades_input = input("Habilidades Requeridas (separadas por vírgula): ")
    skills_requeridas = set([h.strip().upper() for h in habilidades_input.split(',')])
    
    
    novo_evento = {
        'nome': nome,
        'data': data,
        'local': "Online", 
        'vagas': vagas,
        'skills': skills_requeridas, 
        'inscricoes': [] 
    }
    
  
    eventos[proximo_id_evento] = novo_evento
    print(f" Evento '{nome}' criado com sucesso! ID: {proximo_id_evento}")
    proximo_id_evento +=  1

def listar_eventos():
    
    if not eventos:
        print("Nenhum evento cadastrado.")
        return
    
    print("--- Eventos Cadastrados ---")
    
    for id_evento, evento in eventos.items():
        
        print(f"ID: {id_evento} | Nome: {evento['nome']} | Data: {evento['data']} | Inscritos: {len(evento['inscricoes'])}/{evento['vagas']}")

def detalhar_evento(id_evento):
   
    if id_evento in eventos:
        evento = eventos[id_evento]
        print(f" --- Detalhes do Evento ID {id_evento} ---")
        print(f"Nome: {evento['nome']}")
        print(f"Data: {evento['data']}")
        print(f"Vagas: {evento['vagas']}")
        
        
        print(f"Habilidades Requeridas (Total {len(evento['skills'])}): {', '.join(evento['skills'])}")
        
        
        print(f" --- Participantes Inscritos ({len(evento['inscricoes'])}) ---")
        if evento['inscricoes']:
            for i, participante in enumerate(evento['inscricoes']):
                
                print(f"{i+1}. {participante['nome']} ({participante['email']})")
        else:
            print("Nenhum participante inscrito ainda.")
    else:
        print(f" Erro: Evento com ID {id_evento} não encontrado.")

def inscrever_participante(id_evento):
    
    if id_evento not in eventos:
        print(f" Erro: Evento com ID {id_evento} não encontrado.")
        return

    evento = eventos[id_evento]

    
    if len(evento['inscricoes']) >= evento['vagas']:
        print(f" Inscrição não realizada: Evento '{evento['nome']}' está lotado.")
        return

    
    nome_part = input("Nome do Participante: ")
    email_part = input("Email do Participante: ")
    
    
    participante = {
        'nome': nome_part,
        'email': email_part
    }
    evento['inscricoes'].append(participante)
    print(f"Participantearticipante '{nome_part}' inscrito com sucesso no evento '{evento['nome']}'.")

if __name__ == "__main__":
    while True:
        try:
            escolha = menu_principal()
            
            if escolha == '1':
                adicionar_evento()
            
            elif escolha == '2':
                listar_eventos()
            
            elif escolha == '3':
                id_busca = int(input("Digite o ID do evento para detalhar: "))
                detalhar_evento(id_busca)
                
            elif escolha == '4':
                id_inscricao = int(input("Digite o ID do evento para inscrição: "))
                inscrever_participante(id_inscricao)
                
            elif escolha == '5':
                print("Encerrando o sistema. Até mais!")
                break
                
            else:
                print("Opção inválida. Tente novamente.")
                
        except ValueError:
            print("Entrada inválida. Por favor, insira um número para a opção ou ID.")
  