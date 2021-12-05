# _DoorayApi_

Client package that can use Dooray API
* [https://helpdesk.dooray.com/share/pages/9wWo-xwiR66BO5LGshgVTg/2939987647631384419](https://helpdesk.dooray.com/share/pages/9wWo-xwiR66BO5LGshgVTg/2939987647631384419)

## _How to use_
### _Move the library to a directory recognized by python package ._
### _Write code in following to call Dooray Service Client API._

```python
# sample for get post detail
# GET /project/v1/projects/{project-id}/posts/{post-id}
# https://helpdesk.dooray.com/share/pages/9wWo-xwiR66BO5LGshgVTg/2939987647631384419

>>> from dooray_api import ServiceClient 
>>> host='https://api.dooray.com'
>>> request_headers={
    'Authorization': 'dooray-api {your-token}'
}
>>> project_id='{your-project-id}'
>>> post_id='{your-post-id}' 
>>> service_client=ServiceClient(
    host=host,
    request_headers=request_headers,
    ).project.v1.projects._(project_id).posts._(post_id).get()
>>> body, status_code=service_client.to_dict, service_client.status_code
>>> print(body)
...
...
 {'organizationMemberId': '2888709708850455062', 'name': '이재준', 'workflowId': '2888709710732876099'}}], 'cc': []}, 'workflowClass': 'registered', 'milestone': None, 'workflow': {'id': '8709710732876099', 'name': '등록'}}}
>>> print(status_code)
200
```

* Set host & request headers
  * default Content-Type: application/json
* Add the API address for the request through the dot.
  * If address containing a specific variable value is required, value is written with an underscore.
* Finally, create a client by creating a request type. [get, post, delete]
* ServiceClient object can check status_code and response body.