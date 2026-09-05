"""Entry point — run the OpenAI-compatible DeepSeek server.

    python app.py            # serves on http://localhost:8000

On first use (no saved session) a browser window opens for you to sign in by
hand; run `python -m deepseek.auth` to do that ahead of time. Set
DEEPSEEK_PROFILE_DIR to reuse an existing signed-in Chrome profile.
"""

import os

import uvicorn
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port_str = os.getenv("PORT", "8000")
    
    # Ensure PORT is a valid integer
    try:
        port = int(port_str)
    except ValueError:
        print(f"Warning: PORT='{port_str}' is not a valid integer, using 8000")
        port = 8000
    
    uvicorn.run(
        "server.api:app",
        host=host,
        port=port,
        reload=False,
    )
