🎮 KBC Quiz Game - Python Tkinter Application

A desktop-based quiz application inspired by Kaun Banega Crorepati (KBC). Built with Python Tkinter, it features category-based quizzes, randomized answer options, sound effects, progress tracking, and a modern user interface.

🚀 Features

. Modern Dark Theme UI: Clean and engaging design for a pleasant user experience.

. User Login: Personalize your quiz by entering your name.

. Category Selection: Choose from Coding, General Knowledge, Movies, and more.

. Randomized Answer Options: Options are shuffled every time to prevent memorization.

. Progress Tracking: Progress bar and question counter to monitor your quiz journey.

. Instant Feedback: Get ✅ correct or ❌ incorrect feedback after each question.

. Sound Effects: Success ding for correct answers and soft buzz for incorrect ones.

. Final Scoreboard: Displays total score and performance summary after quiz completion.


🧰 Tech Stack

Component	Technology
GUI	Python Tkinter
Sound Effects	pygame
Logic	Python (OOP concepts)
Data Management	Python Dictionaries


📁 Project Structure

pgsql
Copy
Edit
KBC-GAME/
│
├── kbc_gui.py       – Main application file (GUI + logic)
├── questions.py     – Quiz questions data (dictionary format)
├── correct.wav      – Sound effect for correct answer
├── wrong.wav        – Sound effect for incorrect answer
├── README.md        – Project documentation
└── __pycache__/     – Python cache files


📥 Setup Instructions

1. Clone the Repository :
bash
Copy
Edit
git clone https://github.com/priyanshi20045/KBC-GAME.git
cd KBC-GAME

2. Install Required Dependencies :
bash
Copy
Edit
pip install pygame

3. Run the Application :
bash
Copy
Edit
python kbc_gui.py


🎁 Application Flow

. Enter your name to start the quiz.

. Select your preferred category.

. Answer each question with shuffled options every time.

. Receive immediate feedback after each response.

. Track progress using the progress bar and question counter.

. At the end, see your final score and performance summary.


👩‍💻 Developed By

Priyanshi Seth
B.Tech (CSE), 2021–2025
GitHub: priyanshi20045

📝 License

This project is licensed under the MIT License.
