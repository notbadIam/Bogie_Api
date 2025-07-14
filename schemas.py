from pydantic import BaseModel
from datetime import date

class BMBCChecksheet(BaseModel):
    adjustingTube: str
    cylinderBody: str
    pistonTrunnion: str
    plungerSpring: str

class BogieChecksheet(BaseModel):
    axleGuide: str
    bogieFrameCondition: str
    bolster: str
    bolsterSuspensionBracket: str
    lowerSpringSeat: str

class BogieDetails(BaseModel):
    bogieNo: str
    dateOfIOH: date
    deficitComponents: str
    incomingDivAndDate: str
    makerYearBuilt: str

class BogieFormCreate(BaseModel):
    bmbcChecksheet: BMBCChecksheet
    bogieChecksheet: BogieChecksheet
    bogieDetails: BogieDetails
    formNumber: str
    inspectionBy: str
    inspectionDate: date




class WheelFields(BaseModel):
    axleBoxHousingBoreDia: str
    bearingSeatDiameter: str
    condemningDia: str
    intermediateWWP: str
    lastShopIssueSize: str
    rollerBearingBoreDia: str
    rollerBearingOuterDia: str
    rollerBearingWidth: str
    treadDiameterNew: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelDiscWidth: str
    wheelGauge: str
    wheelProfile: str

class WheelFormCreate(BaseModel):
    fields: WheelFields
    formNumber: str
    submittedBy: str
    submittedDate: date
