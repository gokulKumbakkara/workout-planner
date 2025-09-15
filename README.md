# Workout Plan Generator

A Streamlit-based web application that generates personalized workout plans using the GROQ AI API.

## Features

- Select from various muscle groups (Chest, Shoulder, Triceps, Back, Biceps, Legs, Abs)
- AI-powered workout plan generation
- Simple and intuitive user interface

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- GROQ API key

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd workout-planner
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your GROQ API key:
     ```
     GROQ_API_KEY="your_groq_api_key_here"
     ```

## Usage

1. Start the Streamlit application:
   ```bash
   python -m streamlit run app/main.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

3. Select a muscle group from the sidebar and view your personalized workout plan

## Project Structure

```
workout-planner/
├── app/
│   ├── __init__.py
│   ├── langchain/
│   │   ├── __init__.py
│   │   └── helper.py
│   └── main.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── settings.py
```

## Dependencies

- streamlit
- python-dotenv
- langchain-groq
- langchain-core

## Configuration

All configuration is done through the `.env` file. The following environment variables are used:

- `GROQ_API_KEY`: Your GROQ API key (required)

## Troubleshooting

- If you encounter issues with environment variables, ensure the `.env` file is in the project root
- Make sure your GROQ API key is valid and has sufficient credits
- Check the terminal for any error messages when starting the application

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [GROQ AI](https://groq.com/)
- Uses [LangChain](https://www.langchain.com/) for AI integration
