
import os
import unittest
import subprocess

ENDPOINT_URL = os.getenv('URL')
AWS_ACCESS_KEY_ID = os.getenv('ID')
AWS_SECRET_ACCESS_KEY = os.getenv('SECRET')
HREF_BASE_URL = os.getenv('BASE')
ARGUMENTS = os.getenv('ARGUMENTS')
        
class TestExampleScript(unittest.TestCase):
    def test_script_output(self):
        # Run the script using subprocess
        result = subprocess.run(
            ["python", "src/ye3sld/ye3sld.py",
             "--endpoint_url", ENDPOINT_URL,
             "--aws_access_key_id", AWS_ACCESS_KEY_ID,
             "--aws_secret_access_key", AWS_SECRET_ACCESS_KEY,
             "--href_base_url", HREF_BASE_URL,
             ARGUMENTS,
            ],
            capture_output=True,
            text=True
        )
        
        # Print the output for debugging
        print("Script output:", result.stdout.strip())
        
        # Check if the output starts with "Success"
        self.assertTrue(result.stdout.strip().startswith("Success"))
        
        # Optionally, check if there were no errors
        self.assertEqual(result.returncode, 0)

if __name__ == "__main__":
    unittest.main()
