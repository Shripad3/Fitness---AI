import function
import os
import time

time_start = time.time()

name = ""
gender = ""
age = ""
weight = ""
height = ""
food_preference = ""
goal = ""

prompt_text = f'''
My name is {name}. I am a {age} year old {gender}.
My weight is {weight}, my height is {height} and I prefer {food_preference} food.
Give me a detailed diet plan and a workout plan to achieve this goal ({goal}).
'''
text = ""
text = function.ask_gemini(prompt_text)
print(text)
time_end = time.time()
print(time_end - time_start)