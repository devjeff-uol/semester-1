"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }
state_keys = list(states)

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"
time_in_state = 0

# Simulate the traffic light system up to time=maxtime in 1-second steps
while systime <= maxtime:
    state_index = state_keys.index(state)
    if time_in_state == states[state]:
        state = state_keys[(state_index + 1) % len(state_keys)]
        time_in_state = 0
    
    print(f"Time {systime:03} State {state}")
    systime = systime + 1
    time_in_state += 1

# At the end of each step you should output the time and state using the statement on line 14