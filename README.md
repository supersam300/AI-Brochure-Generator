# Brochure Generator AI

A modern web application that uses OpenAI's GPT-4o to transform any website into a professional corporate brochure.

## Features

- **AI-Powered Analysis**: Scrapes website content and intelligently selects relevant links.
- **Automated Brochure Generation**: Creates a structured markdown brochure using GPT-4o.
- **Modern UI**: Polished, responsive frontend with glassmorphism aesthetics.
- **FastAPI Backend**: Robust Python backend serving both the API and static assets.

## Prerequisites

- Python 3.8+
- OpenAI API Key

## Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install fastapi uvicorn python-multipart requests beautifulsoup4 openai python-dotenv ipython
    ```

4.  **Set up Environment Variables**:
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_api_key_here
    ```

## Usage

1.  **Start the Server**:
    ```bash
    uvicorn app:app --reload
    ```

2.  **Access the Application**:
    Open your browser and navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

3.  **Generate a Brochure**:
    - Enter a valid URL (e.g., `https://example.com`).
    - Click **Generate Brochure**.
    - The AI will scrape the site, analyze links, and generate a brochure below.

## Project Structure

- `app.py`: FastAPI entry point and API routes.
- `main.py`: Core logic for scraping and OpenAI interaction.
- `scraper.py`: Helper functions for web scraping.
- `static/`: Frontend assets (HTML, CSS, JS).

## License

[MIT](LICENSE)
