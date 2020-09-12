def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("Is healthy must be a boolean")
    
    ending = "because YOLO!"

    if is_healthy:
        ending = "because my body is a temple!"

    return f"I am eating {food} {ending}"

def nap(num_hours):
    if(num_hours >= 2):
        return f"Ugh, I overslept. I didn't mean to nap for {num_hours} whole hours."
    return f"I am feeling refreshed after my {num_hours} hour nap."

def is_funny(person):
    if person == "tim":
        return False
    return True