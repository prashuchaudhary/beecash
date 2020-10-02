# beecash

### Running Locally
* Install Python3.7 and pipenv **(for MacOS)** <br>
`brew install python3`
 <br>
`brew install pipenv`

* Clone the Repo and `cd` into the directory
* Setup virtual environment for this project <br>
`pipenv shell`

* Install all dependencies <br>
`pipenv install`

* Copy `.env.template` to `.env` and modify the various settings as per your system credentials

### Run server
* `invoke rs`
* go to `localhost:8000/`

### Swagger Docs
* Used Swagger to list all the APIs and their request and response bodies
* Local API Docs at http://localhost:8000/docs

### Folder Structure
* `repos` for any DB interaction
* `models` for defining DB Table structure
* `serializers` for request/response validation
* `interactors` for any Business Logic
* `views` for defining API handlers and processing Request/Response
* `urls` for routing request to given view method

### Design Details
* Using Django Rest Framework for providing crisp and thin API layers  
* Followed Interactor/Repo pattern    
