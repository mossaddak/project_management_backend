# balamzify-backend
All backend business logic seamlessly integrates with the <b>projectmanagement</b> project, a sophisticated Django application powered by Django REST Framework.

<b>Database design [click](https://dbdiagram.io/d/Project-management-6774712d5406798ef7047173)</b>

## API Document

    http://127.0.0.1:8000/api/docs


## Project Setup

**Setting up a virtualenv**

    cd ~
    python3 -m venv env
    source ~/env/bin/activate
    source venv/bin/activate


**Install the Python dependencies for the project**

    pip install -r requirements/development.txt


**Run the development server**

    python manage.py runserver 0:8000

You can now visit 127.0.0.1:8000 on your browser and see that the project is running.

---