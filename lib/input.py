excluded_fields = ["id", "ultima_consulta", "consultas", "recetas", "pruebas_de_laboratorio", "consulta"]
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
            inp = input(f"Capturar {key} separados/as por coma: ")
            result[key] = inp.split(',')
            continue

        if key in multiple_input_fields:
            multi_input_keys = multi_fields_map[key]
            multi_result = {}

            for multi_key in multi_input_keys:
                multi_result[multi_key] = input(f"- Capturar {multi_key}: ")

            result[key] = multi_result
            continue

        result[key] = input(f"Capturar {key}: ")

    return result
