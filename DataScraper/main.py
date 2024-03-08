import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import csv

def scrape_data(url, category):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    if category == "Classes":
        data = [tag.get('class') for tag in soup.find_all()]
    elif category == "Links":
        data = [link.get('href') for link in soup.find_all('a')]
    elif category == "Paragraphs":
        data = [p.text for p in soup.find_all('p')]
    elif category == "Images":
        data = [img.get('src') for img in soup.find_all('img')]
    else:
        data = []

    return data

def search():
    url = url_entry.get()
    category = category_combobox.get()

    if url:
        data = scrape_data(url, category)

        with open('scraped_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([category])
            for item in data:
                writer.writerow([item])

root = tk.Tk()
root.title("Web Scraper")

url_label = tk.Label(root, text="Enter URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

category_label = tk.Label(root, text="Select Category:")
category_label.grid(row=1, column=0, padx=5, pady=5)

categories = ["Classes", "Links", "Paragraphs", "Images"]
category_combobox = ttk.Combobox(root, values=categories)
category_combobox.grid(row=1, column=1, padx=5, pady=5)
category_combobox.current(0)

search_button = tk.Button(root, text="Search", command=search)
search_button.grid(row=2, columnspan=2, padx=5, pady=5)

root.mainloop()
