# Script para modelo M/G/1, M/D/1 y M/Ek/1

def mg1_calculator():
    print("Cálculos para el modelo M/G/1")
    
    # Solicitar parámetros
    unidad_tiempo = input("Ingrese la unidad de tiempo (h para horas, m para minutos): ").strip().lower()
    if unidad_tiempo not in ["h", "m"]:
        print("Unidad de tiempo no válida. Debe ser 'h' o 'm'.")
        return
    
    unidad_tiempo_nombre = "horas" if unidad_tiempo == "h" else "minutos"
    lamda = float(input(f"Ingrese el valor de λ (tasa de llegadas por unidad de tiempo en {unidad_tiempo_nombre}): "))
    mu = float(input(f"Ingrese el valor de μ (tasa de servicio por unidad de tiempo en {unidad_tiempo_nombre}): "))
    sigma = (1 / mu) * 0.1  # Calculando la desviación estándar como 10% del tiempo promedio de servicio
    print(f"El error típico calculado (σ) es: {sigma:.4f} {unidad_tiempo_nombre}.")

    # Validar que el sistema sea estable
    rho = lamda / mu
    if rho >= 1:
        print("El sistema no es estable porque ρ >= 1.")
        return

    # Cálculos
    P0 = 1 - rho
    Lq = (lamda**2 * sigma**2 + rho**2) / (2 * (1 - rho))
    Ls = Lq + rho
    Wq = Lq / lamda
    Ws = Wq + 1 / mu

    # Resultados
    print(f"\nResultados para M/G/1:")
    print(f"Utilización promedio (ρ): {rho:.4f}")
    print(f"Probabilidad de que no haya clientes en el sistema (P0): {P0:.4f}")
    print(f"Número promedio de clientes en la cola (Lq): {Lq:.4f}")
    print(f"Número promedio de clientes en el sistema (Ls): {Ls:.4f}")
    print(f"Tiempo promedio de espera en la cola (Wq) en {unidad_tiempo_nombre}: {Wq:.4f}")
    print(f"Tiempo promedio de estancia en el sistema (Ws) en {unidad_tiempo_nombre}: {Ws:.4f}")

def md1_calculator():
    print("\nCálculos para el modelo M/D/1")
    
    # Solicitar parámetros
    unidad_tiempo = input("Ingrese la unidad de tiempo (h para horas, m para minutos): ").strip().lower()
    if unidad_tiempo not in ["h", "m"]:
        print("Unidad de tiempo no válida. Debe ser 'h' o 'm'.")
        return

    unidad_tiempo_nombre = "horas" if unidad_tiempo == "h" else "minutos"
    lamda = float(input(f"Ingrese el valor de λ (tasa de llegadas por unidad de tiempo en {unidad_tiempo_nombre}): "))
    mu = float(input(f"Ingrese el valor de μ (tasa de servicio por unidad de tiempo en {unidad_tiempo_nombre}): "))
    
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

    # Resultados
    print(f"\nResultados para M/D/1:")
    print(f"Utilización promedio (ρ): {rho:.4f}")
    print(f"Probabilidad de que no haya clientes en el sistema (P0): {P0:.4f}")
    print(f"Número promedio de clientes en la cola (Lq): {Lq:.4f}")
    print(f"Número promedio de clientes en el sistema (Ls): {Ls:.4f}")
    print(f"Tiempo promedio de espera en la cola (Wq) en {unidad_tiempo_nombre}: {Wq:.4f}")
    print(f"Tiempo promedio de estancia en el sistema (Ws) en {unidad_tiempo_nombre}: {Ws:.4f}")

def mek1_calculator():
    print("\nCálculos para el modelo M/Ek/1")
    
    # Solicitar parámetros
    unidad_tiempo = input("Ingrese la unidad de tiempo (h para horas, m para minutos): ").strip().lower()
    if unidad_tiempo not in ["h", "m"]:
        print("Unidad de tiempo no válida. Debe ser 'h' o 'm'.")
        return

    unidad_tiempo_nombre = "horas" if unidad_tiempo == "h" else "minutos"
    lamda = float(input(f"Ingrese el valor de λ (tasa de llegadas por unidad de tiempo en {unidad_tiempo_nombre}): "))
    mu = float(input(f"Ingrese el valor de μ (tasa de servicio por unidad de tiempo en {unidad_tiempo_nombre}): "))
    sigma = float(input(f"Ingrese el valor del error típico (σ) en los tiempos de servicio en {unidad_tiempo_nombre}: "))

    # Calcular k
    k = 1 / (mu**2 * sigma**2)
    print(f"El valor calculado de k es: {k:.4f}")

    # Validar que el sistema sea estable
    rho = lamda / mu
    if rho >= 1:
        print("El sistema no es estable porque ρ >= 1.")
        return

    # Cálculos
    P0 = 1 - rho
    Lq = (rho**2 * (1 + k)) / (2 * k * (1 - rho))
    Ls = Lq + rho
    Wq = Lq / lamda
    Ws = Wq + 1 / mu

    # Resultados
    print(f"\nResultados para M/Ek/1:")
    print(f"Utilización promedio (ρ): {rho:.4f}")
    print(f"Probabilidad de que no haya clientes en el sistema (P0): {P0:.4f}")
    print(f"Número promedio de clientes en la cola (Lq): {Lq:.4f}")
    print(f"Número promedio de clientes en el sistema (Ls): {Ls:.4f}")
    print(f"Tiempo promedio de espera en la cola (Wq) en {unidad_tiempo_nombre}: {Wq:.4f}")
    print(f"Tiempo promedio de estancia en el sistema (Ws) en {unidad_tiempo_nombre}: {Ws:.4f}")
mek1_calculator()