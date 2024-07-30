# SkillAegis
<img alt="SkillAegis Logo" align="right" src="application/skillaegis-logo.svg"/> 

**SkillAegis** is a platform to design, run, and monitor exercise scenarios, enhancing skills in applications like MISP and training users in best practices for information management and protective tools. Its gamification system makes learning engaging and effective, ensuring users acquire essential technical skills and adhere to industry standards.


## Features

- **Create Exercise Scenarios**: Design and customize various training exercises tailored to your needs.
- **Run Exercises**: Deploy scenarios and manage sessions with real-time execution.
- **Live Dashboard**: Monitor progress and performance with the live dashboard, providing instant insights and analytics.

## Installation

To get started with SkillAegis, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/SkillAegis.git
    ```
2. Navigate to the project directory:
    ```bash
    cd SkillAegis
    ```
3. Initialize the submodules
    ```bash
    git submodule update --init --recursive
    ```

## Project Structure

The project is composed of two application:

1. **SkillAegis Editor**: The scenario builder to create new training exercises.
2. **SkillAegis Dashboard**: Start a training session and keep track of participants' progress in real-time.

## Usage
1. Start the main web server
```bash
python3 SkillAegis.sh
```

## SkillAegis Editor
The **Edditor** can be used to design or edit scenario.

## SkillAegis Dashboard
The **Dashboard** can be used to run a training session and visualize the progress of participants in real-time

## Contributing

We welcome contributions from the community. To contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request.
.
