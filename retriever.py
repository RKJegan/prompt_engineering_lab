from context import DOCUMENTS


def retrieve_context(customer_message: str) -> str:

    message = customer_message.lower()

    if "payment" in message or "charged" in message:
        return DOCUMENTS["payment"]

    if "package" in message or "shipping" in message or "delivery" in message:
        return DOCUMENTS["shipping"]

    if "password" in message or "login" in message or "account" in message:
        return DOCUMENTS["account"]

    return ""