print("how many mountains should i display?")
mountain_number = int(input())
print("displaying...:")
for count in range(0, mountain_number, 1):
    print("""
      /\\
     /  \\
    /    \\ """)
print("displaying complete.")