# SISTEMA DE TRASLADO DE EQUIPOS

# Arreglos de equipos
codigos = ["EQ001", "EQ002", "EQ003"]
descripciones = ["Equipo Rayos X Portátil", "Detector Digital", "Laptop de Registro"]
marcas = ["Mindray", "Fujifilm", "Lenovo"]
modelos = ["RX100", "D200", "ThinkPad"]
series = ["SR001", "SR002", "SR003"]
ubicaciones = ["CS San Juan", "CS Villa El Salvador", "Almacén Central"]
estados = ["Operativo", "Operativo", "Mantenimiento"]

# Arreglos de movimientos
mov_codigos = []
mov_origenes = []
mov_destinos = []
mov_responsables = []
mov_motivos = []
mov_fechas = []
mov_estados = []

def buscar_equipo(codigo):
    for i in range(len(codigos)):
        if codigos[i] == codigo:
            return i
    return -1

def registrar_traslado():
    codigo = input("Ingrese el código del equipo: ").upper()
    pos = buscar_equipo(codigo)

    if pos == -1:
        print("Equipo no encontrado.")
    else:
        if estados[pos] == "Operativo":
            origen = ubicaciones[pos]
            destino = input("Ingrese establecimiento de destino: ")
            responsable = input("Ingrese responsable del traslado: ")
            motivo = input("Ingrese motivo del traslado: ")
            fecha = input("Ingrese fecha del traslado: ")

            mov_codigos.append(codigo)
            mov_origenes.append(origen)
            mov_destinos.append(destino)
            mov_responsables.append(responsable)
            mov_motivos.append(motivo)
            mov_fechas.append(fecha)
            mov_estados.append(estados[pos])

            ubicaciones[pos] = destino

            print("Traslado registrado correctamente.")
        else:
            print("El equipo no está disponible para traslado.")
            print("Estado actual:", estados[pos])

def consultar_ubicacion():
    codigo = input("Ingrese el código del equipo: ").upper()
    pos = buscar_equipo(codigo)

    if pos == -1:
        print("Equipo no encontrado.")
    else:
        print("Código:", codigos[pos])
        print("Descripción:", descripciones[pos])
        print("Ubicación actual:", ubicaciones[pos])
        print("Estado:", estados[pos])

def mostrar_historial():
    if len(mov_codigos) == 0:
        print("No hay traslados registrados.")
    else:
        print("\n===== HISTORIAL DE TRASLADOS =====")
        for i in range(len(mov_codigos)):
            print(f"\nTraslado {i+1}")
            print("Código:", mov_codigos[i])
            print("Origen:", mov_origenes[i])
            print("Destino:", mov_destinos[i])
            print("Responsable:", mov_responsables[i])
            print("Motivo:", mov_motivos[i])
            print("Fecha:", mov_fechas[i])
            print("Estado del equipo:", mov_estados[i])

def generar_reporte():
    total_traslados = len(mov_codigos)

    operativos = 0
    mantenimiento = 0
    baja = 0

    for estado in estados:
        if estado == "Operativo":
            operativos += 1
        elif estado == "Mantenimiento":
            mantenimiento += 1
        elif estado == "Baja":
            baja += 1

    destinos_unicos = []
    conteos = []

    for destino in mov_destinos:
        encontrado = False
        for i in range(len(destinos_unicos)):
            if destinos_unicos[i] == destino:
                conteos[i] += 1
                encontrado = True
                break
        if not encontrado:
            destinos_unicos.append(destino)
            conteos.append(1)

    print("\n===== REPORTE DE INDICADORES =====")
    print("Total de equipos registrados:", len(codigos))
    print("Total de traslados realizados:", total_traslados)
    print("Equipos operativos:", operativos)
    print("Equipos en mantenimiento:", mantenimiento)
    print("Equipos dados de baja:", baja)

    if len(destinos_unicos) > 0:
        mayor = conteos[0]
        pos_mayor = 0
        for i in range(1, len(conteos)):
            if conteos[i] > mayor:
                mayor = conteos[i]
                pos_mayor = i
        print("Destino con mayor número de traslados:", destinos_unicos[pos_mayor])
        print("Cantidad de traslados a ese destino:", mayor)
    else:
        print("Aún no existen destinos registrados.")

def menu():
    opcion = 0
    while opcion != 5:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Registrar traslado")
        print("2. Consultar ubicación actual")
        print("3. Mostrar historial de traslados")
        print("4. Generar reporte")
        print("5. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            registrar_traslado()
        elif opcion == 2:
            consultar_ubicacion()
        elif opcion == 3:
            mostrar_historial()
        elif opcion == 4:
            generar_reporte()
        elif opcion == 5:
            print("Programa finalizado.")
        else:
            print("Opción inválida.")

menu()