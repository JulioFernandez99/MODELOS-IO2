def calcular_medidas(mu, lambd, k, tiempo_formato="m"):
    """
    Calcula las métricas de rendimiento basadas en las fórmulas dadas.
    
    Args:
        mu (float): Tasa de servicio (clientes por unidad de tiempo).
        lambd (float): Tasa de llegada (clientes por unidad de tiempo).
        k (int): Capacidad del sistema.
        tiempo_formato (str): "m" para minutos o "h" para horas.
        
    Returns:
        dict: Diccionario con los valores de rho, Lq, Ls, Wq, y Ws.
    """
    # Convertir tiempos si el formato es en horas
    if tiempo_formato == "h":
        mu /= 60  # De minutos a horas
        lambd /= 60
    
    # Tasa de utilización
    rho = lambd / mu
    if rho >= 1:
        return {"error": "El sistema no es estable (ρ >= 1). Verifica los valores de λ y μ."}
    
    # Probabilidad de rechazo (P_k)
    pk = (1 - rho) * (rho ** k) / (1 - rho ** (k + 1))
    
    # Tasa efectiva de llegadas
    lambd_ef = lambd * (1 - pk)
    
    # Número promedio de clientes en el sistema (Ls)
    Ls = (rho / (1 - rho)) - ((k + 1) * (rho ** (k + 1)) / (1 - rho ** (k + 1)))
    
    # Número promedio de clientes en cola (Lq)
    Lq = Ls - (1 - pk)
    
    # Tiempo promedio en el sistema (Ws)
    Ws = Ls / lambd_ef
    
    # Tiempo promedio en la cola (Wq)
    Wq = Lq / lambd_ef
    
    return {
        "rho": round(rho, 4),
        "Lq": round(Lq, 4),
        "Ls": round(Ls, 4),
        "Wq": round(Wq, 4),
        "Ws": round(Ws, 4),
    }

def main():
    print("Sistema M/M/1/K - Cálculo de medidas de rendimiento")
    
    # Solicitar entradas al usuario
    mu = float(input("Ingrese la tasa de servicio (μ) en clientes por minuto: "))
    lambd = float(input("Ingrese la tasa de llegada (λ) en clientes por minuto: "))
    k = int(input("Ingrese la capacidad del sistema (K): "))
    
    formato = input("¿Desea trabajar en horas o minutos? (escriba 'h' para horas o 'm' para minutos): ").strip().lower()
    if formato not in ["h", "m"]:
        print("Formato inválido. Usando 'm' (minutos) por defecto.")
        formato = "m"
    
    # Calcular medidas de rendimiento
    resultados = calcular_medidas(mu, lambd, k, formato)
    
    # Mostrar resultados
    if "error" in resultados:
        print(resultados["error"])
    else:
        unidad = "horas" if formato == "h" else "minutos"
        print("\nResultados:")
        print(f"Tasa de utilización (ρ): {resultados['rho']}")
        print(f"Número promedio de clientes en cola (Lq): {resultados['Lq']}")
        print(f"Número promedio de clientes en el sistema (Ls): {resultados['Ls']}")
        print(f"Tiempo promedio de espera en cola (Wq): {resultados['Wq']} {unidad}")
        print(f"Tiempo promedio de estancia en el sistema (Ws): {resultados['Ws']} {unidad}")

if __name__ == "__main__":
    main()
