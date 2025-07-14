# 🧠 Reddit User Persona Generator

This project scrapes a Reddit user's posts and comments to generate a detailed User Persona using OpenAI's GPT models.

## 📌 Features
<ul>

<li>✅ Scrapes up to 50 posts and comments from any Reddit user's public profile</li>

<li>🤖 Uses OpenAI GPT-3.5/GPT-4 to analyze and generate a persona</li>

<li>📄 Outputs a text file summarizing:</li>
<ul>
<li>Interests</li>

<li>Personality traits</li>

<li>Writing style</li>

<li>Beliefs and quirks</li>

<li>📝 Cites specific posts/comments for each trait</li>
</ul>
</ul>

## 🗂️ Repository Structure

reddit-persona-assignment/
│
├── generate_persona.py          # Main script to run the pipeline <br>
├── reddit_api.py                # Reddit API client (PRAW) <br>
├── content_scraper.py           # Scrapes submissions & comments <br>
├── persona_builder.py           # Sends content to OpenAI for persona generation <br>
├── utils.py                     # File saving, utilities <br>
├── .env                         # Stores Reddit and OpenAI API keys <br>
├── output/                      # Stores generated persona text files <br>

## 🔧 Setup Instructions

### 1. Clone the repo

git clone https://github.com/yourusername/reddit-persona-assignment.git
cd reddit-persona-assignment

### 2. Install dependencies

pip install -r requirements.txt

### 3. Create a .env file
Create a .env file in the root directory:

REDDIT_CLIENT_ID=your_reddit_client_id <br>
REDDIT_CLIENT_SECRET=your_reddit_client_secret <br>
REDDIT_USER_AGENT=persona_extractor <br>
OPENAI_API_KEY=your_openai_api_key <br>

### 🧪 How to Run

python generate_persona.py <reddit_username>

Example: 
python generate_persona.py kojied

### 📁 Output
A file like output/kojied_persona.txt will be generated containing:
<ul>
<li></li>Sections like:</li>
<ul>
<li>Interests</li>

<li>Personality Traits</li>

<li>Writing Style</li>

<li>Beliefs/Values</li>
</ul>
<li>Citations: Each point references the post/comment it was derived from.</li>

</ul>

### 🛠️ Technologies Used
<ul>
<li>Python 3.10+</li>

<li>PRAW – Reddit API wrapper</li>

<li>OpenAI Python SDK</li>

<li>dotenv, tqdm</li>
</ul>

### 🚨 Notes
⚠️ Make sure you don’t exceed OpenAI free tier limits. You may get:
<ul>
<li>"You exceeded your current quota, please check your plan and billing details."</li>

<li>This script only works with public Reddit profiles.</li>
</ul>
