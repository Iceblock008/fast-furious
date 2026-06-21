import sys

# 1. The Ultimate Fast Crew Database
crew_database = {
    "Dominic Toretto": {"skills": ["driving", "muscle", "tactics", "leadership"], "specialty": "Muscle Cars / Family / Leadership", "power_level": 10},
    "Brian O'Conner": {"skills": ["driving", "stealth", "tactics"], "specialty": "Import Cars / Undercover", "power_level": 9},
    "Tej Parker": {"skills": ["hacking", "tech", "driving"], "specialty": "Cyber Security / Gadgets", "power_level": 8},
    "Roman Pearce": {"skills": ["driving", "distraction"], "specialty": "Improvisation / Comedic Relief", "power_level": 7},
    "Letty Ortiz": {"skills": ["driving", "muscle", "combat"], "specialty": "Street Fighting / Superbikes", "power_level": 9},
    "Han Lue": {"skills": ["driving", "stealth"], "specialty": "Drifting / Surveillance", "power_level": 8},
    "Luke Hobbs": {"skills": ["muscle", "combat", "tactics"], "specialty": "Heavy Weapons / Brawling", "power_level": 10},
    "Deckard Shaw": {"skills": ["combat", "stealth", "tactics", "driving"], "specialty": "Special Ops / Assassination", "power_level": 10},
    "Ramsey": {"skills": ["hacking", "tech"], "specialty": "God's Eye Creator / Software", "power_level": 8},
    "Gisele Yashar": {"skills": ["stealth", "combat", "driving"], "specialty": "Weapons Expert / Infiltration", "power_level": 8}
}

# 2. Keyword Mapper to Detect Required Skills automatically
def analyze_mission_description(description):
    detected_skills = set()
    desc_lower = description.lower()
    
    # Mapping real-world words to system skills
    keyword_map = {
        "driving": ["drive", "car", "race", "getaway", "chase", "vehicle", "drift"],
        "hacking": ["hack", "computer", "system", "mainframe", "firewall", "data", "cyber"],
        "tech": ["tech", "gadget", "device", "tracker", "satellite"],
        "muscle": ["heavy", "lift", "break", "door", "truck", "strength"],
        "combat": ["fight", "brawl", "guard", "combat", "weapons", "shoot"],
        "stealth": ["sneak", "spy", "stealth", "infiltration", "unnoticed", "secret"],
        "distraction": ["distract", "noise", "bait", "attention"]
    }
    
    for skill, keywords in keyword_map.items():
        for keyword in keywords:
            if keyword in desc_lower:
                detected_skills.add(skill)
                
    return list(detected_skills)

# 3. Allocation and Planning Engine
def run_mission_planner(mission_title, description, difficulty):
    required_skills = analyze_mission_description(description)
    
    if not required_skills:
        # Default skill if no keywords match perfectly
        required_skills = ["driving"] 
        
    selected_crew = []
    
    # Core allocation logic
    if difficulty == "3" or "nuclear" in description.lower() or "world" in description.lower():
        selected_crew = list(crew_database.keys())
        difficulty_label = "Extreme (All Hands on Deck)"
    else:
        difficulty_label = "High" if difficulty == "2" else "Standard"
        for skill in required_skills:
            best_candidate = None
            highest_power = -1
            for character, profile in crew_database.items():
                if skill in profile["skills"] and character not in selected_crew:
                    if profile["power_level"] > highest_power:
                        highest_power = profile["power_level"]
                        best_candidate = character
            if best_candidate:
                selected_crew.append(best_candidate)

    # Outputting the customized base plan
    print("\n" + "="*50)
    print(f"🚨 MISSION BRIEFING: {mission_title.upper()} 🚨")
    print(f"Threat Level: {difficulty_label}")
    print(f"Intel Gathered (Detected Requirements): {', '.join([s.capitalize() for s in required_skills])}")
    print("="*50)
    
    print("\n👥 THE ASSIGNED CREW:")
    for member in selected_crew:
        print(f" • {member} -> Role: {crew_database[member]['specialty']}")
        
    print("\n📋 DYNAMIC BASE PLAN:")
    step = 1
    if any(s in required_skills for s in ["hacking", "tech"]):
        techs = [c for c in selected_crew if "hacking" in crew_database[c]["skills"] or "tech" in crew_database[c]["skills"]]
        print(f"{step}. TECH PHASE: {', '.join(techs)} will compromise the security matrix and clear the blind spots.")
        step += 1
    if any(s in required_skills for s in ["stealth", "distraction"]):
        stealthy = [c for c in selected_crew if "stealth" in crew_database[c]["skills"] or "distraction" in crew_database[c]["skills"]]
        print(f"{step}. INFILTRATION: {', '.join(stealthy)} will sneak past boundaries or cause a scene to draw attention.")
        step += 1
    if any(s in required_skills for s in ["muscle", "combat"]):
        fighters = [c for c in selected_crew if "muscle" in crew_database[c]["skills"] or "combat" in crew_database[c]["skills"]]
        print(f"{step}. ASSAULT PHASE: {', '.join(fighters)} will establish a hard perimeter and neutralize immediate threats.")
        step += 1
    if "driving" in required_skills:
        drivers = [c for c in selected_crew if "driving" in crew_database[c]["skills"]]
        print(f"{step}. GETAWAY PHASE: {', '.join(drivers)} will execute high-speed extraction utilizing custom tuning.")
        step += 1
        
    if "Dominic Toretto" in selected_crew:
        print(f"{step}. TORRETO'S RULE: Hit the NOS on count of three. No matter what happens, we don't turn our backs on family.")
    print("="*50 + "\n")

# 4. Interactive User Interface Loop
def main():
    print("🏎️ Welcome to the Fast & Furious Mission Allocation Terminal 🏎️")
    print("Type 'exit' at any prompt to shut down the terminal.\n")
    
    while True:
        title = input("Enter Mission Name / Objective: ").strip()
        if title.lower() == 'exit': break
        if not title: continue
            
        description = input("Describe the problem/scenario (e.g., 'Need to hack a server vault and escape via a street race'): ").strip()
        if description.lower() == 'exit': break
        
        print("Select Difficulty Level:")
        print(" 1 - Standard Street Ops")
        print(" 2 - High Risk International Heist")
        print(" 3 - Extreme Global Threat")
        difficulty = input("Choice (1-3): ").strip()
        if difficulty.lower() == 'exit': break
        if difficulty not in ['1', '2', '3']: difficulty = '1'
        
        run_mission_planner(title, description, difficulty)

if __name__ == "__main__":
    main()