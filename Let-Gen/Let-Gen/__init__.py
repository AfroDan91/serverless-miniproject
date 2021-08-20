import logging
import random
import string
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
        
    letters1 = random.choice(string.ascii_letters) + random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)

    return func.HttpResponse(
        f"{letters1.lower()}",
        status_code=200
    )
