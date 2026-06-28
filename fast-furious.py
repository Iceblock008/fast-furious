"""
Fast & Furious Mission Planner
------------------------------
This file acts as the main system.

Responsibilities:
- Analyze mission description
- Select best crew members
- Assign cars to each member
"""

from unit_1_oop_cars_storage_data import assign_car_to_driver

# -------------------------------
# CREW DATABASE
# -------------------------------
crew_database = {
    "Dominic Toretto": {"skills": ["driving", "muscle"], "power": 10},
    "Brian O'Conner": {"skills": ["driving", "stealth"], "power": 10},
    "Letty Ortiz": {"skills": ["driving", "combat"], "power": 8},
    "Roman Pearce": {"skills": ["distraction"], "power": 7},
    "Tej Parker": {"skills": ["tech", "hacking"], "power": 8},
    "Han Lue": {"skills": ["stealth", "driving"], "power": 9},
    "Luke Hobbs": {"skills": ["muscle", "combat"], "power": 10},
    "Deckard Shaw": {"skills": ["combat", "stealth"], "power": 10},
    "Ramsey": {"skills": ["hacking", "tech"], "power": 8.5},
}

# -------------------------------
# SKILL DETECTION
# -------------------------------
def analyze_mission_description(description: str):
    """
    Extract required skills from mission description.
    """
    desc = description.lower()
    skills = []

    if "hack" in desc:
        skills.append("hacking")
    if "drive" in desc or "car" in desc or "race" in desc:
        skills.append("driving")
    if "fight" in desc or "combat" in desc:
        skills.append("combat")
    if "sneak" in desc or "stealth" in desc:
        skills.append("stealth")
    if "tech" in desc:
        skills.append("tech")

    return skills if skills else ["driving"]


# -------------------------------
# CREW SELECTION
# -------------------------------
def select_crew(required_skills):
    """
    Select best crew members based on skills and power.
    """
    selected = []

    for skill in required_skills:
        best_candidate = None
        highest_power = -1

        for name, data in crew_database.items():
            if skill in data["skills"] and name not in selected:
                if data["power"] > highest_power:
                    best_candidate = name
                    highest_power = data["power"]

        if best_candidate:
            selected.append(best_candidate)

    return selected


# -------------------------------
# MISSION EXECUTION
# -------------------------------
def run_mission_planner(title: str, description: str, difficulty: str):
    """
    Main function to run mission planning.
    """
    required_skills = analyze_mission_description(description)
    crew = select_crew(required_skills)

    print("\n" + "=" * 50)
    print(f"MISSION: {title}")
    print(f"Difficulty Level: {difficulty}")
    print(f"Required Skills: {required_skills}")
    print("=" * 50)

    print("\nCREW + CAR ASSIGNMENT:\n")

    for member in crew:
        primary_skill = crew_database[member]["skills"][0]

        # Assign car
        car = assign_car_to_driver(member, primary_skill)

        if car:
            print(f"{member} → {primary_skill.upper()} → {car.model}")
        else:
            print(f"{member} → No car available")

    print("\nMission Ready 🚀\n")


# -------------------------------
# MAIN LOOP (CLI)
# -------------------------------
def main():
    print("🏎️ Fast & Furious Mission System")
    print("Type 'exit' to quit\n")

    while True:
        title = input("Mission Name: ").strip()
        if title.lower() == "exit":
            break

        description = input("Describe Mission: ").strip()
        difficulty = input("Difficulty (1-3): ").strip()

        run_mission_planner(title, description, difficulty)


if __name__ == "__main__":
    main()
