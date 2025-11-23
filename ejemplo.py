import numpy as np
import matplotlib.pyplot as plt

# ============================
# CONSTANTES Y PARÁMETROS
# ============================
R = 8.314
n = 1.0
gamma = 1.4

T1 = 400
V1 = 0.01
V2 = 0.03
V3 = 0.015

# ============================
# 1) PROCESO ISOTÉRMICO (1→2)
# ============================
V_iso = np.linspace(V1, V2, 200)
P_iso = n * R * T1 / V_iso
W_iso = n * R * T1 * np.log(V2/V1)

# ============================
# 2) PROCESO ADIABÁTICO (2→3)
# ============================
P2 = n * R * T1 / V2
K = P2 * (V2**gamma)

V_adi = np.linspace(V2, V3, 200)
P_adi = K / (V_adi**gamma)
W_adi = (P2*V2 - P_adi[-1]*V3) / (gamma - 1)

# ============================
# TRABAJO TOTAL
# ============================
W_total = W_iso + W_adi

print("Trabajo isotérmico:", W_iso)
print("Trabajo adiabático:", W_adi)
print("Trabajo total del ciclo:", W_total)

# ============================
# GRÁFICO P-V
# ============================
plt.plot(V_iso, P_iso, label="Isotérmico 1→2")
plt.plot(V_adi, P_adi, label="Adiabático 2→3")
plt.xlabel("Volumen (m3)")
plt.ylabel("Presión (Pa)")
plt.title("Simulación de Ciclo Termodinámico")
plt.legend()
plt.grid()
plt.show()
