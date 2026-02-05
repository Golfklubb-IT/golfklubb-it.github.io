#!/usr/bin/env python3
"""
Golfklubb-IT GitHub Pages Index Generator
Automatically discovers and lists all active GitHub Pages in the organization.
"""

import os
import sys
import requests
from datetime import datetime
from typing import List, Dict, Optional

# Configuration
ORG_NAME = "Golfklubb-IT"
GITHUB_API_URL = f"https://api.github.com/orgs/{ORG_NAME}/repos"
PAGES_BASE_URL = f"https://golfklubb-it.github.io"
TIMEOUT = 10  # seconds

def get_github_token() -> Optional[str]:
    """Get GitHub token from environment."""
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("Warning: GITHUB_TOKEN not found in environment", file=sys.stderr)
    return token

def fetch_repositories(token: Optional[str]) -> List[Dict]:
    """Fetch all repositories from the organization."""
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'Golfklubb-IT-Pages-Index'
    }
    
    if token:
        headers['Authorization'] = f'token {token}'
    
    try:
        print(f"Fetching repositories from {ORG_NAME}...")
        response = requests.get(GITHUB_API_URL, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()
        repos = response.json()
        print(f"Found {len(repos)} repositories")
        return repos
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}", file=sys.stderr)
        return []

def check_pages_url(repo_name: str) -> bool:
    """Check if a GitHub Pages URL is active."""
    # Skip the main organization page itself
    if repo_name == f"{ORG_NAME}.github.io".lower():
        return False
    
    url = f"{PAGES_BASE_URL}/{repo_name}/"
    
    try:
        response = requests.get(url, timeout=TIMEOUT, allow_redirects=True)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def find_active_pages(repos: List[Dict]) -> List[Dict]:
    """Find all repositories with active GitHub Pages."""
    active_pages = []
    
    for repo in repos:
        repo_name = repo['name']
        print(f"Checking {repo_name}...", end=" ")
        
        if check_pages_url(repo_name):
            print("✓ Active")
            active_pages.append({
                'name': repo_name,
                'description': repo.get('description') or 'Ingen beskrivelse tilgjengelig',
                'url': f"{PAGES_BASE_URL}/{repo_name}/",
                'html_url': repo['html_url']
            })
        else:
            print("✗ Not active")
    
    print(f"\nFound {len(active_pages)} active GitHub Pages")
    return active_pages

def generate_html(active_pages: List[Dict]) -> str:
    """Generate the HTML page."""
    now = datetime.utcnow()
    timestamp = now.strftime("%d.%m.%Y kl. %H:%M UTC")
    
    # Build the pages list HTML
    if active_pages:
        pages_html = ""
        for page in sorted(active_pages, key=lambda x: x['name'].lower()):
            pages_html += f"""
            <div class="page-card">
                <div class="card-header">
                    <h2>{page['name']}</h2>
                    <a href="{page['html_url']}" class="github-link" target="_blank" rel="noopener">
                        <svg width="20" height="20" viewBox="0 0 16 16" fill="currentColor">
                            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
                        </svg>
                    </a>
                </div>
                <p class="description">{page['description']}</p>
                <a href="{page['url']}" class="visit-button" target="_blank" rel="noopener">Besøk side →</a>
            </div>
"""
    else:
        pages_html = """
            <div class="no-pages">
                <p>Ingen aktive GitHub Pages funnet i organisasjonen.</p>
                <p>For å aktivere GitHub Pages for et repository, gå til Settings → Pages i det aktuelle repository.</p>
            </div>
"""
    
    html = f"""<!DOCTYPE html>
<html lang="no">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Golfklubb-IT GitHub Pages Oversikt</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #e8f5e9 100%);
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        header {{
            background: linear-gradient(135deg, #2d5016 0%, #3d7021 100%);
            color: white;
            padding: 40px 20px;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        
        header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 700;
        }}
        
        header .subtitle {{
            font-size: 1.2em;
            opacity: 0.95;
            font-weight: 300;
        }}
        
        .golf-icon {{
            font-size: 3em;
            margin-bottom: 10px;
        }}
        
        .intro {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        
        .intro p {{
            margin-bottom: 10px;
            color: #555;
        }}
        
        .pages-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }}
        
        .page-card {{
            background: white;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            border-left: 4px solid #2d5016;
        }}
        
        .page-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 4px 16px rgba(45, 80, 22, 0.2);
        }}
        
        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }}
        
        .page-card h2 {{
            color: #2d5016;
            font-size: 1.5em;
            font-weight: 600;
        }}
        
        .github-link {{
            color: #666;
            transition: color 0.3s ease;
        }}
        
        .github-link:hover {{
            color: #2d5016;
        }}
        
        .description {{
            color: #666;
            margin-bottom: 20px;
            line-height: 1.5;
        }}
        
        .visit-button {{
            display: inline-block;
            background: #2d5016;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            transition: all 0.3s ease;
            font-weight: 500;
        }}
        
        .visit-button:hover {{
            background: #3d7021;
            transform: translateX(5px);
        }}
        
        .no-pages {{
            background: white;
            padding: 40px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        
        .no-pages p {{
            color: #666;
            margin-bottom: 10px;
        }}
        
        footer {{
            background: white;
            padding: 25px;
            text-align: center;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            color: #666;
        }}
        
        footer p {{
            margin-bottom: 8px;
        }}
        
        footer a {{
            color: #2d5016;
            text-decoration: none;
            font-weight: 500;
        }}
        
        footer a:hover {{
            text-decoration: underline;
        }}
        
        .update-time {{
            font-size: 0.9em;
            color: #999;
        }}
        
        @media (max-width: 768px) {{
            header h1 {{
                font-size: 1.8em;
            }}
            
            header .subtitle {{
                font-size: 1em;
            }}
            
            .pages-grid {{
                grid-template-columns: 1fr;
            }}
            
            .container {{
                padding: 10px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="golf-icon">🏌️</div>
            <h1>Golfklubb-IT GitHub Pages Oversikt</h1>
            <p class="subtitle">Automatisk oppdatert portal for alle våre nettsider</p>
        </header>
        
        <div class="intro">
            <p><strong>Velkommen til Golfklubb-IT sin GitHub Pages portal!</strong></p>
            <p>Denne siden viser en automatisk generert oversikt over alle aktive GitHub Pages i vår organisasjon. 
            Siden oppdateres automatisk hver dag for å sikre at informasjonen alltid er ajour.</p>
        </div>
        
        <div class="pages-grid">
{pages_html}
        </div>
        
        <footer>
            <p><strong>Sist oppdatert:</strong> <span class="update-time">{timestamp}</span></p>
            <p>Automatisk generert av <a href="https://github.com/Golfklubb-IT/golfklubb-it.github.io/actions">GitHub Actions</a></p>
            <p><a href="https://github.com/Golfklubb-IT" target="_blank" rel="noopener">← Tilbake til Golfklubb-IT på GitHub</a></p>
        </footer>
    </div>
</body>
</html>
"""
    return html

def main():
    """Main function."""
    print("=" * 60)
    print("Golfklubb-IT GitHub Pages Index Generator")
    print("=" * 60)
    
    # Get GitHub token
    token = get_github_token()
    
    # Fetch repositories
    repos = fetch_repositories(token)
    if not repos:
        print("No repositories found or error occurred", file=sys.stderr)
        # Generate empty page
        html = generate_html([])
    else:
        # Find active pages
        active_pages = find_active_pages(repos)
        
        # Generate HTML
        html = generate_html(active_pages)
    
    # Write to index.html
    output_file = "index.html"
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"\n✓ Generated {output_file} successfully")
    except IOError as e:
        print(f"Error writing to {output_file}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
