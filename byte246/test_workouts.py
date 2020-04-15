"""
Bite 246. Test print / standard output

In this Bite you test a function that prints to stdout. Check out pytest's Capturing of the stdout/stderr output how
to test this. You probably want to use the capsys / capfd fixture in your test code.

Have fun and keep calm and code in Python!
"""


WORKOUTS = {'mon': 'upper body #1',
            'tue': 'lower body #1',
            'wed': '30 min cardio',
            'thu': 'upper body #2',
            'fri': 'lower body #2'}


def print_workout_days(workout: str, my_workouts: dict = WORKOUTS) -> None:
    """Print the days (comma separated and title cased) of my_workouts
       that (partially) match the workout string passed in. If no
       workout matches, print 'No matching workout'
    """
    days = [day.title() for day, wo in my_workouts.items()
            if workout.lower() in wo.lower()]
    print(', '.join(days) if days else 'No matching workout')
