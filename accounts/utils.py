def normalize_phone_number(phone: str) -> str:
    """Удаляет пробелы, дефисы и приводит к формату +7XXXXXXXXXX"""
    phone = phone.replace(" ", "").replace("-", "")
    if phone.startswith("8"):
        phone = "+7" + phone[1:]
    elif phone.startswith("7"):
        phone = "+7" + phone[1:]
    elif phone.startswith("9"):
        phone = "+7" + phone
    return phone
