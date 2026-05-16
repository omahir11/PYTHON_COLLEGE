"""
╔══════════════════════════════════════════════╗
║         TERMINAL QUIZ GAME - QUIZMASTER       ║
║         Beginner-Friendly Python Game         ║
╚══════════════════════════════════════════════╝

Author  : QuizMaster
Version : 1.0
Requires: Python 3.6+ (standard library only)
"""

import time
import random
import sys
import os
import threading

# ─────────────────────────────────────────────
#  ANSI COLOR CODES (work on most terminals)
# ─────────────────────────────────────────────
class Color:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BG_BLUE = "\033[44m"
    BG_GREEN= "\033[42m"
    BG_RED  = "\033[41m"

# ─────────────────────────────────────────────
#  QUESTION BANK
#  Each question is a dict with:
#    "q"       : question text
#    "options" : list of 4 choices [A, B, C, D]
#    "answer"  : correct option letter ("A"/"B"/"C"/"D")
#    "diff"    : difficulty ("Easy" / "Medium" / "Hard")
# ─────────────────────────────────────────────
ALL_QUESTIONS = [
    # ── EASY ──────────────────────────────────
    {
        "q": "What is the output of  print(2 ** 3)  in Python?",
        "options": ["6", "8", "9", "5"],
        "answer": "B",
        "diff": "Easy"
    },
    {
        "q": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Jupiter", "Mars", "Saturn"],
        "answer": "C",
        "diff": "Easy"
    },
    {
        "q": "How many sides does a hexagon have?",
        "options": ["5", "6", "7", "8"],
        "answer": "B",
        "diff": "Easy"
    },
    {
        "q": "What is the chemical symbol for water?",
        "options": ["WA", "HO", "H2O", "OX"],
        "answer": "C",
        "diff": "Easy"
    },
    {
        "q": "Which data type is used to store True/False in Python?",
        "options": ["int", "str", "bool", "float"],
        "answer": "C",
        "diff": "Easy"
    },
    # ── MEDIUM ────────────────────────────────
    {
        "q": "What does CPU stand for?",
        "options": [
            "Central Process Unit",
            "Central Processing Unit",
            "Computer Personal Unit",
            "Core Processing Unit"
        ],
        "answer": "B",
        "diff": "Medium"
    },
    {
        "q": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "C",
        "diff": "Medium"
    },
    {
        "q": "What is the speed of light (approx.) in km/s?",
        "options": ["200,000", "300,000", "150,000", "400,000"],
        "answer": "B",
        "diff": "Medium"
    },
    {
        "q": "In Python, which method adds an element to the end of a list?",
        "options": ["add()", "insert()", "push()", "append()"],
        "answer": "D",
        "diff": "Medium"
    },
    {
        "q": "What year was the World Wide Web invented?",
        "options": ["1985", "1989", "1995", "2001"],
        "answer": "B",
        "diff": "Medium"
    },
    {
        "q": "Which of these is NOT a Python built-in data structure?",
        "options": ["list", "tuple", "array", "dictionary"],
        "answer": "C",
        "diff": "Medium"
    },
    # ── HARD ──────────────────────────────────
    {
        "q": "What is the time complexity of binary search?",
        "options": ["O(n)", "O(n²)", "O(log n)", "O(1)"],
        "answer": "C",
        "diff": "Hard"
    },
    {
        "q": "Which Python module is used to work with regular expressions?",
        "options": ["regex", "re", "regexp", "rx"],
        "answer": "B",
        "diff": "Hard"
    },
    {
        "q": "What does GIL stand for in Python?",
        "options": [
            "Global Instance Lock",
            "General Input Layer",
            "Global Interpreter Lock",
            "Generic Iterator Loop"
        ],
        "answer": "C",
        "diff": "Hard"
    },
    {
        "q": "In Python, what is the result of  bool([])  ?",
        "options": ["True", "False", "None", "Error"],
        "answer": "B",
        "diff": "Hard"
    },
]

# Session-wide high score tracker  {name: score}
HIGH_SCORES: list = []   # list of (name, score, total, diff_label) tuples


# ─────────────────────────────────────────────
#  UTILITY HELPERS
# ─────────────────────────────────────────────
def clear_screen():
    """Clear terminal screen cross-platform."""
    os.system("cls" if os.name == "nt" else "clear")


def c(text, *codes):
    """Wrap text with ANSI color codes and auto-reset."""
    return "".join(codes) + str(text) + Color.RESET


def center(text, width=60):
    """Center plain text within given width."""
    return text.center(width)


def hline(char="─", width=60, color=Color.CYAN):
    """Print a horizontal divider line."""
    print(c(char * width, color))


def slow_print(text, delay=0.03):
    """Print text character by character for dramatic effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def loading_dots(message="Loading", dots=5, delay=0.3):
    """Animate loading dots after a message."""
    sys.stdout.write(c(message, Color.DIM))
    sys.stdout.flush()
    for _ in range(dots):
        time.sleep(delay)
        sys.stdout.write(c(".", Color.YELLOW))
        sys.stdout.flush()
    print()


def countdown_bar(seconds=15, label="Time"):
    """
    Display a live countdown progress bar.
    Returns True if the player still has time, False if timed out.
    The bar refreshes in-place using carriage return.
    """
    bar_width = 30
    for remaining in range(seconds, -1, -1):
        filled   = int(bar_width * remaining / seconds)
        empty    = bar_width - filled
        bar      = "█" * filled + "░" * empty
        color    = Color.GREEN if remaining > seconds // 2 else (
                   Color.YELLOW if remaining > 3 else Color.RED)
        line = (
            f"\r  {c(label + ':', Color.BOLD)} "
            f"{c('[' + bar + ']', color)} "
            f"{c(str(remaining).rjust(2) + 's', color)}  "
        )
        sys.stdout.write(line)
        sys.stdout.flush()
        if remaining > 0:
            time.sleep(1)
    print()   # move to next line after countdown


# ─────────────────────────────────────────────
#  SCREEN: WELCOME BANNER
# ─────────────────────────────────────────────
def show_welcome():
    """Display the animated welcome/title screen."""
    clear_screen()
    time.sleep(0.2)

    banner_lines = [
        "╔══════════════════════════════════════════════════════════╗",
        "║                                                          ║",
        "║        ██████╗ ██╗   ██╗██╗███████╗                     ║",
        "║       ██╔═══██╗██║   ██║██║╚══███╔╝                     ║",
        "║       ██║   ██║██║   ██║██║  ███╔╝                      ║",
        "║       ██║▄▄ ██║██║   ██║██║ ███╔╝                       ║",
        "║       ╚██████╔╝╚██████╔╝██║███████╗                     ║",
        "║        ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝  M A S T E R       ║",
        "║                                                          ║",
        "║            🧠  Test Your Knowledge!  🧠                  ║",
        "║                                                          ║",
        "╚══════════════════════════════════════════════════════════╝",
    ]

    for line in banner_lines:
        print(c(center(line, 62), Color.CYAN, Color.BOLD))
        time.sleep(0.05)

    print()
    instructions = [
        ("📋", "HOW TO PLAY"),
        ("▸",  "Choose a difficulty: Easy / Medium / Hard / Mixed"),
        ("▸",  "Answer each MCQ by typing  A, B, C, or D"),
        ("▸",  "You have 15 seconds per question"),
        ("▸",  "Score 1 point for every correct answer"),
        ("▸",  "No penalty for wrong answers — just learn!"),
    ]
    hline()
    for icon, text in instructions:
        if icon == "📋":
            print(c(f"  {icon}  {text}", Color.YELLOW, Color.BOLD))
        else:
            print(c(f"  {icon}  {text}", Color.WHITE))
    hline()
    print()


# ─────────────────────────────────────────────
#  SCREEN: GET PLAYER NAME
# ─────────────────────────────────────────────
def get_player_name() -> str:
    """Prompt for and validate the player's name."""
    while True:
        name = input(c("  Enter your name: ", Color.CYAN, Color.BOLD)).strip()
        if not name:
            print(c("  ⚠  Name cannot be empty. Try again.", Color.RED))
        elif len(name) > 20:
            print(c("  ⚠  Name too long (max 20 chars). Try again.", Color.RED))
        else:
            return name


# ─────────────────────────────────────────────
#  SCREEN: CHOOSE DIFFICULTY
# ─────────────────────────────────────────────
def choose_difficulty() -> str:
    """Let the player choose a difficulty level. Returns the chosen label."""
    options = {
        "1": ("Easy",   Color.GREEN,   5),
        "2": ("Medium", Color.YELLOW,  5),
        "3": ("Hard",   Color.RED,     5),
        "4": ("Mixed",  Color.MAGENTA, 10),
    }
    print()
    print(c("  Select Difficulty:", Color.BOLD, Color.WHITE))
    print()
    print(c("    [1]  🟢  Easy    (5 questions)", Color.GREEN))
    print(c("    [2]  🟡  Medium  (5 questions)", Color.YELLOW))
    print(c("    [3]  🔴  Hard    (5 questions)", Color.RED))
    print(c("    [4]  🌈  Mixed   (10 questions, all levels)", Color.MAGENTA))
    print()

    while True:
        choice = input(c("  Your choice (1/2/3/4): ", Color.CYAN)).strip()
        if choice in options:
            label, color, _ = options[choice]
            print()
            loading_dots(f"  Setting up {c(label, color)} mode")
            return label
        print(c("  ⚠  Please enter 1, 2, 3, or 4.", Color.RED))


# ─────────────────────────────────────────────
#  QUESTION SELECTOR
# ─────────────────────────────────────────────
def select_questions(difficulty: str) -> list:
    """
    Filter the question bank by difficulty and return a randomised subset.
    Mixed mode draws from all levels.
    """
    if difficulty == "Mixed":
        pool = ALL_QUESTIONS.copy()
        count = 10
    else:
        pool  = [q for q in ALL_QUESTIONS if q["diff"] == difficulty]
        count = min(5, len(pool))

    random.shuffle(pool)
    return pool[:count]


# ─────────────────────────────────────────────
#  DISPLAY: SINGLE QUESTION
# ─────────────────────────────────────────────
def display_question(q_data: dict, q_num: int, total: int, score: int):
    """
    Print the question box with options.
    Returns nothing; caller handles input separately.
    """
    diff_colors = {"Easy": Color.GREEN, "Medium": Color.YELLOW, "Hard": Color.RED}
    diff_color  = diff_colors.get(q_data["diff"], Color.WHITE)

    print()
    hline("═")
    # Header row: Q number | difficulty | score
    print(
        c(f"  Q{q_num}/{total}", Color.BOLD, Color.WHITE) +
        "   " +
        c(f"[{q_data['diff']}]", diff_color, Color.BOLD) +
        "   " +
        c(f"Score: {score}/{q_num - 1}", Color.CYAN)
    )
    hline("─")
    print()
    # Question text
    slow_print(c(f"  {q_data['q']}", Color.WHITE, Color.BOLD), delay=0.02)
    print()

    # Options
    option_colors = [Color.CYAN, Color.MAGENTA, Color.YELLOW, Color.GREEN]
    labels = ["A", "B", "C", "D"]
    for i, (label, option) in enumerate(zip(labels, q_data["options"])):
        print(
            "    " +
            c(f"[{label}]", option_colors[i], Color.BOLD) +
            f"  {option}"
        )
    print()


# ─────────────────────────────────────────────
#  INPUT: GET PLAYER ANSWER WITH TIMER
# ─────────────────────────────────────────────
def get_answer_with_timer(time_limit: int = 15):
    """
    Run a visible countdown while waiting for the player's answer.
    Uses a background thread so the countdown ticks while input() blocks.

    Returns the player's answer (upper-cased) or "TIMEOUT" if no answer.
    """
    answer_holder = [None]   # mutable container to pass into thread
    timer_done    = [False]

    def _timer():
        """Background thread: tick down and mark timeout."""
        for remaining in range(time_limit, -1, -1):
            if answer_holder[0] is not None:
                break   # player already answered
            bar_width = 25
            filled    = int(bar_width * remaining / time_limit)
            empty     = bar_width - filled
            bar       = "█" * filled + "░" * empty
            color     = (Color.GREEN  if remaining > time_limit // 2 else
                         Color.YELLOW if remaining > 3 else
                         Color.RED)
            line = (
                f"\r  ⏱  {c('[' + bar + ']', color)} "
                f"{c(str(remaining).rjust(2) + 's', color)}   "
            )
            sys.stdout.write(line)
            sys.stdout.flush()
            if remaining > 0:
                time.sleep(1)

        if answer_holder[0] is None:
            timer_done[0] = True
            # Push a newline so the prompt moves down after timeout
            sys.stdout.write("\n")
            sys.stdout.flush()

    t = threading.Thread(target=_timer, daemon=True)
    t.start()

    while True:
        try:
            raw = input(c("  Your answer (A/B/C/D): ", Color.CYAN, Color.BOLD))
        except EOFError:
            raw = ""

        if timer_done[0]:
            # Countdown finished before we got input
            answer_holder[0] = "TIMEOUT"
            return "TIMEOUT"

        ans = raw.strip().upper()
        if ans in ("A", "B", "C", "D"):
            answer_holder[0] = ans
            t.join(timeout=0.1)
            return ans
        else:
            print(c("  ⚠  Invalid input! Please enter A, B, C, or D.", Color.RED))


# ─────────────────────────────────────────────
#  DISPLAY: ANSWER RESULT FEEDBACK
# ─────────────────────────────────────────────
def show_result(correct: bool, correct_answer: str, options: list):
    """Show coloured correct/wrong feedback."""
    labels = ["A", "B", "C", "D"]
    correct_idx  = labels.index(correct_answer)
    correct_text = options[correct_idx]

    if correct:
        print()
        print(c("  ✅  CORRECT!  Well done!", Color.GREEN, Color.BOLD))
    else:
        print()
        print(c("  ❌  WRONG!", Color.RED, Color.BOLD))
        print(
            c("  ✔  Correct answer: ", Color.YELLOW) +
            c(f"[{correct_answer}]  {correct_text}", Color.GREEN, Color.BOLD)
        )
    time.sleep(1.5)


# ─────────────────────────────────────────────
#  DISPLAY: TIMEOUT FEEDBACK
# ─────────────────────────────────────────────
def show_timeout(correct_answer: str, options: list):
    """Feedback when the timer runs out."""
    labels       = ["A", "B", "C", "D"]
    correct_idx  = labels.index(correct_answer)
    correct_text = options[correct_idx]

    print()
    print(c("  ⏰  TIME'S UP!", Color.RED, Color.BOLD))
    print(
        c("  ✔  Correct answer was: ", Color.YELLOW) +
        c(f"[{correct_answer}]  {correct_text}", Color.GREEN, Color.BOLD)
    )
    time.sleep(1.8)


# ─────────────────────────────────────────────
#  MAIN GAME LOOP
# ─────────────────────────────────────────────
def run_quiz(player_name: str, difficulty: str) -> tuple:
    """
    Core game loop.
    Returns (score, total_questions) when finished.
    """
    questions = select_questions(difficulty)
    total     = len(questions)
    score     = 0

    for i, q_data in enumerate(questions, start=1):
        clear_screen()
        display_question(q_data, i, total, score)

        answer = get_answer_with_timer(time_limit=15)

        if answer == "TIMEOUT":
            show_timeout(q_data["answer"], q_data["options"])
        elif answer == q_data["answer"]:
            score += 1
            show_result(True, q_data["answer"], q_data["options"])
        else:
            show_result(False, q_data["answer"], q_data["options"])

    return score, total


# ─────────────────────────────────────────────
#  DISPLAY: FINAL SCORE SCREEN
# ─────────────────────────────────────────────
def show_final_score(player_name: str, score: int, total: int, difficulty: str):
    """
    Full end-of-game results screen with:
      - score, percentage, performance badge
      - visual score bar
      - session high scores table
    """
    clear_screen()
    percentage = (score / total) * 100 if total else 0

    # Performance tier
    if percentage == 100:
        badge, badge_color = "🏆  PERFECT SCORE!", Color.CYAN
    elif percentage >= 80:
        badge, badge_color = "🌟  EXCELLENT!",    Color.GREEN
    elif percentage >= 60:
        badge, badge_color = "👍  GOOD JOB!",     Color.YELLOW
    elif percentage >= 40:
        badge, badge_color = "📚  KEEP LEARNING", Color.MAGENTA
    else:
        badge, badge_color = "💪  TRY AGAIN!",    Color.RED

    # ── Results box ───────────────────────────
    print()
    hline("═")
    print(c(center("  G A M E   O V E R  ", 60), Color.BOLD, Color.CYAN))
    hline("═")
    print()
    print(c(f"  Player     : {player_name}", Color.WHITE))
    print(c(f"  Difficulty : {difficulty}",  Color.WHITE))
    print(c(f"  Score      : {score} / {total}", Color.WHITE, Color.BOLD))
    print(c(f"  Percentage : {percentage:.1f}%", Color.WHITE, Color.BOLD))
    print()
    print(c(f"  {badge}", badge_color, Color.BOLD))
    print()

    # Visual score bar
    bar_width = 40
    filled    = int(bar_width * score / total) if total else 0
    empty     = bar_width - filled
    bar       = "█" * filled + "░" * empty
    print(c(f"  [{bar}]  {score}/{total}", badge_color))
    print()

    # ── Session high scores ────────────────────
    HIGH_SCORES.append((player_name, score, total, difficulty))
    # Sort descending by score, then percentage
    sorted_scores = sorted(
        HIGH_SCORES,
        key=lambda x: (x[1] / x[2] if x[2] else 0, x[1]),
        reverse=True
    )

    hline("─")
    print(c("  🏅  SESSION HIGH SCORES", Color.YELLOW, Color.BOLD))
    hline("─")
    print(c(f"  {'#':<4} {'Name':<16} {'Score':<10} {'%':<8} {'Diff'}", Color.DIM))
    for rank, (name, sc, tot, diff) in enumerate(sorted_scores[:5], 1):
        pct   = (sc / tot * 100) if tot else 0
        medal = ["🥇", "🥈", "🥉", "  ", "  "][rank - 1]
        row   = f"  {medal} {name:<16} {sc}/{tot:<7}  {pct:>5.1f}%  {diff}"
        color = Color.YELLOW if rank == 1 else Color.WHITE
        print(c(row, color))
    hline("═")
    print()


# ─────────────────────────────────────────────
#  REPLAY PROMPT
# ─────────────────────────────────────────────
def ask_replay() -> bool:
    """Ask the player if they want to play again. Returns True/False."""
    while True:
        choice = input(
            c("  Play again? (", Color.WHITE) +
            c("Y", Color.GREEN, Color.BOLD) +
            c(" / ", Color.WHITE) +
            c("N", Color.RED, Color.BOLD) +
            c("): ", Color.WHITE)
        ).strip().upper()

        if choice in ("Y", "YES"):
            return True
        elif choice in ("N", "NO"):
            return False
        else:
            print(c("  ⚠  Please enter Y or N.", Color.RED))


# ─────────────────────────────────────────────
#  EXIT SCREEN
# ─────────────────────────────────────────────
def show_exit():
    """Friendly goodbye message."""
    print()
    hline("─")
    slow_print(c("  Thanks for playing QuizMaster! See you next time! 👋", Color.CYAN), delay=0.025)
    hline("─")
    print()
    time.sleep(0.5)


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────
def main():
    """Main program controller: handles game loop and replay logic."""
    show_welcome()
    player_name = get_player_name()

    print()
    loading_dots(f"  Welcome, {c(player_name, Color.GREEN, Color.BOLD)}! Preparing your quiz")
    time.sleep(0.4)

    while True:
        clear_screen()
        difficulty = choose_difficulty()
        score, total = run_quiz(player_name, difficulty)
        show_final_score(player_name, score, total, difficulty)

        if not ask_replay():
            break

        print()
        loading_dots("  Resetting game")
        time.sleep(0.3)

    show_exit()


# ─────────────────────────────────────────────
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(c("\n  Game interrupted. Goodbye! 👋", Color.YELLOW))
        sys.exit(0)