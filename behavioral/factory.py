from abc import ABC


class Vehicle(ABC):
    specifications = None

    def __init__(self, specifications):
        self.specifications = specifications # must be a VehicleSpecification
        pass

    def start_vehicle(self):
        pass

class VehicleSpecification:
    color = None
    plate = None  # Could be a Plate object with ID and state, or just None

    def __init__(self,
                 color=None,
                 plate=None):
        self.color = color
        self.plate = plate


class Hybrid(Vehicle):
    def __init__(self, specifications, aux_battery_capacity):
        super().__init__(specifications)
        self.aux_battery_capacity = aux_battery_capacity

    def start_vehicle(self):
        print('Starting Hybrid Vehicle...')
        self.start_engine()
        self.start_battery_system()

    def start_engine(self):
        print(' > Starting engine')
        pass

    def start_battery_system(self):
        print(' > Starting battery system')
        pass


class Gas(Vehicle):
    def start_vehicle(self):
        print('Starting Gas Vehicle...')
        self.start_engine()

    def start_engine(self):
        print(' > Starting engine')
        pass


class Bike(Vehicle):
    def start_vehicle(self):
        print('Starting Bike Vehicle...')
        print(' > Nothing to start, really')


class VehicleFactory:
    def __init__(self):
        pass

    @staticmethod
    def new(query_vehicle, vehicle_specifications):
        return_vehicle = None

        if query_vehicle == 'hybrid':
            return_vehicle = Hybrid(vehicle_specifications, aux_battery_capacity=100)
        elif query_vehicle == 'gas':
            return_vehicle = Gas(vehicle_specifications)
        elif query_vehicle == 'bike':
            return_vehicle = Bike(vehicle_specifications)
        else:
            raise Exception('Invalid query_vehicle for VehicleFactory')

        return return_vehicle

if __name__ == '__main__':
    vehicle_factory = VehicleFactory()
    my_bike = vehicle_factory.new('bike', VehicleSpecification(color='white'))
    my_gas = vehicle_factory.new('gas', VehicleSpecification(color='black', plate='13372GD'))
    my_hybrid = vehicle_factory.new('hybrid', VehicleSpecification(color='red'))

    my_bike.start_vehicle()
    my_gas.start_vehicle()
    my_hybrid.start_vehicle()
