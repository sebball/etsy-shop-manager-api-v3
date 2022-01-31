import pkce
import requests


token_url = 'https://github.com/login/oauth/access_token'

def authorize_account():

    scope = "transactions_r transactions_w"
    state = "superstate"
    redirect_uri = "https://bad-lionfish-72.loca.lt"
    response_type = "code"
    code_challenge_method = "S256"
    authorization_base_url = 'https://www.etsy.com/oauth/connect'

    code_verifier = pkce.generate_code_verifier(length=128)
    code_challenge = pkce.get_code_challenge(code_verifier)

    print(code_verifier, code_challenge)

    response = requests.get(authorization_base_url, params={"client_id": client_id,
                                                            "scope": scope,
                                                            "state": state,
                                                            "redirect_uri": redirect_uri,
                                                            "response_type": response_type,
                                                            "code_challenge": code_challenge,
                                                            "code_challenge_method": code_challenge_method})

    print(response.url)


elif auth_or_token == "token":
    post_json = {
        "grant_type": "authorization_code",
        f"client_id": f"{client_id}",
        "redirect_uri": f"{redirect_uri}",
        "code": "fuo06HPm_Wu2kQLBUgwUgP6XPuN6o0rC6gZaPrihHcQ649DHekXzmdmdGDdcc34J-lmWD2V-4lzoz4CRrLvdV3Tc6z6jzVOU327J",
        "code_verifier": "yzgni4nGvrsuZSFCQ76h0eIUo7SF4gTaXSZICpyefMnuEBoc_Fh9p0hyZVONmpVwSFLbYI3I3NIdiUgHmXXHDEGEQkQ4Mt9S7mvdOEuYb2YZPRayKP7fe5u2JF2rrMOS"}

    response = requests.post(url="https://api.etsy.com/v3/public/oauth/token", json=post_json)

    print(response.json())

elif auth_or_token == "refresh":
    post_json = {
        "grant_type": "refresh_token",
        "client_id": f"{client_id}",
        "refresh_token": "537896753.KCJfHVOyd6t3b8dsJiTaq7vrPX9yQCKfTmvS8T_vH5vlUeILc17Kg4hos1tGWF63e1w4VhfKdUG5IoSzEc5h1lU4Vo",
    }
    response = requests.post(url="https://api.etsy.com/v3/public/oauth/token", json=post_json)

    print(response.json())
