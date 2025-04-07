#Coleccion de paises:
paises = [
    {
        "nombre": "Colombia",
        "capital": "Bogotá",
        "moneda": "Peso colombiano",
        "ciudades":
        [
            {
                "nombre": "Bogotá",
                "poblacion": 8,
                "fundacion": 1538,
            },
            {
                "nombre": "Medellin",
                "poblacion": 2.6,
                "fundacion": 1616,
            },
            {
                "nombre": "Cali",
                "poblacion": 2.3,
                "fundacion": 1536,
            },
        ]
    },
    {
        "nombre": "Perú",
        "capital": "Lima",
        "moneda": "Sol",
        "ciudades": 
        [
            {
                "nombre": "Lima",
                "poblacion": 9.7,
                "fundacion": 1535,
            },
            {
                "nombre": "Cuzco",
                "poblacion": 0.43,
                "fundacion": 1534,
            },
        ]
    },
    {
        "nombre": "Argentina",
        "capital": "Buenos Aires",
        "moneda": "Peso argentino",
        "ciudades":
        [
            {
                "nombre": "Buenos Aires",
                "poblacion": 3.1,
                "fundacion": 1536,
            },
            {
                "nombre": "Rosario",
                "poblacion": 1.7,
                "fundacion": 1725,
            },
        ]
    },
]

#Iterar cada pais
print("--------------")
print("Recorrido de Paises")
print("--------------")

for pais in paises:
    print("Nombre:", pais["nombre"])
    print("Capital:", pais["capital"])
    print("Moneda:", pais["moneda"])
    print("Ciudades Principales", pais["nombre"])
    for ciudad in pais["ciudades"]:
        print("--Ciudad:", ciudad["nombre"])
        print("-", ciudad["poblacion"], "millones de habitantes")
        print("Fundacion:", ciudad["fundacion"])
    print("--------------")
