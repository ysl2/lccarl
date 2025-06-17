import json

import requests
import selenium
import webdriver_manager.chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tqdm.auto import tqdm


def main():
    service = selenium.webdriver.ChromeService(webdriver_manager.chrome.ChromeDriverManager().install())
    options = selenium.webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = selenium.webdriver.Chrome(service=service, options=options)

    driver.get('https://www.markji.com/deck/677629bf4b4cda45377c7a6e')
    chapter_with_cards = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@class="chapter-with-cards"]'))
    )
    with open('README1.md', 'w') as f:
        for row in tqdm(chapter_with_cards.find_elements(By.XPATH, './li')):
            row_class = row.get_attribute('class')
            row_text = row.find_element(By.XPATH, './div/span[2]').text
            if row_class == 'chapter-item':
                row_text = row_text.split('(')[0]
            else:
                row_idstr = row_text.split('.')[0]
                # NOTE: git clone git@github.com:ysl2/leetcode-api.git
                row_engurl = requests.get(f'http://127.0.0.1:8000/problem/{row_idstr}').text
                row_engurl = json.loads(row_engurl)
                row_engurl = row_engurl['url']
                row_engtitle = row_engurl.split('/')[-2]
                row_cnurl = f'https://leetcode.cn/problems/{row_engtitle}/description'

                main_window = driver.current_window_handle

                driver.execute_script('window.open("about:blank", "_blank");')
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(row_cnurl)
                row_cntitle = (
                    WebDriverWait(driver, 10)
                    .until(EC.presence_of_element_located((By.XPATH, f'//*[@href="/problems/{row_engtitle}/"]')))
                    .text
                )
                if row_text.split(' | ')[0] == row_cntitle:
                    row_text = f'[{row_text}]({row_cnurl})'
                driver.close()

                driver.switch_to.window(main_window)
            f.write(f'{"##" if row_class == "chapter-item" else "###"} {row_text}\n')
    driver.quit()


if __name__ == '__main__':
    main()
