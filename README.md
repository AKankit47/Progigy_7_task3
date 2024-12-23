# Progigy_7_task3

# Password Strength Checker

This is a user-friendly GUI-based Password Strength Checker built using Python's Tkinter module. The tool evaluates the strength of a password based on various criteria and provides actionable feedback to improve it.

## Features

- **Dynamic Strength Assessment**: Evaluates the strength of passwords as "Weak," "Moderate," or "Strong."
- **Customized GUI**: Aesthetic design with user-friendly interaction.
- **Feedback System**: Provides specific suggestions to improve the password.
- **Clear Functionality**: Allows users to reset the input fields and feedback.
- **Responsive Colors**: Strength indicators are color-coded for better understanding.

## Criteria for Password Strength
The password is assessed based on:
1. Minimum length of **8 characters**.
2. At least **one uppercase letter**.
3. At least **one lowercase letter**.
4. At least **one number**.
5. At least **one special character** (e.g., `!@#$%^&*`).

## Requirements

- Python 3.7+
- Tkinter (comes pre-installed with Python)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AKankit47/Prodigy_7_task3.git
    cd Prodigy_7_task3
    ```
2. Run the script:
    ```bash
    python task3.py
    ```

## Usage

1. Enter a password into the input field.
2. Click on **"Check Strength"** to evaluate the password.
3. Review the strength indicator and feedback for improvement.
4. Use the **"Clear"** button to reset the input and feedback.


## How It Works

The program uses regular expressions to check for the following:
- Password length.
- Presence of uppercase and lowercase letters.
- Presence of numbers.
- Presence of special characters.

A score out of 5 is calculated based on these criteria, and the password strength is categorized as:
- **Strong**: All criteria met.
- **Moderate**: 3-4 criteria met.
- **Weak**: Less than 3 criteria met.

## Customization

You can modify the colors, fonts, and layout by editing the `Tkinter` code in the `password_strength_checker.py` file. For example:
- Update `bg` and `fg` parameters for background and text colors.
- Adjust font sizes in `font=(...)`.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature-name"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

**Ankit Kumar**  
Intermediate hacker and cybersecurity enthusiast  
[LinkedIn Profile](www.linkedin.com/in/ankit-ak47)

