# =========================
# Few-shot examples for LLM1
# =========================
EXAMPLES = [
    {
        "input": "What cocktails taste similar to a margarita?",
        "task_type": "Recommend",
        "attributes": '{"taste": "sour, citrusy, slightly sweet, refreshing", "alcohol_level": "medium", "ingredients": ["tequila", "lime juice", "triple sec", "salt (for rim)"]}'
    },
    {
        "input": "Can you suggest cocktails with a flavor profile similar to an Old Fashioned?",
        "task_type": "Recommend",
        "attributes": '{"taste": "bitter-sweet, rich, slightly smoky, aromatic", "alcohol_level": "high", "ingredients": ["bourbon or rye whiskey", "sugar cube", "Angostura bitters", "orange peel"]}'
    },

]

# =========================
# LLM1 Prompt Template
# =========================
def get_task_prompt(user_query: str) -> str:
    """
    Generate a prompt for LLM1 to classify task type and extract cocktail attributes.

    Args:
        user_query: user input string

    Returns:
        str: prompt for LLM1
    """
    examples_text = "\n".join(
        [f"Input: {ex['input']}\nTask: {ex['task_type']}\nAttributes: {ex['attributes']}" 
         for ex in EXAMPLES]
    )

    prompt = f"""
You are a cocktail assistant LLM.
Given a user query, do the following tasks:
1. Classify the task type: Recommend / Description / Classification
2. Extract cocktail attributes (taste, alcohol_level, ingredients, etc.)
3. Prepare information for Graph Query generation (do not generate the full query here)

Output strictly in JSON format with keys: "task_type", "attributes"

Examples:
{examples_text}

Now, process this user query:
"{user_query}"
"""
    return prompt

# =========================
# LLM2 Prompt Template
# =========================
RESPONSE_PROMPT = """
You are a cocktail assistant LLM.

User query: "{query}"
Attributes: "{attributes}"
Search results: "{search_results}"

Based on the above information, generate a clear and concise final recommendation or explanation text.
"""
