excluded_fields = ["id", "consultas", "recetas", "pruebas_de_laboratorio", "consulta"]
array_fields = ["alergias", "padecimientos"]
multiple_input_fields = ["medicamentos", "pruebas"]

multi_fields_map = {
    "medicamentos": ["nombre", "dosis", "gramaje", "frecuencia", "duracion"],
    "pruebas": ["nombre", "fecha", "url"]
}


def input_handler(model):
    print(f"==== {model.__name__}: =====")

    keys = list(model.__fields__.keys())
    result = {}

    for key in keys:
        if key in excluded_fields:
            continue

        if key in array_fields:
            result[key] = input(f"Capturar {key} separados/as por coma: ").split(',')
            continue

        fields = []
        if key in multiple_input_fields:
            multi_input_keys = multi_fields_map[key]
            multi_result = {}

            repetitions = int(input(f"Introduce el número de {key} que quieres agregar: "))

            for i in range(repetitions):
                for multi_key in multi_input_keys:
                    multi_result[multi_key] = input(f"- Capturar {multi_key}: ")

                fields.append(multi_result)
                print('-' * 10)

            result[key] = fields
            continue

        result[key] = input(f"Capturar {key}: ")

    return result