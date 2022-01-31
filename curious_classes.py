import curious_functions as cf
import curious_variables as cv
import typing
import logging


import useful_functions
# import curious_variables as cv


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.CRITICAL)
log = logging.critical("Testing program:")

class Shop:
    def __init__(self):
        self.type_object = "shop"
        self.info = Info(parent_object=self)





        # if secrets:
        #     for this_secret in self.secrets:
        #         self.secrets[nesecret] = secret
        # get_new_info = input("Do you want to add or change secret information? y/n: ")
        # if get_new_info == "y":
        #
        # if
        #     print("You need to add a 'secret_variables_RichmondCuriosities.txt' file")
        #     return
        # secrets = cf.get_secret_dictionary()
        #
        # def ask_for_secret(self, secret):
        #     secret_choices = []
        #
        #
        #
        # self.,my_api_key = my_api_key
        # self.my_shop_id = my_shop_id
    #


    # class ShopSecrets(self, ):
    #
    # def new_secrets(self, self):
    #
    # def get_secret_dictionary():
    #     secret_path = Path("secret_variables_RichmondCuriosities.txt")
    #     if secret_path.is_file():
    #         secret_object = open("secret_variables_RichmondCuriosities.txt", "r")
    #         secret_dictionary = secret_object.read()
    #         return secret_dictionary


class Info:
    """Return information dictionary from etsy api about the class it calls

    Attributes
    dict: Dictionary of values returned by etsy api calls. Contents depend on the type of the parent object.
    type: Small description of classes use
    parent_object: the object (type of info: eg shop, listings) Info is assigned to"""
    def __init__(self, parent_object, api_call=""):

        self.type = "info"
        self.dict = {}
        self.parent_object = parent_object

        if parent_object.type_object == "shop":
            self.dict.update({"end_points": cv.end_points})
        elif parent_object.type_object == "listings":
            self.dict.update()



# class Listings:
#     def __init__(self):
#         self.type = "listings"
#         self.parent_object = "shop"
#         def get_info(type):
#             self.info = Info(parent_object="listings", api_call="")



shop = Shop()
shop2  = Shop()


print(shop.info.parent_object.type_object)





    #     self.shoprequired = ["shop_id", "shop_name"]
    #     self.shop = info_dictionary
    #     log.critical(f"{self.shop}")
    #
    # # def add(self, dict_to_update):
    # #     log(f"add function start: self = {type(self)} {self.shop}")
    #     self_copy = useful_functions.dict_fresh_id(self)
    #     #log(f"add function self copied: self = {self}, self_copy = {self_copy}")
    #     for i, key in enumerate(dict_to_update):
    #        # log(f"add function i: {i}, key: {key}, self = {self}, self_copy:{self_copy}")
    #         for value in dict_to_update[key]:
    #             self_copy[key] = value
    #     self = self_copy
    #     del self_copy



    # def check_required(info_object):
    #     for requirement in info_class.required:
    #         assert requirement in info_class
#
# curious_info = {"shop_id": "32027063", "shop_name": "RichmondCuriosities",}
# shop = Shop()
# print(type(curious_info))
# info = Info(info_dictionary=curious_info)
# # log(f"{info_dictionary.shop}")
# print(info, info.shop["shop_id"])
#
# info.add(dict_to_update={"he;;op": "rffae"})
# print(info.shop)
#
# new_info = Info(shop_info=curious_info)
# print(new_info.shop)
# new_info.add({['did', 'add'], ['it', '?']})
# print(new_info.shop)