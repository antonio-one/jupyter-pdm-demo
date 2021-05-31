sql_command = """
SELECT
    communityState,
    INITCAP(communityCity) as communityCity,
    service,
    status,
    COUNT(DISTINCT stationId) AS number_of_stations
FROM `bigquery-public-data.fcc_political_ads.broadcast_tv_radio_station`
GROUP BY communityState, communityCity, service, status
"""
