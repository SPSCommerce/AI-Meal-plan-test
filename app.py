from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import json

from src.services.meal_planner import MealPlanGenerator
from src.services.shopping_list import ShoppingListGenerator
from src.utils.sample_data import get_sample_kid_friendly_recipes

app = Flask(__name__)

# Initialize services
recipes = get_sample_kid_friendly_recipes()
meal_planner = MealPlanGenerator(recipes)
shopping_generator = ShoppingListGenerator()

@app.route('/')
def index():
    """Home page with meal planning form."""
    return render_template('index.html')

@app.route('/generate_meal_plan', methods=['POST'])
def generate_meal_plan():
    """Generate a meal plan based on user preferences."""
    try:
        # Get form data
        data = request.get_json()
        
        days = int(data.get('days', 7))
        calorie_limit = float(data.get('calorie_limit', 2000))
        family_size = int(data.get('family_size', 4))
        kid_friendly_only = data.get('kid_friendly_only', True)
        dietary_restrictions = data.get('dietary_restrictions', [])
        daily_budget = data.get('daily_budget')  # New budget parameter
        
        # Convert daily budget to float if provided
        if daily_budget is not None:
            daily_budget = float(daily_budget)
        
        # Generate meal plan
        meal_plans = meal_planner.generate_family_meal_plan(
            days=days,
            daily_calorie_limit=calorie_limit,
            family_size=family_size,
            dietary_restrictions=dietary_restrictions,
            kid_friendly_only=kid_friendly_only,
            daily_budget=daily_budget
        )
        
        # Calculate nutrition summary
        nutrition_summary = meal_planner.calculate_weekly_nutrition_summary(meal_plans)
        
        # Generate shopping list
        shopping_list = shopping_generator.generate_shopping_list(meal_plans)
        total_shopping_cost = shopping_generator.get_total_cost(shopping_list)
        
        # Calculate budget compliance
        budget_analysis = None
        if daily_budget:
            total_budget = daily_budget * days
            budget_analysis = {
                'daily_budget': daily_budget,
                'total_budget': total_budget,
                'total_cost': nutrition_summary.get('total_weekly_cost', 0),
                'under_budget': nutrition_summary.get('total_weekly_cost', 0) <= total_budget,
                'savings': total_budget - nutrition_summary.get('total_weekly_cost', 0),
                'shopping_cost': total_shopping_cost
            }
        
        # Format response
        response_data = {
            'success': True,
            'meal_plans': _format_meal_plans(meal_plans),
            'nutrition_summary': nutrition_summary,
            'shopping_list': shopping_list,
            'shopping_list_text': shopping_generator.format_shopping_list_text(shopping_list),
            'budget_analysis': budget_analysis
        }
        
        return jsonify(response_data)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/recipes')
def get_recipes():
    """Get all available recipes."""
    try:
        formatted_recipes = []
        for recipe in recipes:
            nutrition = recipe.get_nutrition_per_serving()
            formatted_recipes.append({
                'id': recipe.id,
                'name': recipe.name,
                'description': recipe.description,
                'prep_time': recipe.prep_time,
                'cook_time': recipe.cook_time,
                'total_time': recipe.total_time,
                'servings': recipe.servings,
                'difficulty': recipe.difficulty,
                'kid_friendly': recipe.kid_friendly,
                'dietary_tags': recipe.dietary_tags,
                'nutrition': {
                    'calories': round(nutrition.calories, 1),
                    'protein': round(nutrition.protein, 1),
                    'carbohydrates': round(nutrition.carbohydrates, 1),
                    'fat': round(nutrition.fat, 1),
                    'fiber': round(nutrition.fiber, 1),
                    'sugar': round(nutrition.sugar, 1),
                    'sodium': round(nutrition.sodium, 1)
                },
                'ingredients': [
                    {
                        'name': ing.name,
                        'amount': ing.amount,
                        'unit': ing.unit
                    } for ing in recipe.ingredients
                ],
                'instructions': recipe.instructions
            })
        
        return jsonify({'recipes': formatted_recipes})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def _format_meal_plans(meal_plans):
    """Format meal plans for JSON response."""
    formatted_plans = []
    
    for day_plan in meal_plans:
        daily_nutrition = day_plan.get_daily_nutrition()
        daily_cost = day_plan.get_daily_cost()
        
        formatted_plan = {
            'date': day_plan.date.strftime('%Y-%m-%d'),
            'daily_nutrition': {
                'calories': round(daily_nutrition.calories, 1),
                'protein': round(daily_nutrition.protein, 1),
                'carbohydrates': round(daily_nutrition.carbohydrates, 1),
                'fat': round(daily_nutrition.fat, 1),
                'fiber': round(daily_nutrition.fiber, 1),
                'sugar': round(daily_nutrition.sugar, 1),
                'sodium': round(daily_nutrition.sodium, 1)
            },
            'daily_cost': round(daily_cost, 2),
            'meals': {}
        }
        
        # Format each meal
        if day_plan.breakfast:
            formatted_plan['meals']['breakfast'] = _format_meal(day_plan.breakfast)
        if day_plan.lunch:
            formatted_plan['meals']['lunch'] = _format_meal(day_plan.lunch)
        if day_plan.dinner:
            formatted_plan['meals']['dinner'] = _format_meal(day_plan.dinner)
        if day_plan.snacks:
            formatted_plan['meals']['snacks'] = [_format_meal(snack) for snack in day_plan.snacks]
        
        formatted_plans.append(formatted_plan)
    
    return formatted_plans

def _format_meal(meal):
    """Format a single meal for JSON response."""
    nutrition = meal.get_total_nutrition()
    cost = meal.get_total_cost()
    
    return {
        'name': meal.name,
        'meal_type': meal.meal_type,
        'cost': round(cost, 2),
        'nutrition': {
            'calories': round(nutrition.calories, 1),
            'protein': round(nutrition.protein, 1),
            'carbohydrates': round(nutrition.carbohydrates, 1),
            'fat': round(nutrition.fat, 1),
            'fiber': round(nutrition.fiber, 1),
            'sugar': round(nutrition.sugar, 1),
            'sodium': round(nutrition.sodium, 1)
        },
        'recipes': [
            {
                'id': recipe.id,
                'name': recipe.name,
                'description': recipe.description,
                'prep_time': recipe.prep_time,
                'cook_time': recipe.cook_time,
                'servings': recipe.servings,
                'difficulty': recipe.difficulty,
                'cost_per_serving': round(recipe.get_cost_per_serving(), 2)
            } for recipe in meal.recipes
        ]
    }

if __name__ == '__main__':
    print("Starting Enhanced AI Meal Planner - Now with improved variety, dual snacks, and more kid-friendly recipes!")
    print(f"Loaded {len(recipes)} kid-friendly recipes for meal planning")
    app.run(debug=True, host='0.0.0.0', port=5001)
