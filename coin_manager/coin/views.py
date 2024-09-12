from .models import *
import requests
import json
from django.http.response import HttpResponse , JsonResponse
def find_price(request , coin_name):
    url = "https://api.wallex.ir/v1/currencies/stats?key={}".format(coin_name)
    response = requests.get(url)
    response = json.loads(response.content)
    price = response["result"][0]['price']
    last_day = response["result"][0]['percent_change_24h']
    final_result = {
        "price": price,
        "last_day_change_percent": last_day
    }
    final_result_json = json.dumps(final_result)
    return JsonResponse(final_result_json , safe = False)
    