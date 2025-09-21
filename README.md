# 🚀 Multi-Agent Production Scheduler (CrewAI)

This project implements a **multi-agent system for adaptive production scheduling** using [CrewAI](https://github.com/joaomdmoura/crewai).
It models a **factory with 1 Manager agent** and **3 Worker agents** (Cutting, Welding, Assembly).
Jobs are loaded from a CSV file, assigned to the correct machines, and executed in a coordinated schedule.

---

## 📦 Prerequisites

Before setting up the project, ensure you have the following installed:

1. **Python** (>= 3.10, recommended 3.11)

   * [Download Python](https://www.python.org/downloads/)
   * Verify:

     ```bash
     python --version
     ```

2. **uv** – fast Python package/dependency manager

   * Install:

     ```bash
     pip install uv
     ```
   * Verify:

     ```bash
     uv --version
     ```

3. **Git** (to clone the repository)

   * [Download Git](https://git-scm.com/downloads)
   * Verify:

     ```bash
     git --version
     ```

4. **Ollama** (for running local LLMs like Llama 3)

   * [Download Ollama](https://ollama.com/download)
   * After install, verify:

     ```bash
     ollama --version
     ```
   * Pull a model (example: Llama 3.1):

     ```bash
     ollama pull llama3.1
     ```

---

## 🛠️ Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YOUR_ORG/mpr7.git
   cd mpr7
   ```

2. **Set up Virtual Environment (with uv)**

   ```bash
   uv venv
   ```

3. **Activate the Virtual Environment**

   * Windows (PowerShell):

     ```powershell
     .venv\Scripts\Activate
     ```
   * macOS/Linux (bash/zsh):

     ```bash
     source .venv/bin/activate
     ```

   You should see `(mpr7)` prefix in your terminal.

4. **Install Dependencies**

   ```bash
   uv pip install crewai crewai-tools
   ```

5. **Check Installation**

   ```bash
   uv pip list | findstr crewai
   ```

   You should see:

   ```
   crewai          x.y.z
   crewai-tools    x.y.z
   ```

---

## 📂 Project Structure

```
mpr7/
│
├── jobs/
│   └── jobs.csv              # Input jobs for scheduling
│
├── src/
│   └── mpr7/
│       ├── main.py           # Entry point
│       ├── crew.py           # Crew creation
│       ├── config/
│       │   ├── agents.py     # Agents (Manager + Workers)
│       │   └── tasks.py      # Scheduling & execution tasks
│       └── tools/
│           └── job_reader.py # Custom tool for reading jobs
│
├── README.md                 # Setup instructions (this file)
└── pyproject.toml / uv.lock  # Dependencies
```

---

## ▶️ Running the Project

1. Make sure your virtual environment is activated:

   ```bash
   .venv\Scripts\Activate   # Windows
   source .venv/bin/activate # macOS/Linux
   ```

2. Start the Crew:

   ```bash
   crewai run
   ```

3. Expected output:

   * The **Manager Agent** reads jobs from `jobs/jobs.csv`.
   * Jobs are assigned to **Cutting, Welding, or Assembly workers**.
   * A **schedule table** is printed in the console.

---

## 🛑 Stopping Ollama (if needed)

* **Windows**:

  ```powershell
  net stop ollama
  ```

  Or stop the `ollama.exe` process from **Task Manager**.

* **macOS**:

  ```bash
  brew services stop ollama
  ```

  Or:

  ```bash
  pkill ollama
  ```

* **Linux**:

  ```bash
  sudo systemctl stop ollama
  ```
