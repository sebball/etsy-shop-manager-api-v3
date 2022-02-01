import pkce
import requests
import curious_variables as cv

# Define unchanging variables relevant for OAuth2 authentication flow
scope = "transactions_r transactions_w"
state = "superstate"
redirect_uri = "http://localhost:5000"
response_type = "code"
code_challenge_method = "S256"
authorization_base_url = 'https://www.etsy.com/oauth/connect'
token_url = 'https://github.com/login/oauth/access_token'


def authorize_account():
    code_verifier = pkce.generate_code_verifier(length=128)
    code_challenge = pkce.get_code_challenge(code_verifier)

    cv.secret_dict["code_verifier"] = code_verifier
    cv.secret_dict["code_challenge"] = code_challenge

    print(type(cv.secret_dict), cv.secret_dict)

    response = requests.get(authorization_base_url, params={"client_id": cv.secret_dict["client_id"],
                                                            "scope": scope,
                                                            "state": state,
                                                            "redirect_uri": redirect_uri,
                                                            "response_type": response_type,
                                                            "code_challenge": cv.secret_dict["code_challenge"],
                                                            "code_challenge_method": code_challenge_method})

    return response.url


def request_token(code_string):
    post_json = {
        "grant_type": "authorization_code",
        f"client_id": cv.secret_dict["client_id"],
        "redirect_uri": f"{redirect_uri}",
        "code": code_string,
        "code_verifier": cv.secret_dict["code_verifier"]}

    response = requests.post(url="https://api.etsy.com/v3/public/oauth/token", json=post_json)
    return response.json()

#
# elif auth_or_token == "refresh":
#     post_json = {
#         "grant_type": "refresh_token",
#         "client_id": f"{client_id}",
#         "refresh_token": "537896753.KCJfHVOyd6t3b8dsJiTaq7vrPX9yQCKfTmvS8T_vH5vlUeILc17Kg4hos1tGWF63e1w4VhfKdUG5IoSzEc5h1lU4Vo",
#     }
#     response = requests.post(url="https://api.etsy.com/v3/public/oauth/token", json=post_json)
#
#     print(response.json())
authorize_account()