from typing import List
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.models.meal_models import Recipe, Ingredient, NutritionInfo
from src.utils.additional_recipes import get_additional_kid_friendly_recipes

def get_sample_kid_friendly_recipes() -> List[Recipe]:
    """Get a collection of kid-friendly recipes with nutritional information."""
    
    recipes = []
    
    # Breakfast Recipes
    recipes.append(Recipe(
        id="breakfast_001",
        name="Fluffy Pancakes with Berries",
        description="Light, fluffy pancakes topped with fresh berries and a drizzle of maple syrup",
        ingredients=[
            Ingredient("Flour", 1.0, "cup", NutritionInfo(95, 3, 20, 0.2, 0.7, 0.1, 2), 0.25),
            Ingredient("Milk", 1.0, "cup", NutritionInfo(150, 8, 12, 8, 0, 12, 105), 0.50),
            Ingredient("Eggs", 1.0, "large", NutritionInfo(70, 6, 0.4, 5, 0, 0.2, 70), 0.25),
            Ingredient("Butter", 2.0, "tbsp", NutritionInfo(204, 0.2, 0, 23, 0, 0, 164), 0.30),
            Ingredient("Mixed Berries", 0.5, "cup", NutritionInfo(40, 0.5, 10, 0.2, 4, 7, 1), 1.50),
            Ingredient("Maple Syrup", 2.0, "tbsp", NutritionInfo(104, 0, 27, 0, 0, 24, 2), 0.40)
        ],
        instructions=[
            "Mix dry ingredients in a bowl",
            "Combine wet ingredients separately",
            "Fold wet ingredients into dry ingredients until just combined",
            "Cook pancakes on medium heat until bubbles form",
            "Flip and cook until golden brown",
            "Serve with berries and maple syrup"
        ],
        prep_time=10,
        cook_time=15,
        servings=4,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=["vegetarian"]
    ))
    
    recipes.append(Recipe(
        id="breakfast_002",
        name="Cheesy Scrambled Eggs",
        description="Creamy scrambled eggs with mild cheddar cheese",
        ingredients=[
            Ingredient("Eggs", 4.0, "large", NutritionInfo(280, 24, 1.6, 20, 0, 0.8, 280), 1.00),
            Ingredient("Cheddar Cheese", 0.25, "cup", NutritionInfo(110, 7, 1, 9, 0, 0.1, 180), 1.25),
            Ingredient("Butter", 1.0, "tbsp", NutritionInfo(102, 0.1, 0, 11.5, 0, 0, 82), 0.15),
            Ingredient("Milk", 2.0, "tbsp", NutritionInfo(19, 1, 1.5, 1, 0, 1.5, 13), 0.13)
        ],
        instructions=[
            "Crack eggs into a bowl and whisk with milk",
            "Heat butter in a non-stick pan over low heat",
            "Pour in eggs and gently stir constantly",
            "Add cheese when eggs are almost set",
            "Remove from heat and continue stirring until creamy"
        ],
        prep_time=5,
        cook_time=8,
        servings=2,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=["vegetarian", "gluten-free"]
    ))
    
    # Additional Breakfast Recipes for Variety
    recipes.append(Recipe(
        id="breakfast_003",
        name="Cinnamon French Toast",
        description="Golden French toast with a hint of cinnamon and powdered sugar",
        ingredients=[
            Ingredient("Bread", 4.0, "slices", NutritionInfo(320, 12, 60, 4, 4, 4, 640), 1.00),
            Ingredient("Eggs", 2.0, "large", NutritionInfo(140, 12, 0.8, 10, 0, 0.4, 140), 0.50),
            Ingredient("Milk", 0.25, "cup", NutritionInfo(38, 2, 3, 2, 0, 3, 26), 0.13),
            Ingredient("Cinnamon", 0.5, "tsp", NutritionInfo(3, 0.1, 0.8, 0, 0.3, 0, 0.5), 0.05),
            Ingredient("Butter", 1.0, "tbsp", NutritionInfo(102, 0.1, 0, 11.5, 0, 0, 82), 0.15),
            Ingredient("Powdered Sugar", 1.0, "tbsp", NutritionInfo(30, 0, 8, 0, 0, 8, 0), 0.10)
        ],
        instructions=[
            "Whisk eggs, milk, and cinnamon in a shallow bowl",
            "Dip bread slices in egg mixture",
            "Cook in buttered pan until golden on both sides",
            "Dust with powdered sugar before serving"
        ],
        prep_time=8,
        cook_time=12,
        servings=2,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=["vegetarian"]
    ))
    
    recipes.append(Recipe(
        id="breakfast_004",
        name="Banana Oatmeal",
        description="Warm oatmeal with sliced bananas and a touch of honey",
        ingredients=[
            Ingredient("Rolled Oats", 1.0, "cup", NutritionInfo(154, 5, 28, 3, 4, 1, 2), 0.75),
            Ingredient("Milk", 2.0, "cups", NutritionInfo(300, 16, 24, 16, 0, 24, 210), 1.00),
            Ingredient("Banana", 1.0, "medium", NutritionInfo(105, 1, 27, 0.4, 3, 14, 1), 0.60),
            Ingredient("Honey", 1.0, "tbsp", NutritionInfo(64, 0.1, 17, 0, 0, 16, 1), 0.35)
        ],
        instructions=[
            "Bring milk to a boil in a saucepan",
            "Add oats and simmer for 5-7 minutes",
            "Slice banana and stir into oatmeal",
            "Drizzle with honey before serving"
        ],
        prep_time=5,
        cook_time=10,
        servings=2,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=["vegetarian", "gluten-free"]
    ))
    
    # Lunch Recipes
    recipes.append(Recipe(
        id="lunch_001",
        name="Grilled Cheese and Tomato Soup",
        description="Classic grilled cheese sandwich with creamy tomato soup",
        ingredients=[
            Ingredient("Bread", 4.0, "slices", NutritionInfo(320, 12, 60, 4, 4, 4, 640), 1.00),
            Ingredient("Cheddar Cheese", 4.0, "slices", NutritionInfo(440, 28, 4, 36, 0, 0.4, 720), 2.00),
            Ingredient("Butter", 2.0, "tbsp", NutritionInfo(204, 0.2, 0, 23, 0, 0, 164), 0.30),
            Ingredient("Tomato Soup", 2.0, "cups", NutritionInfo(180, 4, 36, 2, 6, 24, 1400), 2.50)
        ],
        instructions=[
            "Butter one side of each bread slice",
            "Place cheese between bread slices, butter side out",
            "Cook in pan over medium heat until golden and cheese melts",
            "Heat tomato soup according to package instructions",
            "Serve sandwich with soup"
        ],
        prep_time=5,
        cook_time=10,
        servings=2,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=["vegetarian"]
    ))
    
    recipes.append(Recipe(
        id="lunch_002",
        name="Chicken Nuggets with Sweet Potato Fries",
        description="Homemade baked chicken nuggets with crispy sweet potato fries",
        ingredients=[
            Ingredient("Chicken Breast", 1.0, "lb", NutritionInfo(480, 90, 0, 10.4, 0, 0, 320), 6.99),
            Ingredient("Breadcrumbs", 1.0, "cup", NutritionInfo(110, 4, 20, 1.5, 2, 2, 230), 0.75),
            Ingredient("Sweet Potato", 2.0, "medium", NutritionInfo(200, 4, 46, 0.2, 6.8, 8.4, 12), 2.00),
            Ingredient("Olive Oil", 2.0, "tbsp", NutritionInfo(240, 0, 0, 28, 0, 0, 0), 0.50),
            Ingredient("Egg", 1.0, "large", NutritionInfo(70, 6, 0.4, 5, 0, 0.2, 70), 0.25)
        ],
        instructions=[
            "Cut chicken into nugget-sized pieces",
            "Dip chicken in beaten egg, then coat with breadcrumbs",
            "Cut sweet potatoes into fry shapes",
            "Toss sweet potatoes with olive oil and seasonings",
            "Bake nuggets and fries at 400°F for 15-20 minutes",
            "Serve hot with ketchup"
        ],
        prep_time=15,
        cook_time=20,
        servings=4,
        difficulty="medium",
        kid_friendly=True,
        dietary_tags=["gluten-free"]
    ))
    
    # Additional Lunch Recipes
    recipes.append(Recipe(
        id="lunch_003",
        name="Mini Turkey and Cheese Pinwheels",
        description="Fun pinwheel sandwiches with turkey and cheese",
        ingredients=[
            Ingredient("Tortillas", 2.0, "large", NutritionInfo(240, 6, 40, 6, 4, 2, 480), 1.50),
            Ingredient("Turkey Slices", 4.0, "oz", NutritionInfo(120, 24, 2, 2, 0, 1, 720), 3.50),
            Ingredient("Cream Cheese", 2.0, "tbsp", NutritionInfo(100, 2, 2, 10, 0, 1, 90), 0.75),
            Ingredient("Cheddar Cheese", 2.0, "slices", NutritionInfo(220, 14, 2, 18, 0, 0.2, 360), 1.00),
            Ingredient("Lettuce", 4.0, "leaves", NutritionInfo(4, 0.3, 0.8, 0, 0.4, 0.2, 3), 0.25)
        ],
        instructions=[
            "Spread cream cheese on tortillas",
            "Layer turkey, cheese, and lettuce",
            "Roll up tightly and slice into pinwheels",
            "Serve with fruit or veggie sticks"
        ],
        prep_time=10,
        cook_time=0,
        servings=2,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=[]
    ))
    
    recipes.append(Recipe(
        id="lunch_004",
        name="Mac and Cheese",
        description="Creamy homemade macaroni and cheese",
        ingredients=[
            Ingredient("Macaroni Pasta", 2.0, "cups", NutritionInfo(400, 14, 80, 2, 3, 2, 8), 1.25),
            Ingredient("Cheddar Cheese", 1.0, "cup", NutritionInfo(440, 28, 4, 36, 0, 0.4, 720), 4.00),
            Ingredient("Milk", 0.5, "cup", NutritionInfo(75, 4, 6, 4, 0, 6, 53), 0.25),
            Ingredient("Butter", 2.0, "tbsp", NutritionInfo(204, 0.2, 0, 23, 0, 0, 164), 0.30),
            Ingredient("Flour", 1.0, "tbsp", NutritionInfo(28, 0.8, 6, 0.1, 0.2, 0, 0.6), 0.06)
        ],
        instructions=[
            "Cook macaroni according to package directions",
            "Make cheese sauce with butter, flour, milk, and cheese",
            "Mix pasta with cheese sauce",
            "Serve hot"
        ],
        prep_time=5,
        cook_time=20,
        servings=4,
        difficulty="medium",
        kid_friendly=True,
        dietary_tags=["vegetarian"]
    ))
    
    # Dinner Recipes
    recipes.append(Recipe(
        id="dinner_001",
        name="Spaghetti with Mild Meat Sauce",
        description="Kid-friendly spaghetti with a mild, flavorful meat sauce",
        ingredients=[
            Ingredient("Spaghetti", 1.0, "lb", NutritionInfo(1600, 56, 320, 8, 12, 8, 16), 1.25),
            Ingredient("Ground Beef", 0.5, "lb", NutritionInfo(560, 50, 0, 40, 0, 0, 160), 4.50),
            Ingredient("Tomato Sauce", 2.0, "cups", NutritionInfo(140, 6, 32, 1, 8, 24, 1400), 1.50),
            Ingredient("Onion", 0.5, "medium", NutritionInfo(20, 0.6, 4.6, 0.1, 1.4, 2.1, 2), 0.50),
            Ingredient("Garlic", 2.0, "cloves", NutritionInfo(8, 0.4, 2, 0, 0.1, 0.1, 1), 0.25),
            Ingredient("Parmesan Cheese", 0.25, "cup", NutritionInfo(108, 10, 1, 7, 0, 0.2, 340), 1.25)
        ],
        instructions=[
            "Cook spaghetti according to package directions",
            "Brown ground beef in a large pan",
            "Add diced onion and garlic, cook until soft",
            "Add tomato sauce and simmer for 15 minutes",
            "Season with salt and pepper to taste",
            "Serve over spaghetti with parmesan cheese"
        ],
        prep_time=10,
        cook_time=25,
        servings=4,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=[]
    ))
    
    recipes.append(Recipe(
        id="dinner_002",
        name="Baked Chicken Tenders with Rice",
        description="Crispy baked chicken tenders served with fluffy white rice",
        ingredients=[
            Ingredient("Chicken Tenders", 1.0, "lb", NutritionInfo(480, 90, 0, 10.4, 0, 0, 320), 7.99),
            Ingredient("Panko Breadcrumbs", 1.0, "cup", NutritionInfo(110, 4, 20, 1.5, 2, 2, 230), 0.75),
            Ingredient("White Rice", 1.0, "cup", NutritionInfo(680, 14, 148, 1.2, 2.4, 0.2, 8), 0.50),
            Ingredient("Olive Oil", 1.0, "tbsp", NutritionInfo(120, 0, 0, 14, 0, 0, 0), 0.25),
            Ingredient("Egg", 1.0, "large", NutritionInfo(70, 6, 0.4, 5, 0, 0.2, 70), 0.25)
        ],
        instructions=[
            "Preheat oven to 425°F",
            "Dip chicken tenders in beaten egg",
            "Coat with panko breadcrumbs",
            "Place on baking sheet and drizzle with olive oil",
            "Bake for 15-18 minutes until golden",
            "Cook rice according to package directions",
            "Serve chicken over rice"
        ],
        prep_time=10,
        cook_time=20,
        servings=4,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=[]
    ))
    
    # Additional Dinner Recipes
    recipes.append(Recipe(
        id="dinner_003",
        name="Mini Meatballs with Mashed Potatoes",
        description="Kid-sized meatballs with creamy mashed potatoes",
        ingredients=[
            Ingredient("Ground Beef", 1.0, "lb", NutritionInfo(1120, 100, 0, 80, 0, 0, 320), 9.00),
            Ingredient("Breadcrumbs", 0.5, "cup", NutritionInfo(55, 2, 10, 0.75, 1, 1, 115), 0.38),
            Ingredient("Egg", 1.0, "large", NutritionInfo(70, 6, 0.4, 5, 0, 0.2, 70), 0.25),
            Ingredient("Potatoes", 4.0, "medium", NutritionInfo(640, 16, 144, 0.8, 12, 8, 32), 2.50),
            Ingredient("Milk", 0.25, "cup", NutritionInfo(38, 2, 3, 2, 0, 3, 26), 0.13),
            Ingredient("Butter", 2.0, "tbsp", NutritionInfo(204, 0.2, 0, 23, 0, 0, 164), 0.30)
        ],
        instructions=[
            "Mix ground beef, breadcrumbs, and egg for meatballs",
            "Form into small, kid-friendly meatballs",
            "Bake at 375°F for 20 minutes",
            "Boil and mash potatoes with milk and butter",
            "Serve meatballs over mashed potatoes"
        ],
        prep_time=15,
        cook_time=30,
        servings=4,
        difficulty="medium",
        kid_friendly=True,
        dietary_tags=[]
    ))
    
    recipes.append(Recipe(
        id="dinner_004",
        name="Cheese Quesadillas with Rice",
        description="Crispy cheese quesadillas served with Spanish rice",
        ingredients=[
            Ingredient("Tortillas", 4.0, "medium", NutritionInfo(480, 12, 80, 12, 8, 4, 960), 3.00),
            Ingredient("Cheddar Cheese", 1.0, "cup", NutritionInfo(440, 28, 4, 36, 0, 0.4, 720), 4.00),
            Ingredient("White Rice", 1.0, "cup", NutritionInfo(680, 14, 148, 1.2, 2.4, 0.2, 8), 0.50),
            Ingredient("Tomato Sauce", 0.25, "cup", NutritionInfo(18, 0.8, 4, 0.1, 1, 3, 175), 0.19),
            Ingredient("Olive Oil", 1.0, "tbsp", NutritionInfo(120, 0, 0, 14, 0, 0, 0), 0.25)
        ],
        instructions=[
            "Cook rice with tomato sauce for Spanish rice",
            "Place cheese between two tortillas",
            "Cook quesadillas in pan until crispy",
            "Cut into triangles and serve with rice"
        ],
        prep_time=10,
        cook_time=25,
        servings=4,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=["vegetarian"]
    ))
    
    # Snack Recipes
    recipes.append(Recipe(
        id="snack_001",
        name="Apple Slices with Peanut Butter",
        description="Fresh apple slices served with creamy peanut butter",
        ingredients=[
            Ingredient("Apple", 1.0, "medium", NutritionInfo(95, 0.5, 25, 0.3, 4.4, 19, 2), 1.25),
            Ingredient("Peanut Butter", 2.0, "tbsp", NutritionInfo(190, 8, 8, 16, 2, 3, 140), 0.75)
        ],
        instructions=[
            "Wash and core the apple",
            "Cut into wedges or slices",
            "Serve with peanut butter for dipping"
        ],
        prep_time=5,
        cook_time=0,
        servings=1,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=["vegetarian", "gluten-free"]
    ))
    
    recipes.append(Recipe(
        id="snack_002",
        name="Cheese and Crackers",
        description="Mild cheese cubes with whole grain crackers",
        ingredients=[
            Ingredient("Mild Cheddar Cheese", 1.0, "oz", NutritionInfo(110, 7, 1, 9, 0, 0.1, 180), 0.75),
            Ingredient("Whole Grain Crackers", 6.0, "crackers", NutritionInfo(120, 3, 18, 4.5, 3, 0, 230), 0.50)
        ],
        instructions=[
            "Cut cheese into small cubes",
            "Arrange cheese and crackers on a plate",
            "Serve as a healthy snack"
        ],
        prep_time=3,
        cook_time=0,
        servings=1,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=["vegetarian"]
    ))
    
    # Additional Snacks
    recipes.append(Recipe(
        id="snack_003",
        name="Banana with Nutella",
        description="Sliced banana with a small amount of Nutella for dipping",
        ingredients=[
            Ingredient("Banana", 1.0, "medium", NutritionInfo(105, 1, 27, 0.4, 3, 14, 1), 0.60),
            Ingredient("Nutella", 1.0, "tbsp", NutritionInfo(100, 1, 11, 6, 1, 10, 5), 0.50)
        ],
        instructions=[
            "Slice banana into rounds",
            "Serve with Nutella for dipping"
        ],
        prep_time=2,
        cook_time=0,
        servings=1,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=["vegetarian"]
    ))
    
    recipes.append(Recipe(
        id="snack_004",
        name="Mini Muffins",
        description="Small blueberry muffins perfect for little hands",
        ingredients=[
            Ingredient("Flour", 1.5, "cups", NutritionInfo(142, 4.5, 30, 0.3, 1.1, 0.15, 3), 0.38),
            Ingredient("Sugar", 0.5, "cup", NutritionInfo(387, 0, 100, 0, 0, 100, 2), 0.35),
            Ingredient("Egg", 1.0, "large", NutritionInfo(70, 6, 0.4, 5, 0, 0.2, 70), 0.25),
            Ingredient("Milk", 0.5, "cup", NutritionInfo(75, 4, 6, 4, 0, 6, 53), 0.25),
            Ingredient("Blueberries", 0.5, "cup", NutritionInfo(42, 0.5, 11, 0.2, 2, 7, 1), 2.00),
            Ingredient("Butter", 0.25, "cup", NutritionInfo(407, 0.5, 0, 46, 0, 0, 328), 0.60)
        ],
        instructions=[
            "Mix dry ingredients in a bowl",
            "Combine wet ingredients separately",
            "Fold wet into dry ingredients with blueberries",
            "Bake in mini muffin tins at 375°F for 12-15 minutes"
        ],
        prep_time=10,
        cook_time=15,
        servings=12,
        difficulty="medium",
        kid_friendly=True,
        dietary_tags=["vegetarian"]
    ))
    
    # Add additional kid-friendly recipes for more variety
    additional_recipes = get_additional_kid_friendly_recipes()
    recipes.extend(additional_recipes)
    
    return recipes
