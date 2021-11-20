print("Informe o horário de início do experimento em horas, minutos e segundos:")
h_inicial = int(input("Hora que iniciou o experimento:"))
min_inicial = int(input("Minuto que iniciou o experimento:"))
s_inicial = int(input("Segundo que iniciou o experimento:"))

dur = int(input("\nInforme a duração do experimento em segundos:"))

# converte a duração de segundos para horas, minutos e segudos
h_dur = dur // 3600
min_dur = (dur % 3600) // 60
s_dur = (dur % 3600) % 60

# horário final
s_final = s_inicial + s_dur
min_final = min_inicial + min_dur
h_final = h_inicial + h_dur

# condições para soma dos horários
if s_final >= 60:
    min_final += 1
    s_final -= 60
if min_final >= 60:
    h_final += 1
    min_final -= 60
if h_final >= 24:
    dias = h_final // 24    # calcula quantos dias depois o experimento fica pronto
    h_final -= (h_final // 24) * 24    # limita as horas em 24H
    print(f"O experimento termina às {h_final}:{min_final}:{s_final} do {dias}º"
          f" dia subsequente ao dia do início do experimento.")
else:
    print(f'O experimento termina às {h_final}:{min_final}:{s_final}.')
