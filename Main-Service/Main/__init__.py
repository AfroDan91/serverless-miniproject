import logging
import requests
import azure.functions as func
from azure.cosmos import exceptions, CosmosClient, PartitionKey, partition_key

endpoint = 'https://user-gen-db.documents.azure.com:443/'
key = ''

client = CosmosClient(endpoint, key)

database = client.create_database_if_not_exists(id="user-gen-rand-names")
container = database.create_container_if_not_exists(
    id = 'user-gen-rand-names-container',
    partition_key= PartitionKey(path="/username"),
    offer_throughput=400
)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    letters = requests.get('https://username-app1.azurewebsites.net/api/let-gen?code=Lrd0SfuHWfFLyF2DRqSy7HaSi0eEYrFnJO5qacGJhcNM6RiZUwKTxg==').text
    numbers = requests.get('https://username-app.azurewebsites.net/api/num-gen?code=UTRSciqNaLf4PgRIxoKpM/gfvyKXb/fbwiOKISiaAU75P92mOsHo/g==').text

    count = 0
    newstr = ''

    while count < 5:
        newstr += letters[count] + numbers[count]
        count += 1

    container.create_item(body={
        "id": str(1),
        "username": newstr
        })

    return func.HttpResponse(
        newstr,
        status_code=200
    )
