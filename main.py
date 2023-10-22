import unittest

from UnitTest.test_solution import TestSolution

from WebUI.app import App
from WebUI.test_ui import TestUI

import multiprocessing
import os

def start_flask_server():
    webui = App()
    webui.run()

def run_unit_tests():
    print("UnitTest:")
    unittest.main()

if __name__ == "__main__":
    # Create two separate processes for running the Flask server and unittests
    flask_process = multiprocessing.Process(target=start_flask_server)
    unittest_process = multiprocessing.Process(target=run_unit_tests)

    # Start the Flask server process
    flask_process.start()

    # Start the unittest process
    unittest_process.start()
    unittest_process.join()

    flask_process.terminate()

