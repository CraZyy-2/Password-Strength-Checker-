Password-Strength-Checker

A simple tool to help you create and maintain strong, secure passwords.

📥 Installation

Clone the repository:

git clone https://github.com/CraZyy-2/Password-Strength-Checker-.git

🛡️ Why Use It

Weak passwords are one of the most common causes of account hacks.
This checker runs your password through a test and lets you know if it's strong enough to protect your online accounts.

🔍 What It Checks

The script evaluates your password based on several factors:

Length – longer passwords score higher.

Character Variety – mix of uppercase, lowercase, numbers, and special characters.

Complexity – overall structural diversity.

Common Passwords – compares against a list of 10 million known weak passwords.

⚙️ How It Works

The checker uses a point-based system:

Common Passwords
Cross-checks your password against a 10 million-entry list of commonly used passwords. If it’s found, the password is immediately marked weak.

Length
Assigns points according to the total number of characters.

Character Types
Awards points for including multiple character categories (uppercase, lowercase, numbers, symbols).

Final Score
Combines all points and reports your password strength (e.g., Weak, Moderate, Strong) using simple if statements.

🧑‍💻 Contributing

Pull requests and ideas are welcome. Go ahead and open an issue to report bugs or request new features.
