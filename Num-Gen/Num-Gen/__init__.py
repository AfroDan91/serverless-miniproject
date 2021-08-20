import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    numbers = random.randint(10000, 99999)

    return func.HttpResponse(
        f"{str(numbers)}",
        status_code=200
    )
