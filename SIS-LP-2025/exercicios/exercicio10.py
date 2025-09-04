for horas in range(24):
    for minutos in range(0, 60, 15):
        if minutos == 0:
            minutos = "00"
        print(f"{horas}:{minutos}")