from utils import read_data
from utils import pet_analyzer as pa

# Función para listar las mascotas vendidas
def list_sold_pets(data):
    sold_pets = [(pet["id"], pet["name"]) for pet in data if pet["status"] == "sold"]
    return sold_pets

# Cargar datos desde el archivo
filename = 'pet_data.json'
data = read_data.load_data_from_file(filename)

if data:
    # Utilizar la función para listar las mascotas vendidas
    sold_pets = list_sold_pets(data)
    print("Mascotas vendidas:")
    for pet in sold_pets:
        print(f"{pet[0]} - {pet[1]}\n")

    # Utilizar la clase para contar los nombres de las mascotas
    pet_analyzer = pa.PetAnalyzer(data)
    name_count = pet_analyzer.count_names()
    print("Conteo de nombres de mascotas:")
    for name, count in name_count.items():
        print(f"{name}: {count}")
else:
    print(f"No se encontró el archivo '{filename}' o su formato es incorrecto.")
