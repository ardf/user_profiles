# User Profile Manager

This is a Django REST Framework project that allows users to create and update profiles through an API endpoint.

## Description

The project provides a Django API endpoint where authenticated users can create and update profiles. The profile includes fields such as name, email, bio, and profile picture. Users can send POST requests to create a new profile or PATCH requests to update existing profiles.

The project utilizes Django's authentication and authorization mechanisms to ensure that only authenticated users can create or update profiles.

## Installation

1. Clone the repository:

```
git clone <repository-url>
cd user_profiles
```

2. Install the dependencies using Poetry:

```
poetry install
```

3. Apply database migrations:

```
poetry install
```

4. Run the development server:

```
python manage.py migrate
```

5. Access the API endpoint at `http://localhost:8000/api/profile`.

## Usage

### Create a Profile

Send a POST request to `/api/profile` with the following JSON payload:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "bio": "Sample bio",
  "profile_picture": "<base64-encoded-image>"
}
```

### Update a Profile

Send a PATCH request to /api/profile/{profile_id} with the following JSON payload:

```json
{
  "name": "Updated Name",
  "bio": "Updated bio",
  "profile_picture": "<base64-encoded-image>"
}
```

Ensure that you include the appropriate authentication credentials in the request headers.

## Testing

To run the unit tests, use the following command:

```
python manage.py test
```
