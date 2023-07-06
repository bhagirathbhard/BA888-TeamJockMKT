import jockmkt_sdk as jockmkt
import json
import os

JockApiClient = jockmkt.JockApiClient("CLIENT_ID", "CLIENT_SECRET", "REFRESH_TOKEN")
athlete_shares = JockApiClient.athlete_share_count("LeBron James")
print(athlete_shares)