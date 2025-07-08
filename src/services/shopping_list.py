from typing import List, Dict
from ..models.meal_models import DayMealPlan

class ShoppingListGenerator:
    """Service for generating shopping lists from meal plans."""
    
    def generate_shopping_list(self, meal_plans: List[DayMealPlan]) -> Dict[str, Dict[str, Dict[str, float]]]:
        """
        Generate a consolidated shopping list from meal plans.
        
        Args:
            meal_plans: List of DayMealPlan objects
            
        Returns:
            Dictionary with categories as keys and ingredient dictionaries as values.
            Each ingredient contains 'amount' and 'cost' keys.
        """
        # Consolidate all ingredients
        ingredient_totals = {}
        
        for day_plan in meal_plans:
            # Process all meals in the day
            all_meals = []
            if day_plan.breakfast:
                all_meals.append(day_plan.breakfast)
            if day_plan.lunch:
                all_meals.append(day_plan.lunch)
            if day_plan.dinner:
                all_meals.append(day_plan.dinner)
            all_meals.extend(day_plan.snacks)
            
            for meal in all_meals:
                for recipe in meal.recipes:
                    for ingredient in recipe.ingredients:
                        key = f"{ingredient.name} ({ingredient.unit})"
                        if key in ingredient_totals:
                            ingredient_totals[key]['amount'] += ingredient.amount
                            ingredient_totals[key]['cost'] += ingredient.get_total_cost()
                        else:
                            ingredient_totals[key] = {
                                'amount': ingredient.amount,
                                'cost': ingredient.get_total_cost(),
                                'unit_cost': ingredient.cost_per_unit or 0.0
                            }
        
        # Categorize ingredients
        categories = {
            "Produce": ["apple", "berries", "onion", "garlic", "tomato", "sweet potato"],
            "Dairy": ["milk", "cheese", "butter", "egg"],
            "Meat & Seafood": ["chicken", "beef", "fish", "tenders"],
            "Pantry": ["flour", "rice", "pasta", "oil", "sauce", "syrup", "breadcrumbs", "spaghetti"],
            "Frozen": ["nugget"],
            "Bakery": ["bread", "crackers"],
            "Condiments": ["peanut butter", "ketchup"]
        }
        
        categorized_list = {cat: {} for cat in categories.keys()}
        categorized_list["Other"] = {}
        
        for ingredient_key, data in ingredient_totals.items():
            ingredient_name = ingredient_key.split(" (")[0].lower()
            categorized = False
            
            for category, keywords in categories.items():
                if any(keyword in ingredient_name for keyword in keywords):
                    categorized_list[category][ingredient_key] = data
                    categorized = True
                    break
            
            if not categorized:
                categorized_list["Other"][ingredient_key] = data
        
        # Remove empty categories
        return {k: v for k, v in categorized_list.items() if v}
    
    def format_shopping_list_text(self, shopping_list: Dict[str, Dict[str, Dict[str, float]]]) -> str:
        """Format the shopping list as readable text with costs."""
        text = "SHOPPING LIST WITH BUDGET BREAKDOWN\n" + "="*60 + "\n\n"
        
        total_cost = 0.0
        
        for category, items in shopping_list.items():
            if items:
                category_cost = sum(item['cost'] for item in items.values())
                text += f"{category.upper()} (${category_cost:.2f})\n" + "-"*(len(category) + 10) + "\n"
                
                for ingredient, data in items.items():
                    amount = data['amount']
                    cost = data['cost']
                    
                    # Round amounts for better readability
                    if amount.is_integer():
                        text += f"• {ingredient}: {int(amount)} - ${cost:.2f}\n"
                    else:
                        text += f"• {ingredient}: {amount:.1f} - ${cost:.2f}\n"
                
                total_cost += category_cost
                text += "\n"
        
        text += "="*60 + "\n"
        text += f"TOTAL ESTIMATED COST: ${total_cost:.2f}\n"
        
        return text
    
    def get_total_cost(self, shopping_list: Dict[str, Dict[str, Dict[str, float]]]) -> float:
        """Calculate total cost of the shopping list."""
        total_cost = 0.0
        for category, items in shopping_list.items():
            for ingredient, data in items.items():
                total_cost += data['cost']
        return total_cost
