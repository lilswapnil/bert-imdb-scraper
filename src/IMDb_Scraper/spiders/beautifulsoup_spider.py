"""
BeautifulSoup and Requests based IMDb scraper
Alternative to Scrapy for users who prefer simpler approach
"""

import requests
from bs4 import BeautifulSoup
import time
import csv
import json
from urllib.parse import urljoin, urlparse
import re


class BeautifulSoupIMDbScraper:
    def __init__(self, delay=2):
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        })
        self.movies = []

    def get_page(self, url):
        """Fetch a page with error handling and delays"""
        try:
            print(f"Fetching: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            time.sleep(self.delay)  # Be respectful
            return response
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_movie_list(self, url):
        """Parse IMDb chart pages to get movie URLs"""
        response = self.get_page(url)
        if not response:
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        movie_links = []
        
        # Find movie links in the chart
        for link in soup.find_all('a', href=re.compile(r'/title/tt\d+')):
            href = link.get('href')
            if href and '/title/tt' in href:
                full_url = urljoin('https://www.imdb.com', href)
                movie_links.append(full_url)
        
        return list(set(movie_links))  # Remove duplicates

    def parse_movie_details(self, url):
        """Parse individual movie page for details"""
        response = self.get_page(url)
        if not response:
            return None

        soup = BeautifulSoup(response.content, 'html.parser')
        
        movie_data = {
            'title': None,
            'year': None,
            'rating': None,
            'category': None,
            'description': None,
            'url': url,
            'image_url': None
        }

        # Extract title
        title_elem = soup.find('h1')
        if title_elem:
            movie_data['title'] = title_elem.get_text(strip=True)

        # Extract year
        year_elem = soup.find('span', {'data-testid': 'hero-title-block__year'})
        if not year_elem:
            # Try to find year in any text
            year_match = re.search(r'\((\d{4})\)', soup.get_text())
            if year_match:
                movie_data['year'] = year_match.group(1)
        else:
            movie_data['year'] = year_elem.get_text(strip=True)

        # Extract rating
        rating_elem = soup.find(attrs={'data-testid': 'hero-rating-bar__aggregate-rating__score'})
        if rating_elem:
            movie_data['rating'] = rating_elem.get_text(strip=True)

        # Extract genres
        genre_links = soup.find_all('a', href=re.compile(r'/search/title\?genres='))
        if genre_links:
            genres = [link.get_text(strip=True) for link in genre_links]
            movie_data['category'] = ', '.join(genres)

        # Extract description
        desc_elem = soup.find(attrs={'data-testid': 'plot-xl'})
        if desc_elem:
            movie_data['description'] = desc_elem.get_text(strip=True)

        # Extract image URL
        img_elem = soup.find('img', {'data-testid': 'hero-media__poster'})
        if not img_elem:
            img_elem = soup.find('div', class_='poster')
            if img_elem:
                img_elem = img_elem.find('img')
        if img_elem:
            movie_data['image_url'] = img_elem.get('src')

        return movie_data

    def scrape_imdb_charts(self, max_movies=50):
        """Scrape movies from IMDb charts"""
        chart_urls = [
            "https://www.imdb.com/chart/top/",
            "https://www.imdb.com/chart/moviemeter/",
            "https://www.imdb.com/chart/boxoffice/",
        ]
        
        all_movie_urls = []
        
        # Get movie URLs from all charts
        for chart_url in chart_urls:
            print(f"Scraping chart: {chart_url}")
            movie_urls = self.parse_movie_list(chart_url)
            all_movie_urls.extend(movie_urls)
            time.sleep(self.delay)
        
        # Remove duplicates and limit
        unique_urls = list(set(all_movie_urls))[:max_movies]
        
        # Scrape individual movie details
        for i, movie_url in enumerate(unique_urls, 1):
            print(f"Scraping movie {i}/{len(unique_urls)}: {movie_url}")
            movie_data = self.parse_movie_details(movie_url)
            if movie_data and movie_data['title'] and movie_data['rating']:
                self.movies.append(movie_data)
                print(f"✓ Scraped: {movie_data['title']} ({movie_data['rating']})")
            else:
                print(f"✗ Failed to scrape: {movie_url}")
            
            time.sleep(self.delay)

    def save_to_csv(self, filename='imdb_movies.csv'):
        """Save scraped data to CSV file"""
        if not self.movies:
            print("No movies to save!")
            return
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'year', 'rating', 'category', 'description', 'url', 'image_url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.movies)
        
        print(f"Saved {len(self.movies)} movies to {filename}")

    def save_to_json(self, filename='imdb_movies.json'):
        """Save scraped data to JSON file"""
        if not self.movies:
            print("No movies to save!")
            return
        
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(self.movies, jsonfile, indent=2, ensure_ascii=False)
        
        print(f"Saved {len(self.movies)} movies to {filename}")


def main():
    """Main function to run the scraper"""
    print("🎬 Starting IMDb BeautifulSoup Scraper")
    print("=" * 50)
    
    scraper = BeautifulSoupIMDbScraper(delay=2)  # 2 second delay between requests
    
    try:
        # Scrape movies from IMDb charts
        scraper.scrape_imdb_charts(max_movies=20)  # Limit to 20 movies for testing
        
        # Save results
        if scraper.movies:
            scraper.save_to_csv('imdb_movies_beautifulsoup.csv')
            scraper.save_to_json('imdb_movies_beautifulsoup.json')
            
            print("\n🎉 Scraping completed successfully!")
            print(f"📊 Total movies scraped: {len(scraper.movies)}")
            
            # Show sample results
            print("\n📋 Sample results:")
            for i, movie in enumerate(scraper.movies[:3], 1):
                print(f"{i}. {movie['title']} ({movie['year']}) - Rating: {movie['rating']}")
        else:
            print("❌ No movies were scraped successfully")
            
    except KeyboardInterrupt:
        print("\n⏹️  Scraping interrupted by user")
    except Exception as e:
        print(f"\n❌ Error during scraping: {e}")


if __name__ == "__main__":
    main()
