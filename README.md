# Django 360

## Installation and launch

1. Clone repositories:
   ```bash
   git clone https://github.com/k0drin/Panorama.git
   ```
2. Go to the installed directory:
   ```bash
    cd Panorama
    ```
3. Install the virtual environment and activate it:
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
    ```
4. Install all dependencies:
   ```bash
    pip install -r requirements.txt
    ```
5. Perform migrations:
   ```bash
    python manage.py migrate
    ```
6. Create a super user:
   ```bash
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```bash
    python manage.py runserver
    ```
8. Create a panorama model in the admin panel:
   - **GET** `http://127.0.0.1:8000/admin/` — Django admin panel.

   ![image](https://github.com/k0drin/Panorama/assets/124861436/4ade76ce-b643-4adb-ac77-308f9b9a94f2)

   Press "Add panorama":
   ![image](https://github.com/k0drin/Panorama/assets/124861436/58419f3a-556d-45e6-800d-6be6613f81af)
   
   Then fill out all the fields and click "Save":
   ![image](https://github.com/k0drin/Panorama/assets/124861436/9dfedb14-5c28-40ab-9daa-9b316a5fc850)

9.Now everything is ready to enjoy the panorama:
      - **GET** `http://127.0.0.1:8000/walk_app/panorama/1/` — Our virtual tour.


## Using
1. To switch between panoramas use the blue marker:
   ![image](https://github.com/k0drin/Panorama/assets/124861436/715188ef-f7ee-411a-8c82-40820394e4b2)

2. To subscribe to the proposed newsletter, go to the desired URL address and fill out the form:
   - **GET** `http://127.0.0.1:8000/walk_app/subscription/` — Subscribes form.

   ![image](https://github.com/k0drin/Panorama/assets/124861436/408b9b6f-6ccd-47d5-974f-5de0c5eb4634)


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

