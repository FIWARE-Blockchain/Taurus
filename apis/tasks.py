from background_task import background

@background(schedule=2)
def demo_task(message):
    print(message)
