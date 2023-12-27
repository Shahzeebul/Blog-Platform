# Blog-Platform
The provided code and instructions offer a solid foundation for a simple blog platform using Flask. Here's a breakdown of the key components and steps:

### Back-End (Flask App):

1. Install Flask:
   - Flask is a lightweight web framework for Python. The installation is done using `pip install Flask`.

2. Create a Flask App (`app.py`):
   - The Flask app is the core of the back-end. It includes route definitions for rendering the home page and handling post creation.
   - Two routes are defined:
     - `/`: Renders the home page, displaying existing blog posts.
     - `/create`: Handles both GET (rendering the creation form) and POST (processing form submission) requests.

3. Run the Flask App:
   - By running the Flask app (`python app.py`), the development server is started, and the blog platform becomes accessible locally.

### Front-End (HTML/CSS with Jinja Templating):

4. Templates Folder:
   - The `templates` folder is created to store HTML templates. Flask automatically looks for templates in this folder.

5. HTML Templates:
   - Two HTML templates are created:
     - `index.html`: Displays the home page with a list of existing blog posts and a link to create a new post.
     - `create.html`: Provides a form for creating a new blog post.

### Key Concepts:

- Jinja Templating:
  - Jinja templating is used for dynamic content rendering in HTML. This allows the integration of Python code within HTML templates.

- Form Handling:
  - Form data is submitted via POST requests, and Flask's `request` object is used to retrieve form data for post creation.

- Redirects:
  - After successfully creating a post, the user is redirected to the home page to view the updated list of posts.

