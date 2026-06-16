# ==========================================
# Day 4 Assignment - Cinema Ticket Pricing System
# ==========================================

print("\n===== CINEMA TICKET PRICING SYSTEM =====\n")

# Base ticket price
BASE_PRICE = 1000

# ----------------------------
# User Input
# ----------------------------
age = int(input("Enter Customer Age: "))
day = input("Enter Day of the Week: ").strip().lower()
member_input = input("Are you a Member? (yes/no): ").strip().lower()

# Convert yes/no to Boolean
is_member = member_input == "yes"

# ----------------------------
# Ticket Pricing by Age
# ----------------------------
if age < 5:
    category = "Child (Under 5)"
    final_price = 0
    discount_applied = "100% Discount (Free Entry)"

elif age < 18:
    category = "Minor"
    final_price = BASE_PRICE * 0.50
    discount_applied = "50% Discount"

elif age >= 60:
    category = "Senior Citizen"
    final_price = BASE_PRICE * 0.70
    discount_applied = "30% Discount"

else:
    category = "Adult"
    final_price = BASE_PRICE
    discount_applied = "No Age Discount"

# ----------------------------
# Extra Member Discount
# ----------------------------
weekdays = {"monday", "tuesday", "wednesday", "thursday", "friday"}

if is_member and day in weekdays and final_price > 0:
    final_price *= 0.90
    discount_applied += " + 10% Member Discount"

# ----------------------------
# Free Popcorn Offer (Nested If)
# ----------------------------
if is_member:
    if age >= 18:
        popcorn_offer = "Large Popcorn Free 🍿"
    else:
        popcorn_offer = "Regular Popcorn Free 🍿"
else:
    popcorn_offer = "No Popcorn Offer"

# ----------------------------
# Closing Message (Ternary Expression)
# ----------------------------
message = "Free Entry 🎉" if final_price == 0 else "Enjoy the Show! 🎬"

# ----------------------------
# Output Summary
# ----------------------------
print("\n" + "=" * 45)
print("          CINEMA TICKET SUMMARY")
print("=" * 45)

print(f"Category           : {category}")
print(f"Customer Age       : {age}")
print(f"Day                : {day.title()}")
print(f"Member             : {'Yes' if is_member else 'No'}")
print(f"Discount Applied   : {discount_applied}")
print(f"Popcorn Offer      : {popcorn_offer}")
print(f"Final Ticket Price : Rs. {final_price:.2f}")
print(f"Message            : {message}")

print("=" * 45)