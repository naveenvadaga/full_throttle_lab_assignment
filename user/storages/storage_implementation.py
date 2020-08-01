from typing import List

from user.interactors.storages.storage import Storage, UserDetailsDTO, UserActivityPeriodsDTO
from user.models import User, UserActivityPeriod


class StorageImplementation(Storage):
    def get_users_details(self) -> List[
            UserDetailsDTO]:
        user_objs = User.objects.all()

        user_details_dtos = []
        for each_obj in user_objs:
            user_details_dtos.append(
                UserDetailsDTO(
                    user_id=each_obj.id,
                    real_name=each_obj.real_name,
                    time_zone=each_obj.time_zone
                )
            )

        return user_details_dtos

    def get_users_activity_periods(self) -> List[
            UserActivityPeriodsDTO]:

        user_activity_period_objs = \
            UserActivityPeriod.objects.all()

        user_activity_period_dtos = []

        for each_obj in user_activity_period_objs:
            user_activity_period_dtos.append(
                UserActivityPeriodsDTO(
                    user_id=each_obj.user_id,
                    start_time=each_obj.start_time,
                    end_time=each_obj.end_time
                )
        )

        return user_activity_period_dtos
