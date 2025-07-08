from typing import List
from src.models.meal_models import Recipe, Ingredient, NutritionInfo

def get_additional_kid_friendly_recipes() -> List[Recipe]:
    """Get additional kid-friendly recipes to enhance variety."""
    
    recipes = []
    
    # Additional Breakfast Recipes
    recipes.append(Recipe(
        id="breakfast_005",
        name="Rainbow Fruit Parfait",
        description="Colorful layers of yogurt and fresh fruit with a sprinkle of granola",
        ingredients=[
            Ingredient("Greek Yogurt", 1.5, "cups", NutritionInfo(195, 33, 9, 0, 0, 9, 75), 2.25),
            Ingredient("Strawberries", 0.5, "cups", NutritionInfo(25, 0.5, 6, 0.3, 1.5, 3.5, 1), 1.50),
            Ingredient("Blueberries", 0.5, "cups", NutritionInfo(42, 0.5, 11, 0.2, 2, 7, 1), 2.00),
            Ingredient("Banana", 1.0, "medium", NutritionInfo(105, 1, 27, 0.4, 3, 14, 1), 0.60),
            Ingredient("Granola", 0.25, "cup", NutritionInfo(120, 3, 18, 6, 2, 6, 10), 0.75),
            Ingredient("Honey", 1.0, "tbsp", NutritionInfo(64, 0.1, 17, 0, 0, 16, 1), 0.35)
        ],
        instructions=[
            "Layer yogurt and fruits in clear glasses or bowls",
            "Top with granola",
            "Drizzle with honey",
            "Serve immediately"
        ],
        prep_time=10,
        cook_time=0,
        servings=2,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=["vegetarian"]
    ))
    
    recipes.append(Recipe(
        id="breakfast_006",
        name="Mini Breakfast Burritos",
        description="Small handheld breakfast burritos with scrambled eggs and cheese",
        ingredients=[
            Ingredient("Small Tortillas", 4.0, "pieces", NutritionInfo(240, 8, 44, 4, 4, 0, 480), 2.00),
            Ingredient("Eggs", 4.0, "large", NutritionInfo(280, 24, 1.6, 20, 0, 0.8, 280), 1.00),
            Ingredient("Cheddar Cheese", 0.5, "cup", NutritionInfo(220, 14, 2, 18, 0, 0.2, 360), 2.50),
            Ingredient("Bell Pepper", 0.5, "medium", NutritionInfo(15, 0.5, 3, 0.2, 1, 2, 1), 0.75),
            Ingredient("Butter", 1.0, "tbsp", NutritionInfo(102, 0.1, 0, 11.5, 0, 0, 82), 0.15),
            Ingredient("Milk", 2.0, "tbsp", NutritionInfo(19, 1, 1.5, 1, 0, 1.5, 13), 0.13)
        ],
        instructions=[
            "Scramble eggs with milk and diced bell pepper",
            "Warm tortillas in a dry pan",
            "Fill each tortilla with scrambled eggs and cheese",
            "Fold into burritos and serve warm"
        ],
        prep_time=10,
        cook_time=10,
        servings=4,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=["vegetarian"]
    ))
    
    # Additional Lunch Recipes
    recipes.append(Recipe(
        id="lunch_005",
        name="Mini Pizzas on English Muffins",
        description="Kid-sized pizzas made on English muffins with toppings",
        ingredients=[
            Ingredient("English Muffins", 4.0, "pieces", NutritionInfo(260, 8, 52, 2, 4, 4, 420), 2.50),
            Ingredient("Pizza Sauce", 0.5, "cup", NutritionInfo(60, 2, 8, 3, 2, 6, 600), 1.25),
            Ingredient("Mozzarella Cheese", 1.0, "cup", NutritionInfo(336, 24, 2, 28, 0, 2, 600), 3.50),
            Ingredient("Bell Peppers", 0.5, "cup", NutritionInfo(15, 0.5, 3, 0.2, 1, 2, 1), 0.75),
            Ingredient("Mushrooms", 0.5, "cup", NutritionInfo(10, 1, 2, 0, 0.5, 1, 1), 1.00),
            Ingredient("Pepperoni", 0.25, "cup", NutritionInfo(140, 6, 2, 12, 0, 0, 560), 1.50)
        ],
        instructions=[
            "Split English muffins in half",
            "Spread pizza sauce on each half",
            "Top with cheese and chosen toppings",
            "Bake at 375°F for 10-12 minutes until cheese is melted"
        ],
        prep_time=10,
        cook_time=12,
        servings=4,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=[]
    ))
    
    recipes.append(Recipe(
        id="lunch_006",
        name="Taco Cups",
        description="Fun, crunchy taco cups with ground beef and cheese",
        ingredients=[
            Ingredient("Ground Beef", 0.5, "lb", NutritionInfo(560, 50, 0, 40, 0, 0, 160), 4.50),
            Ingredient("Taco Seasoning", 1.0, "packet", NutritionInfo(30, 1, 6, 0.5, 1, 0, 1200), 1.00),
            Ingredient("Tortillas", 6.0, "medium", NutritionInfo(720, 18, 120, 18, 12, 6, 1440), 3.00),
            Ingredient("Cheddar Cheese", 1.0, "cup", NutritionInfo(440, 28, 4, 36, 0, 0.4, 720), 4.00),
            Ingredient("Lettuce", 1.0, "cup", NutritionInfo(8, 0.6, 1.6, 0.1, 0.8, 0.4, 6), 0.50),
            Ingredient("Tomato", 1.0, "medium", NutritionInfo(22, 1, 5, 0.2, 1.5, 3, 6), 0.75)
        ],
        instructions=[
            "Press tortillas into muffin tins to form cups",
            "Bake at 375°F for 10 minutes until crisp",
            "Brown ground beef and mix with taco seasoning",
            "Fill tortilla cups with meat, cheese, and toppings"
        ],
        prep_time=15,
        cook_time=15,
        servings=6,
        difficulty="medium",
        kid_friendly=True,
        dietary_tags=[]
    ))
    
    # Additional Dinner Recipes
    recipes.append(Recipe(
        id="dinner_005",
        name="Baked Chicken Fingers with Sweet Potato Fries",
        description="Crispy baked chicken fingers with homemade sweet potato fries",
        ingredients=[
            Ingredient("Chicken Tenders", 1.0, "lb", NutritionInfo(480, 90, 0, 10.4, 0, 0, 320), 7.99),
            Ingredient("Breadcrumbs", 1.0, "cup", NutritionInfo(110, 4, 20, 1.5, 2, 2, 230), 0.75),
            Ingredient("Sweet Potato", 2.0, "medium", NutritionInfo(200, 4, 46, 0.2, 6.8, 8.4, 12), 2.00),
            Ingredient("Olive Oil", 2.0, "tbsp", NutritionInfo(240, 0, 0, 28, 0, 0, 0), 0.50),
            Ingredient("Egg", 1.0, "large", NutritionInfo(70, 6, 0.4, 5, 0, 0.2, 70), 0.25),
            Ingredient("Garlic Powder", 1.0, "tsp", NutritionInfo(10, 0.5, 2, 0, 0.2, 0, 1), 0.10)
        ],
        instructions=[
            "Cut sweet potatoes into fries and toss with oil and seasonings",
            "Bake sweet potatoes at 425°F for 20 minutes",
            "Dip chicken tenders in beaten egg, then coat with seasoned breadcrumbs",
            "Bake chicken at 425°F for 15-18 minutes until crispy and cooked through",
            "Serve with ketchup or other dipping sauce"
        ],
        prep_time=15,
        cook_time=20,
        servings=4,
        difficulty="medium",
        kid_friendly=True,
        dietary_tags=[]
    ))
    
    recipes.append(Recipe(
        id="dinner_006",
        name="Mini Meatloaf Muffins",
        description="Individual meatloaf portions baked in a muffin tin",
        ingredients=[
            Ingredient("Ground Beef", 1.0, "lb", NutritionInfo(1120, 100, 0, 80, 0, 0, 320), 9.00),
            Ingredient("Breadcrumbs", 0.5, "cup", NutritionInfo(55, 2, 10, 0.75, 1, 1, 115), 0.38),
            Ingredient("Egg", 1.0, "large", NutritionInfo(70, 6, 0.4, 5, 0, 0.2, 70), 0.25),
            Ingredient("Onion", 0.5, "small", NutritionInfo(20, 0.6, 4.6, 0.1, 1.4, 2.1, 2), 0.25),
            Ingredient("Ketchup", 0.25, "cup", NutritionInfo(60, 1, 16, 0, 0, 12, 960), 0.50),
            Ingredient("Garlic", 2.0, "cloves", NutritionInfo(8, 0.4, 2, 0, 0.1, 0.1, 1), 0.25)
        ],
        instructions=[
            "Mix ground beef with breadcrumbs, egg, and chopped onion and garlic",
            "Press mixture into greased muffin tins",
            "Top each with a spoonful of ketchup",
            "Bake at 375°F for 20-25 minutes until cooked through",
            "Serve with mashed potatoes and veggies"
        ],
        prep_time=15,
        cook_time=25,
        servings=6,
        difficulty="medium",
        kid_friendly=True,
        dietary_tags=[]
    ))
    
    # Additional Snack Recipes
    recipes.append(Recipe(
        id="snack_005",
        name="Fruit and Yogurt Popsicles",
        description="Frozen yogurt popsicles with real fruit chunks",
        ingredients=[
            Ingredient("Greek Yogurt", 2.0, "cups", NutritionInfo(260, 44, 12, 0, 0, 12, 100), 3.00),
            Ingredient("Mixed Berries", 1.0, "cup", NutritionInfo(80, 1, 20, 0.4, 8, 14, 2), 3.00),
            Ingredient("Honey", 2.0, "tbsp", NutritionInfo(128, 0.2, 34, 0, 0, 32, 2), 0.70)
        ],
        instructions=[
            "Mix yogurt with honey",
            "Fold in berries",
            "Pour into popsicle molds",
            "Freeze for at least 4 hours",
            "Run molds under warm water to release popsicles"
        ],
        prep_time=10,
        cook_time=0,
        servings=6,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=["vegetarian", "gluten-free"]
    ))
    
    recipes.append(Recipe(
        id="snack_006",
        name="Crunchy Chickpeas",
        description="Crispy roasted chickpeas with mild seasoning",
        ingredients=[
            Ingredient("Canned Chickpeas", 1.0, "can", NutritionInfo(210, 11, 35, 2, 10, 2, 400), 0.89),
            Ingredient("Olive Oil", 1.0, "tbsp", NutritionInfo(120, 0, 0, 14, 0, 0, 0), 0.25),
            Ingredient("Salt", 0.25, "tsp", NutritionInfo(0, 0, 0, 0, 0, 0, 580), 0.01),
            Ingredient("Paprika", 0.5, "tsp", NutritionInfo(3, 0.2, 0.5, 0.1, 0.2, 0.1, 1), 0.05)
        ],
        instructions=[
            "Drain and rinse chickpeas",
            "Pat dry with paper towels",
            "Toss with olive oil and seasonings",
            "Spread on a baking sheet",
            "Bake at 400°F for 20-30 minutes until crispy"
        ],
        prep_time=5,
        cook_time=25,
        servings=4,
        difficulty="easy",
        kid_friendly=True,
        dietary_tags=["vegetarian", "gluten-free", "vegan"]
    ))
    
    return recipes
