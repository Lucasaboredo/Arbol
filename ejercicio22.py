from arbol_avl import BinaryTree

tree = BinaryTree()

# Lista de criaturas y quién las derrotó
creatures_data = [
    {"name": "Ceto", "defeated_by": "-"},
    {"name": "Tifón", "defeated_by": "Zeus"},
    {"name": "Equidna", "defeated_by": "Argos Panoptes"},
    {"name": "Dino", "defeated_by": "-"},
    {"name": "Pefredo", "defeated_by": "-"},
    {"name": "Enio", "defeated_by": "-"},
    {"name": "Escila", "defeated_by": "Cloto"},
    {"name": "Caribdis", "defeated_by": "Láquesis"},
    {"name": "Euríale", "defeated_by": "-"},
    {"name": "Esteno", "defeated_by": "-"},
    {"name": "Medusa", "defeated_by": "Perseo"},
    {"name": "Ladón", "defeated_by": "Heracles"},
    {"name": "Águila del Cáucaso", "defeated_by": "-"},
    {"name": "Quimera", "defeated_by": "Belerofonte"},
    {"name": "Hidra de Lerna", "defeated_by": "Heracles"},
    {"name": "León de Nemea", "defeated_by": "Heracles"},
    {"name": "Esfinge", "defeated_by": "Edipo"},
    {"name": "Dragón de la Cólquida", "defeated_by": "-"},
    {"name": "Cerbero", "defeated_by": "-"},
    {"name": "Cerda de Cromión", "defeated_by": "Teseo"},
    {"name": "Toro de Creta", "defeated_by": "Teseo"},
    {"name": "Jabalí de Calidón", "defeated_by": "Atalanta"},
    {"name": "Carcinos", "defeated_by": "-"},
    {"name": "Gerión", "defeated_by": "Heracles"},
    {"name": "Cloto", "defeated_by": "-"},
    {"name": "Láquesis", "defeated_by": "-"},
    {"name": "Átropos", "defeated_by": "-"},
    {"name": "Minotauro de Creta", "defeated_by": "Teseo"},
    {"name": "Harpías", "defeated_by": "-"},
    {"name": "Argos Panoptes", "defeated_by": "Hermes"},
    {"name": "Aves del Estínfalo", "defeated_by": "Heracles"},
    {"name": "Talos", "defeated_by": "Medea"},
    {"name": "Sirenas", "defeated_by": "-"},
    {"name": "Pitón", "defeated_by": "Apolo"},
    {"name": "Cierva de Cerinea", "defeated_by": "-"},
    {"name": "Basilisco", "defeated_by": "-"},
    {"name": "Jabalí de Erimanto", "defeated_by": "-"}
]

# Cargar criaturas en el árbol AVL
for creature in creatures_data:
    tree.insert_node(creature["name"], {
        "defeated_by": creature["defeated_by"],
        "captured_by": None,
        "description": None
    })

# Punto a: Listado inorden de las criaturas y quién las derrotó
def in_order_list(tree):
    def __in_order(node):
        if node is not None:
            __in_order(node.left)
            defeated_by = node.other_value["defeated_by"] if node.other_value["defeated_by"] != "-" else "No fue derrotado"
            print(f'Criatura: {node.value}, Derrotado por: {defeated_by}')
            __in_order(node.right)

    __in_order(tree.root)

# Punto b: Permitir cargar una breve descripción sobre cada criatura
def agregar_descripcion(tree, creature_name, description):
    node = tree.search(creature_name)
    if node:
        node.other_value["description"] = description
        print(f'Descripción agregada a {creature_name}: {description}')
    else:
        print(f'{creature_name} no encontrado.')

# Punto c: Mostrar toda la información de la criatura Talos
def mostrar_info_creature(tree, creature_name):
    creature = tree.search(creature_name)
    if creature:
        defeated_by = creature.other_value["defeated_by"] if creature.other_value["defeated_by"] != "-" else "No fue derrotado"
        captured_by = creature.other_value["captured_by"] if creature.other_value["captured_by"] else "No capturada"
        description = creature.other_value["description"] if creature.other_value["description"] else "Sin descripción"
        print(f'Criatura: {creature.value}\nDerrotado por: {defeated_by}\nCapturada por: {captured_by}\nDescripción: {description}')
    else:
        print(f'{creature_name} no encontrado en el árbol.')

# Punto d: Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
def top_3_heroes(tree):
    hero_counts = {}
    
    def __in_order(node):
        if node is not None:
            __in_order(node.left)
            defeated_by = node.other_value["defeated_by"]
            if defeated_by != "-":
                if defeated_by in hero_counts:
                    hero_counts[defeated_by] += 1
                else:
                    hero_counts[defeated_by] = 1
            __in_order(node.right)

    __in_order(tree.root)

    top_3 = sorted(hero_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    for hero, count in top_3:
        print(f'{hero} derrotó a {count} criaturas')

# Punto e: Listar las criaturas derrotadas por un héroe (Heracles)
def criaturas_derrotadas_por(tree, hero_name):
    def __in_order(node):
        if node is not None:
            __in_order(node.left)
            if node.other_value["defeated_by"] == hero_name:
                print(node.value)
            __in_order(node.right)

    __in_order(tree.root)

# Punto f: Listar las criaturas que no han sido derrotadas
def criaturas_no_derrotadas(tree):
    def __in_order(node):
        if node is not None:
            __in_order(node.left)
            if node.other_value["defeated_by"] == "-":
                print(node.value)
            __in_order(node.right)

    __in_order(tree.root)

# Punto g: Cada nodo tiene un campo "capturada"
def capturar_criatura(tree, creature_name, hero_name):
    node = tree.search(creature_name)
    if node:
        node.other_value["captured_by"] = hero_name
        print(f'{hero_name} capturó a {creature_name}')
    else:
        print(f'{creature_name} no encontrada')

# Punto h: Marcar criaturas como capturadas por Heracles
def marcar_criaturas_capturadas_por_heracles(tree):
    criaturas = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
    for criatura in criaturas:
        capturar_criatura(tree, criatura, "Heracles")

# Punto i: Búsquedas por coincidencia
def busqueda_por_coincidencia(tree, search_value):
    def __in_order(node):
        if node is not None:
            __in_order(node.left)
            if search_value.lower() in node.value.lower():
                print(node.value)
            __in_order(node.right)

    __in_order(tree.root)

# Punto j: Eliminar criaturas (Basilisco y Sirenas)
def eliminar_criaturas(tree, criaturas):
    for criatura in criaturas:
        eliminado = tree.delete_node(criatura)
        if eliminado:
            print(f'{criatura} eliminada del árbol')
        else:
            print(f'{criatura} no encontrada en el árbol')

# Punto k: Modificar el nodo de las Aves del Estínfalo
def modificar_aves_stinfalo(tree):
    node = tree.search("Aves del Estínfalo")
    if node:
        node.value = "Aves del Estínfalo Modificado"
        print("Nombre modificado a Aves del Estínfalo Modificado")
    else:
        print("Aves del Estínfalo no encontrada en el árbol")

# Punto l: Listar las criaturas capturadas
def listar_criaturas_capturadas(tree):
    def __in_order(node):
        if node is not None:
            __in_order(node.left)
            captured_by = node.other_value["captured_by"]
            if captured_by:
                print(f'Criatura: {node.value}, Capturada por: {captured_by}')
            __in_order(node.right)

    __in_order(tree.root)

# Punto m: Crear un listado de criaturas ordenadas por quién las capturó
def listar_criaturas_ordenadas_por_capturador(tree):
    criaturas_capturadas = []

    def __in_order(node):
        if node is not None:
            __in_order(node.left)
            captured_by = node.other_value["captured_by"]
            if captured_by:
                criaturas_capturadas.append((node.value, captured_by))
            __in_order(node.right)

    __in_order(tree.root)
    criaturas_capturadas.sort(key=lambda x: x[1])  # Ordenar por el nombre del capturador
    for criatura, capturador in criaturas_capturadas:
        print(f'Criatura: {criatura}, Capturada por: {capturador}')

# Punto n: Contar la cantidad de criaturas capturadas por cada héroe
def contar_criaturas_capturadas_por_heroe(tree):
    hero_counts = {}

    def __in_order(node):
        if node is not None:
            __in_order(node.left)
            captured_by = node.other_value["captured_by"]
            if captured_by:
                if captured_by in hero_counts:
                    hero_counts[captured_by] += 1
                else:
                    hero_counts[captured_by] = 1
            __in_order(node.right)

    __in_order(tree.root)

    for hero, count in hero_counts.items():
        print(f'{hero} ha capturado {count} criaturas.')

# Llamadas a las funciones de los nuevos puntos
in_order_list(tree)
agregar_descripcion(tree, "Ceto", "Diosa del mar y madre de monstruos.")
mostrar_info_creature(tree, "Talos")
top_3_heroes(tree)
criaturas_derrotadas_por(tree, "Heracles")
criaturas_no_derrotadas(tree)
marcar_criaturas_capturadas_por_heracles(tree)
busqueda_por_coincidencia(tree, "Criatura")
eliminar_criaturas(tree, ["Basilisco", "Sirenas"])
modificar_aves_stinfalo(tree)
listar_criaturas_capturadas(tree)
listar_criaturas_ordenadas_por_capturador(tree)
contar_criaturas_capturadas_por_heroe(tree)


