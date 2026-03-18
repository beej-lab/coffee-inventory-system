\# Coffee Shop Inventory System



A Django-based inventory management system designed for small coffee shops.

This application helps track ingredients, products, and stock levels to ensure efficient inventory management.



---



\## Features



\* Manage inventory items (coffee beans, milk, syrups, cups, etc.)

\* Track stock quantities

\* Record stock movements (incoming and outgoing)

\* Organize items by category

\* Admin dashboard for easy management

\* Basic reporting for stock levels



---



\## Tech Stack



\* Python

\* Django

\* SQLite (default Django database)

\* Git for version control



---



\## Project Structure



```

coffee-inventory-system/

│

├── .venv/                  # Virtual environment (not committed)

├── inventory/              # Django app for inventory management

├── core/                   # Django project configuration

│

├── manage.py

├── requirements.txt

├── .gitignore

└── README.md

```



---



\## Setup Instructions



\### 1. Clone the repository



```

git clone https://github.com/beej-lab/coffee-inventory-system.git

```



\### 2. Navigate into the project folder



```

cd coffee-inventory-system

```



\### 3. Create a virtual environment



```

python -m venv .venv

```



\### 4. Activate the virtual environment



Windows PowerShell:



```

.venv\\Scripts\\Activate

```



\### 5. Install dependencies



```

pip install -r requirements.txt

```



\### 6. Apply database migrations



```

python manage.py migrate

```



\### 7. Start the development server



```

python manage.py runserver

```



Then open your browser and go to:



```

http://127.0.0.1:8000

```



---



\## Future Improvements



\* Low stock alerts

\* Inventory dashboard

\* Supplier tracking

\* Sales and usage reports

\* REST API for integration with POS systems



---



\## Author



Bezalel



