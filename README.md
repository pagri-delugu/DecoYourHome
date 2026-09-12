# DecoYourHome

## About our Project

**This is our course completion website coding project for Interior design and furnishing business, using Django/Python for the UX, and HTML/CSS for the UI 😀**

We hope you enjoy it! This project is free to clone and edit in your own way.

Some useful informations below:
- Tools/Languages we used: 
    + Claude, ChatGPT *for better support and template designs*
    + Bootstrap 5.3.8 *for basic components and a better range of frontend options in case CSS is not optimized*
    + Python, HTML, CSS *as our main programming languages*
    + *Other tools in requirements.txt*

- The template's primary language is **VIETNAMESE**

- This project can be further improved with better Django techniques and tools 

## Guides to deploying the Project

### Virtual Environment

Since we use Django as the project's framework and also other tools, it would be better if you have the virtual environment to deploy and perform testing on your local computer.

- First, create a folder *(root directory)* and clone the project into it. When finished cloning the project, open Visual Studio Code terminal or OS terminal at the root directory. **To setup virtual environment and install all the other tools along with Django, type these following commands**:

    ```bash
    python -m venv env
    pip install -r requirements.txt
    ```

- Then, if you see an **"env" folder** at the root directory, and **all the tools required installed at "\env\Lib\site-packages"**, the environment setup is done and you can **activate it (if not automatically activated) via the following command:**

    ```bash
    # Windows
    env\Scripts\activate

    # MacOS / Linux
    source env/bin/activate
    ```

- Finally, you can run the project with **```python manage.py runserver```** to view the templates, or edit the files in the way you want.

### Admin Login

We suggest the username and password below:

- Username: **thebigadmin**
- Password: **sasalele@big2026**

*You can create your own by ```python manage.py createsuperuser```*
## Credits

- Project Manager: **Tan Phuc** (pagri-delugu)
- Collaborator: **minhphucx** 
- Supervising Teacher: **Mr. Nguyen Anh Trong**

This project is a part of our studies at class ***TE-C-PA-1518-2023LTWD-0011, TEKY Academy, Vietnam***

Finished in September, 2026

