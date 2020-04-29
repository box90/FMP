#FUNCTIONS
#serialization/deserialization
def tournament_to_dict(obj):
        #  Populate the dictionary with object meta data 
        obj_dict = {

        }
        
        #  Populate the dictionary with object properties
        obj_dict.update(obj.__dict__)
  
        return obj_dict



def dict_to_tournament(our_dict):
    class_name = "Tournament"
    module_name = "tournament"
    module = __import__(module_name)
    class_ = getattr(module,class_name)
    obj = class_(**our_dict)

    return obj