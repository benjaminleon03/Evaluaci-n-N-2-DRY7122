import urllib.parse
import requests


main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "j3wkdQtFjx3cGDNceUSbQmoMK0I8Wgfj"

while True:
    origen = input("Ingrese Ciudad de Origen (o presione 'q' para salir): ")
    if origen.lower() == 'q':
        print("Saliendo del programa...")
        break
        
    destino = input("Ingrese Ciudad de Destino (o presione 'q' para salir): ")
    if destino.lower() == 'q':
        print("Saliendo del programa...")
        break


    url = main_api + urllib.parse.urlencode({"key": key, "from": origen, "to": destino, "unit": "k"})
    
   
    json_data = requests.get(url).json()

    
    if json_data["info"]["statuscode"] == 0:
        print("\n--- RESUMEN DEL VIAJE ---")
        
        
        distancia = json_data["route"]["distance"]
        
        
        combustible_gal = json_data["route"].get("fuelUsed", 0)
        combustible_litros = combustible_gal * 3.78541
        
        
        tiempo_segundos = json_data["route"]["realTime"]
        horas = int(tiempo_segundos / 3600)
        minutos = int((tiempo_segundos % 3600) / 60)
        segundos = tiempo_segundos % 60
        
        # Imprimir con 2 decimales (.2f)
        print(f"Distancia: {distancia:.2f} kilómetros")
        print(f"Duración: {horas:02d} horas, {minutos:02d} minutos, {segundos:02d} segundos")
        print(f"Combustible requerido: {combustible_litros:.2f} litros\n")
        
        # 4. Narrativa del viaje
        print("--- NARRATIVA DEL VIAJE ---")
        for maneuver in json_data["route"]["legs"][0]["maneuvers"]:
            print("- " + maneuver["narrative"])
        print("\n" + "="*40 + "\n")
    else:
        print("Error en la solicitud. Verifique los nombres de las ciudades.\n")