import sys
from reddit_api import get_reddit_instance
from citations_formatter import collect_user_content
from persona_builder import build_user_persona, save_persona_to_file


def main():
    if len(sys.argv) < 2:
        print("❌ Please provide a Reddit username. Example:")
        print("   python generate_persona.py spez")
        return

    username = sys.argv[1]
    print(f"\n🔍 Scraping Reddit profile for user: {username}")

    # Get Reddit API client
    reddit = get_reddit_instance()

    # Fetch posts and comments
    content_blocks = collect_user_content(reddit, username)
    if not content_blocks:
        print("❌ No content found for user.")
        return

    # Generate persona
    print(f"\n🧠 Generating persona for {username}...")
    persona = build_user_persona(content_blocks, username)

    # Print result
    print("\n📄 Persona Output:\n")
    print(persona)

    if "Error generating persona" not in persona:
        save_persona_to_file(username, persona)
        print("✅ Persona saved.")
    else:
        print("❌ Persona was not generated. Check your OpenAI API quota.")


    # Optionally save to file
    save_persona_to_file(username, persona)


if __name__ == "__main__":
    main()
