class KefkaTrip:
    time = 15
    def __init__(self, time_parameter):
        self.time = time_parameter
        print('kefkan retki kesti'+ str(self.time))

trip1 = KefkaTrip(20)
trip2 = KefkaTrip(40)
