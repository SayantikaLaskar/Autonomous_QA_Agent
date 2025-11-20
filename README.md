# Autonomous QA Agent for Test Case and Script Generation

An intelligent QA agent that builds a "testing brain" from project documentation to generate comprehensive test cases and executable Selenium scripts.

## Features

- **Document Ingestion**: Upload and process support documents (MD, TXT, JSON, PDF)
- **Knowledge Base**: Vector database for document-grounded test reasoning
- **Test Case Generation**: AI-powered test case creation based on documentation
- **Selenium Script Generation**: Convert test cases to executable Python scripts
- **Web Interface**: Streamlit UI for easy interaction

## Requirements

- Python 3.8+
- FastAPI
- Streamlit
- ChromaDB (Vector Database)
- Sentence Transformers
- Selenium
- Additional dependencies in requirements.txt

## Setup Instructions

1. **Clone and navigate to project directory**
```bash
git clone <repository-url>
cd qa-agent
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download required models**
```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
```

## Running the Application

### Option 1: Automatic Start (Recommended)
```bash
python start_app.py
```
This will start both FastAPI backend and Streamlit frontend automatically.

### Option 2: Manual Start (Alternative)
**Terminal 1 - Start Backend:**
```bash
python run_backend.py
```

**Terminal 2 - Start Frontend:**
```bash
python run_frontend.py
```

### Option 3: Individual Components
**Backend only:**
```bash
cd backend
python -m uvicorn main:app --reload --port 8000
```

**Frontend only:**
```bash
streamlit run frontend/app.py --server.port 8501
```

### Access the Application
- Streamlit UI: http://localhost:8501
- FastAPI docs: http://localhost:8000/docs

## Usage Examples

### 1. Upload Documents
- Navigate to "Document Upload" section
- Upload support documents (product_specs.md, ui_ux_guide.txt, etc.)
- Upload or paste checkout.html content
- Click "Build Knowledge Base"

### 2. Generate Test Cases
- Go to "Test Case Generation" section
- Enter a query like: "Generate test cases for discount code feature"
- Review generated test cases with document references

### 3. Generate Selenium Scripts
- Select a test case from the generated list
- Click "Generate Selenium Script"
- Copy the generated Python script for execution

## Project Structure

```
qa-agent/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── models/              # Data models
│   ├── services/            # Business logic
│   └── utils/               # Utility functions
├── frontend/
│   └── app.py               # Streamlit interface
├── assets/
│   ├── checkout.html        # Target web application
│   └── support_docs/        # Sample support documents
├── tests/
│   └── generated_scripts/   # Generated Selenium scripts
├── requirements.txt
└── README.md
```

## Support Documents Included

1. **product_specs.md** - Feature specifications and business rules
2. **ui_ux_guide.txt** - UI/UX guidelines and validation rules
3. **api_endpoints.json** - API endpoint specifications
4. **test_scenarios.md** - Additional test scenarios and edge cases
5. **checkout.html** - Target e-commerce checkout page

## Key Features of checkout.html

- Product catalog with "Add to Cart" functionality
- Shopping cart with quantity management
- Discount code application (SAVE15 = 15% off)
- User details form with validation
- Shipping method selection (Standard/Express)
- Payment method selection (Credit Card/PayPal)
- Form validation with error messages
- Success confirmation on valid submission

## Architecture

The system uses a RAG (Retrieval-Augmented Generation) approach:

1. **Document Processing**: Extract and chunk text from uploaded documents
2. **Vector Storage**: Store document embeddings in ChromaDB
3. **Query Processing**: Retrieve relevant context for test generation
4. **LLM Integration**: Generate grounded test cases and scripts
5. **Script Validation**: Ensure Selenium scripts match actual HTML structure

## Troubleshooting

### Common Issues

1. **ChromaDB Permission Error**
   - Delete `.chroma` directory and restart

2. **Model Download Issues**
   - Ensure internet connection for initial model download
   - Models are cached locally after first download

3. **Selenium Script Errors**
   - Verify ChromeDriver is installed and in PATH
   - Check HTML selectors match the actual checkout.html structure

### Performance Tips

- Use smaller document chunks for better retrieval accuracy
- Limit document size for faster processing
- Clear knowledge base periodically to avoid conflicts

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes with tests
4. Submit a pull request

## License

MIT License - see LICENSE file for details