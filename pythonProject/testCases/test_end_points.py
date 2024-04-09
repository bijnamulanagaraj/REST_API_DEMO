import logging

import pytest
from http import HTTPStatus

from utilities.API_Logger import LogGen
from testCases.confest import test_api
from API_List.Test_APIS import List_of_APIS

logger = LogGen.loggen()

@pytest.mark.parametrize( "first_name, last_name, email",
    [
        ("Janet", "Weaver", "janet.weaver@reqres.in")
    ],)

@pytest.mark.first_name
def test_get_singleuser_para(test_api,first_name,last_name,email):
    logger.info("***** verifying User first_name *****")
    end_ponits_before_0 = List_of_APIS.single_user

    params = {
        "user_name" : "nagaraj"
    }
    response = test_api.get(end_ponits_before_0,params)
    data = response.json()

    name = data.get('data', {}).get('first_name', '')

    if name == first_name:
        assert True
        logging.info("***** first_name is passed *****")
    else:
        logging.info("***** first_name is not passsed")
        assert False

    logger.info("***** user first_name validated *****")

@pytest.mark.userlist
def test_get_user_list(test_api):
    logger.info("***** verifying User list *****" )
    end_ponits_0 = List_of_APIS.user_list
    params = {"page" : 1}
    response = test_api.get(end_ponits_0,params) # calling GET request to get the user list
    data = response.json()  #storing the response in json format
    logger.info(f'the api response {data}')

    if response.status_code == HTTPStatus.OK:  # validating whether the status code is 200
        assert True
        logging.info("***** response code 200 is passed")
    else:
        logger.error("*** response code 200 is failed ")
        assert False

    assert response.json()  # validating whether the response in json format
    print(response.content)
    print(response.status_code)
    print(response.headers)
    print(response.url)

    logger.info("***** User list validated t*****")



@pytest.mark.singleuser
def test_get_single_user(test_api):
    logger.info("***** verifying single user *****")
    end_ponits_1 = List_of_APIS.single_user
    expected_text = "To keep ReqRes free, contributions towards server costs are appreciated!"  # storing the response in a variable for assertion
    response = test_api.get(end_ponits_1)
    data = response.json()
    logger.info(f"API response {data}")
    support_text = data.get('support', {}).get('text', '')  # sorting the required text in a variable for the assertion

    if support_text == expected_text:  # validating whether the condition is true or not
        assert True
        logging.info("***** Usertext is passed")
    else:
        logging.error("***** Usertext is not passed")
        assert False

    assert response.status_code == 200
    print(response.content)
    print(response.status_code)
    print(response.headers)
    print(response.url)

    logger.info("***** SingleUser is validated *****")



@pytest.mark.usernotfound
def test_user_not_found(test_api):
    logger.info("***** verifying user_not_found *****")
    end_ponits_2 = List_of_APIS.user_not_found
    response = test_api.get(end_ponits_2)
    assert response.status_code == 404
    assert response.status_code != 200  # validating whether the obtained status code is not equal to 200

    print(response.content)
    print(response.status_code)
    print(response.headers)
    print(response.url)

    logging.info("***** user_not_found is validated")



@pytest.mark.createuser
def test_createUser(test_api):
    logging.info("***** verifying new_user is created *****")
    body = {  # storing the json content in a variable to pass to the request
        "name": "niyog",
        "job": "qa",
        "Content-Type": "application/json"
    }



    job = 'qa'  # storing the text in a variable for assertion
    name = 'niyog'
    end_ponits_3 = List_of_APIS.create_user
    response = test_api.post(end_ponits_3,body) #calling put method

    data = response.json()
    expectedname = data.get('name')
    expectedjob = data.get('job')
    assert expectedjob == job
    assert response.status_code == 201

    if expectedname == name:
        assert True
        logging.info("***** creating new_user test is passed *****")
    else:
        logging.error("***** creating new_user test is not passed*****")
        assert False

    print(response.json())
    print(response.content)
    print(response.status_code)
    print(response.headers)
    print(response.url)

    logging.info("***** creating new_user is validated *****")


@pytest.mark.updateuser
def test_update_existing_user(test_api):
    logging.info("***** verifying update_existing_user *****")
    body = {
        "name": "morpheus",
        "job": "zion resident",
        "Content-Type": "application/json"
    }
    name = 'morpheus'
    job = 'zion resident'
    end_ponits_4 = List_of_APIS.single_user
    response = test_api.put(end_ponits_4,body) # calling PUT method
    data = response.json()
    expectedname = data.get('name')
    expectedjob = data.get('job')
    assert expectedname == name
    print(response.json())

    if expectedjob == job:
        assert True
        logging.info("***** update_existing_user test is passed *****")
    else:
        logging.error("***** update_existing_user test is not passed*****")
        assert False

    logging.info("***** update_existing_user is validated *****")



@pytest.mark.deleteuser
def test_delete_existing_user(test_api):
    logging.info("***** verifying delete_existing_user *****")
    end_ponits_5 = List_of_APIS.single_user
    response = test_api.delete(end_ponits_5) #calling delete method

    assert response.status_code == 204
    assert response.status_code != 200
    print(response)

    logging.info("***** delete_existing_user is validated")


@pytest.mark.sigNupuser
def test_signUp_user(test_api):
    logging.info("***** verifying user_signUp Sucessfully *****")
    body = {
        "email": "eve.holt@reqres.in",
        "password": "pistol",
        "Content-Type": "application/json"
    }

    id = 4
    end_ponits_6 = List_of_APIS.register
    response = test_api.post(end_ponits_6, body)
    print(response.json())
    data = response.json()
    expectedid = data.get('id')

    assert response.status_code == 200
    assert expectedid == id
    if response.status_code not in [200, 201]:  # if condition which check for the status code either 200 or 201 if not it will throw assertion error
        assert False

    logging.info("***** user_signUp is validated Successfully *****")


@pytest.mark.unscussessfulreg
def test_unsuccessfullreg(test_api):
    logging.info("***** verifying unSuccessfull register *****")

    body = {
        "email": "niyog@google.com"
    }

    error = 'Missing password'
    end_ponits_7 = List_of_APIS.register
    response = test_api.post(end_ponits_7, body)
    print(response.json())
    data = response.json()

    expectederror = data.get("error")

    assert expectederror == error
    assert response.status_code == 400
    assert response.status_code != 200

    logging.info("***** unSuccessfull regster validated *****")


@pytest.mark.userloginsuccess
def test_userlogin(test_api):
    logging.info("***** verifying user_login Test *****")
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    token = 'QpwL5tke4Pnpja7X4'
    end_ponits_8 = List_of_APIS.login
    response = test_api.post(end_ponits_8, body)
    print(response.json())
    data = response.json()
    expectedtoken = data.get('token')

    assert expectedtoken == token
    assert response.status_code == 200

    logging.info("***** verifying user_login Test *****")


@pytest.mark. loginfailed
def test_userloginfailed(test_api):
    logging.info("***** verifying user_login_failed *****")
    body = {
        "email": "eve.holt@reqres.in"
    }

    error = 'Missing password'
    end_ponits_9 = List_of_APIS.login
    response = test_api.post(end_ponits_9, body)
    print(response.json())
    data = response.json()
    expectederror = data.get('error')
    assert expectederror == error

    if response.status_code == 400:
        logging.info("***** user_login_failed test is passed ")
        assert True
    else:
        logging.error("***** user_login_failed test is failed")


    logging.info("***** user_login_failed is valideted *****")







