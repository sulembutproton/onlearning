from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def helloworld(request):
    logging.error('Hello world Online Learning in the log...')
    print('Hello world Online Learning in a print statement...')
    response = """<html><body><p>Hello world Online Learning in HTML</p>
    <p>This sample code is available at
    <a href="https://github.com/sulembutproton/onlearning">
    https://github.com/sulembutproton/onlearning</a></p>
    </body></html>"""
    return HttpResponse(response)

