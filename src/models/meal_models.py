from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class NutritionInfo:
    """Represents nutritional information for a food item or recipe."""
    calories: float
    protein: float  # in grams
    carbohydrates: float  # in grams
    fat: float  # in grams
    fiber: float  # in grams
    sugar: float  # in grams
    sodium: float  # in mg
    
    def __post_init__(self):
        """Validate nutritional data."""
        if self.calories < 0:
            raise ValueError("Calories cannot be negative")
        if any(value < 0 for value in [self.protein, self.carbohydrates, self.fat, self.fiber, self.sugar, self.sodium]):
            raise ValueError("Nutritional values cannot be negative")

@dataclass
class Ingredient:
    """Represents an ingredient in a recipe."""
    name: str
    amount: float
    unit: str
    nutrition_per_unit: Optional[NutritionInfo] = None
    cost_per_unit: Optional[float] = None  # Cost per unit in dollars
    
    def get_total_nutrition(self) -> Optional[NutritionInfo]:
        """Calculate total nutrition for this ingredient amount."""
        if not self.nutrition_per_unit:
            return None
        
        multiplier = self.amount
        return NutritionInfo(
            calories=self.nutrition_per_unit.calories * multiplier,
            protein=self.nutrition_per_unit.protein * multiplier,
            carbohydrates=self.nutrition_per_unit.carbohydrates * multiplier,
            fat=self.nutrition_per_unit.fat * multiplier,
            fiber=self.nutrition_per_unit.fiber * multiplier,
            sugar=self.nutrition_per_unit.sugar * multiplier,
            sodium=self.nutrition_per_unit.sodium * multiplier
        )
    
    def get_total_cost(self) -> float:
        """Calculate total cost for this ingredient amount."""
        if self.cost_per_unit is None:
            return 0.0
        return self.cost_per_unit * self.amount

@dataclass
class Recipe:
    """Represents a recipe with ingredients and nutritional information."""
    id: str
    name: str
    description: str
    ingredients: List[Ingredient]
    instructions: List[str]
    prep_time: int  # in minutes
    cook_time: int  # in minutes
    servings: int
    difficulty: str  # "easy", "medium", "hard"
    kid_friendly: bool = True
    dietary_tags: List[str] = None  # ["vegetarian", "gluten-free", etc.]
    
    def __post_init__(self):
        if self.dietary_tags is None:
            self.dietary_tags = []
    
    @property
    def total_time(self) -> int:
        """Get total cooking time."""
        return self.prep_time + self.cook_time
    
    def get_nutrition_per_serving(self) -> NutritionInfo:
        """Calculate nutrition per serving."""
        total_nutrition = NutritionInfo(0, 0, 0, 0, 0, 0, 0)
        
        for ingredient in self.ingredients:
            ingredient_nutrition = ingredient.get_total_nutrition()
            if ingredient_nutrition:
                total_nutrition.calories += ingredient_nutrition.calories
                total_nutrition.protein += ingredient_nutrition.protein
                total_nutrition.carbohydrates += ingredient_nutrition.carbohydrates
                total_nutrition.fat += ingredient_nutrition.fat
                total_nutrition.fiber += ingredient_nutrition.fiber
                total_nutrition.sugar += ingredient_nutrition.sugar
                total_nutrition.sodium += ingredient_nutrition.sodium
        
        # Divide by servings
        return NutritionInfo(
            calories=total_nutrition.calories / self.servings,
            protein=total_nutrition.protein / self.servings,
            carbohydrates=total_nutrition.carbohydrates / self.servings,
            fat=total_nutrition.fat / self.servings,
            fiber=total_nutrition.fiber / self.servings,
            sugar=total_nutrition.sugar / self.servings,
            sodium=total_nutrition.sodium / self.servings
        )
    
    def get_cost_per_serving(self) -> float:
        """Calculate cost per serving."""
        total_cost = 0.0
        for ingredient in self.ingredients:
            total_cost += ingredient.get_total_cost()
        return total_cost / self.servings

@dataclass
class Meal:
    """Represents a meal with multiple recipes."""
    name: str
    recipes: List[Recipe]
    meal_type: str  # "breakfast", "lunch", "dinner", "snack"
    
    def get_total_nutrition(self) -> NutritionInfo:
        """Calculate total nutrition for the meal."""
        total = NutritionInfo(0, 0, 0, 0, 0, 0, 0)
        
        for recipe in self.recipes:
            nutrition = recipe.get_nutrition_per_serving()
            total.calories += nutrition.calories
            total.protein += nutrition.protein
            total.carbohydrates += nutrition.carbohydrates
            total.fat += nutrition.fat
            total.fiber += nutrition.fiber
            total.sugar += nutrition.sugar
            total.sodium += nutrition.sodium
        
        return total

    def get_total_cost(self) -> float:
        """Calculate total cost for the meal."""
        total_cost = 0.0
        for recipe in self.recipes:
            total_cost += recipe.get_cost_per_serving()
        return total_cost

@dataclass
class DayMealPlan:
    """Represents a full day of meals."""
    date: datetime
    breakfast: Optional[Meal] = None
    lunch: Optional[Meal] = None
    dinner: Optional[Meal] = None
    snacks: List[Meal] = None
    
    def __post_init__(self):
        if self.snacks is None:
            self.snacks = []
    
    def get_daily_nutrition(self) -> NutritionInfo:
        """Calculate total nutrition for the day."""
        total = NutritionInfo(0, 0, 0, 0, 0, 0, 0)
        
        for meal in [self.breakfast, self.lunch, self.dinner] + self.snacks:
            if meal:
                nutrition = meal.get_total_nutrition()
                total.calories += nutrition.calories
                total.protein += nutrition.protein
                total.carbohydrates += nutrition.carbohydrates
                total.fat += nutrition.fat
                total.fiber += nutrition.fiber
                total.sugar += nutrition.sugar
                total.sodium += nutrition.sodium
        
        return total
    
    def get_daily_cost(self) -> float:
        """Calculate total cost for the day."""
        total_cost = 0.0
        
        for meal in [self.breakfast, self.lunch, self.dinner] + self.snacks:
            if meal:
                total_cost += meal.get_total_cost()
        
        return total_cost
    
    def is_within_calorie_limit(self, calorie_limit: float) -> bool:
        """Check if daily calories are within the specified limit."""
        return self.get_daily_nutrition().calories <= calorie_limit
    
    def is_within_budget(self, daily_budget: float) -> bool:
        """Check if daily cost is within the specified budget."""
        return self.get_daily_cost() <= daily_budget
