import pytest

STANDARD_USER = "standard_user"
PASSWORD = "secret_sauce"

INVALID_USER = "invalid_user"
INVALID_PASSWORD = "invalid_user"

LOGIN_NEGATIVE_CASES = [
    pytest.param(
        INVALID_USER,
        INVALID_PASSWORD,
        "Username and password do not match any user in this service",
        id="invalid_user_and_password"
    ),
    pytest.param(
        STANDARD_USER,
        INVALID_PASSWORD,
        "Username and password do not match any user in this service",
        id="valid_user_wrong_password"
    ),
    pytest.param(
        "",
        PASSWORD,
        "Username is required",
        id="missing_username"
    ),
    pytest.param(
        STANDARD_USER,
        "",
        "Password is required",
        id="missing_password"
    ),
]