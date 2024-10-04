Contributing to KataKrypt
Thank you for considering contributing to KataKrypt! We appreciate your interest in improving the project. Whether you're fixing a bug, adding new features, or improving documentation, your contributions are welcome.

This document provides guidelines to help you contribute effectively.

Table of Contents
Code of Conduct
How Can I Contribute?
Reporting Bugs
Suggesting Enhancements
Improving Documentation
Submitting Pull Requests
Development Guidelines
Project Structure
Coding Standards
Commit Messages
Branching Model
License
Contact
Code of Conduct
By participating in this project, you agree to abide by the Code of Conduct. Please read it to understand the expectations for all contributors.

How Can I Contribute?
Reporting Bugs
If you find a bug in the project, please open an issue on GitHub:

Search Existing Issues: Before creating a new issue, check if the problem has already been reported.

Create a New Issue: If it hasn't been reported, create a new issue and include:

A clear, descriptive title.
Steps to reproduce the issue.
Expected and actual results.
Screenshots or error messages, if applicable.
Your environment details (operating system, Python version, etc.).
Report a Bug

Suggesting Enhancements
We welcome ideas to improve KataKrypt!

Search Existing Suggestions: See if your idea has already been proposed.

Create a New Issue: Provide details about the enhancement:

A clear, descriptive title.
A detailed explanation of the enhancement.
The benefits and potential drawbacks.
Any relevant examples or mockups.
Suggest an Enhancement

Improving Documentation
Good documentation helps others understand and use KataKrypt effectively.

Fix Typos or Errors: Feel free to correct any mistakes you find.
Add Explanations: Enhance existing documentation with more detailed explanations.
Update README or Help Guides: Improve instructions or update information to reflect recent changes.
Submitting Pull Requests
When you're ready to contribute code:

Fork the Repository: Click the "Fork" button on the GitHub page to create your own copy.

Clone Your Fork:

bash
Copy code
git clone https://github.com/your-username/KataKrypt.git
cd KataKrypt
Create a Branch:

bash
Copy code
git checkout -b feature/your-feature-name
Make Changes: Implement your changes, following the Coding Standards.

Commit Changes:

bash
Copy code
git add .
git commit -m "Brief description of your changes"
Push to Your Fork:

bash
Copy code
git push origin feature/your-feature-name
Open a Pull Request:

Go to the original repository.
Click "New Pull Request".
Select your branch and submit the pull request.
Provide a clear description of your changes.
Create a Pull Request

Development Guidelines
Project Structure
Understanding the project structure helps in navigating and making effective contributions.

graphql
Copy code
KataKrypt/
│
├── KataKrypt.py         # Main Python script
├── help.html            # Help guide
├── README.md            # Project overview
├── CONTRIBUTING.md      # Contribution guidelines
├── LICENSE              # License information
├── bmp_images/          # Folder with BMP images used by the application
├── resources/           # Additional resources (icons, images)
├── tests/               # Test scripts
└── docs/                # Documentation
Coding Standards
To maintain code consistency:

Language: Use Python 3.x.

Style Guide: Follow PEP 8 style guidelines.

Indentation: Use 4 spaces per indentation level.

Comments: Write clear, concise comments where necessary.

Docstrings: Use docstrings for modules, classes, and functions.

python
Copy code
def function_name(parameters):
    """
    Brief description of the function.

    Args:
        param1 (type): Description.
        param2 (type): Description.

    Returns:
        type: Description.
    """
    # Function body
Imports: Group imports in the following order:

Standard library imports.
Related third-party imports.
Local application imports.
Use absolute imports over relative imports.

Commit Messages
Write meaningful commit messages to describe your changes:

Format:

css
Copy code
Short summary of the commit (50 characters max)

More detailed description if necessary. Wrap the body at 72 characters.
Guidelines:

Use the imperative mood ("Add feature" not "Added feature").
Reference issues or pull requests if applicable (e.g., "Fixes #123").
Branching Model
We recommend using the following branching strategy:

main Branch: Contains the stable codebase.

Feature Branches: Create branches for new features or bug fixes (e.g., feature/new-algorithm, bugfix/issue-456).

Pull Requests: Merge feature branches into main via pull requests after review.

License
By contributing, you agree that your contributions will be licensed under the MIT License.

Contact
If you have any questions or need further assistance:

GitHub Issues: https://github.com/jarch13/KataKrypt/issues
Email: You may contact the repository owner via GitHub.
Thank you for your interest in contributing to KataKrypt! Your efforts help make this project better for everyone.

Note: Please ensure that you have the necessary rights to contribute your code and that it does not infringe on any third-party rights.
