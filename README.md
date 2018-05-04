# doctor-reviews-service
* A service which creates, retrieves, and updates comments for a given doctor.  

## Endpoints

`POST /comment/`  
Creates a comment for a doctor, returns a list of recommended doctors.  

* example request body: 
```
{
	"doctor_id": 1, 
	"comment_body": "Great doctor!", 
	"rating": 5, 
	"author_id": 2,
	"active": True
}
``` 
* example response:: 
```
[
  {
    "address": 123 Main St. Los Angeles, CA 90016,
    "created_at": "Thu, 03 May 2018 22:16:23 GMT",
    "group_id": "2",
    "id": 1,
    "latitude": 90,
    "longitude": 90,
    "name": "Dr. Ben",
    "specialties": [],
    "updated_at": null
  },
  {
    "address": 123 Main St. Los Angeles, CA 90016,
    "created_at": "Thu, 03 May 2018 22:16:23 GMT",
    "group_id": "2",
    "id": 2,
    "latitude": 80,
    "longitude": 80,
    "name": "Dr. Ali",
    "specialties": [],
    "updated_at": null
  } 
]
```  

* `GET /comment/<int:comment_id>`
Retrives a doctor's comment by id.

* example response: 
```
{
  "active": true,
  "author_id": 2,
  "comment_body": "This doc was great!",
  "created_at": "Thu, 03 May 2018 22:16:23 GMT",
  "doctor_id": 2,
  "id": 1,
  "rating": 5,
  "updated_at": "Fri, 04 May 2018 00:59:32 GMT"
}
``` 

* `PUT /comment/<int:comment_id>`
Updates a doctor's comment by id. 

* example request body: 
```
{
  "active": false,
}

 example response: 
```
{
  "active": false,
  "author_id": 2,
  "comment_body": "This doc was great!",
  "created_at": "Thu, 03 May 2018 22:16:23 GMT",
  "doctor_id": 2,
  "id": 1,
  "rating": 5,
  "updated_at": "Fri, 04 May 2018 00:59:32 GMT"
}  
```

## Testing

Run tests with `python -m pytest`

## Database Changes

### adding a migration

`FLASK_APP=app.app:flask_app python -m flask db migrate`  

### running migrations

`FLASK_APP=app.app:flask_app python -m flask db upgrade`

### reverting a migration

`FLASK_APP=app.app:flask_app python -m flask db downgrade`

## Manual Dev Setup

### software

`pip install -r requirements.txt`

`brew install mysql` (and run the command to autorun)

### database

Migrate the database

* `FLASK_APP=app.app:flask_app python -m flask db upgrade`

### run a local server
* run `FLASK_APP=app.app:flask_app python -m flask run`


## Author
* Ali Tycast
