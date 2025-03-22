import psycopg2
import json

db_params = {
        "dbname": "postgres",
        "user": "postgres",
        "password": "mysecret",
        "host": "localhost",
        "port": "5432"
    }

def add_recipe_to_db(recipe):
    # Add the recipe to the database
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        ingredients_json = json.dumps(recipe['ingredients'])
        insert_query = "INSERT INTO recipes (name, ingredients, instructions, meal_type) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (recipe['name'], ingredients_json, recipe['instructions'], recipe['meal_type']))
        conn.commit()
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def get_recipes_from_db():
    # Get all recipes from the database
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        select_query = "SELECT * FROM public.recipes"
        cursor.execute(select_query)

        columns = [desc[0] for desc in cursor.description]
        recipes = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        return recipes
    except Exception as e:
        print(f"Error connecting to the database: {e}")
    finally:
        cursor.close()
        conn.close()