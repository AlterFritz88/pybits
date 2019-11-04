import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    return re.match(r'PB-[0-9A-Z]{8}-[0-9A-Z]{8}-[0-9A-Z]{8}-[0-9A-Z]{8}$', key) != None

print(validate_license('PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4'))
print(validate_license('PB-NDT7C6BM-9YRKGHOU-ZO9I4BJ1-0TA9PHR7A'))