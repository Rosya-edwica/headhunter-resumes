import unittest

from module.headhunter.tools import create_query, get_count_of_resumes, get_soup, get_count_of_pages


class HeadHunterTest(unittest.TestCase):
    def test_create_query(self):
        self.assertEqual(create_query("программист 1с", 1), 
                        "https://hh.ru/search/resume?area=1&pos=position&text=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82+1%D1%81&no_magic=False&order_by=relevance&exp_period=all_time&logic=normal&search_period=0&items_on_page=20")
        self.assertEqual(create_query("manager", 113), 
                         "https://hh.ru/search/resume?area=113&pos=position&text=manager&no_magic=False&order_by=relevance&exp_period=all_time&logic=normal&search_period=0&items_on_page=20")
    
    

if __name__ == "__main__":
    unittest.main()