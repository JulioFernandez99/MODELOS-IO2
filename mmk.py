
def calculate_mm1k_metrics(lam, mu, k,pc):

    rho = lam / mu

    # Probabilidad de que el sistema esté vacío (P0)
    if rho != 1:
        P0 = (1 - rho) / (1 - (rho ** (k + 1)))
    else:
        P0 = 1 / (k + 1)
    
    pc = P0
    # Tasa efectiva de llegada (λef)
    lam_ef = lam * (1 - (rho ** k) * P0)

    # Número promedio de clientes en el sistema (Ls)
    if rho != 1:
        Ls = (rho / (1 - rho)) - ((k + 1) * (rho ** (k + 1)) / (1 - rho ** (k + 1)))
    else:
        Ls = k / 2

    # Número promedio de clientes en cola (Lq)
    Lq = Ls - (1 - P0)

    # Tiempo promedio en el sistema (Ws)
    Ws = Ls / lam_ef

    # Tiempo promedio en la cola (Wq)
    Wq = Lq / lam_ef

    return lam_ef, rho, Lq, Ls, Wq, Ws,pc, None


def main():
    print("Cálculo para un sistema M/M/1/K")
    unit = input("¿Los valores están en horas o minutos? (h/m): ").strip().lower()
    pc = 0
    if unit not in ['h', 'm']:
        print("Entrada no válida. Usa 'h' para horas o 'm' para minutos.")
        return

    lam = float(input("Ingrese la tasa de llegada (λ): "))
    mu = float(input("Ingrese la tasa de servicio (μ): "))
    k = int(input("Ingrese la capacidad máxima del sistema (k): "))

    # Convertir valores si están en minutos
    if unit == 'm':
        lam /= 60  # Convertir λ de por minuto a por hora
        mu /= 60   # Convertir μ de por minuto a por hora

    lam_ef, rho, Lq, Ls, Wq, Ws,pc, error = calculate_mm1k_metrics(lam, mu, k,pc)

    if error:
        print(error)
    else:
        # Ajustar salida de tiempos a las unidades originales
        if unit == 'm':
            Wq *= 60  # Convertir tiempo promedio de horas a minutos
            Ws *= 60
       
        print("\nResultados:")
        print(f"Probabilidad que no haya nadie en el sistema(P0): {pc} -> {pc*100}%")
        print(f"Tasa efectiva de llegada (λef): {lam_ef:.4f}")
        print(f"Factor de utilización (ρ): {rho:.4f}")
        print(f"Número esperado de clientes en la cola (Lq): {Lq:.4f}")
        print(f"Número esperado de clientes en el sistema (Ls): {Ls:.4f}")
        print(f"Tiempo promedio en la cola (Wq): {Wq:.4f} {'minutos' if unit == 'm' else 'horas'}")
        print(f"Tiempo promedio en el sistema (Ws): {Ws:.4f} {'minutos' if unit == 'm' else 'horas'}")


if __name__ == "__main__":
    main()
