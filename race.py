def ask_for_distance(name):
  dist = float(input(f'How far did {name} run (in feet)?'))
  return dist
def ask_for_minutes(name,dist):
    min2 = input(f'How many minutes did {name} take to run {dist} feet?')
    return min2
def compute_speed(minute,dist):
    secs = float(minute) *60
    speed = dist/secs
    return speed

def run(name):
    distance = ask_for_distance(name)
    minutes = ask_for_minutes(name,distance)
    speed = compute_speed(minutes,distance)
    return speed

def main():
    jane_speed = run('Jane')
    peter_speed = run('Peter')
    if jane_speed > peter_speed:
        print(f'Jane was the fastest at {jane_speed} f/s')
    elif peter_speed > jane_speed:
        print(f'Peter was the fastest at {peter_speed} f/s')
    else:
        print(f'The race was a tie!')
    print('Well done Peter and Jane!')



main()
