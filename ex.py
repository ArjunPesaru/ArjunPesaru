import datetime

def generate_about_me():
    """
    Function to generate an 'About Me' summary dynamically.
    """
    # Static details
    name = "Arjun Pesaru"
    current_role = "Master's Student and Data Science Teaching Assistant"
    skills = [
        "Data Science Foundations",
        "ETL Processes",
        "Google Cloud Integration",
        "AI Pipeline Development",
        "Project Management (Jira, ClickUp)"
    ]
    previous_experience = [
        "Worked at California Burrito",
        "Worked at Qdoba",
    ]
    applying_for = "Data Scientist Intern, Product Analytics at Meta"
    current_city = "Boston, MA"

    # Dynamic calculations
    current_year = datetime.datetime.now().year
    years_experience = current_year - 2018  # Assuming professional experience started in 2018

    # Interests
    interests = [
        "Building medical chatbots",
        "Analyzing data for actionable insights",
        "Optimizing kitchen workflows (from previous roles)",
        "Learning advanced machine learning techniques"
    ]

    # Generate summary
    about_me_summary = f"""
    Hello! My name is {name}, and I am currently based in {current_city}.

    I am a {current_role} with over {years_experience} years of experience across industries, including food service 
and data science. My journey started in customer-facing roles at {', '.join([job.split()[2] for job in previous_experience])}, 
where I developed a strong work ethic and process optimization skills.

    Today, I focus on leveraging data to create impactful solutions. My core skills include:
    - {skills[0]}
    - {skills[1]}
    - {skills[2]}
    - {skills[3]}
    - {skills[4]}

    Recently, I have been exploring {interests[0]} and {interests[1]}. I am also applying my passion for efficiency 
from my past roles to areas like {interests[2]}.

    I am thrilled to apply for the {applying_for} position, where I hope to contribute my analytical expertise 
and problem-solving mindset to Meta's mission.

    Thank you for learning a bit about me! Feel free to reach out to connect or discuss opportunities.
    """

    return about_me_summary

if __name__ == "__main__":
    # Generate and display the 'About Me' summary
    print(generate_about_me())
