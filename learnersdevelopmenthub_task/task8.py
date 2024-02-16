#  Input your Python job domains,
# let Python refine your choices, and print your last chosen one. 

Python_careers = ["Machine Learning", "Data Analyst", "Data Scientist", "Full Stack Development", "DevOps Engineer", "Robotics", "Game Development", "AI Development", "Cyber Security Analyst"]
print ("available python careers are ",Python_careers)
future_domain = input ("enter your python _career:")
Python_careers = [future_domain] if future_domain in Python_careers else []
print("your domain is:", str(Python_careers))