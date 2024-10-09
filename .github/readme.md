# Task Tracker Setup Instructions

Follow these steps to set up the Task Tracker project on your local machine.

## Prerequisites

- Ensure you have Python 3.11.10 installed on your system.

## Setup Steps

1. **clone the repository:**
navigate to the directory where you want to store the Task Tracker project and run the following command:
    ```bash
    git clone https://github.com/DIRECTVIRUS/task_tracker.git
    ```
    This will create a new directory called `task_tracker` containing the project files.

2. **Navigate into the `task_tracker` directory:**
    ```bash
    cd task_tracker
    ```

3. **Create a virtual environment:**
    ```bash
    python3.11 -m venv venv
    ```

4. **Activate the virtual environment:**
    - **Linux:**
    ```bash
    source venv/bin/activate
    ```
    - **Windows:**
    ```bash
    .\venv\Scripts\activate
    ```

5. **Verify that the virtual environment is activated:**
    - **Linux:**
    ```bash
    which python
    ```
    - **Windows:**
    ```bash
    where python
    ```
    The output should be the path to the virtual environment's Python executable, e.g., `C:\path\to\task_tracker\venv\Scripts\python.exe` (Windows) or `/path/to/task_tracker/venv/bin/python` (Linux).

6. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

You are now ready to start using the Task Tracker project.

## **Running the Application**

To run the Task Tracker application, execute the following command:
```bash
python main.py
```

## **accessing the task tracker**

To access the Task Tracker application, open a web browser and go to the following URL:
```http://127.0.0.1:5000/``` or ```http://localhost:5000/```

You should now see the Task Tracker application in your web browser.

## **what you can do with the task tracker**

The Task Tracker application allows you to perform the following actions:
- Create a new task (task name and due date)
- View all tasks
- mark a task as complete
- delete a task
- see task status (complete, incomplete or overdue) using a colour key

## planned features
- allow users to add a description to task that can be viewed with a drop down
- allow users to filter tasks by status
- allow users to filter tasks by a due date range
- allow users to enter an edit mode to edit task details (name, due date, description)