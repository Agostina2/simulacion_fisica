from r_equivalente import resolver_serie_paralelo
from metodo_mallas import resolver_mallas

def main():
    
    print("\n" * 2)
    print("╔" + "═" * 70 + "╗")
    print("║{:^68}║".format("⚡ ANALISIS DE CIRCUITOS DE CORRIENTE CONTINUA ⚡"))
    print("╠" + "═" * 70 + "╣")
    print("║{:^70}║".format("Version 1.0"))
    print("╚" + "═" * 70 + "╝")
    
    print("\nBienvenido/a al sistema de análisis de circuitos eléctricos.")
    print("Este programa permite resolver:")
    print("  • Circuitos en serie")
    print("  • Circuitos en paralelo")
    print("  • Circuitos mixtos con método de nodos o mallas\n")
    

    print("Seleccione una opción:")
    print("  1) Resolver circuito serie / paralelo")
    print("  2) Resolver circuito por método de mallas")
    print("  3) Salir")
    print("═"*72)
    
    while True:

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            resolver_serie_paralelo()
        elif opcion == "2":
            resolver_mallas()
        elif opcion == "3":
            print("\nSaliendo del programa...")
            break
        else:
            print("\n❌ Opción inválida. Intente nuevamente.")



# Ejecutar la función principal
if __name__ == "__main__":
    main()