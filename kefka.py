class KefkaTrip:
    time = 15
    def __init__(self, time_parameter):
        self.time = time_parameter
        

trips = [KefkaTrip(20), KefkaTrip(40)]

for trip in trips:
    print('kefkan retki kesti ' + str(trip.time))