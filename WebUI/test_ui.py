import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from parameterized import parameterized

class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:5000")

    @parameterized.expand([
        ([[2,2,2],[2,2,2],[2,2,2]], "Time: 0"),  # Test 1
        ([[0,0,0],[0,0,0],[0,0,0]], "Time: 0"),  # Test 2
        ([[1,1,1],[1,1,1],[1,1,1]], "Time: -1"),  # Test 3
        ([[2,1,1],[1,1,0],[0,1,1]], "Time: 4")   # Test 4
    ])
    def test_orangesRotting(self, input_grid, expected_result):
        textarea = self.driver.find_element(By.NAME, "grid")
        submit = self.driver.find_element(By.NAME, "submit")
        textarea.clear()
        textarea.send_keys(str(input_grid))
        submit.click()
        result = self.driver.find_element(By.ID, "Solution").text
    @parameterized.expand([
        ("//form[@method='POST']",),
        ("//label[@for='grid']",),
        ("//textarea[@id='grid'][@name='grid']",),
        ("//input[@id='submit'][@name='submit'][@type='submit'][@value='Submit']",)
    ])
    def test_form_elements(self, xpath):
        self.assertTrue(self.driver.find_element(By.XPATH, xpath))
        
    def _test_time_element(self):
        textarea = self.driver.find_element(By.NAME, "grid")
        submit = self.driver.find_element(By.NAME, "submit")
        textarea.clear()
        textarea.send_keys(str([]))
        submit.click()
        time_element = self.driver.find_element(By.XPATH, "//p[@id='Solution']")
        self.assertTrue(time_element.is_displayed())
        self.assertTrue("Time: " in time_element.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
