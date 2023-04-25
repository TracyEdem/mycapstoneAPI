from pydantic import BaseModel

class Measurement(BaseModel):
    # measurementId: int
    bustCirc: float
    waistCirc: float
    accrossBack: float
    biceps: float
    sleeveLen: float
    shoulderWaist: float
    # clientId: int
    nipNip: float
    nipShoulder: float
    dressLen: float
    hipCirc: float
    kneeCirc: float
    skirtLen: float
    thighWidth: float
    trouserLen: float
    waistKnee: float