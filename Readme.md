## Start up
 - install docker https://docs.docker.com/engine/install/
 - clone repo `git clone https://github.com/Singrity/testtask_ucar.git`  
 - copy template from `.env_example` to `.env` file
 - configure variables in `.env` for your db creds
 - run application `docker compose -f docker_compose.yml up --build -d`
 - check status of containers `docker ps` - should see 2 containers UP incident_api_service and postgresql
 - visit http://localhost/docs to try api methods
## Existing endpoints

### /create_incident
#### summary=Creates an incident
#### description=Create a new incident! status - only allow: 'normal', 'asap', 'blocking',source - only allow: 'operator', 'monitoring', 'partner'
#### Example request:
curl -X 'POST' \
  'http://localhost/create_incident' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "description": "string",
  "status": "normal",
  "source": "operator"
}'
#### Example response:

Code	\
201 \
Response body \
Download
{
  "id": "9771aa0a-ee45-47fa-aa71-9d3c674d287e",\
  "description": "string",\
  "status": "normal",\
  "source": "operator",\
  "created_at": "2025-11-10T12:43:05.316806",\
  "updated_at": null\
} \
Error - 422	
Validation Error \
error triggers if status or source not in allow list

### /get_incidents_by_status
#### summary="Get a list of incidents by status filter"
#### description="Returns list of all incidents filtered by status"
#### Example request:
curl -X 'GET' \
  'http://localhost/get_incidents_by_status?status=normal' \
  -H 'accept: application/json'

#### Example response:
Code \
200	\
Response body \

[ \
  { \
    "id": "ffa43202-c602-4e69-98ae-0785786841d4", \
    "description": "bla bla", \
    "status": "normal", \
    "source": "operator", \
    "created_at": "2025-11-10T00:00:00", \
    "updated_at": "2025-11-10T12:17:46.301850" \
  } \
] 

Error - 422	
Validation Error \
error triggers if status not in allow list

### /update_incident
#### summary="Update an existing incident by id"
#### description="Update an existing incident by id. Returns updated incident! status - only allow: 'normal', 'asap', 'blocking', source - only allow: 'operator', 'monitoring', 'partner'
#### Example request:
curl -X 'PUT' \
  'http://localhost/update_incident?incident_id=ffa43202-c602-4e69-98ae-asd' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  
}'

#### Example response:
200	
Successful Response \
{ \
  "id": "string", \
  "description": "string", \
  "status": "normal", \
  "source": "operator", \
  "created_at": "2025-11-10T09:54:39.934Z", \
  "updated_at": "2025-11-10T09:54:39.934Z" \
} 

Error 404 \
Not Found \
Response body \
{ \
  "detail": "Incident with id 'ffa43202-c602-4e69-98ae-asd' not found." \
}

Error 422 Validation Error
triggers when source or status not in allow list

