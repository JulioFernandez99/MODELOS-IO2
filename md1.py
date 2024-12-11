def md1_calculator():
    print("\nCálculos para el modelo M/D/1")
    
    # Solicitar parámetros
    unidad_tiempo = input("Ingrese la unidad de tiempo (h o m): ").strip().lower()
    if unidad_tiempo not in ["h", "m"]:
        print("Unidad de tiempo no válida. Debe ser 'horas' o 'minutos'.")
        return

    lamda = float(input(f"Ingrese el valor de λ (tasa de llegadas por unidad de tiempo en {unidad_tiempo}): "))
    mu = float(input(f"Ingrese el valor de μ (tasa de servicio por unidad de tiempo en {unidad_tiempo}): "))
    
    # Validar que el sistema sea estable
    rho = lamda / mu
    if rho >= 1:
        print("El sistema no es estable porque ρ >= 1.")
        return

    # Cálculos
    P0 = 1 - rho
    Lq = rho**2 / (2 * (1 - rho))
    Ls = Lq + rho
    Wq = Lq / lamda
    Ws = Wq + 1 / mu
    pc = (1 - rho)*100
    # Resultados
    print(f"\nResultados para M/D/1:")
    print(f"Utilización promedio (ρ): {rho:.4f}")
    print(f"Probabilidad de que no haya clientes en el sistema (P0): {P0:.4f}")
    print(f"Número promedio de clientes en la cola (Lq): {Lq:.4f}")
    print(f"Número promedio de clientes en el sistema (Ls): {Ls:.4f}")
    print(f"Tiempo promedio de espera en la cola (Wq) en {unidad_tiempo}: {Wq:.4f}")
    print(f"Tiempo promedio de estancia en el sistema (Ws) en {unidad_tiempo}: {Ws:.4f}")
    print(f"Promedio de tener cero clientes en el sistema: {pc:.4f}%")

md1_calculator()