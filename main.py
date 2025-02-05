from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google_ads_utils import create_campaign
import uvicorn

app = FastAPI()

class CampaignData(BaseModel):
    customer_id: str
    business_niche: str
    budget: float
    keywords: list[str]

@app.post("/create_campaign")
async def create_campaign_endpoint(data: CampaignData):
    try:
        response = create_campaign(
            customer_id=data.customer_id, 
            business_niche=data.business_niche, 
            budget=data.budget, 
            keywords=data.keywords
        )
        return {"status": "success", "campaign_id": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
