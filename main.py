from pyscript import display, document

def club1(e):
    club1 = {
        "name": "science club",
        "description": "a club for students interested in science experiments.",
        'meeting_time': "fridays at 3 pm",
        "location": "room 101",
        "club_moderator": "mr. smith",
        "number_of_members": 25,
    }
    
    document.getElementById("output").innerHTML = ""
    document.getElementById("info").innerHTML = ""
    
    display(f'club name: ', target="info")
    display(f'description: ', target="info")
    display(f'meeting time: ', target="info")
    display(f'location: ', target="info")
    display(f'club moderator: ', target="info")
    display(f'# of members: ', target="info")
    
    display(f'{club1['name']}', target="output")
    display(f'{club1['description']}', target="output")
    display(f'{club1['meeting_time']}', target="output")
    display(f'{club1['location']}', target="output")
    display(f'{club1['club_moderator']}', target="output")
    display(f'{club1['number_of_members']}', target="output")
    
def club2(e):
    club2 = {
        "name": "commarts club",
        "description": "a club for students passionate about communication and the arts.",
        'meeting_time': "wednesdays at 2 pm",
        "location": "room 102",
        "club_moderator": "mr. jefferson",
        "number_of_members": 20,
    }
    
    document.getElementById("output").innerHTML = ""
    document.getElementById("info").innerHTML = ""
    
    display(f'club name: ', target="info")
    display(f'description: ', target="info")
    display(f'meeting time: ', target="info")
    display(f'location: ', target="info")
    display(f'club moderator: ', target="info")
    display(f'# of members: ', target="info")
    
    display(f'{club2['name']}', target="output")
    display(f'{club2['description']}', target="output")
    display(f'{club2['meeting_time']}', target="output")
    display(f'{club2['location']}', target="output")
    display(f'{club2['club_moderator']}', target="output")
    display(f'{club2['number_of_members']}', target="output")
    
def club3(e):
    club3 = {
        "name": "graphic design club",
        "description": "a club for students who love graphic design and digital art.",
        'meeting_time': "mondays at 4 pm",
        "location": "room 104",
        "club_moderator": "mr. garcia",
        "number_of_members": 100,
    }
    
    document.getElementById("output").innerHTML = ""
    document.getElementById("info").innerHTML = ""
    
    display(f'club name: ', target="info")
    display(f'description: ', target="info")
    display(f'meeting time: ', target="info")
    display(f'location: ', target="info")
    display(f'club moderator: ', target="info")
    display(f'# of members: ', target="info")
    
    display(f'{club3['name']}', target="output")
    display(f'{club3['description']}', target="output")
    display(f'{club3['meeting_time']}', target="output")
    display(f'{club3['location']}', target="output")
    display(f'{club3['club_moderator']}', target="output")
    display(f'{club3['number_of_members']}', target="output")