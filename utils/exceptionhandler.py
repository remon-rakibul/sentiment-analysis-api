from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:
        message = [field_errors for field_name, field_errors in response.data.items()]
        response.data = {
            'status_code': response.status_code,
            'message': message[0]
        }

    exception_class=exc.__class__.__name__

    return response