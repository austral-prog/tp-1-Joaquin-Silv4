def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    horas_completas=total_segundos//3600
    sobrante_horas=total_segundos%3600
    minutos_completos_restantes=sobrante_horas//60
    segundos_restantes=5%60
    print(horas_completas)
    print(minutos_completos_restantes)
    print(segundos_restantes)
