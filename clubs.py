from pyscript import Element

clubs = {
    "politics": {
        "name": "Politics and Government Club",
        "description": "Experience real-world politics through simulations, debates, and fun activities.",
        "time": "Every Thursday 4:00–5:30 PM",
        "location": "Room 204",
        "advisor": "Mr. Romero"
    },
    "basketball": {
        "name": "Basketball Varsity",
        "description": "Train, compete, and stay physically fit with the varsity team.",
        "time": "Mon/Wed/Fri 3:00–6:00 PM",
        "location": "Gymnasium",
        "advisor": "Coach Bong"
    },
    "arts": {
        "name": "Arts & Humanities",
        "description": "Express yourself through art, music, writing, and creativity.",
        "time": "Every Wednesday 4:00–5:30 PM",
        "location": "Art Studio",
        "advisor": "Ms. Torres"
    },
    "robotics": {
        "name": "Robotics Club",
        "description": "Learn coding, robotics, and join competitions and hackathons.",
        "time": "Every Tuesday 3:45–5:30 PM",
        "location": "Computer Lab",
        "advisor": "Ms. Cruz"
    },
    "mun": {
        "name": "Model United Nations",
        "description": "Develop diplomacy, leadership, and public speaking skills.",
        "time": "Friday 4:00–5:30 PM",
        "location": "Room 303",
        "advisor": "Mr. Dela Cruz"
    },
    "advocacy": {
        "name": "Advocacy Club",
        "description": "Organize charity drives, outreach programs, and social campaigns.",
        "time": "Every Monday 4:00–5:00 PM",
        "location": "Room 115",
        "advisor": "Ms. Fortea"
    }
}

def show_info(event):
    from pyscript import Element
    
    selected = Element("clubDropdown").value
    
    if selected in clubs:
        club = clubs[selected]
        Element("clubName").write(club["name"])
        Element("clubDesc").write(f"Description: {club['description']}")
        Element("clubTime").write(f"Meeting Time: {club['time']}")
        Element("clubLocation").write(f"Location: {club['location']}")
        Element("clubAdvisor").write(f"Advisor: {club['advisor']}")
    else:
        Element("clubName").write("")
        Element("clubDesc").write("")
        Element("clubTime").write("")
        Element("clubLocation").write("")
        Element("clubAdvisor").write("")
