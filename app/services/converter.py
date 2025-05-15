import requests
from app.core.config import settings

def convert_currency(from_currency: str, to_currency: str, amount: float):
    url = f"{settings.EXCHANGE_API_URL}/{settings.EXCHANGE_API_KEY}/latest/{from_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "conversion_rates" in data:
            rate = data["conversion_rates"].get(to_currency)
        elif "rates" in data:
            rate = data["rates"].get(to_currency)
        else:
            return {"error": "Unexpected API response structure."}

        if rate is None:
            return {"error": f"Invalid target currency: {to_currency}"}

        return {
            "from": from_currency,
            "to": to_currency,
            "original_amount": amount,
            "converted_amount": round(amount * rate, 2),
            "rate": rate
        }
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error: {http_err}"}
    except requests.exceptions.RequestException as err:
        return {"error": f"Request failed: {err}"}
    except ValueError:
        return {"error": "Failed to parse API response as JSON"}
