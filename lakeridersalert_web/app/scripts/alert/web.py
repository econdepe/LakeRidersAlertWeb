import requests

HOME_PAGE = "https://lakeridersclub.ch/index.php"
AUTHENTICATION_PAGE = "https://lakeridersclub.ch/membres/connexion.php"
CALENDAR_PAGE = "https://lakeridersclub.ch/membres/reservations.php"


class InvalidCredentialsError(Exception):
    pass


def create_browser_session():
    session = requests.Session()
    session.get(HOME_PAGE)
    return session


def get_session_authorized(session, email, password):
    session.post(
        url=AUTHENTICATION_PAGE,
        data={
            "adresse_electronique": email,
            "mot_de_passe": password,
            "rester_connecte": 1,
            "action": "se_connecter",
        },
    )


def get_reservations_html(session, email, password):
    response = session.get(CALENDAR_PAGE, timeout=10)
    if response.url == HOME_PAGE:
        # The session is not authenticated. Re-authenticate
        get_session_authorized(session=session, email=email, password=password)
        authenticated_response = session.get(CALENDAR_PAGE, timeout=10)
        if authenticated_response.url == HOME_PAGE:
            raise InvalidCredentialsError("Invalid credentials")
        return authenticated_response.text
    else:
        return response.text
