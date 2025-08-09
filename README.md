# 🍽️ Restaurant Brand Name Generator

A fun and interactive **Python console application** that generates unique and catchy restaurant brand names by combining random or user-provided prefixes with curated suffixes. Perfect for brainstorming your next restaurant or food startup!

---

## 📌 Features

- Generate creative restaurant brand names by combining prefixes and suffixes.
- Optionally use your own custom prefix to tailor name generation.
- Generate multiple random names at once.
- Prevents repeating the same prefix and suffix.
- Outputs names in nicely formatted **Capitalized Words** with spaces.
- User-friendly console interface with input validation.
- Type `stop` anytime to exit the program gracefully.

---

## 🛠️ Technologies Used

- Python 3.x
- Standard Library: `random` module
- Console input/output

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your machine.  
2. Copy the code into a file named `restaurant_brand_name_generator.py`.  
3. Open a terminal or command prompt.  
4. Run the program using:  
   python restaurant_brand_name_generator.py
5. Follow on-screen prompts to generate restaurant brand names.


---


## 📄 Example Usage

<pre>

🍽️ Welcome to the Restaurant Brand Name Generator!
Type 'stop' anytime to exit.

Do you want to use your own prefix? (y/n): y
Enter your custom prefix: randy
💡 Your restaurant name: Randy Tavern
Generate again with same prefix? (y/n): n
Do you want to use your own prefix? (y/n): n
How many random restaurant names do you want? (default 1): 10

💡 Your random restaurant names:
- Crispy Portside
- Hot Hall
- Classic Orchard
- Garlic Retreat
- District Terrace
- Seaside Express
- Wok Stop
- Tandoori Jar
- Emerald Clan
- Sultan's Mortar

Generate again with same settings? (y/n): stop
✅ Thanks for using the Restaurant Brand Name Generator! Goodbye 😄
  
</pre>


---


## 🧠 How It Works

- The program randomly selects a prefix and suffix from predefined lists.

- If you provide a prefix, it pairs it with a random suffix ensuring they differ.

- It formats the final name in Capitalized Words separated by a space.

- Users can repeatedly generate names or exit anytime by typing stop.


---


## 💡 Future Improvements

- Add the ability to save generated names to a text file.

- Build a GUI version using tkinter or PyQt for better user experience.

- Allow users to add custom prefixes and suffixes dynamically.

- Integrate with social media APIs to check domain or handle availability.

