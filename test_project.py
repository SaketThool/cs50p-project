import pytest
from project import all_departure_stations, all_arrival_stations
from train import TrainRoute

def test_all_departure_stations():
    routes = []
    stations = all_departure_stations(routes)
    assert stations == []

    routes = [
        TrainRoute(1 ,"11022", "AAA", "NGP", "CSMT", "08:00", "23:00", 10, "mon")
        ]
    stations = all_departure_stations(routes)
    assert stations == ["NGP"]

    routes = [
            TrainRoute(1 ,"11022", "AAA", "NGP", "CSMT", "08:00", "23:00", 10, "mon"),
            TrainRoute(1 ,"11022", "AAA", "NGP", "CSMT", "08:00", "23:00", 10, "mon")
            ]
    stations = all_departure_stations(routes)
    assert stations == ["NGP"]

    routes = [
            TrainRoute(1 ,"11022", "AAA", "NGP", "CSMT", "08:00", "23:00", 10, "mon"),
            TrainRoute(1 ,"11022", "AAA", "TNA", "CSMT", "08:00", "23:00", 10, "mon")
            ]
    stations = all_departure_stations(routes)
    assert stations == ["NGP", "TNA"]

def test_all_arrival_stations():
    routes = []
    stations = all_arrival_stations(routes, "NGP")
    assert stations == []

    routes = [
        TrainRoute(1 ,"11022", "AAA", "NGP", "CSMT", "08:00", "23:00", 10, "mon")
        ]
    stations = all_arrival_stations(routes, "NGP")
    assert stations == ["CSMT"]