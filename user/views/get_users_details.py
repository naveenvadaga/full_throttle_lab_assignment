from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_user_details(
        request, format=None):
    if request.method == "GET":
        from user.storages.storage_implementation \
            import StorageImplementation
        storage = StorageImplementation()

        from user.presenters.presenter_implementation import PresenterImplementation
        presenter = PresenterImplementation()

        from user.interactors.get_users_data \
            import GetUsersData
        interactor = GetUsersData(storage, presenter)

        response = interactor.get_users_data()

        # return response
        return Response(
            data=response, status=status.HTTP_200_OK)
