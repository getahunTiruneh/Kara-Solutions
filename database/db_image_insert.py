import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd
import ast

# Load environment variables from .env file
load_dotenv()

# PostgreSQL connection function
def connect_db():
    try:
        # Connect to your PostgreSQL DB
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

# Function to insert detection result data into PostgreSQL
def insert_detection_data(df):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            insert_query = """
            INSERT INTO detection_results (image_name, confidence_score, class_name, bbox_coordinates, result_image_path)
            VALUES (%s, %s, %s, %s, %s)
            """
            # Iterate through the DataFrame rows and insert data into PostgreSQL
            for index, row in df.iterrows():
                # Convert bbox_coordinates to a list if it's a string representation
                if isinstance(row['bbox_coordinates'], str):
                    row['bbox_coordinates'] = ast.literal_eval(row['bbox_coordinates'])

                # Ensure bbox_coordinates is a list and convert to string with braces
                if isinstance(row['bbox_coordinates'], list):
                    bbox_coords = '{' + ','.join(map(str, row['bbox_coordinates'])) + '}'
                else:
                    raise ValueError("bbox_coordinates must be a list.")

                cursor.execute(insert_query, (
                    row['image_name'], 
                    row['confidence_score'], 
                    row['class_name'], 
                    bbox_coords,
                    row['result_image_path']
                ))

            # Commit the transaction
            conn.commit()
            cursor.close()
            print("Data successfully inserted into PostgreSQL.")
        except Exception as e:
            print(f"Error inserting data into PostgreSQL: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database.")