class Bicycle:
    def __init__(self, buyDate,brand,model,type,color,bicycleFrameSize,wheelSize):
        self._buyDate=buyDate
        self._brand=brand
        self._model=model
        self._type=type
        self._color=color
        self._bicycleFrameSize=bicycleFrameSize
        self._wheelSize=wheelSize
        self._repairList=None