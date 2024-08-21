import random
import time

is_raining = random.choice([True, False])
have_umbrella = random.choice([True, False])
print(is_raining)
print(have_umbrella)

if not is_raining:
    print("Let's go")
elif have_umbrella:
    print("Pick an umbrella and let's go")
else:
    while is_raining:
        print("Wait a minute")
        time.sleep(3)
        is_raining = random.choice([True, False])
        print(is_raining)
        if not is_raining:
            print("Now you can go")
            break
    

