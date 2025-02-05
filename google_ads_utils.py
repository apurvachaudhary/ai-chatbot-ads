from google.ads.google_ads.client import GoogleAdsClient

def create_campaign(customer_id, business_niche, budget, keywords):
    client = GoogleAdsClient.load_from_storage("google-ads.yaml")
    campaign_service = client.get_service("CampaignService")
    campaign_operation = client.get_type("CampaignOperation")
    campaign = campaign_operation.create
    campaign.name = f"AI Campaign for {business_niche}"
    campaign.status = client.enums.CampaignStatusEnum.PAUSED
    campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.SEARCH
    return "dummy_campaign_id"
