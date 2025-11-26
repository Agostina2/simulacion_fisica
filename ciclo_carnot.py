import tkinter as tk
from tkinter import ttk
from math import log
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

R = 8.314  # Constante de los gases

# Lee entradas de la interfaz
def leer_entradas():
    try:
        n = float(entry_n.get())
        gamma = float(entry_gamma.get())
        T_hot = float(entry_Th.get())
        T_cold = float(entry_Tc.get())
        V1 = float(entry_V1.get())
        V2 = float(entry_V2.get())

        if V2 <= V1:
            mostrar_error("Error: V2 debe ser mayor que V1.")
            return None

        return n, gamma, T_hot, T_cold, V1, V2

    except ValueError:
        mostrar_error("ERROR: Ingresa valores numéricos válidos.")
        return None

# Mostrar mensaje de error
def mostrar_error(mensaje):
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, mensaje)

# Calcula presiones y volúmenes de cada estado
def calcular_presiones_volumenes(n, gamma, T_hot, T_cold, V1, V2):
    P1 = n * R * T_hot / V1
    P2 = n * R * T_hot / V2
    V3 = V2 * (T_hot / T_cold) ** (1 / (gamma - 1))
    P3 = n * R * T_cold / V3
    V4 = V1 * (T_hot / T_cold) ** (1 / (gamma - 1))
    P4 = n * R * T_cold / V4
    return P1, P2, V3, P3, V4, P4

# Calcula trabajo, calor y energía interna
def calcular_trabajo_Q_dU(n, gamma, T_hot, T_cold, V1, V2, V3, V4):
    Cv = R / (gamma - 1)

    W_12 = n * R * T_hot * log(V2 / V1)
    Q_12 = W_12
    dU_12 = 0

    dU_23 = n * Cv * (T_cold - T_hot)
    W_23 = -dU_23
    Q_23 = 0

    W_34 = n * R * T_cold * log(V4 / V3)
    Q_34 = W_34
    dU_34 = 0

    dU_41 = n * Cv * (T_hot - T_cold)
    W_41 = -dU_41
    Q_41 = 0

    W_net = W_12 + W_23 + W_34 + W_41
    Q_in = Q_12 if Q_12 > 0 else 0
    eficiencia = W_net / Q_in if Q_in != 0 else float("nan")

    return (W_12, Q_12, dU_12,
            W_23, Q_23, dU_23,
            W_34, Q_34, dU_34,
            W_41, Q_41, dU_41,
            W_net, Q_in, eficiencia)

# Mostar resultados en la interfaz
def mostrar_resultados(W_12, Q_12, dU_12,
                        W_23, Q_23, dU_23,
                        W_34, Q_34, dU_34,
                        W_41, Q_41, dU_41,
                        W_net, Q_in, eficiencia):
    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, "=== RESULTADOS DEL CICLO DE CARNOT ===\n\n")
    resultado_text.insert(tk.END, f"W 1→2: {W_12:.3f} J\nQ 1→2: {Q_12:.3f} J\nΔU 1→2: {dU_12:.3f} J\n\n")
    resultado_text.insert(tk.END, f"W 2→3: {W_23:.3f} J\nQ 2→3: {Q_23:.3f} J\nΔU 2→3: {dU_23:.3f} J\n\n")
    resultado_text.insert(tk.END, f"W 3→4: {W_34:.3f} J\nQ 3→4: {Q_34:.3f} J\nΔU 3→4: {dU_34:.3f} J\n\n")
    resultado_text.insert(tk.END, f"W 4→1: {W_41:.3f} J\nQ 4→1: {Q_41:.3f} J\nΔU 4→1: {dU_41:.3f} J\n\n")
    resultado_text.insert(tk.END, "--------------------------------------\n")
    resultado_text.insert(tk.END, f"Trabajo neto W_net = {W_net:.3f} J\n")
    resultado_text.insert(tk.END, f"Calor absorbido Q_in = {Q_in:.3f} J\n")
    resultado_text.insert(tk.END, f"Rendimiento = {eficiencia:.3f}\n")

# Grafica el ciclo P-V
def graficar_ciclo(P1, P2, V1, V2, V3, P3, V4, P4, gamma, n, T_hot, T_cold):
    fig.clear()
    ax = fig.add_subplot(111)

    V_iso1 = np.linspace(V1, V2, 300)
    P_iso1 = n * R * T_hot / V_iso1

    C23 = P2 * (V2 ** gamma)
    V_adi23 = np.linspace(V2, V3, 300)
    P_adi23 = C23 / (V_adi23 ** gamma)

    V_iso3 = np.linspace(V3, V4, 300)
    P_iso3 = n * R * T_cold / V_iso3

    C41 = P4 * (V4 ** gamma)
    V_adi41 = np.linspace(V4, V1, 300)
    P_adi41 = C41 / (V_adi41 ** gamma)

    ax.plot(V_iso1, P_iso1, label="1→2 Isoterma caliente")
    ax.plot(V_adi23, P_adi23, label="2→3 Adiabática")
    ax.plot(V_iso3, P_iso3, label="3→4 Isoterma fría")
    ax.plot(V_adi41, P_adi41, label="4→1 Adiabática")

    ax.set_xlabel("Volumen (m³)")
    ax.set_ylabel("Presión (Pa)")
    ax.set_title("Ciclo de Carnot - Diagrama P-V")
    ax.grid(True)
    ax.legend()
    canvas.draw()

# Función principal
def generar_ciclo():
    entradas = leer_entradas()
    if entradas is None:
        return

    n, gamma, T_hot, T_cold, V1, V2 = entradas
    P1, P2, V3, P3, V4, P4 = calcular_presiones_volumenes(n, gamma, T_hot, T_cold, V1, V2)
    resultados = calcular_trabajo_Q_dU(n, gamma, T_hot, T_cold, V1, V2, V3, V4)
    mostrar_resultados(*resultados)
    graficar_ciclo(P1, P2, V1, V2, V3, P3, V4, P4, gamma, n, T_hot, T_cold)

# INTERFAZ TKINTER
root = tk.Tk()
root.title("Simulación del Ciclo de Carnot")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

# Entradas
ttk.Label(frame, text="n (mol):").grid(row=0, column=0)
entry_n = ttk.Entry(frame)
entry_n.insert(0, "1")
entry_n.grid(row=0, column=1)

ttk.Label(frame, text="γ (gamma):").grid(row=1, column=0)
entry_gamma = ttk.Entry(frame)
entry_gamma.insert(0, "1.4")
entry_gamma.grid(row=1, column=1)

ttk.Label(frame, text="T_hot (K):").grid(row=2, column=0)
entry_Th = ttk.Entry(frame)
entry_Th.insert(0, "444")
entry_Th.grid(row=2, column=1)

ttk.Label(frame, text="T_cold (K):").grid(row=3, column=0)
entry_Tc = ttk.Entry(frame)
entry_Tc.insert(0, "278")
entry_Tc.grid(row=3, column=1)

ttk.Label(frame, text="V1 (m³):").grid(row=4, column=0)
entry_V1 = ttk.Entry(frame)
entry_V1.insert(0, "2.27")
entry_V1.grid(row=4, column=1)

ttk.Label(frame, text="V2 (m³):").grid(row=5, column=0)
entry_V2 = ttk.Entry(frame)
entry_V2.insert(0, "6")
entry_V2.grid(row=5, column=1)

ttk.Button(frame, text="Generar Ciclo", command=generar_ciclo).grid(row=6, column=0, columnspan=2, pady=10)

resultado_text = tk.Text(frame, width=60, height=18)
resultado_text.grid(row=7, column=0, columnspan=2)

fig = plt.Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().grid(row=0, column=2, rowspan=20, padx=10)

root.mainloop()