def handle_command(self, message):
    match message:  # (1)
        case ['BEEPER', frequency, times]:  # (2)
            self.beep(times, frequency)
        case ['NECK', angle]:  # (3)
            self.rotate_neck(angle)
        case ['LED', pin, intensity]:  # (4)
            self.leds[ident].set_brightness(pin, intensity)
        case ['LED', pin, red, green, blue]:  # (5)
            self.leds[ident].set_color(pin, red, green, blue)
        case _:  # (6)
            raise InvalidCommand(message)
        
# tipo o switch case da linguagem c

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:  # (1)
            case [name, _, _, (lat, lon)] if lon <= 0:  # (2)
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

if __name__ == '__main__':
    main()