# Week 01 – Weather REST API client

Calls the OpenWeatherMap REST API, parses the JSON, stores it in a `WeatherReport`
dataclass and prints a summary. The API key lives in `.env`, never in the code.

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your key (free at https://home.openweathermap.org/api_keys)
cp .env.example .env             # Windows: copy .env.example .env
# then edit .env -> OPENWEATHER_API_KEY=your_real_key
```

New keys can take up to ~2 hours to activate (you'll get HTTP 401 until then).

## Run

```bash
python weather.py
```

## Concepts covered

| Topic | Where |
|---|---|
| venv | setup steps above |
| HTTP/REST (GET + query string) | `fetch_weather()` – `urllib.parse.urlencode` + `urlopen` |
| JSON deserialization | `json.loads()` → dict |
| OOP | `WeatherReport` dataclass, `from_json` classmethod, `summary()` |
| Secrets handling | `.env` + `python-dotenv`, `.env` in `.gitignore`, key masked in output |
| Error handling | HTTP errors (401, 404), network errors, bad JSON |
