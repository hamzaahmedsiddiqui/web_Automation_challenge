# Automated UI Testing Project for Quipu   

This project automates the UI testing of the [AutomationPractice](http://www.automationpractice.pl/index.php) website using Selenium, Pytest, and Allure for reporting. It includes tests for login, product search, and adding items to the cart.

---

## Table of Contents  

- [Frameworks and Tools Used](#frameworks-and-tools-used)  
- [Setup Instructions](#setup-instructions)  
- [Test Scenarios](#test-scenarios)  
- [Known Issues](#known-issues)  
- [Reporting](#reporting)  

---

## Frameworks and Tools Used  

- **Python**: 3.x  
- **Selenium**: 4.x  
- **Pytest**: 7.x  
- **Allure-Pytest**: 2.x  
- **Webdriver Manager**: 3.x  

---

## Setup Instructions  

### Prerequisites  

- Python 3.x installed on your system.  
- pip (Python package manager).  

### Installation  

1. Install the required Python packages:  
   ```bash  
   pip install selenium pytest allure-pytest webdriver-manager
   
2.	Download and install the necessary WebDriver for your browser.
-  For Chrome:
Install ChromeDriver using WebDriver Manager:
   ```bash
   pip install webdriver-manager

### Running the Tests
1.	Clone the repository:
    ```bash
    git clone https://github.com/hamzaahmedsiddiqui/web_Automation_challenge

2.	Navigate to the project directory:
    ```bash
    cd web_Automation_challenge
3. Run the tests with Pytest:
    ```bash
     pytest --alluredir=allure-results
4. After test are completed, generatge the Allure report: 
    ```bash
     allure serve allure-results

### Test Scenarios
1. Login Test
   - Verify that the user can successfully log in with valid credentials.
	- Check for proper error messages when invalid login credentials are used.

2. Product Search Test

   - Search for a product using the search bar.
	- Verify the search results are displayed correctly.
	- Ensure that clicking on a product redirects to the product details page.

3. Add to Cart Test

   - A product, add to the cart.
	- Verify that the success message is displayed after adding a product to the cart.
	- Ensure that the cart contains the selected product.
