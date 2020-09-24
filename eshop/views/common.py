import validators

BAD_REQUEST = {'error': 'Bad Request'}, 400
NOT_FOUND = {'error': 'Not Found'}, 404


async def validate_uuid(uuid):
    return validators.uuid(uuid)
