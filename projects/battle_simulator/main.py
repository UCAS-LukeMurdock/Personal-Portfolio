# Luke Murdock, Updated Battle Simulator

"""
Enhance your existing RPG Character Creator and Battle Simulator by incorporating data visualization, statistical analysis, and random data generation using Python libraries. This project will focus on reading and implementing features from library documentation.
REQUIREMENTS:
Library Integration:
    Use Matplotlib for character stat visualizations
    Use Pandas for data manipulation and basic statistical analysis
    Use Faker for generating random character names and descriptions
Character Visualization:
    Create a radar chart or bar graph to display a character's stats using Matplotlib
Data Analysis:
    Use Pandas to load character data into a DataFrame
    Implement basic statistical analysis on character attributes (e.g., mean, median, max, min)
Random Generation:
    Use Faker to generate random character names and backstories
Enhanced User Interface:
    Create a menu system that allows users to access new visualization and analysis features
Documentation Reading:
    Demonstrate understanding of library documentation by implementing at least one additional feature from each library not explicitly required above
Additional Features (Optional): (Note: only awarded IF all 20 points are earned, they cannot make up for lost points)
    Dynamic Battle Simulation and Analysis
    Use the Matplotlib animation module to create a dynamic visualization of a battle between two characters. Display health bars, damage dealt, and critical hits in real-time. After the battle, use Pandas to analyze the battle data, such as the number of turns, average damage per turn, and the most effective attacks. Present this analysis in a clear, graphical format using Matplotlib.
        Implement a dynamic battle visualization using Matplotlib animations (3 points)
        Add statistical analysis of the battle data using Pandas (4 points)
        Combine the dynamic visualization and data analysis into a comprehensive battle report (5 points)
    Character Progression Forecasting:
    Implement a feature that uses Pandas and Matplotlib to forecast a character's growth over time. Allow users to input a number of levels or experience points, and then use statistical analysis to predict how the character's attributes might change. Display this information using line graphs or area charts, showing the potential growth curves for different attributes. Include confidence intervals in the visualization to represent the range of possible outcomes.
        Implement a feature to forecast character growth over time (3 points)
        Use Pandas and Matplotlib to visualize the growth predictions (4 points)
        Include confidence intervals in the growth forecasts (5 points)
    Procedural World Generation:
    Use the Faker library in combination with Pandas to generate a small game world with locations, NPCs, and quests. Create a DataFrame to store information about different locations, their inhabitants, and available quests. Use Matplotlib to create a simple 2D map visualization of the generated world. Implement a feature that allows players to "explore" this world, updating the character's experience and attributes based on completed quests and encounters.
        Generate a small game world with locations, NPCs, and quests using Faker and Pandas (3 points)
        Create a 2D map visualization of the generated world using Matplotlib (4 points)
        Implement a feature that allows players to explore the generated world (5 points)
"""
from projects.battle_simulator.file_handler import intput
from projects.battle_simulator.character_handler import create, display, remove
from projects.battle_simulator.battle_file import battle
from projects.battle_simulator.store import shop, equip
from projects.battle_simulator.library_use import visual, analysis, characs_visual_analysis

def main(): # Introduces the program and then lets the user choose one of the options
    print("\n\nWelcome to this Battle Simulator, where you can create, see, remove, shop for, or fight RPG characters.")
    while True:
        choice = intput("\nCreate(1) Display(2) Stat Visuals(3) Data Analysis(4) Remove(5) Character Comparison(6) Fight(7) Shop(8) Equip Sword(9) Exit(10)\n", 1,10)
        if choice == 1:
            create()
        elif choice == 2:
            display()
        elif choice == 3:
            visual()
        elif choice == 4:
            analysis()
        elif choice == 5:
            remove()
        elif choice == 6:
            characs_visual_analysis()
        elif choice == 7:
            battle()
        elif choice == 8:
            shop()
        elif choice == 9:
            equip()
        elif choice == 10:
            print("Come Back Soon!")
            break
        else:
            print("Something Broke")
            continue

if __name__ == "__main__":
    main()