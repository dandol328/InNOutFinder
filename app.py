#!/usr/bin/env python3
"""
Simple web interface to display In-N-Out locations.
"""

from flask import Flask, render_template, jsonify
from database import get_all_locations, get_location_count
import os


app = Flask(__name__)


@app.route('/')
def index():
    """Main page displaying all In-N-Out locations."""
    return render_template('index.html')


@app.route('/api/locations')
def api_locations():
    """API endpoint to get all locations as JSON."""
    try:
        locations = get_all_locations()
        count = get_location_count()
        return jsonify({
            'success': True,
            'count': count,
            'locations': locations
        })
    except Exception:
        return jsonify({
            'success': False,
            'error': 'Failed to retrieve locations'
        }), 500


@app.route('/api/stats')
def api_stats():
    """API endpoint for statistics."""
    try:
        locations = get_all_locations()
        
        # Count by state
        states = {}
        for loc in locations:
            state = loc['state']
            states[state] = states.get(state, 0) + 1
        
        return jsonify({
            'success': True,
            'total': len(locations),
            'by_state': states
        })
    except Exception:
        return jsonify({
            'success': False,
            'error': 'Failed to retrieve statistics'
        }), 500


if __name__ == '__main__':
    # Check if database exists
    if not os.path.exists('innout.db'):
        print("Error: Database not found. Please run:")
        print("  python scraper.py")
        print("  python database.py import")
        exit(1)
    
    print("Starting In-N-Out Finder web interface...")
    print("Open http://localhost:5000 in your browser")
    # Set debug=False for production use
    # For development, debug can be enabled via environment variable
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
