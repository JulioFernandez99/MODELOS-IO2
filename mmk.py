def calculate_mmk(lam, mu, k):
    rho = lam / (k * mu)  # Tasa de utilización
    if rho >= 1:
        return None, None, None, None, None, f"El sistema no es estable (ρ = {rho:.2f}) porque ρ >= 1."

    # Probabilidad de que no haya clientes en el sistema (P0)
    summation = sum((lam / mu) ** n / factorial(n) for n in range(k))
    last_term = ((lam / mu) ** k) / (factorial(k) * (1 - rho))
    P0 = 1 / (summation + last_term)

    # Número esperado de clientes en la cola (Lq)
    Lq = (P0 * ((lam / mu) ** k) * rho) / (factorial(k) * (1 - rho) ** 2)

    # Número esperado de clientes en el sistema (Ls)
    Ls = Lq + lam / mu

    # Tiempo promedio en la cola (Wq)
    Wq = Lq / lam

    # Tiempo promedio en el sistema (Ws)
    Ws = Ls / lam

    # Probabilidades
    P_ocupado = rho  # Probabilidad de estar ocupado
    P_libre = 1 - rho  # Probabilidad de estar libre

    return rho, Lq, Ls, Wq, Ws, P_libre, P_ocupado, None

def main_mmk():
    print("Cálculo para un sistema M/M/k")
    unit = input("¿Los valores están en horas o minutos? (h/m): ").strip().lower()

    if unit not in ['h', 'm']:
        print("Entrada no válida. Usa 'h' para horas o 'm' para minutos.")
        return

    lam = float(input("Ingrese la tasa de llegada (λ): "))
    mu = float(input("Ingrese la tasa de servicio (μ): "))
    k = int(input("Ingrese el número de servidores (k): "))

    # Convertir valores si están en minutos
    if unit == 'm':
        lam /= 60
        mu /= 60

    rho, Lq, Ls, Wq, Ws, P_libre, P_ocupado, error = calculate_mmk(lam, mu, k)

    if error:
        print(error)
    else:
        if unit == 'm':
            Wq *= 60
            Ws *= 60

        print("\nResultados:")
        print(f"Factor de utilización (ρ): {rho:.4f}")
        print(f"Número esperado de clientes en la cola (Lq): {Lq:.4f}")
        print(f"Número esperado de clientes en el sistema (Ls): {Ls:.4f}")
        print(f"Tiempo promedio en la cola (Wq): {Wq:.4f} {'minutos' if unit == 'm' else 'horas'}")
        print(f"Tiempo promedio en el sistema (Ws): {Ws:.4f} {'minutos' if unit == 'm' else 'horas'}")
        print(f"Probabilidad de que el sistema esté libre: {P_libre:.4f}")
        print(f"Probabilidad de que el sistema esté ocupado: {P_ocupado:.4f}")

if __name__ == "__main__":
    main_mmk()
