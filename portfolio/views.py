from django.shortcuts import render

def index_view(request):
    context = {
        'linkedin_url': 'https://www.linkedin.com/in/abhijeet-rana-583a7b284',  # LinkedIn URL
        'github_url': 'https://github.com/rana932',  # GitHub URL
        'email': 'ranaabhi9068@gmail.com',  # Your email
        'experience': 'Junior professional',  # Your experience
        'education': '''MCA - Masters Degree
               B.Sc.[CS] - Bachelors Degree''',  # Your education
        'about_me': '''I’m a passionate full stack web developer.
               I create responsive, user-friendly websites with a strong focus on design and functionality. 
               I bring ideas to life with HTML, CSS, JavaScript, Python, PHP, and frameworks like Django.
               With a balanced approach to both technical and creative aspects, I take pride in delivering efficient, high-quality code. 
               Let’s collaborate and build something exceptional together!''', # Your about me text
        'web_skills': [
            {'name': 'HTML'},
            {'name': 'CSS'},
            {'name':'Bootstrap'},
            {'name': 'MySQL'},
        ],
        'pro_skills': [
            {'name': 'Python'},
            {'name': 'C Language'},
            {'name': 'PHP'},
            {'name': 'JavaScript'},
        ],
        'frame_skills': [
            {'name': 'Django'},
        ],
        'libraries': [
            {'name': 'Pandas'},
            {'name': 'Seaborn'},
            {'name': 'Matplotlib'},
            {'name': 'Numpy'}
        ],
  
        'certificates': [
            {'name': 'Python Programming Step by Step', 'image': 'portfolio/assets/python_mindluster.jpg', 'live_url': 'https://www.mindluster.com/student/certificate/662525059'},
            {'name': 'CS50 Introduction to Programming with Python', 'image': 'portfolio/assets/CS50P.png', 'live_url': 'https://cs50.harvard.edu/certificates/56968772-698e-446a-9a4b-031e1437516d'},
            {'name': 'Python Django Tutorial by Simplilearn', 'image':'portfolio/assets/python_django.jpg', 'live_url':'https://simpli-web.app.link/e/vJhuq5D5yRb'},
            {'name': 'Python Bootcamp for Engineers and Scientists', 'image':'portfolio/assets/python_udemy.jpg', 'live_url':'https://www.udemy.com/certificate/UC-69f72ab9-3bb6-4862-b806-f273e2265afe/'},
        ],
        
        'projects': [
            {'name': 'Blogger', 'image': 'portfolio/assets/project-1.png', 
            'description':''' A fully responsive blog platform where users can post articles, comment, and interact with content. 
            The platform allows users to create, read, and manage blog posts.
            Built using HTML, CSS, JavaScript, PHP and MySQL.''',
            'github_url': 'https://github.com/rana932', 'live_demo_url': '/'},
            {'name': 'The Book Pond', 'image': 'portfolio/assets/project-2.png', 
            'description':'''An interactive eBook platform that allows users to easily browse, download, and read eBooks online. 
            The platform offers a simple and intuitive user interface with search functionality, categorized genres.
            Built using HTML, CSS, Bootstrap and JavaScript, this platform focuses on a smooth, mobile-friendly reading experience.''', 
            'github_url': 'https://github.com/rana932/thebookpond', 'live_demo_url': 'https://rana932.github.io/thebookpond/index.html'},
            {'name': 'The Vintage Vault', 'image': 'portfolio/assets/project-3.png', 
            'description':'''Vintage Vault is a secure, user-friendly online marketplace for buying and selling antique items. 
            The platform allows users to list, browse, and purchase vintage collectibles, furniture, art, and more. 
            Featuring easy-to-navigate search filters, detailed product descriptions, and secure payment options, 
            Vintage Vault is the ultimate destination for antique lovers. 
            Built using modern web technologies to ensure a smooth and responsive experience across devices. ''', 
            'github_url': 'https://github.com/rana932/thevintagevault', 'live_demo_url': 'https://vintagevault.kesug.com'},
        ],
    }

    return render(request, 'index.html', context)
