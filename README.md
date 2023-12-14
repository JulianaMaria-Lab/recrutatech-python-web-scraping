# Recrutatech Python Web Scraping

This project includes web scraping scripts to extract information from a website and perform matching with job profiles.

## Project Structure

- `web_scraping/`: Folder containing web scraping scripts.
- `match_rank.ipynb`: Jupyter Notebook for ranking and matching.
- `raspagem_candidatos.py`: Python script for candidate scraping.

### web_scraping/app.js

A simple Express.js application serving an HTML page at http://localhost:8000. The HTML page displays candidate information.

### raspagem_candidatos.py

A Python script that performs web scraping on the candidate information displayed on http://localhost:8000.

### match_rank.ipynb

A Jupyter Notebook that uses the TF-IDF algorithm for ranking and matching candidates based on their resumes.

## How to Run

1. Install the required Python packages:

 ```bash
pip install flask requests beautifulsoup4 pandas scikit-learn nltk
   
```

2. Run the Flask application:

`py raspagem_candidatos.py`

The application will be available at http://localhost:7000.

3. Run the Jupyter Notebook match_rank.ipynb using a Jupyter environment.

## Usage

### Candidate Scraping

Send a POST request to http://localhost:7000/scraping with a JSON body containing the candidate's information:

```bash
{
  "cargo": "desired_job_title",
  "conhecimentos": ["skill1", "skill2"],
  "habilidades": ["ability1", "ability2"],
  "atitudes": ["attitude1", "attitude2"],
  "filtro": 50
}
```

The script will match the candidate's skills, abilities, and attitudes with the available job profiles and return the top matches. Additionally, you can fine-tune the results using percentage filters:

- Minimum Filter:
Send a POST request to http://localhost:7000/scraping/filtroMin with a JSON body containing the candidate's information and a minimum percentage filter (filtro).

- Maximum Filter:
Send a POST request to http://localhost:7000/scraping/filtroMax with a JSON body containing the candidate's information and a maximum percentage filter (filtro).
