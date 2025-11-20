"""
Sample Generated Test Script - Discount Code Validation
Test Case: TC-001
Feature: Discount Code
Scenario: Apply valid discount code SAVE15
Expected Result: Total price is reduced by 15%
Grounded In: product_specs.md, business_requirements.md
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestTC_001:
    def __init__(self):
        self.driver = None
        self.wait = None
    
    def setup(self):
        """Setup Chrome driver and navigate to checkout page"""
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Remove for visible browser
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        
        # Navigate to checkout page (update path as needed)
        checkout_path = "file://" + os.path.abspath("assets/checkout.html")
        self.driver.get(checkout_path)
        time.sleep(2)
    
    def test_valid_discount_code(self):
        """Test applying valid discount code SAVE15"""
        try:
            # Add items to cart first
            add_to_cart_btn = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick*='addToCart']")))
            add_to_cart_btn.click()
            time.sleep(1)
            
            # Get original total
            total_element = self.driver.find_element(By.CSS_SELECTOR, "#total")
            original_total_text = total_element.text.replace('Total: $', '').replace(',', '')
            original_total = float(original_total_text)
            
            # Apply discount code
            discount_field = self.driver.find_element(By.CSS_SELECTOR, "#discountCode")
            discount_field.clear()
            discount_field.send_keys("SAVE15")
            
            apply_button = self.driver.find_element(By.CSS_SELECTOR, "#applyDiscount")
            apply_button.click()
            time.sleep(2)
            
            # Verify discount applied (15% off)
            new_total_text = total_element.text.replace('Total: $', '').replace(',', '')
            new_total = float(new_total_text)
            expected_total = original_total * 0.85  # 15% discount
            
            assert abs(new_total - expected_total) < 0.01, f"Expected {expected_total}, got {new_total}"
            print("✓ Valid discount code test passed")
            
        except Exception as e:
            print(f"✗ Valid discount code test failed: {e}")
            raise
    
    def test_invalid_discount_code(self):
        """Test applying invalid discount code"""
        try:
            # Apply invalid discount code
            discount_field = self.driver.find_element(By.CSS_SELECTOR, "#discountCode")
            discount_field.clear()
            discount_field.send_keys("INVALID")
            
            apply_button = self.driver.find_element(By.CSS_SELECTOR, "#applyDiscount")
            apply_button.click()
            time.sleep(2)
            
            # Verify error message appears
            error_element = self.driver.find_element(By.CSS_SELECTOR, "#discountError")
            assert error_element.is_displayed(), "No error message displayed for invalid discount code"
            
            # Verify error message text
            assert "Invalid discount code" in error_element.text, "Incorrect error message"
            
            print("✓ Invalid discount code test passed")
            
        except Exception as e:
            print(f"✗ Invalid discount code test failed: {e}")
            raise
    
    def teardown(self):
        """Clean up and close browser"""
        if self.driver:
            self.driver.quit()
    
    def run_test(self):
        """Run the complete test"""
        try:
            self.setup()
            
            # Run all test methods
            print("Running test_valid_discount_code...")
            self.test_valid_discount_code()
            
            print("Running test_invalid_discount_code...")
            self.test_invalid_discount_code()
            
            print("\n✓ All tests completed successfully!")
            
        except Exception as e:
            print(f"\n✗ Test execution failed: {e}")
        finally:
            self.teardown()

# Run the test
if __name__ == "__main__":
    import os
    test = TestTC_001()
    test.run_test()