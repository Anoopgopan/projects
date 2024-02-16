# Sorting Your 2024 Goals! 🚀🔤 
# Input your aspirations, and let Python organize them in alphabetical order. 


n=list(map(str,input("Enter your goals list seperated by commas: ").split(',')))
n.sort()
print("In 2024 you need to achieve:\n"+'\n'.join(n))

