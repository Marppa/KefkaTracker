class KefkaTrip:
    def __init__(self, time, behaviour, poop):
        self.time = time
        self.behaviour = behaviour
        self.poop = poop

trips = [KefkaTrip(20, 'hermostunut', True), KefkaTrip(40, 'tohko', False)]

for trip in trips:
    print('kefkan retki kesti ' + str(trip.time))
    print('kefka oli ' + str(trip.behaviour))
    if trip.poop:
        print('tuli kakka')
    else:
        print('ei kakkaa')
    print('')