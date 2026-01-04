test_settings={
    "wifi":"on",
    "bluetooth":"off",
    "mobile_data":"off"
}

def add_settings(user_settings,pair):
    k,v=pair
    key=k.lower()
    val=v.lower()
    if key in user_settings.keys():
        return(f"Setting '[{key}]' already exists! Cannot add a new setting with this name.")
    else:
        user_settings.update({key:val})
        return (f"Setting '[{key}]' added with value '[{val}]' successfully!")

def update_settings(user_settings,pair):
    k,v=pair
    key=k.lower()
    val=v.lower()
    if key in user_settings.keys():
        user_settings[key]=val
        return (f"Setting '[{key}]' updated to '[{val}]' successfully!")
    else:
        return (f"Setting '[{key}]' does not exist! Cannot update a non-existing setting.")      


# print(add_settings(test_settings,("wifi","off")))
# print(test_settings)