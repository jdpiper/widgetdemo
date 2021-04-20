# Widget Demo

This project is a demo Django REST project to manage Widgets. A widget has a name and a number of parts, as well as an automatically
maintained created and modified date.

## Installing

First, ensure that you have [python3 and pipenv installed](https://docs.python-guide.org/dev/virtualenvs/) correctly. Once they are
working, run `pipenv shell` in the `widgetdemo` directory to switch to the project's environment.

Generate a random secret key, and edit `.env` to set it:

```shell
SECRET_KEY=django-insecure-y-000000000000000000000000000000000000000000000000
```

Run `./manage.py migrate` to generate the database.

Next, run `./manage.py createsuperuser` and follow the prompts to create an admin user.

Finally, if all of the previous commands completed successfully, run `./manage.py runserver`. A web server listening on
http://localhost:8000/ should launch. If everything is working correctly, you can now make requests to the `widgets` endpoint:

```shell
❯ curl -H 'Accept: application/json; indent=4' -u admin:ch4ng3m3 http://localhost:8000/api/widgets/
{
    "count": 0,
    "next": null,
    "previous": null,
    "results": []
}%
```

To create a new Widget, `POST` to the `widgets` endpoint:

```shell
❯ curl -X POST -d '{"name":"Widget #000","num_parts":10}' -H 'Content-Type: application/json' -H 'Accept: application/json; indent=4
{
    "id": 1,
    "name": "Widget #000",
    "num_parts": 10,
    "created": "2021-04-20T11:26:28.125847Z",
    "modified": "2021-04-20T11:32:35.026709Z"
}%
```

The new Widget should become visible in the list:

```shell
❯ curl -H 'Accept: application/json; indent=4' -u admin:ch4ng3m3 http://localhost:8000/api/widgets/
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Widget #000",
            "num_parts": 10,
            "created": "2021-04-20T11:26:28.125847Z",
            "modified": "2021-04-20T11:26:28.125882Z"
        }
    ]
}%
```

You can also fetch the details of a single widget:

```shell
❯ curl -H 'Accept: application/json; indent=4' -u admin:ch4ng3m3 http://localhost:8000/api/widgets/1/
{
    "id": 1,
    "name": "Widget #000",
    "num_parts": 10,
    "created": "2021-04-20T11:26:28.125847Z",
    "modified": "2021-04-20T11:26:28.125882Z"
}
```

To update an existing Widget, use the `PUT` method:

```shell
❯ curl -X PUT -d '{"name":"Widget #000","num_parts":20}' -H 'Content-Type: application/json' -H 'Accept: application/json; indent=4' -u admin:ch4ng3m3 http://localhost:8000/api/widgets/1/
{
    "id": 1,
    "name": "Widget #000",
    "num_parts": 20,
    "created": "2021-04-20T11:26:28.125847Z",
    "modified": "2021-04-20T11:32:35.026709Z"
}%
```

Finally, to delete an existing Widget, use the `DELETE` method:

```shell
❯ curl -X DELETE -H 'Content-Type: application/json' -H 'Accept: application/json; indent=4' -u admin:ch4ng3m3 http://localhost:8000/api/widgets/1/
❯ curl -H 'Accept: application/json; indent=4' -u admin:ch4ng3m3 http://localhost:8000/api/widgets/
{
    "count": 0,
    "next": null,
    "previous": null,
    "results": []
}%
```

## Web Interfaces

In addition to the programmatic endpoints, an admin UI, API frontend and an OpenAPI spec are available. The Admin UI can be found at
http://localhost:8000/admin/. The API frontend can be found by navigating to http://localhost:8000/api/. The OpenAPI spec can be
found at http://localhost:8000/openapi.
