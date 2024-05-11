import json


#გავხსნათ და წავიკითხოთ ფაილი.

def read_file(file_name):
    with open(file_name, 'r') as file:
        file_contents = json.load(file)
    return file_contents


#შევინახოთ საჭმლის მოსამზადებლად საჭირო ინგრედიენტები, დააბრუნებს სიას.
def ingredients_needed(meal, meals_content):
    ingredients = meals_content.get(meal)
    return ingredients

#მოვძებნოთ მაღაზიები, რომლებშიც ამ ინგრედიენტების ყიდვას შევძლებთ.
def markets_to_go(ingredients, markets_content):
    markets = []
    for ing in ingredients:
        for market, ings in markets_content.items():
            if ing in ings:
                markets.append(market)
                break
        else:
            return "This meal can't be made in this town."
    
    return set(markets)


def main():
    meals_content = read_file("meals.json")
    markets_content = read_file("markets.json")
    meal = (input("Enter the meal you want to prepare: ")).lower()
    ingredients = ingredients_needed(meal, meals_content)
    markets = markets_to_go(ingredients, markets_content)
    
    print(f"You should go to {markets} to make {meal}.")

if __name__ == "__main__":
    main()
            
        
