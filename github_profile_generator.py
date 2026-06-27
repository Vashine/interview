def generate_readme():
    print("=" * 50)
    print(" GITHUB PROFILE README GENERATOR ")
    print("=" * 50)
    
            # Get user details
    name = input("Enter your name: ")
    role = input("Your role (e.g., Python Developer): ")
    location = input("Your location: ")
    
    print("\nEnter your top 5 skills (comma separated):")
    skills = input("Skills: ").split(',')
    
    print("\nEnter 3 projects you're proud of (comma separated):")
    projects = input("Projects: ").split(',')
    
    linkedin = input("LinkedIn profile URL (optional): ")
    email = input("Contact email: ")
    
    # Generate README content
    readme = f"""
# Hi there, I'm {name} 

##  {role} from {location}

###  Tech Stack:
"""
    for skill in skills:
        readme += f"- {skill.strip()}\n"
    
    readme += f"""
###  Featured Projects:
"""
    for i, project in enumerate(projects, 1):
        readme += f"{i}. **{project.strip()}**\n"
    
    readme += f"""
###  Connect with me:
- LinkedIn: {linkedin if linkedin else 'Coming soon'}
- Email: {email}

###  Fun Fact:
I love solving problems with Python and SQL! 

---
 From [Vashine](https://github.com/Vashine)
"""
    
    print("\n" + "=" * 50)
    print(" YOUR README.MD CONTENT IS READY! ")
    print("=" * 50)
    print(readme)
    print("=" * 50)
    print("\n Copy the above content and paste it in a new file called README.md")
    print("r Create that file in your main GitHub profile repo to show it on your profile!")

if __name__ == "__main__":
    generate_readme()
