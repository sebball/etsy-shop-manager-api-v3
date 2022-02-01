# import curious_functions


shop_id = "32027063"

end_points = {
    "listings": {
        "all": "/listings",
        "active": "/listings/active",
        "inactive": "/listings/inactive"
        }

    }

# Extract unique or secret variables from file "secret_variables.txt and save as dictionary"
secret_object = open("secret_variables.txt", "r")
secret_dict_string = secret_object.read()
exec(secret_dict_string)






# "end_points": {

#     "all_listings": f"https://openapi.etsy.com/v3/application/shops/{vars['shop_id']}/listings",
#     "active_by_shop": f"https://openapi.etsy.com/v3/application/shops/{vars['shop_id']}/listings"
#     ""},}
    # "info_dicts": {
    #     "dicts_active": {},
    #     }
    # }
    #
    # # ,
    # #       }}

shop_objects_to_assign = {"info", "listings"}

# url_pathway = {"listings":
#                    {"all":
#                        {"active"
#                     {"path": "/listings",
#                                  {  }
#
#                      }}
