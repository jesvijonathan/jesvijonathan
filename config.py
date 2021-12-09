youtube_1 = ""
youtube_2 = ""
soundcloud = ""

### Main Page
title = "Jesvi Jonathan"           # Main title | mostly hardcoded to html

### Music Page
music_page_content = ""            # Music page's content text goes here            
music_video_display = 2            # Number of music videos to display                   
music_video_display_static = False # Give link manually or automate get latest music video
music_video_static = {             # Static youtube music video links
    "music_video_1": {
        "title":"Soundcloud",      # Description | Source
        "link":"",                 # Link to music video
        "caption":"",              # Caption for video
        "priority":0               # 0 To Include randomly in the list, 1 to include at first before auto links, 2 to include at end, 3 to not include at all
        },}
music_video_getfrom = [youtube_2]    # The channel to auto get the music video from based on uplaod date
music_button_display = 0           # Display the music button container
music_button = {
    "Button_1": {
        "text":"Soundcloud",       # Button text
        "link":"",                 # Link to redirect
        "logo":""                  # Path to logo
        },
    "Button_2": {
        "text":"Youtube",
        "link":"",
        "logo":""
        },}


### Video Page
video_page_content = ""            # Video page's content text goes here            
video_display = 5                  # Number of videos to display                   
video_display_static = False       # Give link manually or automate get latest video upload
video_static = {                   # Static youtube music video links
    "video_1": {
        "title":"Latest Video",    # Description | Source
        "link":"",                 # Link to video
        "caption":"",              # Caption for video
        "priority":0               # 0 To Include randomly in the list, 1 to include at first before auto links, 2 to include at end, 3 to not include at all
        },}
video_caption = False              # Enable video caption
video_getfrom = {                  # The channels to auto get the music video from based on latest upload date
    "channel_1":{
        "link":youtube_1,          # link to channel
        "priority":1               # priority of video list, greater the number more the priority
        }, 
    "channel_2":{
        "link":youtube_2,
        "priority":0
        }, 
    }
subscribe_display = 1              # 0 = False, 1 - Display, 2 - Corousal-display

### Project Page
project_page_content = ""          # Project page's content text goes here
project_cards = True               # Enable project card
project_cards_detail = {           # Details for cards
    "project_1":{
        "name":"Jesvi Bot",        # Name of project
        "Description":"",          # Project description
        "link":"link",
        "visible":True             # Card visible
        },
    "project_2":{
        "name":"Eulah Rom",        # Name of project
        "Description":"",          # Project description
        "link":"link",
        "visible":True             # Card visible
        }, 
    }

### About 
about_page_content = ""
