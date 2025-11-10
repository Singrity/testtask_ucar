## Start up
 - install docker https://docs.docker.com/engine/install/
 - clone repo `git clone https://github.com/Singrity/testtask_ucar.git`  
 - copy template from `.env_example` to `.env` file
 - configure variables in `.env` for your db creds
 - run application `docker compose -f docker_compose.yml up --build -d`
 - check status of containers `docker ps` - should see 2 containers UP incident_api_service and postgresql
 - visit http://localhost/docs to try api methods