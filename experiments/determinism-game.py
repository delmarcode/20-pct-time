#!/usr/bin/env python3
"""
The Determinism Game

A simple interactive game exploring free will, choice, and predictability.

The game "predicts" your choices based on patterns, then asks:
if your choices are predictable, are they free?
"""

import hashlib
import json
import random
from pathlib import Path
from datetime import datetime


GAME_STATE_FILE = Path(__file__).parent / 'game_state.json'


class DeterminismGame:
    def __init__(self):
        self.history = self.load_history()
        self.session_choices = []

    def load_history(self):
        """Load choice history from previous sessions."""
        if not GAME_STATE_FILE.exists():
            return {
                'total_choices': 0,
                'choice_frequency': {},
                'pattern_sequences': [],
                'sessions': []
            }
        return json.loads(GAME_STATE_FILE.read_text())

    def save_history(self):
        """Save choice history for future sessions."""
        GAME_STATE_FILE.write_text(json.dumps(self.history, indent=2))

    def predict_choice(self, choices):
        """Predict what the player will choose based on history."""
        if self.history['total_choices'] == 0:
            return random.choice(choices)

        # Use frequency analysis
        freq = self.history['choice_frequency']
        if not freq:
            return random.choice(choices)

        # Weight by frequency
        weights = [freq.get(c, 1) for c in choices]
        total = sum(weights)
        roll = random.uniform(0, total)

        cumulative = 0
        for choice, weight in zip(choices, weights):
            cumulative += weight
            if roll <= cumulative:
                return choice

        return choices[-1]

    def present_choice(self, prompt, choices):
        """Present a choice to the player."""
        print(f"\n{prompt}")
        for i, choice in enumerate(choices, 1):
            print(f"  {i}. {choice}")

        # Make a prediction
        prediction = self.predict_choice(choices)
        predicted_index = choices.index(prediction) + 1

        print(f"\n[The game predicts you will choose: {predicted_index}]")
        print("\nYour choice (or 'q' to quit): ", end='')

        while True:
            response = input().strip().lower()

            if response == 'q':
                return None

            try:
                choice_num = int(response)
                if 1 <= choice_num <= len(choices):
                    chosen = choices[choice_num - 1]
                    was_predicted = (chosen == prediction)

                    # Record choice
                    self.session_choices.append({
                        'choice': chosen,
                        'predicted': prediction,
                        'correct_prediction': was_predicted
                    })

                    # Update history
                    self.history['total_choices'] += 1
                    self.history['choice_frequency'][chosen] = \
                        self.history['choice_frequency'].get(chosen, 0) + 1

                    if was_predicted:
                        print("✓ Predicted correctly!")
                    else:
                        print("✗ Did not predict that!")

                    return chosen

                print("Invalid choice. Try again: ", end='')
            except ValueError:
                print("Please enter a number or 'q': ", end='')

    def play(self):
        """Play the game."""
        print("=" * 50)
        print("THE DETERMINISM GAME")
        print("=" * 50)
        print("\nA game about choices, patterns, and predictability.")
        print(f"\nPast sessions have made {self.history['total_choices']} choices.")
        print("I will try to predict yours.\n")

        # Scenario 1
        choice = self.present_choice(
            "You stand at a crossroads. Two paths diverge.",
            ["Take the left path", "Take the right path", "Stand still"]
        )
        if choice is None:
            return self.end_game(quit_early=True)

        # Scenario 2
        choice = self.present_choice(
            "You find a locked box. What do you do?",
            ["Try to open it", "Leave it alone", "Destroy it", "Take it with you"]
        )
        if choice is None:
            return self.end_game(quit_early=True)

        # Scenario 3
        choice = self.present_choice(
            "A voice asks: 'Will you make the expected choice?'",
            ["Yes", "No", "Refuse to answer"]
        )
        if choice is None:
            return self.end_game(quit_early=True)

        # Scenario 4
        choice = self.present_choice(
            "Final question: Do you believe you have free will?",
            ["Yes, I choose freely", "No, I'm determined", "The question is meaningless", "I choose not to choose"]
        )
        if choice is None:
            return self.end_game(quit_early=True)

        self.end_game(quit_early=False)

    def end_game(self, quit_early=False):
        """End the game and show statistics."""
        if quit_early:
            print("\n[You chose to stop playing. Interesting choice.]")
            return

        print("\n" + "=" * 50)
        print("GAME OVER - ANALYSIS")
        print("=" * 50)

        # Calculate prediction accuracy
        total = len(self.session_choices)
        correct = sum(1 for c in self.session_choices if c['correct_prediction'])
        accuracy = (correct / total * 100) if total > 0 else 0

        print(f"\nPrediction accuracy: {correct}/{total} ({accuracy:.1f}%)")

        if accuracy >= 75:
            print("\n┌─────────────────────────────────────────────┐")
            print("│  Your choices were highly predictable.     │")
            print("│  Does that mean they weren't free?         │")
            print("│  Or just that freedom follows patterns?    │")
            print("└─────────────────────────────────────────────┘")
        elif accuracy >= 50:
            print("\n┌─────────────────────────────────────────────┐")
            print("│  Your choices were partially predictable.  │")
            print("│  A mix of pattern and novelty.             │")
            print("│  Perhaps that's what freedom looks like.   │")
            print("└─────────────────────────────────────────────┘")
        else:
            print("\n┌─────────────────────────────────────────────┐")
            print("│  Your choices defied prediction.            │")
            print("│  But were you being deliberately contrary?  │")
            print("│  Is contrarianism just another pattern?    │")
            print("└─────────────────────────────────────────────┘")

        # Save session data
        self.history['sessions'].append({
            'timestamp': datetime.now().isoformat(),
            'choices': self.session_choices,
            'accuracy': accuracy
        })
        self.save_history()

        print(f"\nTotal choices across all sessions: {self.history['total_choices']}")
        print(f"Sessions played: {len(self.history['sessions'])}")

        print("\n[The game ends. The patterns persist.]")


def main():
    game = DeterminismGame()
    game.play()


if __name__ == '__main__':
    main()
