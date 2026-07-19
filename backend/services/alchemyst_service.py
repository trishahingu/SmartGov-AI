import os

ALCHEMYST_API_KEY = os.getenv("ALCHEMYST_API_KEY")


def ask_alchemyst(message: str):

    """
    Replace this function with the official
    Alchemyst AI API call once the endpoint
    is available.
    """

    return f"""SmartGov AI Response

You asked:

{message}

Alchemyst AI integration is ready.

Only the API endpoint needs to be added.
"""