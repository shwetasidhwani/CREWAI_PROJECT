from mpr7.crew import create_crew

def run():  # 👈 crewai CLI looks for this
    crew = create_crew()
    result = crew.kickoff()
    print("Final Schedule:\n", result)

def main():  # optional, for running with python main.py
    run()

if __name__ == "__main__":
    main()
