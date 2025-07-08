# AI Family Meal Planner 🍽️

A comprehensive meal planning application that creates nutritionally balanced, kid-friendly meal plans while staying within your budget.

## Features

### 🎯 Core Functionality
- **Nutritionally Balanced Meals**: Ensures proper calorie and nutrient distribution
- **Kid-Friendly Focus**: Prioritizes recipes that children will enjoy
- **Budget Management**: Creates meal plans within your specified daily budget
- **Smart Shopping Lists**: Generates categorized shopping lists with cost breakdowns
- **Dietary Restrictions**: Supports vegetarian, gluten-free, and other dietary needs

### 💰 Budget Features
- **Daily Budget Setting**: Set a daily food budget (e.g., $25/day)
- **Cost-Aware Planning**: Algorithm considers both nutrition and cost when selecting recipes
- **Budget Analysis**: Shows if you're under/over budget with savings breakdown
- **Shopping Cost Tracking**: Complete cost breakdown by category
- **Cost Per Serving**: See individual recipe costs

### 📊 Nutritional Tracking
- **Calorie Management**: Stay within daily calorie limits (default: 2000)
- **Macro & Micronutrient Balance**: Tracks protein, carbs, fat, fiber, sugar, sodium
- **Weekly Summaries**: Average daily nutrition and cost analysis
- **Family-Sized Portions**: Automatically scales for family size (2-6 people)

## Quick Start

1. **Set Your Preferences**:
   - Planning period (3-14 days)
   - Family size (2-6 people)
   - Daily calorie limit
   - **Daily budget** (optional but recommended)
   - Dietary restrictions

2. **Generate Your Plan**:
   - Click "Generate Meal Plan"
   - Review nutrition and budget analysis
   - Browse daily meal schedules

3. **Shop Smart**:
   - Use the generated shopping list
   - See costs by category
   - Stay within your total budget

## Sample Budget Breakdown

For a family of 4 with a $25/day budget:
- **Breakfast**: $5.00 (20%)
- **Lunch**: $8.75 (35%) 
- **Dinner**: $10.00 (40%)
- **Snacks**: $1.25 (5%)

## Technology Stack

- **Backend**: Python Flask
- **Data Models**: SQLAlchemy-compatible models
- **Nutrition Analysis**: Pandas for data processing
- **Frontend**: Modern HTML5/CSS3/JavaScript
- **Cost Tracking**: Real-world grocery pricing data

## Installation

1. **Clone/Download** the project
2. **Activate** the virtual environment:
   ```bash
   meal_planner_env\Scripts\activate
   ```
3. **Install** dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run** the application:
   ```bash
   python app.py
   ```
5. **Open** http://localhost:5000 in your browser

## Recipe Cost Examples

Our sample recipes include realistic grocery costs:
- **Pancakes with Berries**: ~$3.20/serving
- **Grilled Cheese & Soup**: ~$2.95/serving  
- **Chicken Nuggets**: ~$2.62/serving
- **Spaghetti with Meat Sauce**: ~$2.31/serving
- **Apple & Peanut Butter**: ~$2.00/serving

## Future Enhancements

- [ ] Integration with grocery store APIs for real-time pricing
- [ ] Seasonal ingredient cost adjustments
- [ ] Bulk buying recommendations
- [ ] Leftover management and cost savings
- [ ] Custom recipe additions with cost input
- [ ] Export shopping lists to popular grocery apps

## Contributing

This project follows Python best practices:
- Type hints for all functions
- Comprehensive docstrings
- PEP 8 style guidelines
- Family-friendly focus
- Cost-conscious algorithms

---

**Start planning nutritious, budget-friendly meals for your family today!** 🥗💰
