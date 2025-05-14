import pytest
from project import all_departure_stations, all_arrival_stations, find_available_routes
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
            TrainRoute(1 ,"11022", "AAA", "NGP", "NK", "08:00", "23:00", 10, "mon")
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

    routes = [
        TrainRoute(1 ,"11022", "AAA", "NGP", "CSMT", "08:00", "23:00", 10, "mon"),
        TrainRoute(1 ,"11022", "AAA", "TNA", "CSMT", "08:00", "23:00", 10, "mon")
        ]
    stations = all_arrival_stations(routes, "NGP")
    assert stations == ["CSMT"]


    routes = [
        TrainRoute(1 ,"11022", "AAA", "NGP", "CSMT", "08:00", "23:00", 10, "mon"),
        TrainRoute(1 ,"11022", "AAA", "NGP", "G", "08:00", "23:00", 10, "mon")
        ]
    stations = all_arrival_stations(routes, "NGP")
    assert stations == ["CSMT", "G"]


    routes = [
        TrainRoute(1 ,"11022", "AAA", "NGP", "CSMT", "08:00", "23:00", 10, "mon")
        ]
    stations = all_arrival_stations(routes, "PUNE")
    assert stations == []

    routes = [
        TrainRoute(1 ,"11022", "AAA", "NGP", "CSMT", "08:00", "23:00", 10, "mon"),
        TrainRoute(1 ,"11022", "AAA", "PUNE", "G", "08:00", "23:00", 10, "mon"),
        TrainRoute(1 ,"11022", "AAA", "PUNE", "KYN", "08:00", "23:00", 10, "mon")
        ]
    stations = all_arrival_stations(routes, "PUNE")
    assert stations == ["G", "KYN"]

def test_find_available_routes():
    train_1 = TrainRoute(1 ,"11022", "AAA", "NGP", "CSMT", "08:00", "23:00", 10, "mon")
    train_2 = TrainRoute(1 ,"11020", "AAA", "NGP", "CSMT", "08:00", "20:00", 30, "mon/fri")
    train_3 = TrainRoute(1 ,"11050", "AAA", "KYN", "CSMT", "08:00", "20:00", 30, "mon/fri")

    routes = [train_1]
    available_seats ={train_1.id: 1}
    available_routes = find_available_routes(routes, "NGP", "CSMT", "mon", available_seats)
    assert available_routes == [train_1]

    routes = [ train_1]
    available_seats ={train_1.id: 1}
    available_routes = find_available_routes(routes, "NGP", "G", "mon", available_seats)
    assert available_routes == []

    routes = [train_1, train_2, train_3]
    available_seats ={train_1.id: 1, train_2.id: 5, train_3.id: 10}
    available_routes = find_available_routes(routes, "NGP", "CSMT", "mon", available_seats)
    assert available_routes == [train_1, train_2]

    routes = [train_1]
    available_seats ={train_1.id: 1}
    available_routes = find_available_routes(routes, "NGP", "CSMT", "tue", available_seats)
    assert available_routes == []

    routes = [train_1]
    available_seats ={train_1.id: 0}
    available_routes = find_available_routes(routes, "NGP", "CSMT", "mon", available_seats)
    assert available_routes == []