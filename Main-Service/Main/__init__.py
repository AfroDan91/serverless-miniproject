import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    letters = requests.get('https://username-app1.azurewebsites.net/api/let-gen?code=Lrd0SfuHWfFLyF2DRqSy7HaSi0eEYrFnJO5qacGJhcNM6RiZUwKTxg==')
    numbers = requests.get('https://username-app.azurewebsites.net/api/num-gen?code=UTRSciqNaLf4PgRIxoKpM/gfvyKXb/fbwiOKISiaAU75P92mOsHo/g==')

    return func.HttpResponse(
        str(letters.text+numbers.text),
        status_code=200
    )
