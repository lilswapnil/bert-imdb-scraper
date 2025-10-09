import scrapy
from IMDb_Scraper.items import ImdbScraperItem
import re


class ImdbspiderSpider(scrapy.Spider):
    name = "imdbspider"
    allowed_domains = ["imdb.com"]
    
    def start_requests(self):
        # Start with IMDb's top movies page instead of homepage
        urls = [
            "https://www.imdb.com/chart/top/",
            "https://www.imdb.com/chart/moviemeter/",
            "https://www.imdb.com/chart/boxoffice/",
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_movie_list)

    def parse_movie_list(self, response):
        """Parse the movie list pages to extract individual movie URLs"""
        self.logger.info(f"Parsing movie list: {response.url}")
        
        # Extract movie URLs from the chart pages
        movie_links = response.css('a[href*="/title/tt"]::attr(href)').getall()
        
        for link in movie_links[:10]:  # Limit to first 10 movies for testing
            if link:
                # Clean the URL by removing query parameters
                clean_link = link.split('?')[0] if '?' in link else link
                movie_url = response.urljoin(clean_link)
                yield scrapy.Request(url=movie_url, callback=self.parse_movie_details)
        
        # Follow pagination if available
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_movie_list)

    def parse_movie_details(self, response):
        """Parse individual movie pages to extract detailed information"""
        self.logger.info(f"Parsing movie details: {response.url}")
        
        item = ImdbScraperItem()
        
        # Extract movie title
        title = response.css('h1::text').get()
        item['title'] = title.strip() if title else None
        
        # Extract year - look for year in various places
        year = response.css('span[data-testid="hero-title-block__year"]::text').get()
        if not year:
            # Try to extract year from title or other elements
            year_text = response.css('*::text').re_first(r'\((\d{4})\)')
            if year_text:
                year = year_text
        item['year'] = year.strip() if year else None
        
        # Extract rating
        rating = response.css('[data-testid="hero-rating-bar__aggregate-rating__score"]::text').get()
        item['rating'] = rating.strip() if rating else None
        
        # Extract genre - look for genre links
        genres = response.css('a[href*="genre"]::text').getall()
        if not genres:
            # Try alternative genre selectors
            genres = response.css('div[data-testid="genres"] a::text').getall()
        item['category'] = ', '.join(genres) if genres else None
        
        # Extract description/overview
        description = response.css('[data-testid="plot-xl"]::text').get()
        if not description:
            description = response.css('span[data-testid="plot-xl"]::text').get()
        item['description'] = description.strip() if description else None
        
        # Extract URL
        item['url'] = response.url
        
        # Extract image URL
        image_url = response.css('img[data-testid="hero-media__poster"]::attr(src)').get()
        if not image_url:
            image_url = response.css('div.poster img::attr(src)').get()
        item['image_url'] = image_url
        
        # Only yield item if we have at least title and rating
        if item['title'] and item['rating']:
            yield item
        else:
            self.logger.warning(f"Incomplete data for {response.url}: title={item['title']}, rating={item['rating']}")
