def mostrar_menu():
    print("\n¿Qué desea agregar?")
    print("  1) Resistencia en SERIE")
    print("  2) Grupo de resistencias en PARALELO")
    print("  3) Ver resultado y terminar")
    return input("Seleccione una opción: ")

def agregar_serie(r_total):
    try:
        r = float(input("Valor de la resistencia en ohms: "))
        r_total += r
        print(f"✔ Añadida en serie → R_total = {r_total:.2f} Ω")
    except:
        print("❌ Valor inválido")
    return r_total

def agregar_paralelo(r_total):
    resistencias = []
    print("\nIngrese las resistencias del grupo en paralelo.")
    print("Escriba 'x' para dejar de agregar.")

    while True:
        val = input("  Valor (Ω): ")
        if val.lower() == "x":
            break
        try:
            resistencias.append(float(val))
        except:
            print("❌ Valor inválido, intente de nuevo.")

    if len(resistencias) < 2:
        print("❌ Debe ingresar al menos dos resistencias.")
        return r_total

    # Cálculo del paralelo
    inv_sum = sum(1.0/r for r in resistencias)
    r_eq = 1.0 / inv_sum

    print(f"✔ Paralelo calculado: R_eq = {r_eq:.2f} Ω")

    # El equivalente se agrega como si fuera una resistencia serie
    r_total += r_eq
    print(f"✔ Actualizado → R_total = {r_total:.2f} Ω")
    return r_total

def mostrar_resultado(r_total):
    print("\n" + "═"*72)
    print(f"RESISTENCIA TOTAL = {r_total:.2f} Ω")
    print("═"*72 + "\n")

def resolver_serie_paralelo():
    print("═"*72 + "\n")
    print("🔧 Cálculo de Resistencias Equivalentes\n")
    print("═"*72 + "\n")

    r_total = 0  # Acá vamos acumulando la resistencia equivalente total

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            r_total = agregar_serie(r_total)
        elif opcion == "2":
            r_total = agregar_paralelo(r_total)
        elif opcion == "3":
            mostrar_resultado(r_total)
            return r_total
        else:
            print("❌ Opción inválida.")
