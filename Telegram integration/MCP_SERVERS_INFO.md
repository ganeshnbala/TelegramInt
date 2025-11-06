# MCP Servers Used in Telegram Integration

The Telegram bot integration uses **3 MCP (Model Context Protocol) servers** that provide various tools for the AI agent to process user queries.

## Overview

All MCP servers are configured in `config/profiles.yaml`:

```yaml
mcp_servers:
  - id: math
    script: mcp_server_1.py
    cwd: .
  - id: documents
    script: mcp_server_2.py
    cwd: .
  - id: websearch
    script: mcp_server_3.py
    cwd: .
```

---

## 1. Math Server (`mcp_server_1.py`)

**Purpose:** Mathematical operations and computational tasks

**Tools Provided:**
- `add` - Addition of two numbers
- `subtract` - Subtraction
- `multiply` - Multiplication
- `divide` - Division
- `power` - Exponentiation
- `sqrt` - Square root
- `cbrt` - Cube root
- `factorial` - Factorial calculation
- `remainder` - Modulo operation
- `sin`, `cos`, `tan` - Trigonometric functions
- `strings_to_chars_to_int` - Convert strings to ASCII values
- `int_list_to_exponential_sum` - Calculate exponential sum of integers
- `fibonacci_numbers` - Generate Fibonacci sequence
- `run_python_sandbox` - Execute Python code safely
- `run_shell_command` - Execute shell commands
- `run_sql_query` - Execute SQL queries
- `create_thumbnail` - Image processing

**Use Cases:**
- Mathematical calculations
- String manipulation (ASCII conversions)
- Code execution
- Data processing

---

## 2. Documents Server (`mcp_server_2.py`)

**Purpose:** Document processing, search, and extraction

**Tools Provided:**
- `search_documents` - Search indexed documents using FAISS
  - Uses semantic search on indexed documents
  - Returns relevant document chunks
  - Requires FAISS index to be built first
  
- `extract_webpage` - Extract and convert webpage to markdown
  - Downloads webpage content
  - Converts to markdown format
  - Processes images (captions them and removes them)
  
- `extract_pdf` - Convert PDF to markdown
  - Extracts text and images from PDFs
  - Converts to markdown format
  - Handles image extraction and captioning

**Additional Features:**
- FAISS-based document indexing
- Semantic document search
- Image captioning using vision models
- Document chunking and processing
- Automatic document indexing from `documents/` folder

**Use Cases:**
- Searching through indexed documents
- Extracting information from PDFs
- Processing web pages
- Document Q&A

**Dependencies:**
- FAISS for vector search
- Ollama for embeddings (nomic-embed-text)
- Vision models for image captioning

---

## 3. Web Search Server (`mcp_server_3.py`)

**Purpose:** Web search and content fetching

**Tools Provided:**
- `search` - Search DuckDuckGo
  - Performs web searches
  - Returns formatted search results
  - Rate-limited (30 requests/minute)
  - Returns title, link, snippet for each result
  
- `fetch_content` - Fetch and parse webpage content
  - Downloads webpage HTML
  - Extracts clean text content
  - Removes scripts, styles, navigation
  - Rate-limited (20 requests/minute)

**Features:**
- DuckDuckGo search integration
- Rate limiting to prevent abuse
- Clean text extraction from web pages
- BeautifulSoup for HTML parsing

**Use Cases:**
- Finding information online
- Searching for current data
- Fetching content from URLs
- Real-time information retrieval

**Example:**
When user asks "What are the top 10 biggest cities?", the agent can use:
1. `search` tool to find relevant web pages
2. `fetch_content` to get detailed information from those pages

---

## How They Work Together

When a user sends a message to the Telegram bot:

1. **Agent receives the message** via Telegram
2. **Agent analyzes the query** using perception module
3. **Agent selects appropriate tools** from the 3 MCP servers:
   - Math questions → Math server tools
   - Document questions → Documents server tools
   - Web search questions → Web search server tools
4. **Agent executes tools** and processes results
5. **Agent returns final answer** to user
6. **Results saved to Excel** and **emailed** via Gmail

## Configuration

All servers are configured in `config/profiles.yaml` and initialized when the bot starts. The agent can use any combination of tools from all three servers to answer user queries.

## Dependencies

- **Math Server:** Basic Python libraries, PIL for images
- **Documents Server:** FAISS, Ollama (for embeddings), PyMuPDF, Trafilatura, MarkItDown
- **Web Search Server:** httpx, BeautifulSoup4

## Status

✅ All 3 MCP servers are integrated and available to the Telegram bot
✅ Tools are automatically discovered and registered
✅ Agent can use any tool from any server based on the query

