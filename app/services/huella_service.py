import requests
from app.config import CLIMATIQ_API_KEY, CLIMATIQ_API_URL

def detectar_activity_id(motivo: str) -> str:
    motivo = motivo.lower()

    if "comida" in motivo or "alimento" in motivo or "restaurante" in motivo:
        return "food-supply-type_meals"
    elif "salud" in motivo or "medic" in motivo or "doctor" in motivo:
        return "healthcare-medical-equipment"
    elif "transporte" in motivo or "taxi" in motivo or "uber" in motivo:
        return "passenger_vehicle-vehicle_type_car-fuel_source_na-distance_na-engine_size_na"
    elif "ropa" in motivo or "vestimenta" in motivo:
        return "retail-clothing"
    elif "hogar" in motivo or "renta" in motivo or "servicio" in motivo:
        return "services-type_other"
    elif "educacion" in motivo or "escuela" in motivo or "curso" in motivo:
        return "education-type_other"
    else:
        return "services-type_other"  # fallback genérico

def calcular_emision(motivo: str, cantidad: float) -> float:
    activity_id = detectar_activity_id(motivo)

    headers = {
        "Authorization": CLIMATIQ_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "emission_factor": {
            "activity_id": activity_id
        },
        "parameters": {
            "money": cantidad,
            "money_unit": "usd"
        }
    }

    try:
        response = requests.post(f"{CLIMATIQ_API_URL}/estimate", json=data, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result.get("co2e", 0.0)
    except requests.RequestException as e:
        print(f"Error al estimar motivo '{motivo}': {e}")
        return 0.0
