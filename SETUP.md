# Setup on a new machine (macOS) — instructions for Claude / the user

Repo: `git@github.com:Abhiz2411/ai-masterclass-tkiet.git`
Layout: `masterclass/` (RAG + agentic AI notebooks, Python 3.13) and `code/` (third-party course repo, not tracked here).

## 1. Clone
```bash
git clone git@github.com:Abhiz2411/ai-masterclass-tkiet.git
cd ai-masterclass-tkiet
```
(If SSH is not set up: `gh auth login`, or clone via `https://github.com/Abhiz2411/ai-masterclass-tkiet.git` with a Personal Access Token.)

## 2. Clone the course repo (ignored by this repo)
```bash
git clone git@github.com:aagarwal4/generative-ai-2025.git code/generative-ai-2025
```

## 3. Python env (uv, Python 3.13)
```bash
brew install uv            # if missing
cd masterclass
uv sync                    # creates .venv from pyproject.toml + uv.lock
source .venv/bin/activate
```
Dependencies are declared in `masterclass/pyproject.toml`; `uv.lock` pins exact cross-platform versions. Add packages with `uv add <pkg>` and commit both files.

## 4. Secrets (NOT in git)
`masterclass/.env` is git-ignored, so it does not come with the clone. The user must transfer it from the Windows laptop
(AirDrop, USB, or password manager) into `masterclass/.env`. If unavailable, ask the user for the keys, then:
```bash
cd masterclass
cp .env.example .env       # then fill in the three values
```
Keys needed: `TAVILY_API_KEY`, `OPENAI_API_KEY`, `GOOGLE_API_KEY` (Gemini). Never commit `.env`.

## 5. Ollama (needed for embeddings)
```bash
brew install ollama
ollama serve &
ollama pull nomic-embed-text
```

## 6. Run
Open notebooks in `masterclass/` (`rag/`, `agents/`, `exercises/`) with kernel = `masterclass/.venv`.
LLM is Gemini `gemini-flash-latest`. See `masterclass/README.md`.

## Sync workflow
`git pull` before work; `git add -A && git commit -m "msg" && git push` after.

## Troubleshooting
- **`Failed to build numpy==1.26.4` / `NumPy requires GCC >= 8.4`**: someone ran `uv pip install "numpy<2"` (or uncommented an install cell). Python 3.13 has no numpy 1.x wheel, so it tries to compile and fails. Never pin `numpy<2`. Fix: `cd masterclass && uv sync` (restores numpy 2.x). All dependencies are already in `pyproject.toml`; notebook install cells are not needed.
