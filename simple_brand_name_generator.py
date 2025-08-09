import random

prefixes = [
    "Spice", "Golden", "Urban", "The Daily", "Saffron", "Royal", "Crispy", "Grand",
    "Mama's", "The Corner", "Red", "Basil", "Fire", "Stone", "Simply", "Chef's",
    "The Little", "Green", "Fresh", "Happy", "Coastal", "The Local", "Savory",
    "Modern", "Silver", "Lemon", "Street", "Tandoori", "Wok", "Secret",
    "Harvest", "King's", "The Cozy", "Palm", "Zesty", "Clay", "Iron", "Salt",
    "Pepper", "Vineyard", "The Good", "Old", "New", "The Flying", "Global",
    "Hearth", "Garden", "Smoky", "Sweet", "Hot",
    "Amber", "Ginger", "Mountain", "Bliss", "Papa's", "Azure", "Garlic", "River",
    "Joy", "The Farmer's", "Black", "Chili", "Valley", "Ember", "Sultan's", "White",
    "Olive", "Seaside", "Flame", "Emperor's", "Crimson", "Truffle", "Harbor",
    "Spark", "The Baker's", "Emerald", "Honey", "City", "Fusion", "Brother's",
    "Ruby", "Maple", "Village", "Twist", "Sister's", "Rustic", "Cinnamon",
    "Downtown", "Authentic", "Nawab's", "Noble", "Rosemary", "Metro", "Classic",
    "The Fisher's", "Humble", "Thyme", "District", "Divine", "Legacy", "Ancient",
    "Minty", "Kingdom", "Epic", "Heritage"
]

suffixes = [
    "Kitchen", "Grill", "Table", "House", "Bistro", "Eatery", "Spoon", "Pot",
    "Bowl", "Plate", "Cafe", "Diner", "Spice", "Curry", "Tandoor", "Wok",
    "Junction", "Corner", "Bites", "Feast", "Harvest", "Leaf", "Sprout", "Yard",
    "Lounge", "Den", "Canteen", "Hub", "Spot", "Vine", "Root", "Oven",
    "Pan", "Hut", "Joint", "Express", "Co.", "Bay", "Cove", "Barn",
    "Post", "Deck", "Bar", "Room", "Ladle", "Market", "Dhaba", "Cottage",
    "Tavern", "Skillet", "Fare", "Grove", "Pub", "Cauldron", "Provisions", "Orchard",
    "Inn", "Kettle", "Goods", "Meadow", "Hall", "Mortar", "Company", "Creek",
    "Manor", "Pestle", "Collective", "Brook", "Castle", "Fork", "Union", "Spring",
    "Palace", "Knife", "Guild", "Falls", "Villa", "Board", "Clan", "Ridge",
    "Retreat", "Barrel", "Tribe", "Shore", "Hideaway", "Cask", "Story", "Dockside",
    "Nook", "Jar", "Tale", "Portside", "Alley", "Tin", "Journey", "Square",
    "Lane", "Cellar", "Quest", "Plaza", "Pantry", "Stop", "Terrace"
]


def to_camel_case_with_space(prefix, suffix):
    """Convert restaurant name to Capitalized Words with space."""
    return f"{prefix.capitalize()} {suffix.capitalize()}"

def generate_brand_name(prefix=None):
    """Generates a restaurant brand name with optional custom prefix."""
    if prefix:
        random_suffix = random.choice(suffixes)
        while random_suffix.lower() == prefix.lower():
            random_suffix = random.choice(suffixes)
        return to_camel_case_with_space(prefix, random_suffix)
    else:
        random_prefix = random.choice(prefixes)
        random_suffix = random.choice(suffixes)
        while random_suffix.lower() == random_prefix.lower():
            random_suffix = random.choice(suffixes)
        return to_camel_case_with_space(random_prefix, random_suffix)

print("🍽️ Welcome to the Restaurant Brand Name Generator!")
print("Type 'stop' anytime to exit.\n")

while True:
    choice = input("Do you want to use your own prefix? (y/n): ").strip().lower()
    if choice == "stop":
        print("✅ Thanks for using the Restaurant Brand Name Generator! Goodbye 😄")
        break

    if choice == "y":
        custom_prefix = input("Enter your custom prefix: ").strip().capitalize()
        if custom_prefix.lower() == "stop":
            print("✅ Thanks for using the Restaurant Brand Name Generator! Goodbye 😄")
            break

        while True:
            print("💡 Your restaurant name:", generate_brand_name(custom_prefix))
            again = input("Generate again with same prefix? (y/n): ").strip().lower()
            if again == "stop":
                print("✅ Thanks for using the Restaurant Brand Name Generator! Goodbye 😄")
                exit()
            if again != "y":
                break

    elif choice == "n":
        count = input("How many random restaurant names do you want? (default 1): ").strip()
        if count.lower() == "stop":
            print("✅ Thanks for using the Restaurant Brand Name Generator! Goodbye 😄")
            break
        count = int(count) if count.isdigit() and int(count) > 0 else 1

        while True:
            print("\n💡 Your random restaurant names:")
            for _ in range(count):
                print("-", generate_brand_name())
            print()
            again = input("Generate again with same settings? (y/n): ").strip().lower()
            if again == "stop":
                print("✅ Thanks for using the Restaurant Brand Name Generator! Goodbye 😄")
                exit()
            if again != "y":
                break

    else:
        print("❌ Invalid input. Please type 'y', 'n', or 'stop'.\n")
