from typing import List, Dict, Optional, Tuple
import random
from datetime import datetime, timedelta
from ..models.meal_models import Recipe, Meal, DayMealPlan, NutritionInfo, Ingredient

class MealPlanGenerator:
    """Service for generating balanced meal plans for families."""
    
    def __init__(self, recipes: List[Recipe]):
        """Initialize with a list of available recipes."""
        self.recipes = recipes
        self.kid_friendly_recipes = [r for r in recipes if r.kid_friendly]
        self.used_recipes = {}  # Track used recipes by meal type
        self.recently_used_ingredients = []  # Track recently used main ingredients
    
    def generate_family_meal_plan(
        self, 
        days: int = 7, 
        daily_calorie_limit: float = 2000,
        family_size: int = 4,
        dietary_restrictions: List[str] = None,
        kid_friendly_only: bool = True,
        daily_budget: Optional[float] = None
    ) -> List[DayMealPlan]:
        """
        Generate a meal plan for a family.
        
        Args:
            days: Number of days to plan for
            daily_calorie_limit: Maximum calories per day
            family_size: Number of family members
            dietary_restrictions: List of dietary restrictions
            kid_friendly_only: Whether to use only kid-friendly recipes
            daily_budget: Maximum daily food budget in dollars
        
        Returns:
            List of DayMealPlan objects
        """
        if dietary_restrictions is None:
            dietary_restrictions = []
        
        # Reset used recipes tracking for new meal plan
        self.used_recipes = {
            'breakfast': [],
            'lunch': [],
            'dinner': [],
            'snack': []
        }
        
        # Filter recipes based on criteria
        available_recipes = self._filter_recipes(dietary_restrictions, kid_friendly_only)
        
        if not available_recipes:
            raise ValueError("No recipes available with the given criteria")
        
        meal_plans = []
        start_date = datetime.now().date()
        
        for day in range(days):
            current_date = start_date + timedelta(days=day)
            daily_plan = self._generate_daily_plan(
                available_recipes, 
                daily_calorie_limit, 
                current_date,
                daily_budget,
                day  # Pass day number for variety tracking
            )
            meal_plans.append(daily_plan)
        
        return meal_plans
    
    def _filter_recipes(
        self, 
        dietary_restrictions: List[str], 
        kid_friendly_only: bool
    ) -> List[Recipe]:
        """Filter recipes based on dietary restrictions and kid-friendliness."""
        recipes = self.kid_friendly_recipes if kid_friendly_only else self.recipes
        
        if not dietary_restrictions:
            return recipes
        
        filtered_recipes = []
        for recipe in recipes:
            # Check if recipe meets all dietary restrictions
            meets_restrictions = all(
                restriction in recipe.dietary_tags 
                for restriction in dietary_restrictions
            )
            if meets_restrictions:
                filtered_recipes.append(recipe)
        
        return filtered_recipes
    
    def _generate_daily_plan(
        self, 
        available_recipes: List[Recipe], 
        calorie_limit: float,
        date: datetime,
        daily_budget: Optional[float] = None,
        day_number: int = 0
    ) -> DayMealPlan:
        """Generate a balanced meal plan for one day with better distribution for growing children."""
        # Enhanced calorie distribution with two snacks for growing children
        breakfast_calories = calorie_limit * 0.25  # 25% - Important start to the day
        lunch_calories = calorie_limit * 0.30      # 30% - Substantial midday meal
        dinner_calories = calorie_limit * 0.30     # 30% - Main family meal
        morning_snack_calories = calorie_limit * 0.075  # 7.5% - Mid-morning energy
        afternoon_snack_calories = calorie_limit * 0.075  # 7.5% - After-school energy
        
        # Target budget distribution (if budget is specified)
        budget_targets = None
        if daily_budget:
            budget_targets = {
                'breakfast': daily_budget * 0.20,   # 20%
                'lunch': daily_budget * 0.30,      # 30%
                'dinner': daily_budget * 0.35,     # 35%
                'morning_snack': daily_budget * 0.075, # 7.5%
                'afternoon_snack': daily_budget * 0.075  # 7.5%
            }
        
        # Generate meals with variety tracking
        breakfast = self._create_meal("breakfast", available_recipes, breakfast_calories, 
                                    budget_targets['breakfast'] if budget_targets else None, day_number)
        lunch = self._create_meal("lunch", available_recipes, lunch_calories,
                                budget_targets['lunch'] if budget_targets else None, day_number)
        dinner = self._create_meal("dinner", available_recipes, dinner_calories,
                                 budget_targets['dinner'] if budget_targets else None, day_number)
        
        # Two snacks for growing children
        morning_snack = self._create_meal("snack", available_recipes, morning_snack_calories,
                                budget_targets['morning_snack'] if budget_targets else None, day_number)
        
        # Use different selection criteria for afternoon snack to ensure variety
        afternoon_recipes = [r for r in available_recipes 
                            if morning_snack and morning_snack.recipes and 
                            r.id != morning_snack.recipes[0].id]
        if not afternoon_recipes:
            afternoon_recipes = available_recipes
            
        afternoon_snack = self._create_meal("snack", afternoon_recipes, afternoon_snack_calories,
                                budget_targets['afternoon_snack'] if budget_targets else None, day_number + 0.5)
        
        # Compile snacks
        snacks = []
        if morning_snack:
            snacks.append(morning_snack)
        if afternoon_snack:
            snacks.append(afternoon_snack)
        
        return DayMealPlan(
            date=date,
            breakfast=breakfast,
            lunch=lunch,
            dinner=dinner,
            snacks=snacks
        )
    
    def _create_meal(
        self, 
        meal_type: str, 
        available_recipes: List[Recipe], 
        target_calories: float,
        target_budget: Optional[float] = None,
        day_number: int = 0
    ) -> Optional[Meal]:
        """Create a meal that fits the calorie and budget targets with variety."""
        # Filter recipes suitable for this meal type
        suitable_recipes = self._get_suitable_recipes_for_meal_type(
            available_recipes, 
            meal_type
        )
        
        if not suitable_recipes:
            return None
        
        # Remove already used recipes for variety (except for longer meal plans)
        unused_recipes = [r for r in suitable_recipes if r.id not in self.used_recipes[meal_type]]
        
        # If we've used all recipes, allow reuse but prioritize least recently used
        if not unused_recipes and len(suitable_recipes) > 0:
            # For longer meal plans, allow recipe reuse after a few days
            if day_number >= len(suitable_recipes):
                unused_recipes = suitable_recipes
            else:
                # Use the first recipe that was used (least recent)
                unused_recipes = [suitable_recipes[0]]
        
        # Try to find the best recipe that fits both constraints and provides variety
        recipes_to_consider = unused_recipes if unused_recipes else suitable_recipes
        best_recipe = None
        best_score = float('inf')
        
        for recipe in recipes_to_consider:
            nutrition = recipe.get_nutrition_per_serving()
            cost = recipe.get_cost_per_serving()
            
            # Check calorie constraint
            if nutrition.calories > target_calories * 1.2:
                continue
            
            # Check budget constraint if specified
            if target_budget and cost > target_budget * 1.3:
                continue
            
            # Calculate a combined score (lower is better)
            calorie_diff = abs(nutrition.calories - target_calories) / target_calories
            
            if target_budget and target_budget > 0:
                budget_diff = abs(cost - target_budget) / target_budget
                # Weight both factors equally
                score = calorie_diff + budget_diff
            else:
                score = calorie_diff
            
            # Add variety bonus - prefer unused recipes
            if recipe.id not in self.used_recipes[meal_type]:
                score *= 0.8  # 20% bonus for unused recipes
                
            # Add ingredient variety penalty
            if meal_type in ["lunch", "dinner"] and self._has_similar_ingredients(recipe):
                score *= 1.25  # 25% penalty for similar main ingredients
            
            if score < best_score:
                best_recipe = recipe
                best_score = score
        
        if best_recipe:
            # Track this recipe as used
            self.used_recipes[meal_type].append(best_recipe.id)
            # Track the ingredients used in this recipe
            self._track_ingredients(best_recipe)
            
            return Meal(
                name=f"{meal_type.title()} - {best_recipe.name}",
                recipes=[best_recipe],
                meal_type=meal_type
            )
        
        return None
    
    def _get_suitable_recipes_for_meal_type(
        self, 
        recipes: List[Recipe], 
        meal_type: str
    ) -> List[Recipe]:
        """Get recipes suitable for a specific meal type."""
        # Enhanced classification based on recipe names, characteristics, and ID prefixes
        breakfast_keywords = ["pancake", "cereal", "oatmeal", "toast", "egg", "breakfast", "smoothie", 
                             "french toast", "muffin", "waffle", "bagel", "granola", "yogurt"]
        lunch_keywords = ["sandwich", "salad", "soup", "wrap", "lunch", "pasta", "bowl", "quesadilla", 
                         "burger", "taco", "pizza", "grilled cheese", "nugget"]
        dinner_keywords = ["chicken", "beef", "fish", "dinner", "roast", "stir", "casserole", "pasta",
                         "rice", "stew", "curry", "meatball", "taco", "enchilada", "lasagna"]
        snack_keywords = ["snack", "fruit", "yogurt", "crackers", "nuts", "muffin", "cookie", 
                         "popcorn", "chips", "dip", "smoothie", "bar"]
        
        keyword_map = {
            "breakfast": breakfast_keywords,
            "lunch": lunch_keywords,
            "dinner": dinner_keywords,
            "snack": snack_keywords
        }
        
        suitable = []
        keywords = keyword_map.get(meal_type, [])
        
        for recipe in recipes:
            recipe_name_lower = recipe.name.lower()
            recipe_desc_lower = recipe.description.lower()
            
            # First check recipe ID for explicit meal type tagging
            if recipe.id.startswith(meal_type):
                suitable.append(recipe)
                continue
            
            # Then check if any keyword matches in name or description
            if any(keyword in recipe_name_lower or keyword in recipe_desc_lower 
                   for keyword in keywords):
                suitable.append(recipe)
                continue
            
            # Nutritional and cooking time characteristics for meal types
            nutrition = recipe.get_nutrition_per_serving()
            
            # For breakfast: lower calorie, quick prep options
            if meal_type == "breakfast" and recipe.prep_time <= 15 and nutrition.calories <= 500:
                if nutrition.carbohydrates > 20:  # Most breakfasts have good carb content
                    suitable.append(recipe)
                    continue
                    
            # For lunch: moderate calories, moderate prep
            elif meal_type == "lunch" and 250 <= nutrition.calories <= 600:
                suitable.append(recipe)
                continue
                
            # For dinner: higher calories, protein, longer cook time
            elif meal_type == "dinner" and recipe.cook_time > 15:
                if nutrition.calories > 300 and nutrition.protein > 15:
                    suitable.append(recipe)
                    continue
                    
            # For snacks: lower calories, quick prep
            elif meal_type == "snack" and nutrition.calories < 300 and recipe.prep_time <= 10:
                suitable.append(recipe)
                continue
        
        return suitable if suitable else recipes  # Fallback to all recipes
    
    def calculate_weekly_nutrition_summary(
        self, 
        meal_plans: List[DayMealPlan]
    ) -> Dict[str, float]:
        """Calculate average daily nutrition over the week."""
        if not meal_plans:
            return {}
        
        total_nutrition = NutritionInfo(0, 0, 0, 0, 0, 0, 0)
        total_cost = 0.0
        days = len(meal_plans)
        
        for day_plan in meal_plans:
            daily_nutrition = day_plan.get_daily_nutrition()
            total_nutrition.calories += daily_nutrition.calories
            total_nutrition.protein += daily_nutrition.protein
            total_nutrition.carbohydrates += daily_nutrition.carbohydrates
            total_nutrition.fat += daily_nutrition.fat
            total_nutrition.fiber += daily_nutrition.fiber
            total_nutrition.sugar += daily_nutrition.sugar
            total_nutrition.sodium += daily_nutrition.sodium
            total_cost += day_plan.get_daily_cost()
        
        return {
            "avg_daily_calories": total_nutrition.calories / days,
            "avg_daily_protein": total_nutrition.protein / days,
            "avg_daily_carbs": total_nutrition.carbohydrates / days,
            "avg_daily_fat": total_nutrition.fat / days,
            "avg_daily_fiber": total_nutrition.fiber / days,
            "avg_daily_sugar": total_nutrition.sugar / days,
            "avg_daily_sodium": total_nutrition.sodium / days,
            "avg_daily_cost": total_cost / days,
            "total_weekly_cost": total_cost,
        }
