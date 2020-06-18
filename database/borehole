

class Soil_layer:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_info(self, depth, w_sat, qik, fa0, k2):
        self.__depth = depth
        self.__w_sat = w_sat
        self.__qik = qik
        self.__fa0 = fa0
        self.__k2 = k2
    
    def get_depth(self):
        return self.__depth

    # 待增加
    
class Borhole:

    soil_layers = []

    def __init__(self, name):
        self.__name = name  

    def get_name(self):
        return self.__name
    
    def insert_soil_layer(self, soil_layer):
        self.soil_layers.append(soil_layer)

    # 待增加

if __name__ == '__main__':
    layer_1 = Soil_layer("test_layer_1")
    layer_2 = Soil_layer("test_layer_2")

    hole_1 = Borhole("test_hole")
    hole_1.insert_soil_layer(layer_1)
    hole_1.insert_soil_layer(layer_2)

    for i in hole_1.soil_layers:
        print(i.get_name())