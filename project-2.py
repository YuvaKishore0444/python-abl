attended_classes = 36
total_classes = 50
target_percentage = 75.0

current_percentage = (attended_classes / total_classes) * 100
extra_classes = 0

while ((attended_classes + extra_classes) / (total_classes + extra_classes)) * 100 < target_percentage:
    extra_classes += 1

final_percentage = ((attended_classes + extra_classes) / (total_classes + extra_classes)) * 100

print(f"Current Attendance: {current_percentage:.2f}%")
print(f"Target Attendance: {target_percentage:.2f}%")
print(f"Minimum Consecutive Classes Needed: {extra_classes}")
print(f"New Attendance Status: {final_percentage:.2f}%")