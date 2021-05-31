sql_command = """
SELECT
    start_date AS start_datetime,
    start_station_name,
    start_station.latitude AS start_station_lat,
    start_station.longitude AS start_station_lng,
    end_date AS end_datetime,
    end_station_name,
    end_station.latitude AS end_station_lat,
    end_station.longitude AS end_station_lng,
    date_diff(end_date, start_date, MINUTE) AS hire_minutes
FROM `bigquery-public-data.london_bicycles.cycle_hire` AS hire
JOIN `bigquery-public-data.london_bicycles.cycle_stations` AS start_station
    ON hire.start_station_id = start_station.id
JOIN `bigquery-public-data.london_bicycles.cycle_stations` AS end_station
    ON hire.end_station_id = end_station.id
WHERE start_station.installed IS TRUE
    AND end_station.installed IS TRUE
    AND start_date > '2017-06-01 00:00:00' and end_date < '2017-06-02 00:00:00'
ORDER BY start_datetime
"""
