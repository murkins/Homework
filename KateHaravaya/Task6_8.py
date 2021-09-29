'''Task6_8. Implement a Pagination class helpful to arrange text on pages and list content on given page.
The class should take in a text and a positive integer which indicate how many symbols
will be allowed per each page (take spaces into account as well).
You need to be able to get the amount of whole symbols in text, get a number of pages that came out and
method that accepts the page number and return quantity of symbols on this page.
If the provided number of the page is missing print the warning message "Invalid index. Page is missing".
If you're familliar with using of Excpetions in Python display the error message in this way.
Pages indexing starts with 0. '''

import math
class Pagination:
    def __init__(self, text, symbols_per_page):
        self.text = text
        self.symbols_per_page = symbols_per_page

        # Creating array of pages
        self.pages = []
        cur_page = []
        for c in text:
            cur_page.append(c)

            if len(cur_page) == symbols_per_page:
                self.pages.append("".join(cur_page))
                cur_page = []
        if len(cur_page) > 0:
            self.pages.append("".join(cur_page))

    @property
    def item_count(self):
        return len(self.text)

    @property
    def page_count(self):
        return len(self.pages)

    def count_items_on_page(self, page_index):
        if page_index < len(self.pages) and page_index >= 0:
            return len(self.pages[page_index])
        else:
            raise RuntimeError (f"Exception: Invalid index. Page is missing")


    def find_page(self, search_str):
        # Finding search_str start positions in text
        found_starts = []
        for i in range(len(self.text) - len(search_str) + 1):
            start_pos = self.text.find(search_str, i)

            if start_pos != -1:
                if len(found_starts) == 0:
                    found_starts.append(start_pos)
                elif found_starts and found_starts[-1] != start_pos:
                    found_starts.append(start_pos)

        # Finding page indices for each find
        result_indices = []
        for start_pos in found_starts:
            end_pos = start_pos + len(search_str) - 1

            start_page_index = start_pos // self.symbols_per_page
            end_page_index = end_pos // self.symbols_per_page

            for page_index in range(start_page_index, end_page_index + 1):
                if page_index not in result_indices:
                    result_indices.append(page_index)

        if len(result_indices) == 0:
            raise RuntimeError(f"Exception: '{search_str}' is missing on the pages")
        else:
            return result_indices

    def display_page(self, page_index):
        if page_index < len(self.pages) and page_index >= 0:
            print(self.pages[page_index])
        else:
            print("Invalid index. Page is missing")

pages = Pagination("Your beautiful text", 5)

print(pages.item_count)
print(pages.page_count)

try:
    print(pages.count_items_on_page(0))
    print(pages.count_items_on_page(3))
    print(pages.count_items_on_page(4))
except RuntimeError as e:
    print(e)

try:
    print(pages.find_page('Your'))
    print(pages.find_page('e'))
    print(pages.find_page('beautiful'))
    print(pages.find_page('great'))
except RuntimeError as e:
    print(e)

print(pages.display_page(0))
