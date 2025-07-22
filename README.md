# AI Agent Chatbot 🤖

A full-stack AI chatbot application with web interface that integrates multiple AI models (Groq and OpenAI) with web search capabilities using Tavily. Built with FastAPI backend and Streamlit frontend.

## 🌟 Features

- **Multiple AI Providers**: Support for Groq (LLaMA models) and OpenAI (GPT models)
- **Web Search Integration**: Optional Tavily search for real-time information
- **Interactive Web UI**: Clean Streamlit interface for easy interaction
- **RESTful API**: FastAPI backend for scalable deployment
- **Model Selection**: Choose from various models including LLaMA 3.3 70B, GPT-4o-mini, and Mixtral
- **Custom System Prompts**: Define AI agent behavior with custom instructions
- **Real-time Processing**: Fast response generation with optimized inference

## 🏗️ Project Structure

```
AI-Agent-Chatbot/
├── ai_agent.py      # Core AI agent logic with LangGraph
├── backend.py       # FastAPI server and API endpoints
├── frontend.py      # Streamlit web interface
├── README.md        # Project documentation
├── .env            # Environment variables (create from .env.example)
└── requirements.txt # Python dependencies
```

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/nishant0820/AI-Agent-Chatbot.git
cd AI-Agent-Chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install manually:
```bash
pip install streamlit fastapi uvicorn langchain-groq langchain-openai langchain-community langgraph python-dotenv pydantic requests
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

**Get your API keys:**
- **Groq**: https://console.groq.com/keys (Free tier available)
- **Tavily**: https://tavily.com/ (Free tier: 1000 searches/month)
- **OpenAI**: https://platform.openai.com/api-keys (Pay-per-use)

### 4. Run the Application

**Start the Backend Server:**
```bash
python backend.py
```
The API will be available at `http://127.0.0.1:8000`

**Start the Frontend (in a new terminal):**
```bash
streamlit run frontend.py
```
The web interface will open at `http://localhost:8501`

## 📚 API Documentation

### Endpoint: `POST /chat`

Send a chat request to the AI agent.

**Request Body:**
```json
{
    "model_name": "llama-3.3-70b-versatile",
    "model_provider": "Groq",
    "system_prompt": "You are a helpful AI assistant",
    "messages": ["What is the weather like today?"],
    "allow_search": true
}
```

**Response:**
```json
"The AI agent's response text here..."
```

**Available Models:**
- **Groq**: `llama-3.3-70b-versatile`, `llama-3.3-70b-8192`, `mixtral-8x7b-32768`
- **OpenAI**: `gpt-4o-mini`

## 🧩 Component Details

### `ai_agent.py` - Core AI Logic
- Implements the main AI agent using LangGraph
- Handles model initialization for both Groq and OpenAI
- Manages web search integration with Tavily
- Processes queries and returns responses

### `backend.py` - FastAPI Server
- RESTful API server handling chat requests
- Input validation with Pydantic models
- Model selection and provider routing
- Error handling for invalid requests

### `frontend.py` - Streamlit Interface
- Interactive web UI for the chatbot
- Model and provider selection
- System prompt customization
- Real-time chat interface

## 🔧 Configuration

### Model Providers

**Groq Models:**
- `llama-3.3-70b-versatile`: Best for general tasks
- `llama-3.3-70b-8192`: Extended context window
- `mixtral-8x7b-32768`: Fast mixture of experts model

**OpenAI Models:**
- `gpt-4o-mini`: Cost-effective GPT-4 variant

### System Prompts
Customize AI behavior by defining system prompts in the frontend:
```
You are a helpful AI assistant specialized in [domain].
Always provide accurate, concise, and well-structured responses.
```

### Web Search
Enable/disable web search to allow the AI to access real-time information for current events, recent data, or fact-checking.

## 🛠️ Development

### Running in Development Mode

1. **Backend with auto-reload:**
```bash
uvicorn backend:app --reload --host 127.0.0.1 --port 8000
```

2. **Frontend with auto-reload:**
```bash
streamlit run frontend.py --server.runOnSave true
```

### Adding New Models

1. Add model name to `ALLOWED_MODEL_NAMES` in `backend.py`
2. Add to model lists in `frontend.py`
3. Ensure the model is supported by the provider

### Environment Setup for Development

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🐛 Troubleshooting

### Common Issues

**1. API Key Errors**
```
Error: The api_key client option must be set
```
- Ensure `.env` file exists with valid API keys
- Check that environment variables are loaded correctly

**2. Connection Refused**
```
ConnectionError: HTTPConnectionPool
```
- Make sure the backend server is running on port 8000
- Check if the API_URL in frontend.py matches your backend URL

**3. Model Not Found**
```
{"error": "Invalid Model"}
```
- Verify the model name is in `ALLOWED_MODEL_NAMES`
- Check if the model is available for your API key tier

**4. Import Errors**
```
ModuleNotFoundError: No module named 'langchain_groq'
```
- Install missing packages: `pip install langchain-groq`
- Ensure all dependencies are installed

### Debug Mode

Enable debug logging by adding to your `.env`:
```env
DEBUG=true
```

## 🚀 Deployment

### Docker Deployment (Recommended)

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:
```bash
docker build -t ai-chatbot .
docker run -p 8000:8000 --env-file .env ai-chatbot
```

### Cloud Deployment

**For Backend (FastAPI):**
- Railway, Render, or Heroku
- Set environment variables in platform settings

**For Frontend (Streamlit):**
- Streamlit Cloud, Railway, or Render
- Update API_URL to point to deployed backend

## 📊 Performance

- **Response Time**: ~2-5 seconds (depending on model and search)
- **Concurrent Users**: Up to 100 (FastAPI async handling)
- **Rate Limits**: Based on API provider limits

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

- **Issues**: Open an issue on GitHub
- **Discussions**: Use GitHub Discussions for questions
- **Email**: Contact the maintainer for urgent issues

## 🔗 Related Links

- [LangChain Documentation](https://python.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Groq API Documentation](https://console.groq.com/docs)
- [OpenAI API Documentation](https://platform.openai.com/docs)