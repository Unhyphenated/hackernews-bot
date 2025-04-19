# HackerNews Article Summarization Bot

An automated system that fetches and summarizes top HackerNews articles using LangChain and GPT-3.5-turbo. Articles are stored in ChromaDB and summaries are delivered via email every 3 days.

## Features

- Fetches top 3 HackerNews articles every 3 days
- Generates concise summaries using LangChain and GPT-3.5-turbo
- Stores articles and summaries in ChromaDB
- Automated email delivery of summaries
- AWS-based automation (coming soon)

## Project Structure

```
hackernews-bot/
├── src/
│   ├── scrapers/
│   │   └── hackernews.py      # HackerNews API client
│   ├── summarizer/
│   │   └── langchain_sum.py   # LangChain summarization
│   ├── database/
│   │   └── chroma_client.py   # ChromaDB operations
│   ├── email/
│   │   └── ses_sender.py      # AWS SES email (coming soon)
│   └── lambda_handlers/       # AWS Lambda functions (coming soon)
├── terraform/                 # Infrastructure as Code (coming soon)
└── tests/                    # Test suite (coming soon)
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hackernews-bot.git
cd hackernews-bot
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a .env file with your configuration:
```env
OPENAI_API_KEY=your_openai_api_key
```

## Local Development

1. Test the HackerNews scraper:
```bash
python src/scrapers/hackernews.py
```

2. Test the summarizer:
```bash
python src/summarizer/langchain_sum.py
```

3. Test the ChromaDB integration:
```bash
python src/database/chroma_client.py
```

## AWS Deployment (Coming Soon)

The project will use:
- AWS Lambda for serverless execution
- EventBridge for scheduling
- SES for email delivery
- Terraform for infrastructure management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
