# InNOutFinder

A Python-based project that scrapes In-N-Out Burger locations and displays them through a simple web interface.

## Features

- **Scraper**: Collects In-N-Out location data (latitude, longitude, city, state)
- **Database**: Stores locations in a SQLite database
- **Web Interface**: Simple Flask-based UI to view and filter locations

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the scraper to collect location data:
```bash
python scraper.py
```

3. Import data into the database:
```bash
python database.py import
```

4. Start the web server:
```bash
python app.py
```

5. Open your browser to `http://localhost:5000`

## Project Structure

- `scraper.py` - Scrapes In-N-Out location data
- `database.py` - Database initialization and management
- `app.py` - Flask web application
- `templates/index.html` - Web interface
- `innout.db` - SQLite database (created after import)
- `innout_locations.json` - Raw location data (created by scraper)

## Usage

### Scraping Locations
```bash
python scraper.py
```

### Database Operations
```bash
python database.py init      # Create database only
python database.py import    # Create and import data
```

### Running the Web Interface
```bash
python app.py
```

The web interface provides:
- List of all In-N-Out locations
- Filter by state
- Search by city
- Statistics (total locations, states covered)

## Note

The current implementation includes sample location data. For production use with all ~424 actual In-N-Out locations, you would need to implement one of these approaches:

1. Use Google Maps Places API
2. Web scrape from In-N-Out's official location finder
3. Use another mapping service API

## Technologies Used

- Python 3
- Flask (web framework)
- SQLite (database)
- BeautifulSoup4 (web scraping)
- Requests (HTTP library)
