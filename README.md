# The-password-game
A fun little terminal-based game inspired by The Password Game by Neal.fun. Try to create a valid password that satisfies every ridiculous rule!
Each time you enter a valid password, a new rule is unlocked, making it increasingly harder (and funnier) to satisfy them all.

⚙️ Requirements:
Before running, make sure you have:
- pip install prompt_toolkit requests
- ✅ Python 3.8+
- ✅ Internet connection (required to fetch the daily Wordle answer via requests)

📦 Libraries Used:
- prompt_toolkit → for clean interactive password input in the terminal
- datetime → for date and time rules
- requests → to fetch the daily Wordle answer from the internet

How to Play:
- Run the main Python file:
python main.py

- Enter a password that satisfies the first rule.
- Each success unlocks the next rule.
- If you break certain rules (like killing the egg 🥚 or forgetting to feed Booger 🐥), you lose and restart.
- Complete all 21 rules to win and earn your 🍪.

📜 Rules List
- 0- Password must not be empty.
- 1- Must contain a number.
- 2- Must contain an uppercase letter.
- 3- Must contain a symbol (!@#$%^&*).
- 4- Must include today’s date in the format YYYY-MM-DD.
- 5- Must contain a Roman numeral.
- 6- Number of digits must be even.
- 7- Must include a European country name.
- 8- Must contain today’s Wordle answer (requires internet).
- 9- Number of lowercase letters must equal the number of uppercase letters.
- 10- Must contain the current hour and minute in the format HH-MM.
- 11- Must include the year 2014 (when Brazil hosted the FIFA World Cup).
- 12- An egg 🥚 appears — keep it safe!
- 13- The sum of digits at odd positions must be divisible by 4.
- 14- Must contain the name kroxy (the creator).
- 15- The sum of all digits must be divisible by 3.
- 16- The egg hatches — say hi to Booger 🐥.
- 17- Feed Booger exactly one "worm" each attempt.
- 18- Password must contain "strong".
- 19- Password must contain a 3-letter palindrome substring.
- 20- Final Rule: Retype your entire password perfectly.

🧠 Credits
Made with frustration, caffeine, and pure curiosity by kroxy.
Inspired by Neal.fun’s Password Game.
