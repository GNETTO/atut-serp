from extractor import Extractor


class Serp:
    def __init__(self, l_entity, l_attribute):
        self.entities = l_entity
        self.attributes = l_attribute

    def start(self):
        box = []
        for entity in self.entities:
            for attribute in self.attributes:
                inputs = entity + " " + attribute
                extractor = Extractor()
                data = extractor.start_extraction(inputs)
                #print(data)
                box.append(self.format_(data, entity, attribute))
        #print(box)
        return box

    def format_(self, data, ent, attr):
        result = []
        element = {}
        element["entity"] = ent
        element["attribute"] = attr
        element["source"] = data
        result.append(element)
        return result
        #print(result)


