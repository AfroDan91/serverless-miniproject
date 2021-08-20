import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    letters = requests.get('https://username-app1.azurewebsites.net/api/let-gen?code=Lrd0SfuHWfFLyF2DRqSy7HaSi0eEYrFnJO5qacGJhcNM6RiZUwKTxg==').text
    numbers = requests.get('https://username-app.azurewebsites.net/api/num-gen?code=UTRSciqNaLf4PgRIxoKpM/gfvyKXb/fbwiOKISiaAU75P92mOsHo/g==').text

    count = 0
    newstr = ''

    while count < 5:
        newstr += letters[count] + numbers[count]
        count += 1

    return func.HttpResponse(
        newstr,
        status_code=200
    )
