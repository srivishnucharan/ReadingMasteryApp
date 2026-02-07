import time


class ProficiencyEvaluator:
    def __init__(self):
        # A standard text for evaluation (approx 100 words)
        self.passage = (
            "The art of reading is not merely the act of deciphering symbols on a page, "
            "but rather an intricate dance between the author's intent and the reader's "
            "interpretation. To become a proficient reader, one must move beyond literal "
            "understanding. This involves grasping nuanced metaphors and idiomatic "
            "expressions that color our language. Speed is a factor, yet comprehension "
            "remains the ultimate goal. As you progress, you will find that your "
            "vocabulary expands, allowing you to traverse more complex literary landscapes "
            "with ease and confidence."
        )
        self.word_count = len(self.passage.split())

    def start_test(self):
        print("--- READING PROFICIENCY EVALUATION ---")
        print("Instructions: Read the following passage carefully. Press ENTER when finished.")
        input("\nPress ENTER to display the text and start the timer...")

        start_time = time.time()
        print(f"\n{self.passage}\n")

        input("DONE? Press ENTER immediately.")
        end_time = time.time()

        total_time = end_time - start_time
        wpm = int((self.word_count / total_time) * 60)

        return self.categorize_user(wpm)

    def categorize_user(self, wpm):
        print(f"\nYour Reading Speed: {wpm} WPM")

        if wpm < 150:
            category = "Novice"
            advice = "Focus on high-frequency words and sentence structure."
        elif 150 <= wpm <= 250:
            category = "Intermediate"
            advice = "Focus on expanding idiomatic vocabulary and speed."
        else:
            category = "Advanced"
            advice = "Focus on critical analysis and complex literary styles."

        return {"level": category, "speed": wpm, "advice": advice}


# Testing the logic
if __name__ == "__main__":
    evaluator = ProficiencyEvaluator()
    results = evaluator.start_test()
    print(f"Result: You have been placed in the {results['level']} category!")