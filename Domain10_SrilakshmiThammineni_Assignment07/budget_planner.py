import json

class BudgetAdvisor:
    def __init__(self, filename="budget_data.json"):
        self.filename = filename
        self.data = {"income": [], "expenses": []}
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {"income": [], "expenses": []}

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def add_income(self, amount, source):
        try:
            amount = float(amount)
            self.data["income"].append({"amount": amount, "source": source})
            self.save_data()
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def add_expense(self, amount, category):
        try:
            amount = float(amount)
            self.data["expenses"].append({"amount": amount, "category": category})
            self.save_data()
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def total_income(self):
        return sum(item["amount"] for item in self.data["income"])

    def total_expenses(self):
        return sum(item["amount"] for item in self.data["expenses"])

    def show_summary(self):
        total_income = self.total_income()
        total_expenses = self.total_expenses()
        balance = total_income - total_expenses

        print(f"\nTotal Income: ₹{total_income:.2f}")
        print(f"Total Expenses: ₹{total_expenses:.2f}")
        print(f"Balance: ₹{balance:.2f}\n")

        categories = {}
        for e in self.data["expenses"]:
            categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]

        if categories:
            print("Expense Breakdown:")
            for cat, amt in categories.items():
                print(f"{cat}: ₹{amt:.2f} ({(amt / total_expenses * 100):.1f}%)")
        else:
            print("No expenses recorded yet.")

        self.suggest_savings(total_income, total_expenses, categories)

    def suggest_savings(self, income, expenses, categories):
        print("\nSuggestions:")
        if income == 0:
            print("Add your income details to get savings suggestions.")
            return
        savings_rate = (income - expenses) / income * 100
        if savings_rate < 10:
            print("You're saving less than 10% of your income. Try to reduce non-essential expenses.")
        elif savings_rate < 30:
            print("You're saving a fair amount, but aim for at least 30% if possible.")
        else:
            print("Great! You're maintaining a healthy savings rate.")
        if "entertainment" in categories and categories["entertainment"] > 0.2 * expenses:
            print("Consider reducing entertainment expenses.")
        if "food" in categories and categories["food"] > 0.3 * expenses:
            print("Try meal planning to lower food costs.")
        if "shopping" in categories and categories["shopping"] > 0.25 * expenses:
            print("Review shopping expenses and focus on essentials only.")

def main():
    app = BudgetAdvisor()
    while True:
        print("\n=== Personal Budget Advisor ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary & Suggestions")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = input("Enter income amount: ")
            source = input("Enter source of income: ")
            app.add_income(amount, source)
        elif choice == "2":
            amount = input("Enter expense amount: ")
            category = input("Enter expense category: ")
            app.add_expense(amount, category)
        elif choice == "3":
            app.show_summary()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
