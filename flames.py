#Flames
#input two names  lovers probably
name1 = input("Enter first name: ").lower().replace(" ", "")
name2 = input("Enter second name: ").lower().replace(" ", "")

# Convert names to lists for ease in removing common letters
n1 = list(name1)
n2 = list(name2)

# Removing common characters
for char in name1:
    if char in name2:
        n1.remove(char)
        n2.remove(char)
        name2 = name2.replace(char, '', 1)

# Total remaining characters
count = len(n1) + len(n2)

# a list to remove letter after encounter 
flames = ['F', 'L', 'A', 'M', 'E', 'S']
index = 0
# To continue a circular rotation using circulat queues logic
while len(flames) > 1:
    index = (index + count - 1) % len(flames)
    flames.pop(index)

# creamting a dictionary to access the letter that apparently tells us the future
res= {
    'F': 'Friends',
    'L': 'Lovers',
    'A': 'Affection',
    'M': 'Marriage',
    'E': 'Enemies',
    'S': 'Siblings'
}

print("Relationship:", res[flames[0]])
