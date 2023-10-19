# Clase para analizar los datos de las mascotas
class PetAnalyzer:
    def __init__(self, pet_data):
        self.pet_data = pet_data

    def count_names(self):
        name_count = {}
        for pet in self.pet_data:
            name = pet['name']
            if name in name_count:
                name_count[name] += 1
            else:
                name_count[name] = 1
        return name_count
