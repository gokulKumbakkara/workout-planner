import sys
import types

# Create a dummy langchain module with required attributes
if "langchain" not in sys.modules:
    sys.modules["langchain"] = types.SimpleNamespace(
        verbose=False,
        debug=False,
        llm_cache=None
    )
else:
    import langchain
    if not hasattr(langchain, "verbose"):
        langchain.verbose = False
    if not hasattr(langchain, "debug"):
        langchain.debug = False
    if not hasattr(langchain, "llm_cache"):
        langchain.llm_cache = None

import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from settings import GROQ_API_KEY

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

# Initialize LLM
llm = ChatGroq(
    api_key=GROQ_API_KEY, model="openai/gpt-oss-20b",
    temperature=0.8,
    reasoning_format="parsed",
    max_retries=2,
)

def generate_workout_plans(muscle_group: str, no_of_sets: str = "number of sets"):
    # Prompt 1: Generate workout plan for muscle group
    prompt_workout = PromptTemplate.from_template(
        "Suggest workout plans for {muscle_group}"
    )

    # Prompt 2: Suggest sets for that workout
    prompt_sets = PromptTemplate.from_template(
        "Suggest {no_of_sets} for this workout plan: {workout_plan}"
    )

    # Chain together: (muscle_group -> workout -> sets)
    workout_chain = prompt_workout | llm
    sets_chain = prompt_sets | llm

    # First run: get workout plan
    workout_result = workout_chain.invoke({"muscle_group": muscle_group})
    workout_plan = workout_result.content

    # Second run: get number of sets based on workout
    sets_result = sets_chain.invoke(
        {"no_of_sets": no_of_sets, "workout_plan": workout_plan}
    )

    return {
        "muscle_group": muscle_group,
        "workout_plan": workout_plan,
        "no_of_sets": sets_result.content,
    }
