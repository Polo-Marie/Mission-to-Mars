# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemisphere_photos(browser),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    #Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    #Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


# ### JPL Space Featured Images

def featured_image(browser):

    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    
    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url


# ### Mars Facts

def mars_facts():
    try:
        # Use 'read_html" to scrape a website's table with Pandas as a DataFrame
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
        
    except BaseException:
        return None

    # Assign columns and set index of DataFrame   
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")



# ### Mars Hemispheres

def mars_hemispheres(browser):

# Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    #Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    #Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p



def hemisphere_photos(browser):
    # Visit url
    url = 'https://marshemispheres.com/'
    browser.visit(url)

     # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        img_url = img_soup.find('div', class_='collapsible results')
        items = img_url.find_all('div', class_='item')

        hemisphere_image_urls = []

        for item in items:
        
            # 2. Create a list to hold the images and titles - Not needed.
            
            # 3. Write code to retrieve the image urls and titles for each hemisphere.
            # Get links
            hemisphere_url = item.find('a').get('href')
            # print(img_url)
            
            hemispheres = f'https://marshemispheres.com/{hemisphere_url}'
                
            # Visit each link in browser
            browser.visit(hemispheres)
            html = browser.html 
            img_soup = soup(html, 'html.parser')
                
            # Get title
            img_title = img_soup.find('div', class_='cover')
            img_title_hemisphere = img_title.find('h2').text
            #print(img_title_hemisphere)
            
            img_full = img_soup.find('div',class_='downloads')
            #print(img_full)
            img_full_hemisphere = img_full.find('a').get('href')
            #print(img_full_hemisphere)
                
            #Obtain photo link
            hemisphere_url = f'https://marshemispheres.com/{img_full_hemisphere}'
            #print(hemisphere_url)
            
            #print("img_url: " + hemisphere_url, "title: " + img_title_hemisphere)
            
            # 4. Print the list that holds the dictionary of each image url and title.
            
            hemisphere_image_urls.append({"img_url": hemisphere_url, "title": img_title_hemisphere})
            
            browser.back()
        browser.quit()
    
    except AttributeError:
        return None, None

    return hemisphere_image_urls        


if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())

