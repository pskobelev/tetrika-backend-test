from unittest.mock import patch, MagicMock

from selenium.common.exceptions import NoSuchElementException

from task2.solution import scrape_animal_data


class TestScrapeAnimalData:
    @patch('task2.solution.webdriver.Chrome')
    def test_scrape_animal_data_happy_path(self, MockWebDriver):
        mock_driver = MagicMock()
        MockWebDriver.return_value = mock_driver
        mock_elem1 = MagicMock()
        mock_elem1.text = 'Медвед'
        mock_elem2 = MagicMock()
        mock_elem2.text = 'Мышь'
        mock_driver.find_elements.return_value = [mock_elem1, mock_elem2]
        mock_driver.find_element.side_effect = NoSuchElementException
        wiki_url = "https://example.com"
        result = scrape_animal_data(wiki_url)
        assert result == {'М': 2}

    @patch('task2.solution.webdriver.Chrome')
    def test_no_next_page_link(self, MockWebDriver):
        mock_driver = MagicMock()
        MockWebDriver.return_value = mock_driver
        mock_elem = MagicMock()
        mock_elem.text = 'Слон'
        mock_driver.find_elements.return_value = [mock_elem]
        mock_driver.find_element.side_effect = NoSuchElementException
        result = scrape_animal_data("http://example.com")
        assert result == {'С': 1}
