SPEED_OF_LIGHT = 299_792_458

def calculator_light_time(distance):
    return distance / SPEED_OF_LIGHT

distance_between_objects = 1_000_000
time_needed = calculator_light_time(distance_between_objects)

print(f"Світлу потрібно {time_needed} секунд, щоб пройти {distance_between_objects} метрів.")
