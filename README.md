# Django 360

## Installation and launch

1. Clone repositories:
   ```bash
   git clone https://github.com/k0drin/Panorama.git
   ```
2. Install the virtual environment and activate it:
   ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
    ```
3. Install all dependencies:
   ```bash
    pip install -r requirements.txt
    ```
4. Perform migrations:
   ```bash
    python manage.py migrate
    ```
5. Start the development server:
   ```bash
    python manage.py runserver
    ```

## Using

### Endpoints

- **GET** `http://localhost:8000/` — Subscription page (home).
- **GET** `http://127.0.0.1:8000/walk_app/panorama/1/` — Virtual reality tour.
- **GET** `http://127.0.0.1:8000/walk_app/subscription/` — Subscription page.

### Examples of requests

- Subscribe to the newsletter:
 ```http
 GET http://127.0.0.1:8000/walk_app/subscription/
 ````
- Оstart virtual tour":
 ```http
 GET http://127.0.0.1:8000/walk_app/panorama/1/
 ```
## Data structure

Example model for markers:
```python
class Marker(models.Model):
    panorama = models.ForeignKey(
        Panorama, related_name="markers", on_delete=models.CASCADE
    )
    x_coordinate = models.FloatField()
    y_coordinate = models.FloatField()
    tooltip_text = models.CharField(max_length=200)
    linked_panorama = models.ForeignKey(
        Panorama,
        related_name="linked_markers",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

