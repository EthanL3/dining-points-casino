# BU Dining Points Spinner

## Overview
The BU Dining Points Spinner is a Flask web app designed for Boston University students to earn free dining points by participating in surveys. After successfully completing a survey, students get the opportunity to spin a wheel for a chance to win additional dining points. This initiative aims to encourage student engagement with BU surveys while providing an exciting reward system.

## Features
- **User Authentication:** Secure login system to ensure that only BU students can access the spinner and surveys.
- **Survey Interface:** A clean and straightforward interface for students to fill out and submit surveys.
- **Spin the Wheel:** Once a survey is completed, students can spin the wheel to earn dining points.
- **Point Management:** Students can view their earned points and history of spins.

## Technologies
- **Flask:** A micro web framework written in Python, used for building the backend.
- **HTML/CSS:** For frontend development.
- **JavaScript:** For interactive elements like the spinning wheel.
- **SQLite:** A lightweight database to store user data and survey responses.

## Installation

To set up the project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/your-username/BU-Dining-Points-Spinner.git

# Navigate to the project directory
cd BU-Dining-Points-Spinner

# Install dependencies
pip install -r requirements.txt

# Run the Flask application
flask run
