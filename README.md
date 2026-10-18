# Django REST Framework (DRF) Fundamentals & Core Concepts

This repository contains my daily practice files and projects as I learn Django REST Framework to build powerful and robust Web APIs.

## 🚀 Topics Covered

* **DRF Introduction:** Understanding Web APIs, serializers, and the browsable API interface.
* **Views & URLs:** Implementing API views (`@api_view`) and mapping URL paths.
* **Authentication:** Setting up built-in DRF login/logout and user authentication routes (`api-auth/`).

## 📁 File Structure

* **drf-day-01** — API Setup & Authentication: Initialized DRF environment, configured URL routing, and integrated browsable API authentication endpoints.
* **`drf-day-02`** — Complex Data & Admin Customization: Created `rest_api` app, configured complex models (`Aiquest`) with custom fields, installed Pillow for image handling, and customized Django admin panel with `list_display`.
* **`​drf-day-03`** — Model Serializers & Queryset Rendering: Created custom AiquestSerializer, configured function-based views to render complete querysets and individual model instances (pk) into JSON format using JSONRenderer and HttpResponse.
* **`drf-day-04`** — External API Consumption: Created standalone Python script using the requests library to fetch and render JSON data from the Django REST API endpoint. 
* **`​drf-day-05`** — Deserialization & Data Creation: Created custom AiquestSerializer with a create() method, configured function-based views with csrf_exempt and JSONParser to handle incoming JSON POST requests, validate incoming data, and save new model instances to the database.
* **`drf-day-06`** — External Deserialization & Data Insertion: Created a standalone Python script to send external JSON POST requests, process deserialization, and successfully persist new model instances into the database. 
* **`drf-day-07`** — Data Update Operations & API Integration: Implemented function-based views to handle HTTP PUT requests for updating existing model records, configured request body stream parsing, validated incoming serialization data, and developed an external Python script to send structured JSON payloads for seamless database updates. 
* **`​drf-day-08`** — Data Deletion Operations & External Testing: Implemented function-based views to handle HTTP DELETE requests for removing specific database records, configured @csrf_exempt and byte-stream JSON parsing to safely process incoming client data, and developed an external Python script (delete.py) utilizing requests.delete(json=data) for robust API communication and automated deletion testing. 
* **`drf-day-09`** — Function-Based GET APIs & Dynamic Routing: Implemented custom function-based views using @api_view(['GET']) to handle HTTP GET requests, configured dynamic URL routing for collection listing and single-record retrieval via primary key (pk), and utilized DRF serializers for JSON responses. 
* **`​drf-day-10`** — Function-Based POST APIs & Data Validation: Implemented custom function-based views using @api_view(['POST']) to handle incoming client data, utilized DRF serializers for request data parsing, validation (is_valid()), and database insertion with proper success/error JSON responses.
* **`​drf-day-11`** — Function-Based PUT & PATCH APIs: Implemented custom function-based views using @api_view(['PUT', 'PATCH']) to handle full and partial resource updates, retrieved records via primary key (pk), utilized DRF serializers for validation and data persistence, and returned appropriate success JSON responses. 
* **`​drf-day-12`** — Function-Based DELETE API: Implemented custom function-based views using @api_view(['DELETE']) to handle resource deletion, retrieved specific records via primary key (pk), performed database object deletion (.delete()), and returned appropriate success JSON responses.
* **`drf-day-13`** - Class-Based APIViews: Implemented custom Class-Based Views (APIView) in Django REST Framework to handle multiple HTTP methods (GET, POST, PUT, PATCH, DELETE) within a single class, utilized serializers for data validation and transformation, and returned structured JSON responses.
* **`drf-day-14`**- ListModelMixin & GenericAPIView: Implemented ListModelMixin along with GenericAPIView in Django REST Framework to efficiently retrieve and list database records, configured queryset and serializer_class, and returned structured JSON responses.
* **`​drf-day-15`** - CreateModelMixin & GenericAPIView: Implemented CreateModelMixin along with GenericAPIView in Django REST Framework to efficiently handle HTTP POST requests, validate incoming data using serializers, and create new database records with structured JSON responses. 
* **`drf-day-16`** - RetrieveModelMixin & GenericAPIView: Implemented RetrieveModelMixin along with GenericAPIView in Django REST Framework to efficiently retrieve specific database records by primary key, configured queryset and serializer_class, and returned structured JSON responses.
* **`drf-day-17`** - UpdateModelMixin & GenericAPIView: Implemented UpdateModelMixin along with GenericAPIView in Django REST Framework to handle HTTP PUT requests, validate and update existing database records by primary key (`pk`), and return updated structured JSON responses.
* **`drf-day-18`** — DestroyModelMixin & GenericAPIView: Implemented DestroyModelMixin along with GenericAPIView in Django REST Framework to handle HTTP DELETE requests, securely remove specific database records by primary key (pk), and return a 204 No Content structured response.
* **`​drf-day-19`** — CRUD Operations using ModelMixins & GenericAPIView: Combined ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, and DestroyModelMixin with GenericAPIView in DRF to handle full CRUD operations efficiently with clean URL routing.  

 
 

## 🛠️ Environment

* **IDE:** Visual Studio Code
* **Language:** Python 3
* **Framework:** Django & Django REST Framework (DRF)
