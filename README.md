# AirBnB clone - The console

## About this project
This is the first step towards building the full web application: the AirBnB clone. What is built in this project will be used with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

## Features

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Technology

Python, OOP


## Usage/Examples

The entry point into the program is through the console. You do this by running the file `./console.py` at the root directory of the project. A `(hbnb)` prompt is displayed immediately:

```python
AirbNb_clone# ./console.py
(hbnb)
```

In this example, we will look at user management within the program.

### Creating a user
A user object can be created using the `create User` command. Note that the 'U' in "User" is uppercase. The prompt wil display the newly created user's ID.
```python
(hbnb) create User
2960cd8b-fc52-4156-9ba2-5f9f5425f469
(hbnb)
```
### View user
To view a user, use the command `User.show(<user_id>), using the particular user's ID. This will show the user's metadata:
```python
(hbnb) User.show("2960cd8b-fc52-4156-9ba2-5f9f5425f469")
[User] (2960cd8b-fc52-4156-9ba2-5f9f5425f469) {'id': '2960cd8b-fc52-4156-9ba2-5f9f5425f469', 'created_at': datetime.datetime(2023, 7, 16, 12, 55, 1, 478662), 'updated_at': datetime.datetime(2023, 7, 16, 12, 55, 1, 478668)}
(hbnb)
```
Alternatively, you might want to view all the users. For this, use the command `User.all()`. This will display a list of all the users created:
```python
(hbnb) User.all()
["[User] (2960cd8b-fc52-4156-9ba2-5f9f5425f469) {'id': '2960cd8b-fc52-4156-9ba2-5f9f5425f469', 'created_at': datetime.datetime(2023, 7, 16, 12, 55, 1, 478662), 'updated_at': datetime.datetime(2023, 7, 16, 12, 55, 1, 478668)}", "[User] (c71c5ddb-ba12-44ef-abd9-36aa5cc59dbc) {'id': 'c71c5ddb-ba12-44ef-abd9-36aa5cc59dbc', 'created_at': datetime.datetime(2023, 7, 16, 13, 4, 32, 804515), 'updated_at': datetime.datetime(2023, 7, 16, 13, 4, 32, 804521)}"]
(hbnb)
```
### Count users
You may want to know the number of users created. You can user the command `User.count()` to display this statistic:
```python
(hbnb) User.count()
2
(hbnb)
```
### Update user attributes
You can further update/add attributes to an existing user. This can be done in two ways: one attribute at a time, or multiple attributes using a dictionary.

#### Single Attribute Update
To update a single attribute at a time, use this command, providing the user ID, the attribute you wish to modify/add and the new value for that attribute:
```python
(hbnb) User.update("2960cd8b-fc52-4156-9ba2-5f9f5425f469" "first_name" "James")
(hbnb)
```
You can verify that this user's first_name attribute has been updated/added:
```python
(hbnb) User.show("2960cd8b-fc52-4156-9ba2-5f9f5425f469")
[User] (2960cd8b-fc52-4156-9ba2-5f9f5425f469) {'id': '2960cd8b-fc52-4156-9ba2-5f9f5425f469', 'created_at': datetime.datetime(2023, 7, 16, 12, 55, 1, 478662), 'updated_at': datetime.datetime(2023, 7, 16, 13, 13, 51, 572849), 'first_name': 'James'}
(hbnb)
```
#### Multiple Attribute Update
You can as well update/add multiple attributes at once. This is done using aby passing the user ID and a dictionary containing the attributes to update/add. See example:
```python
(hbnb) User.update("2960cd8b-fc52-4156-9ba2-5f9f5425f469" {"last_name": "Okwaro", 'age': 39})
(hbnb) User.show("2960cd8b-fc52-4156-9ba2-5f9f5425f469")
[User] (2960cd8b-fc52-4156-9ba2-5f9f5425f469) {'id': '2960cd8b-fc52-4156-9ba2-5f9f5425f469', 'created_at': datetime.datetime(2023, 7, 16, 12, 55, 1, 478662), 'updated_at': datetime.datetime(2023, 7, 16, 13, 21, 17, 774417), 'first_name': 'James', 'last_name': 'Okwaro', 'age': '39'}
(hbnb)
```
The attributes 'last_name' and 'age' and their corresponding values are now included as part of the user's attributes.

### Delete user
A user can be deleted from the program using the command `User.destroy(<user_id>) and passing the user's ID. We are going to delete user James (ID: 2960cd8b-fc52-4156-9ba2-5f9f5425f469) from our program:
```python
hbnb) User.all()
["[User] (2960cd8b-fc52-4156-9ba2-5f9f5425f469) {'id': '2960cd8b-fc52-4156-9ba2-5f9f5425f469', 'created_at': datetime.datetime(2023, 7, 16, 12, 55, 1, 478662), 'updated_at': datetime.datetime(2023, 7, 16, 13, 21, 17, 774417), 'first_name': 'James', 'last_name': 'Okwaro', 'age': '39'}", "[User] (c71c5ddb-ba12-44ef-abd9-36aa5cc59dbc) {'id': 'c71c5ddb-ba12-44ef-abd9-36aa5cc59dbc', 'created_at': datetime.datetime(2023, 7, 16, 13, 4, 32, 804515), 'updated_at': datetime.datetime(2023, 7, 16, 13, 4, 32, 804521)}"]
(hbnb) User.destroy("2960cd8b-fc52-4156-9ba2-5f9f5425f469")
(hbnb) User.all()
["[User] (c71c5ddb-ba12-44ef-abd9-36aa5cc59dbc) {'id': 'c71c5ddb-ba12-44ef-abd9-36aa5cc59dbc', 'created_at': datetime.datetime(2023, 7, 16, 13, 4, 32, 804515), 'updated_at': datetime.datetime(2023, 7, 16, 13, 4, 32, 804521)}"]
```

## Authors

- [@devKiratu](https://github.com/devKiratu)
- [@jarabi](https://github.com/Jarabi)
