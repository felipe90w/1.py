print("=" * 50)

nome_host = input("Digite o nome do Host (Hostname): ")
endereco_ip = input("Digite o endereço ip do host (ex: 192.168.1.10): ")
endereco_mac = input("Digite o endereço MAC (ex: 00:1B:44:11:3A:B7): ")
sistema_operacional = input("Digite o Sistema Operacional (ex: linux, windows): ")

porta_critica = int(input("Digite a principal porta aberta a monitorar (Ex: 22, 80): "))
nivel_criticidade = int(input("Nível de criticidade do Ativo (1-Baixo a 5-Crítico): "))

tempo_resposta_ping = float(input("Digite o tempo médio de Ping em ms (ex: 12.45): "))
score_cvss = float(input("Pontuação média de vulnerabilidade CVSS (0.0 a 10.0): "))

consumo_banda = float(input("Digite o consumo de banda usado pelo ativo em mbps: "))

firewall_ativo_input = input("O Firewall está ativo? (s/n): ").strip().lower()
firewall_ativo = firewall_ativo_input == 's'

status_ativo_input = input("O host está acessível no momento? (s/n): ").strip().lower()
host_ativo = status_ativo_input == 's'

print("-" * 50)
print(f"Hostname:             {nome_host} (Tipo: {type(nome_host).__name__})")
print(f"Endereço IP:          {endereco_ip}")
print(f"Endereço MAC:         {endereco_mac}")
print(f"Sistema operacional:  {sistema_operacional}")
print(f"Porta Alvo:           {porta_critica} (Tipo: {type(porta_critica).__name__})")
print(f"Nível de criticidade: {nivel_criticidade}/5")

print(f"Latência (Ping):      {tempo_resposta_ping:.2f} ms (Tipo: {type(tempo_resposta_ping).__name__})")

print(f"Score de risco (CVSS):{score_cvss}/10.0")

print(f"Consumo de banda:     {consumo_banda} mbps (Tipo: {type(consumo_banda).__name__})")

print(f"Firewall Ativo:       {firewall_ativo} (Tipo: {type(firewall_ativo).__name__})")
print(f"Host acessivel:       {host_ativo}")
print("-" * 50)

if porta_critica == 21 or porta_critica == 23:
    print("ALERTA: a porta inserida é uma porta padrão do acesso remoto  (21-FTP / 23-Telnet)!")
    print("-" * 50)

alerta_seguranca = (score_cvss >= 7.0) or (not firewall_ativo)
print(f"Alerta de Segurança Requerido? {alerta_seguranca}")

if alerta_seguranca:
    print("ATENÇÃO: Este host possui alto risco de segurança ou o firewall está desativado")
else:
    print("STATUS: Host dentro dos parâmetros de conformidade")
print("=" * 50)
