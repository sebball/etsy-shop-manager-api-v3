import requests
from os.path import exists
# from pprint import pprint
from os.path import exists
from pathlib import Path

# import curious_variables as cv
# from curious_variables import end_points



# def get_secret_dictionary():
#     secret_path = Path("secret_variables_RichmondCuriosities.txt")
#     if secret_path.is_file():
#         secret_object = open("secret_variables_RichmondCuriosities.txt", "r")
#         secret_dictionary = secret_object.read()
#         return secret_dictionary

#
# def get_dicts(id_shop, action, dict_state):
#     header_api = 'x-api-key'
#     api_key  = vars["api_key"]
#     response = requests.get(f"{end_points['active_by_shop']}", headers={header_api: api_key}, params="")
#
#     if action == 'return':
#         vars["info_dicts"]["dicts_active"]=dict(response.json())
#         return
#     elif action == "print":
#         pprint(response.json())
#         return

# print(get_dicts_active())
#
# def get_list_result_dictionaries(dict_listings=vars["dicts_listings_data"]["list_active_data"], action='return'):
#     if action == 'return':
#         return dict_listings["results"]
#     elif action == 'print':
#         pprint(dict_listings["results"])
#
# print(get_secret_dictionary())
#
#
# # def get_list_ids(dict_result_vars=vars, action='return'):
# #     list_ids = []
# #     list_results = dict_result_vars["dict_active"]["results"]
# #     for dict_result in list_results:
# #         for id in dict_result["listing_id"]:
#
#
