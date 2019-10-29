
print("how many bars should be charged?")
user_bars = int(input())
bar_count = 0
block_count = 0
print("charging:")
while (bar_count < user_bars):
    print("\n",end="")
    bar_count = bar_count +1
    print("█ " *bar_count)
print("\nfully charged")