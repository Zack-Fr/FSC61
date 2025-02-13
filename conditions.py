def convert_weight():
    # Prompt the user for their choice
    choice = input("Do you want to convert from (K)ilograms to pounds or from (L)bs to kilograms? Enter K or L: ")

    # Based on the user's choice, perform the conversion
    if choice.lower() == 'k':
        kg = float(input("Enter weight in kilograms: "))
        lbs = kg * 2.20462  # 1 kg ≈ 2.20462 lbs
        print(f"{kg} kg is approximately {lbs:.2f} lbs.")
    elif choice.lower() == 'l':
        lbs = float(input("Enter weight in pounds: "))
        kg = lbs / 2.20462  # 1 lb ≈ 0.453592 kg
        print(f"{lbs} lbs is approximately {kg:.2f} kg.")
    else:
        print("Invalid choice. Please enter 'K' or 'L'.")

if __name__ == "__main__":
    convert_weight()
