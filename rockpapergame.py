import random
import time


class RockPaperScissors:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.choices = ["rock", "paper", "scissors"]
        self.choice_emojis = {
            "rock": "🪨",
            "paper": "📄",
            "scissors": "✂️"
        }
        self.game_history = []

    def display_header(self):
        """Display the game header and title."""
        print("\n" + "=" * 60)
        print("🎮           ROCK-PAPER-SCISSORS GAME           🎮")
        print("=" * 60)
        print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock")
        print("=" * 60)

    def display_menu(self):
        """Display the game menu options."""
        print("\n📋 GAME MENU:")
        print("1. 🪨  Rock")
        print("2. 📄  Paper")
        print("3. ✂️   Scissors")
        print("4. 📊  View Statistics")
        print("5. 📜  View Game History")
        print("6. 🔄  Reset Scores")
        print("7. ❌  Quit Game")

    def get_user_choice(self):
        """Get and validate user's choice."""
        while True:
            try:
                choice = input("\nEnter your choice (1-7): ").strip()

                if choice in ['1', '2', '3']:
                    return self.choices[int(choice) - 1]
                elif choice == '4':
                    self.display_statistics()
                    continue
                elif choice == '5':
                    self.display_history()
                    continue
                elif choice == '6':
                    self.reset_scores()
                    continue
                elif choice == '7':
                    return 'quit'
                else:
                    print("❌ Invalid choice! Please enter a number between 1-7.")

            except (ValueError, IndexError):
                print("❌ Invalid input! Please enter a number between 1-7.")

    def get_computer_choice(self):
        """Generate random choice for computer."""
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner based on game rules."""
        if user_choice == computer_choice:
            return "tie"

        winning_combinations = {
            ("rock", "scissors"): "user",
            ("scissors", "paper"): "user",
            ("paper", "rock"): "user"
        }

        if (user_choice, computer_choice) in winning_combinations:
            return "user"
        else:
            return "computer"

    def display_choices(self, user_choice, computer_choice):
        """Display both player choices with animations."""
        print("\n" + "=" * 40)
        print("         BATTLE ARENA")
        print("=" * 40)

        # Countdown animation
        for i in range(3, 0, -1):
            print(f"           {i}...")
            time.sleep(0.8)

        print("         SHOOT! 🎯")
        time.sleep(0.5)

        print(f"\n👤 You chose:     {self.choice_emojis[user_choice]} {user_choice.upper()}")
        print(f"🤖 Computer chose: {self.choice_emojis[computer_choice]} {computer_choice.upper()}")

    def display_result(self, result, user_choice, computer_choice):
        """Display the round result with visual effects."""
        print("\n" + "-" * 40)

        if result == "tie":
            print("🤝 IT'S A TIE!")
            print("   Great minds think alike!")
        elif result == "user":
            print("🎉 YOU WIN THIS ROUND!")
            print(f"   {user_choice.title()} beats {computer_choice.title()}!")
            self.user_score += 1
        else:
            print("😔 COMPUTER WINS THIS ROUND!")
            print(f"   {computer_choice.title()} beats {user_choice.title()}!")
            self.computer_score += 1

        self.rounds_played += 1

        # Record game history
        self.game_history.append({
            'round': self.rounds_played,
            'user_choice': user_choice,
            'computer_choice': computer_choice,
            'result': result
        })

        print("-" * 40)

    def display_current_score(self):
        """Display current score in a formatted way."""
        print("\n📊 CURRENT SCORE:")
        print(f"┌{'─' * 25}┐")
        print(f"│ 👤 You:      {self.user_score:2d} wins   │")
        print(f"│ 🤖 Computer: {self.computer_score:2d} wins   │")
        print(f"│ 🎮 Rounds:   {self.rounds_played:2d} played │")
        print(f"└{'─' * 25}┘")

    def display_statistics(self):
        """Display detailed game statistics."""
        if self.rounds_played == 0:
            print("\n📊 No games played yet!")
            return

        ties = self.rounds_played - self.user_score - self.computer_score
        user_win_rate = (self.user_score / self.rounds_played) * 100

        print("\n" + "=" * 50)
        print("📊                GAME STATISTICS")
        print("=" * 50)
        print(f"Total Rounds Played:     {self.rounds_played}")
        print(f"Your Wins:              {self.user_score}")
        print(f"Computer Wins:          {self.computer_score}")
        print(f"Ties:                   {ties}")
        print(f"Your Win Rate:          {user_win_rate:.1f}%")

        # Determine overall leader
        if self.user_score > self.computer_score:
            print(f"🏆 Overall Leader:       YOU (+{self.user_score - self.computer_score})")
        elif self.computer_score > self.user_score:
            print(f"🏆 Overall Leader:       COMPUTER (+{self.computer_score - self.user_score})")
        else:
            print("🤝 Overall Status:       TIED GAME")

        print("=" * 50)

    def display_history(self):
        """Display game history."""
        if not self.game_history:
            print("\n📜 No game history available!")
            return

        print("\n" + "=" * 60)
        print("📜                  GAME HISTORY")
        print("=" * 60)
        print("Round │  Your Choice  │ Computer Choice │   Result")
        print("─" * 60)

        for game in self.game_history[-10:]:  # Show last 10 games
            result_symbol = "🎉" if game['result'] == 'user' else "😔" if game['result'] == 'computer' else "🤝"
            result_text = "YOU WIN" if game['result'] == 'user' else "COMPUTER" if game[
                                                                                       'result'] == 'computer' else "TIE"

            print(
                f"  {game['round']:2d}  │    {game['user_choice']:8s}   │     {game['computer_choice']:8s}    │ {result_symbol} {result_text}")

        if len(self.game_history) > 10:
            print(f"\n(Showing last 10 of {len(self.game_history)} games)")
        print("=" * 60)

    def reset_scores(self):
        """Reset all scores and history."""
        confirm = input("\n⚠️  Are you sure you want to reset all scores and history? (y/n): ").lower()
        if confirm == 'y':
            self.user_score = 0
            self.computer_score = 0
            self.rounds_played = 0
            self.game_history = []
            print("✅ Scores and history have been reset!")
        else:
            print("❌ Reset cancelled.")

    def play_again(self):
        """Ask if user wants to play another round."""
        while True:
            choice = input("\n🎮 Play another round? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("❌ Please enter 'y' for yes or 'n' for no.")

    def display_final_summary(self):
        """Display final game summary when quitting."""
        if self.rounds_played == 0:
            print("\n👋 Thanks for checking out the game! Come back anytime!")
            return

        print("\n" + "=" * 50)
        print("🏁              FINAL GAME SUMMARY")
        print("=" * 50)

        self.display_statistics()

        if self.user_score > self.computer_score:
            print("\n🎉 CONGRATULATIONS! You dominated the computer!")
        elif self.computer_score > self.user_score:
            print("\n🤖 The computer proved superior this time!")
        else:
            print("\n🤝 What an evenly matched battle!")

        print("\n👋 Thanks for playing Rock-Paper-Scissors!")
        print("   Come back anytime for another challenge!")

    def run_game(self):
        """Main game loop."""
        self.display_header()

        print("\n🎯 Welcome to the ultimate Rock-Paper-Scissors challenge!")
        print("   Try to beat the computer and become the champion!")

        while True:
            self.display_menu()
            self.display_current_score()

            user_choice = self.get_user_choice()

            if user_choice == 'quit':
                break

            # Generate computer choice and play round
            computer_choice = self.get_computer_choice()

            # Display choices with animation
            self.display_choices(user_choice, computer_choice)

            # Determine and display result
            result = self.determine_winner(user_choice, computer_choice)
            self.display_result(result, user_choice, computer_choice)

            # Ask if player wants to continue
            if not self.play_again():
                break

        # Display final summary
        self.display_final_summary()


def main():
    """Initialize and start the game."""
    try:
        game = RockPaperScissors()
        game.run_game()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please restart the game.")


if __name__ == "__main__":
    main()
