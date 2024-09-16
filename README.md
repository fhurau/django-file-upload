# Django File Upload Project

This project is a simple **Django-based file upload application** that allows users to upload files with validation on file type and size. The form uses Bootstrap for styling to make it responsive and user-friendly.

## Features

- **File Upload Form**: Allows users to upload files such as images or documents.
- **File Validation**: Ensures that the uploaded file meets the following criteria:
  - Maximum file size of 5MB
  - Accepted file types: JPEG, PNG, and PDF
- **Success & Error Messages**: Displays a success message when the file is uploaded successfully and shows error messages if the validation fails.
- **Bootstrap Integration**: The form uses Bootstrap for a modern, responsive design.

## Getting Started

### Prerequisites

- Python 3.x
- Django 5.x or higher

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/django-file-upload.git
   cd django-file-upload
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: .\env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install django
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Django development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the file upload form**:
   Open your browser and go to `http://127.0.0.1:8000/uploads/upload/` to view the form.

### Usage

- Navigate to the file upload page.
- Upload a file (JPEG, PNG, or PDF under 5MB).
- If the file passes validation, a success message will be displayed.
- If the validation fails, an error message will indicate the issue (e.g., file type or size).
