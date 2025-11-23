# 🧭 Compass Route Tracker

## A Linked-List Navigation System built with Django

This project is a Django application designed to create, track, and summarize sequential navigation instructions, using a self-referencing model to form a linked list of route steps. It's ideal for planning multi-step journeys, particularly those involving directional travel and risk assessment.

## ✨ Key Features

* **Instruction Modeling:** Defines a route step with direction (N, SE, W, etc.), distance (in nautical miles), a risk level (0-100), and a description of the surroundings or hazards.
* **Linked List Structure:** Instructions are chained together using a self-referencing foreign key (`previous_instruction`) to define the sequence of the route. This allows any instruction to be the start of a new route or part of an existing chain.
* **Dynamic Route Summary:** The `Instruction` model includes a powerful method (`get_route_summary()`) that traverses the linked list backward from the current step to calculate the **total distance** traveled and the **average risk level** for that segment of the journey.
* **Data Validation:** Distance is enforced to be positive, and Risk Level is limited between 0 (safe) and 100 (deadly).
* **UI Helpers:** Includes methods to map directional codes (e.g., 'N') to rotation degrees (e.g., 0) for easy rendering of compass visuals in frontend templates.
* **Custom Forms:** The `InstructionForm` utilizes custom widgets like an HTML range input for `risk_level` and a `Textarea` with a placeholder for the `description`.

## 👨‍💻 The Team and Contributions

This project was built collaboratively by a team of three, specializing in distinct areas of the Django Model-View-Template (MVT) architecture.

| Role | Responsibility | Key Files Contributed |
| :--- | :--- | :--- |
| Soiman Vasile-Cristian | Project Configuration, URL Routing, and Server Setup. | `settings.py`, project-level `urls.py`, `wsgi.py`, `apps.py`. |
| Gramada Nicolae | Data Modeling, Validation, and Business Logic implementation. | `models.py`, `migrations/`. |
| Aerinei Lucian Ionut | User Interface (UI), Template Design, and Presentation Logic. | `templates/` (e.g., `compass.html`, `Home.html`, `instruction_detail.html`). |

The **`views.py`** and **`forms.py`** files served as the central integration point, ensuring seamless communication between the database, framework, and user interface.

## 🛠️ Project Setup

This project uses Django 5.2.8 and the default SQLite database.

### Prerequisites

* Python (3.x recommended)
* Django (5.2.x recommended)

### Installation and Run

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/SoimanVasile/coderun_django.git](https://github.com/SoimanVasile/coderun_django.git)
    cd coderun_django
    ```

2.  **Install Dependencies:**
    ```bash
    pip install django
    ```

3.  **Run Migrations:**
    This step creates the necessary database tables for the `compass` app.
    ```bash
    python manage.py makemigrations compass
    python manage.py migrate
    ```

4.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    The application will be accessible at `http://127.0.0.1:8000/`.

## 🗺️ Application Routes

The main entry points for the application are:

| URL Path | View Function | Name | Purpose |
| :--- | :--- | :--- | :--- |
| `/` | `first_page` | `home` | Renders the initial `Home.html` template. |
| `/compass/` | `compass_view` | `compass` | Lists all existing instructions and provides the form to add new steps. Handles the form submission (POST) and list display (GET). |
| `/instructions/<int:instruction_id>/` | `instruction_detail_view` | `instruction_detail` | Displays the full details for a single instruction and its corresponding route summary. |

## 📁 Code Structure

The project uses a standard Django layout with a main project (`coderun`) and a single application (`compass`).

### `compass` Application

| File | Description |
| :--- | :--- |
| **`models.py`** | Defines the core `Instruction` model, including direction choices, risk validation, and the linked list traversal logic (`get_route_summary`). |
| **`forms.py`** | Defines the `InstructionForm` based on the model, customizing widget appearances and setting the label/queryset for the self-referencing `previous_instruction` field. |
| **`views.py`** | Contains the request handlers for listing/adding instructions (`compass_view`), displaying individual steps with summaries (`instruction_detail_view`), and the homepage (`first_page`). |
| **`urls.py`** | Configures the path routing for the `compass` app. |
