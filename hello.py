msg = "Roll a dice!"

print(msg)

print(bool('False'))


with open('filename.txt', 'w') as file:
    file.write(your_string)


with open('filename.txt', 'w') as file:
    for item in your_list:
        file.write(f"{item}\n")

with open('filename.txt', 'w') as file:
    file.write('\n'.join(your_list))

with open('filename.txt', 'r') as file:
    your_list = file.readlines()

with open('filename.txt', 'r') as file:
    your_list = [line.strip() for line in file]
