import openai
import os
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")  # Or hardcode it if preferred


def build_user_persona(content_blocks: List[Dict], username: str) -> str:
    """
    Generates a user persona from Reddit posts/comments using GPT-3.5.
    Includes citations for each trait.
    """
    if not openai.api_key:
        raise ValueError("❌ OpenAI API key not found.")

    print("🤖 Building persona using OpenAI GPT...")

    # Debug preview
    if not content_blocks:
        raise ValueError("❌ No content blocks found for the user.")
    
    print("✅ Previewing first content block:")
    print(type(content_blocks[0]), content_blocks[0])

    # Safely format context for the prompt
    context = "\n\n".join([
        f"[{item.get('type', 'UNKNOWN').upper()} from r/{item.get('subreddit', 'UNKNOWN')}]\n"
        f"{item.get('title', '').strip()}\n{item.get('body', '').strip()}\n(Source: {item.get('permalink', '')})"
        for item in content_blocks[:20]
        if isinstance(item, dict)
    ])

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant that analyzes Reddit users and creates detailed personas. "
                "Use the user's posts and comments to guess their interests, personality traits, writing style, values, and quirks. "
                "Structure the response with clear sections like:\n\n"
                "- Interests\n"
                "- Personality Traits\n"
                "- Writing Style\n"
                "- Beliefs and Opinions\n"
                "- Other Notable Observations\n\n"
                "For each claim, cite the specific post or comment it came from using the format (Source: [Reddit URL])."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Reddit user: u/{username}\n\n"
                f"Here are some of their posts and comments:\n\n{context}\n\n"
                "Please build a detailed user persona from this content, and cite sources for every trait you extract."
            )
        }
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=1200
        )

        return response["choices"][0]["message"]["content"]

    except openai.error.OpenAIError as e:
        print(f"❌ OpenAI API error: {e}")
        return "Error generating persona."


# Optional helper if you want to save output
def save_persona_to_file(username: str, persona_text: str, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{username}_persona.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"✅ Persona saved to {file_path}")
