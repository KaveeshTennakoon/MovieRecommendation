# Django Movie Recommender

Django Movie Recommender is a web application that recommends movies based on user preferences. It uses machine learning to analyze movie data and provide personalized recommendations to users.

## Features

- Select a movie from the dropdown menu.
- Fetches details of the selected movie from The Movie Database (TMDb) API.
- Provides recommendations based on selected movies.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/KaveeshTennakoon/MovieRecommendation.git
    ```

2. Navigate to the project directory:

    ```bash
    cd django-movie-recommender
    ```

3. Create and activate a virtual environment:

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## 5. Set up your TMDb API key:
   - Sign up for a free account on [TMDb](https://www.themoviedb.org/) to get an API key.
   - Replace `'your_tmdb_api_key'` in `recommender/views.py` with your actual TMDb API key.

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the web application in your browser at `http://127.0.0.1:8000/`.

## Usage

1. Open the web application in your browser.
2. Select a movie from the dropdown menu.
3. Get recommendations based on selected movies.

## Contributing

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
