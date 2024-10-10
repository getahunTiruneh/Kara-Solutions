import unittest
import psycopg2
import os
import pandas as pd


# Assuming the main code is in a file named `database_operations.py`
from database.databse_conn import get_db_connection

class TestDatabaseConnection(unittest.TestCase):

    def test_db_connection_success(self):
        """Test if the database connection is established successfully."""
        try:
            conn = get_db_connection()
            self.assertIsNotNone(conn)  # Check if connection object is not None
            self.assertTrue(conn.closed == 0)  # Ensure connection is open (0 means connection is open)
        except Exception as e:
            self.fail(f"Database connection failed: {e}")
        finally:
            if conn:
                conn.close()
                self.assertTrue(conn.closed == 1)  # Ensure the connection is closed (1 means connection is closed)

if __name__ == '__main__':
    unittest.main()