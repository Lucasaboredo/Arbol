# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.
from arbol_avl import BinaryTree

tree = BinaryTree()

#Armo Arbol
tree.insert_node("Capitan america", {"is_hero":True})
tree.insert_node("Thanos", {"is_hero":False})
tree.insert_node("Hulk", {"is_hero":True})
tree.insert_node("Loki", {"is_hero":False})
tree.insert_node("Capitana Marvel", {"is_hero":True})
tree.insert_node("Duende Verde", {"is_hero":False})
tree.insert_node("Spiderman", {"is_hero":True})
tree.insert_node("Doctor Strange", {"is_hero":True})

# Listar villanos ordenados alfabéticamente
print("Punto 1")
villanos = tree.inorden_villanos()

# Mostrar superhéroes que empiezan con C
print("Punto 2")
SuperheroesC = tree.inorden_superheros_start_with("C")

# Determinar cuántos superhéroes hay en el arbol
print("Cuantos superheroes hay en el arbol:", tree.contar_super_heroes())


# Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre
print("Punto 3")
hero_node = tree.search('Doctor Strange')
# 2. Si lo encuentras, modificar sus valores
if hero_node is not None:
    # Modificar el nombre del héroe
    hero_node.value = 'Iron Man'
    
    # Modificar su valor adicional
    hero_node.other_value['is_hero'] = True
    print(f"Héroe modificado: {hero_node.value}")
else:
    print("Héroe no encontrado")

# Listar los superhéroes ordenados de manera descendente
print("Punto 4")


print("Nuevo Bosque")
# Generar un bosque a partir de este árbol
# Crear dos árboles para superhéroes y villanos
arbol_superheroes = BinaryTree()
arbol_villanos = BinaryTree()

# Función para separar superhéroes y villanos
def separar_personajes(nodo):
    if nodo is not None:
        # Si el nodo es un superhéroe, lo insertamos en el árbol de superhéroes
        if nodo.other_value.get('is_hero'):
            arbol_superheroes.insert_node(nodo.value, nodo.other_value)
        else:  # Si es un villano, lo insertamos en el árbol de villanos
            arbol_villanos.insert_node(nodo.value, nodo.other_value)
        
        # Llamar recursivamente para los nodos izquierdo y derecho
        separar_personajes(nodo.left)
        separar_personajes(nodo.right)

# Llamar a la función para separar los personajes
separar_personajes(tree.root)

# I. Determinar cuántos nodos tiene cada árbol
num_superheroes = arbol_superheroes.contar_super_heroes()
num_villanos = arbol_villanos.contar_super_heroes()

print(f"Número de superhéroes: {num_superheroes}")
print(f"Número de villanos: {num_villanos}")

# II. Realizar un barrido ordenado alfabéticamente de cada árbol
print("Barrido ordenado de superhéroes:")
arbol_superheroes.inorden()

print("Barrido ordenado de villanos:")
arbol_villanos.inorden()
