from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Инициализация драйвера
chrome_options = Options()
chrome_options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(options=chrome_options)

# авторизация и открытие главной страницы
driver.get('https://allure.x5.ru/project/123/test-cases?treeId=419')
driver.implicitly_wait(10)
login_field = driver.find_element('name', 'username')
login_field.click()
login_field.send_keys('Ariadna.Kraynova')
password_field = driver.find_element('name', 'password')

password_field.click()
password_field.send_keys('Asdasd12345!')
button = driver.find_element('xpath', '//button')
button.click()
driver.implicitly_wait(10)

class MainPage:
    def browser_navigation(self):
        driver.get('https://allure.x5.ru/project/123/test-cases?treeId=419')
        driver.implicitly_wait(10)

        # Вернуться на главную страницу при помощи встроенных инструментов навигации браузера
        driver.execute_script("window.history.go(-1)")

    def check_url(self):
        url = driver.current_url
        assert '/test-cases' in url

class CaseListPage():
    test_case_list_view_features = By.XPATH, "//span[text()='Features']"
    test_case_list_view_folder = By.XPATH, "//ul[@class = 'LoadableTree__view']//li[last()-1]//div[@class = 'GroupIcon']//*[@class='Icon Icon_size_tiny ']"
    case_display_switch = By.XPATH, "//div[@class = 'LoadableTreeViewToggle__arrow']//*[@class = 'Icon Icon_size_small angle angle-down Arrow Arrow_expanded_bottom ']"
    name_test_cases_test_cases = By.XPATH, "//span[text()='Test cases']"
    list_test_cases_no_folder = By.XPATH, "//ul[@class = 'LoadableTree__view']//li[last()-1]//div[@class = 'GroupIcon']//*[@class='Icon Icon_size_tiny ']"
    sort_by_id = By.XPATH, "//div[text()='Id']"
    sort_by_id_active = By.XPATH, "//div[@class = 'LoadableTreeControlPanel__main']//div[last()-3]//*[@class = 'Icon Icon_size_tiny SorterIcon SorterIcon_enabled SorterIcon_rotate']"

    def find_xpath(self, test_case_list_view_features):
        pass

    def check_exists_features(self):
        try:
            self.find_xpath(self.test_case_list_view_features)
        except NoSuchElementException:
            return False
        return True

    def check_exists_folders(self):
        try:
            self.find_xpath(self.test_case_list_view_folder)
        except NoSuchElementException:
            return False
        return True

    def test_case_list_view_test_cases(self):
        case_display_switch_1 = self.find_xpath(self.case_display_switch)
        case_display_switch_1.click()

    def check_name_list_test_cases_test_cases(self):
        try:
            self.find_xpath(self.name_test_cases_test_cases)
        except NoSuchElementException:
            return False
        return True

    def check_exists_no_folders(self):
        try:
            self.find_xpath(self.list_test_cases_no_folder)
        except NoSuchElementException:
            return False
        return True

    def check_exists_sort_by_id(self):
        driver.implicitly_wait(10)
        sort_by_id_1 = self.find_xpath(self.sort_by_id)
        sort_by_id_1.click()

        try:
            self.find_xpath(self.sort_by_id_active)
        except NoSuchElementException:
            return False
        return True

class CaseViewPage():
    ermolow_ed = '//*[text()="Ермолов Эд"]'
    name_test_case = '//*[@class = "LoadableTreeGroupView__children"]//*[@class = "TreeNodeName"]'
    id_test_case = '//*[text()="88531"]'
    name_test_case_1 = '//*[text()="02 Столбцы с модулем"]'
    description_test_case = '//*[text()="Description"]'
    precondition_test_case = "//*[text()='Precondition']"
    scenario_test_case = "//*[text()='Scenario']"

    def check_name_and_id_testcase(self):
        ermolow_ed_1 = self.find_xpath(self.ermolow_ed)
        ermolow_ed_1.click()

        name_test_case_1 = self.find_xpath(self.name_test_case)
        name_test_case_1.click()

        try:
            self.find_xpath(self.id_test_case) and self.find_xpath(self.name_test_case_1)
        except NoSuchElementException:
            return False
        return True

    def check_blocks_in_testcase(self):
        test_case_03 = self.find_xpath(self.name_test_case_1)
        test_case_03.click()

        try:
            self.find_xpath(self.description_test_case) and self.find_xpath(self.precondition_test_case) and self.find_xpath(self.scenario_test_case)
        except NoSuchElementException:
            return False
        return True

input('Press ENTER to exit')
