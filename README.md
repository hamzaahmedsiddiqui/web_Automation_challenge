# Automated UI Testing Project for Quipu   

This project automates the UI testing of the [AutomationPractice](http://www.automationpractice.pl/index.php) website using Selenium, Pytest, and Allure for reporting. It includes tests for login, product search, and adding items to the cart.

---

## Table of Contents  

- [Frameworks and Tools Used](#frameworks-and-tools-used)  
- [Setup Instructions](#setup-instructions)  
- [Test Scenarios](#test-scenarios)  
- [Future Enhancements and Commitments](#Future-Enhancements)  

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

## Future Enhancements and Commitments  
Below are the key areas where I plan future enhancements to ensure comprehensive coverage and better reliability:

- **Cross-Browser Compatibility**: Ensuring that the tests run seamlessly across multiple browsers such as Chrome, Firefox, and Edge, which will enhance the overall robustness of the suite.

- **Parallel Test Execution**: Implementing parallel test execution optimizes the test run time and makes the process more efficient, especially when scaling the test suite.

- **CI/CD Pipeline Integration**: Integrating the suite with CI/CD tools like Jenkins or GitHub Actions to automate testing on every code commit, enabling faster feedback and improving code quality.

- **Data-Driven Testing**: Incorporating data-driven testing techniques using external files (CSV/JSON) to provide broader test coverage with multiple data sets.

- **Accessibility and Usability Testing**: Adding checks for web accessibility standards (WCAG) and usability considerations, making the tests more inclusive and user-centred.

- **Improved Reporting and Metrics**: Enhancing reporting by customizing Allure reports and incorporating metrics that provide actionable insights to stakeholders.

- **Mobile Responsiveness Testing**: Expanding the suite to cover mobile browsers and ensuring the site’s responsiveness is thoroughly tested using tools like Appium.

These initiatives will enhance coverage and ensure that the test suite evolves with best practices, aligns with the project's needs, and leaves a lasting positive impact.  
