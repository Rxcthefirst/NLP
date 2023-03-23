import json

class VendAPIFormat:
    """
    Class to vend new JSON file with hierarchy in API format for angular proof of concept application. Currently in
    testing phase.
    """

    def __init__(self):
        """
        Create a new data structure to vend the hierarchy in a format that is compatible with Angular Fannie Mae
        component.
        """
        self.data = []
        self.exportJSON = {
            'data': self.data
        }
        self.load()
        self.genAPIFormat()
        self.export()

    def load(self, inputFile='C:/test.json'):
        """
        Create a new data structure to vend the hierarchy in a format that is compatible with Angular Fannie Mae
        component.
        """
        with open(inputFile) as hierarchyFile:
            self.hierarchy = json.load(hierarchyFile)

    def genNode(self, inputNode, outputList):
        """
        Create a new data structure to vend the hierarchy in a format that is compatible with Angular Fannie Mae
        component.
        """
        inputChildren = inputNode.get('children', None)
        if inputChildren:
            for childName in inputChildren:
                inputChild = inputChildren[childName]
                id = inputChild['semanticReferenceSet'][0]
                outputParentBlock = self.jsonBlockBuilder(childName, id)
                outputChildBlock = self.genNode(inputChild, outputParentBlock['children'])
                outputParentBlock['children'] = outputChildBlock
                outputList.append(outputParentBlock)
        return outputList

    def genAPIFormat(self):
        """
        Create a new data structure to vend the hierarchy in a format that is compatible with Angular Fannie Mae
        component.
        """
        startAt = self.hierarchy['hierarchy']
        data = self.genNode(startAt, self.exportJSON['data'])
        if data:
            self.exportJSON['data'] = data

    def jsonBlockBuilder(self, name, id):
        """
        Create a new data structure to vend the hierarchy in a format that is compatible with Angular Fannie Mae
        component.
        """
        jsonBlock = {
            "name": name,
            "id": id,
            "children": []
        }
        return jsonBlock

    def export(self, fileName='C:/VendAPIFormat.json'):
        """
        Create a new data structure to vend the hierarchy in a format that is compatible with Angular Fannie Mae
        component.
        """
        with open(fileName, 'w', encoding='utf-8') as theFile:
            json.dump(self.exportJSON,theFile, ensure_ascii=True, sort_keys=True, indent=2)


if __name__ == "__main__":
    VendAPIFormat()