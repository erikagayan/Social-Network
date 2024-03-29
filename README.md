# Social-Network

## Features
In user blog api you can create a user, create posts, edit them and delete them, as well as liking yours or another author's posts. You can also see the analytics of how many likes were given in a certain period of time. And also a bot has been added that can create users, posts and give likes.

# Installation
1. Docker: [Install Docker](https://docs.docker.com/get-docker/)
- If you want to use PostgreSQL: [Install PostgreSQL](https://www.postgresql.org/download/)
2. Clone this repository to your local machine: https://github.com/erikagayan/Social-Network.git
3. Navigate to the project directory
4. Create `.env` file and define environmental variables by following '.env.sample'.
5. Build the Docker container using Docker Compose:`docker-compose build`
6. Access list of containers: `docker ps -a`
7. Create a superuser for accessing the Django admin panel and API: `docker exec -it <container_id here> python manage.py createsuperuser`
8. Start the Docker container: `docker-compose up` 
9. To stop the container, use: `docker-compose down`