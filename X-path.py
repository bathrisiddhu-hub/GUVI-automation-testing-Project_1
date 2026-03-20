"""
Fixed script to find correct XPaths on GUVI login page
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open GUVI
    print("Opening GUVI website...")
    driver.get("https://www.guvi.in")
    time.sleep(3)

    # Look for login button
    print("\nLooking for login button...")

    # Try to find and click login button with wait
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='login-btn']"))
        )
        print("✓ Found clickable login button with ID 'login-btn'")
        login_button.click()
        print("✓ Clicked login button")
        time.sleep(3)
    except:
        print("✗ Could not click login button with ID 'login-btn'")
        print("Trying alternative method...")
        # Try scrolling
        driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(2)
        try:
            login_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Login')] | //a[contains(text(), 'Login')]")
            if login_buttons:
                driver.execute_script("arguments[0].scrollIntoView(true);", login_buttons[0])
                time.sleep(1)
                login_buttons[0].click()
                print("✓ Clicked login button (alternative method)")
                time.sleep(3)
        except Exception as e:
            print(f"✗ Failed to click login button: {str(e)}")

    # Now find form elements
    print("\n" + "="*70)
    print("FORM ELEMENTS ON LOGIN PAGE")
    print("="*70)

    # Find all input elements
    all_inputs = driver.find_elements(By.TAG_NAME, "input")
    print(f"\nTotal INPUT elements found: {len(all_inputs)}\n")

    if len(all_inputs) > 0:
        for i, inp in enumerate(all_inputs, 1):
            inp_type = inp.get_attribute('type')
            inp_id = inp.get_attribute('id')
            inp_name = inp.get_attribute('name')
            inp_placeholder = inp.get_attribute('placeholder')
            inp_class = inp.get_attribute('class')
            inp_visible = inp.is_displayed()

            print(f"INPUT #{i}:")
            print(f"  Type: {inp_type}")
            print(f"  ID: {inp_id}")
            print(f"  Name: {inp_name}")
            print(f"  Placeholder: {inp_placeholder}")
            print(f"  Class: {inp_class}")
            print(f"  Visible: {inp_visible}")
            print()
    else:
        print("No input elements found!")

    # Find all buttons
    all_buttons = driver.find_elements(By.TAG_NAME, "button")
    print(f"\nTotal BUTTON elements found: {len(all_buttons)}\n")

    if len(all_buttons) > 0:
        for i, btn in enumerate(all_buttons, 1):
            btn_text = btn.text
            btn_id = btn.get_attribute('id')
            btn_name = btn.get_attribute('name')
            btn_type = btn.get_attribute('type')
            btn_class = btn.get_attribute('class')
            btn_visible = btn.is_displayed()

            print(f"BUTTON #{i}:")
            print(f"  Text: '{btn_text}'")
            print(f"  ID: {btn_id}")
            print(f"  Name: {btn_name}")
            print(f"  Type: {btn_type}")
            print(f"  Class: {btn_class}")
            print(f"  Visible: {btn_visible}")
            print()
    else:
        print("No button elements found!")

    # Take screenshot
    driver.save_screenshot("login_page_screenshot.png")
    print("\n✓ Screenshot saved as 'login_page_screenshot.png'")

    print("\n" + "="*70)
    print("RECOMMENDED XPATHS FOR YOUR login_page.py")
    print("="*70)

    # Email input
    email_inputs = driver.find_elements(By.XPATH, "//input[@type='email']")
    if email_inputs:
        print(f"\n✓ EMAIL INPUT XPath: //input[@type='email']")
    else:
        print("\n✗ Email input not found with //input[@type='email']")

    # Password input
    password_inputs = driver.find_elements(By.XPATH, "//input[@type='password']")
    if password_inputs:
        print(f"✓ PASSWORD INPUT XPath: //input[@type='password']")
    else:
        print("✗ Password input not found with //input[@type='password']")

    # Submit button
    submit_buttons = driver.find_elements(By.XPATH, "//button[@type='submit']")
    if submit_buttons:
        print(f"✓ SUBMIT BUTTON XPath: //button[@type='submit']")
    else:
        print("✗ Submit button not found with //button[@type='submit']")

    print("\n" + "="*70)
    print("\nWaiting 5 seconds before closing browser...")
    print("Check the screenshot and output above!")
    print("="*70)

    time.sleep(5)

except Exception as e:
    print(f"\n✗ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()

finally:
    driver.quit()
    print("\nBrowser closed.")