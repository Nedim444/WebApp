# WebApp
How I use Anaconda Prompt, first step is based on defining environment.
conda create -n ex #where 'ex' is the name of your new conda environment

Afer we define environment, we need to activate them.
conda activate ex

Install django
conda instal -c conda-forge django

Create project
django-admin createproject 'project'

Create app in project directory
python manage.py startapp 'app' For this task I use visual code editor because I never use Swagger.

Steps in Visual Code Editor

Add app in setings.py "INSTALED APPS". After that, we can change database, in PostgreSQL or MySQL. By Default is sqlite3.
Add path from app in urls.py of project.
Define new urls.py file in app folder.
Create models in models.py. We create models which are based on SQL tables.
After we make models, we apply function for creating tables in django
python manage.py makemigrations python manage.py migrate Now, we have table which we use in next steps. In this task, we use function for ordinary operation. However, this operation we can perform using django admin site.

Create function in views.py for different operatons. For example we create function for create, update, edit, delete information and function for sorting and show all information about entity.
Define path from all function in urls.py file.
Create forms.py file in app and make class forms for our entity. We will use that forms class for performin function form view.
On the end of first task, we need define templates. That templates will use html language.
I create just one template for add transaction like example applying this function.
Last step will set our task on github

Create repisotory
Clone our file
