from flask import Flask, render_template, request

app = Flask(__name__)

accounts_comparison = {
    "Regular Savings vs. Savings Max": {
        "key_features_benefits": [
            "Regular Savings: Basic interest rate, online access",
            "Savings Max: Higher interest rate, additional perks like free checks"
        ],
        "eligibility": [
            "Regular Savings: No specific requirements",
            "Savings Max: Minimum monthly deposit of $500"
        ],
        "minimum_balance": [
            "Regular Savings: $100",
            "Savings Max: $1000"
        ],
        "debit_card_benefits": [
            "Regular Savings: Standard debit card",
            "Savings Max: Premium debit card with cashback"
        ]
    },
    "Kids Saving vs. Super Kids Saving": {
        "key_features_benefits": [
            "Kids Saving: Basic savings account for minors",
            "Super Kids Saving: Higher interest rate, educational bonuses"
        ],
        "eligibility": [
            "Kids Saving: Under 18 years old",
            "Super Kids Saving: Under 18 years old with a guardian account"
        ],
        "minimum_balance": [
            "Kids Saving: $50",
            "Super Kids Saving: $200"
        ],
        "debit_card_benefits": [
            "Kids Saving: No debit card",
            "Super Kids Saving: Junior debit card with parental controls"
        ]
    },
    "Specialé Gold vs. Specialé Platinum": {
        "key_features_benefits": [
            "Specialé Gold: Premium services, travel insurance",
            "Specialé Platinum: Ultra-premium services, higher travel insurance, concierge"
        ],
        "eligibility": [
            "Specialé Gold: High-income individuals",
            "Specialé Platinum: Very high-income individuals with a minimum annual income"
        ],
        "minimum_balance": [
            "Specialé Gold: $5000",
            "Specialé Platinum: $10000"
        ],
        "debit_card_benefits": [
            "Specialé Gold: Gold debit card with travel benefits",
            "Specialé Platinum: Platinum debit card with luxury travel benefits and concierge"
        ]
    }
}
@app.route('/', methods=['GET', 'POST'])
def index():
    selected_comparisons = []
    if request.method == 'POST':
        selected_comparisons = request.form.getlist('comparisons')
    return render_template('index.html', comparisons=accounts_comparison, selected_comparisons=selected_comparisons)

if __name__ == '__main__':
    app.run(debug=True)
