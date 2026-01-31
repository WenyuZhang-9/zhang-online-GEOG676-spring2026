# Homework 02
# Topic: Fun with loops
# Author: Wenyu Zhang
# Course: TAMU GIS Programming

# -------------------------
# Part 1 (30 pt)
# Multiply all list items together
# -------------------------

part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

product = 1
for num in part1:
    product = product * num

print("Part 1 result (product):", product)


# -------------------------
# Part 2 (30 pt)
# Add all list items together
# -------------------------

part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]

total_sum = 0
for num in part2:
    total_sum = total_sum + num

print("Part 2 result (sum):", total_sum)


# -------------------------
# Part 3 (40 pt)
# Add only even numbers
# -------------------------

part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]

even_sum = 0
for num in part3:
    if num % 2 == 0:
        even_sum = even_sum + num

print("Part 3 result (sum of even numbers):", even_sum)
# End of homework02_loops.py