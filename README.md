
A web course exercise which involves creating a website akin to [https://www.varzesh3.com/](https://www.varzesh3.com/), a sports news platform.

This repo is backend side

---

**Setting up the React-Django Project**

1. **Install Django REST framework in Django:**
   Navigate to your Django project directory (here referred to as `react-django`) and run:
   ```
   pip install djangorestframework
   ```

2. **Load Fixtures in Django:**
   To load the fixtures, use the following command within the Django project directory:
   ```
   python manage.py loaddata leads
   ```

3. **Setting up the React Application:**
   Navigate to your React application directory (here referred to as `react-app`) and perform the following installations:

   - Install React, ReactDOM, and PropTypes:
     ```
     npm install react react-dom prop-types --save-dev
     ```
   - Install `weak-key` for development:
     ```
     npm install weak-key --save-dev
     ```

4. **Configure the Proxy in `package.json` for React:**
   In the React application's `package.json` file, add the following line to set up a proxy to your Django server:
   ```json
   "proxy": "http://localhost:8000"
   ```

   This proxy configuration is important for facilitating communication between your React frontend and Django backend during development.



