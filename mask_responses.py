import hashlib

QUEUE_FIELDS = ['user_id', 'app_version',
                'device_type', 'ip', 'locale', 'device_id']
DB_FIELDS = ['user_id', 'app_version', 'device_type',
             'masked_ip', 'locale', 'masked_device_id']
MAPPING = dict(zip(QUEUE_FIELDS, DB_FIELDS))


def mask_helper(response):

    masked_resp = {}
    for field in QUEUE_FIELDS:

        # if 'masked' in Mapping[field]:
        if 'masked' in MAPPING[field]:

            masked_resp[MAPPING[field]] = hashlib.sha256(
                response.get(field).encode('utf-8')).hexdigest()

        else:
            masked_resp[MAPPING[field]] = response.get(field)

    return masked_resp if masked_resp else None


def mask_responses(responses):

    if isinstance(responses, list):
        return [mask_helper(response) for response in responses]
    else:
        return mask_helper(responses)
