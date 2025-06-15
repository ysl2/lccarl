import selenium
import webdriver_manager.chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def main():
    service = selenium.webdriver.ChromeService(webdriver_manager.chrome.ChromeDriverManager().install())
    options = selenium.webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = selenium.webdriver.Chrome(service=service, options=options)

    driver.get('https://www.markji.com/deck/677629bf4b4cda45377c7a6e')
    res = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@class="chapter-with-cards"]'))
    )
    with open('README1.md', 'w') as f:
        for row in res.find_elements(By.XPATH, './li'):
            row_class = row.get_attribute('class')
            row_text = row.find_element(By.XPATH, './div/span[2]').text
            if row_class == 'chapter-item':
                row_text = row_text.split('(')[0]
            f.write(f'{"##" if row_class == "chapter-item" else "###"} {row_text}\n')


if __name__ == '__main__':
    main()
