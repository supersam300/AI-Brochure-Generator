import os
import json
from dotenv import load_dotenv
from IPython.display import display, Markdown, update_display
from scraper import fetch_website_links, fetch_website_contents
from openai import OpenAI   

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print("API key found")
else:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

MODEL = 'gpt-5-mini'
openai  = OpenAI()


link_system_prompt= """ 
 you are provided with a list of links found on a webpage
 you are able to decide which links are most relavent to include in a brochure about the company , 
 such as links to an about page, contact page, and any other pages that you think are relevant
 you should respond in a json format with the links you think are most relavent
 in this example: 
 { 
   "links" : [ {"type": "about", "url": "https://edwarddonner.com/about" },
   {"type": "contact", "url": "https://edwarddonner.com/contact" },]
 }"""

def get_links_user(url):
    user_prompt = f"""here is a list of all the links in the website {url}, decide which links are relavent for a brochure about the company,
    respond with the full https url in json format. do not include ToS, privacy or email links.
    """

    links = fetch_website_links(url)
    user_prompt += "\n".join(links)
    return user_prompt

def find_relavent_links(url):
    print(f"selecting relavent links for {url} by calling {MODEL}")
    response = openai.chat.completions.create(model = MODEL,
     messages =[
        {"role": "system", "content": link_system_prompt},
        {"role": "user", "content": get_links_user(url)}
     ], response_format = {"type": "json_object"}
     )
    result = response.choices[0].message.content
    links = json.loads(result)
    print(f"Found {len(links)} relavent links") 
    return links

def fetch_page_and_all_relevant_links(url):
    contents = fetch_website_contents(url)
    relevant_links = find_relavent_links(url)
    result = f"## Landing Page:\n\n{contents}\n## Relevant Links:\n"
    for link in relevant_links['links']:
        result += f"\n\n### Link: {link['type']}\n"
        result += fetch_website_contents(link["url"])
    return result

def generate_brochure(url):
    brochure_system_prompt = """ you are provided with a list of relavent links and contents from a website, use them to create a brochure about the company in markdown format without code blocks.
    include the name of the company and other details about the company and the other pages in the brochure. include information about employments and any other relevant information."""
    user_prompt = f""" here is a list of relavent links and contents from a website, use them to create a brochure about the company in markdown format without code blocks.
    include the name of the company and other details about the company and the other pages in the brochure. include information about employments and any other relevant information. make it a corperate digital brochure."""
    response = openai.chat.completions.create(model = MODEL,
     messages=[
        {"role": "system", "content": brochure_system_prompt},
        {"role": "user", "content": user_prompt + fetch_page_and_all_relevant_links(url)}
     ],
     )
    result = response.choices[0].message.content
    return result

if __name__ == "__main__":
    usr_link = input("Enter the url of the website: ")
    print(generate_brochure(usr_link))
