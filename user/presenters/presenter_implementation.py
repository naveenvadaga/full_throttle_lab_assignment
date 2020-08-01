from typing import List

from user.interactors.presenters.presenters import Presenter
from user.interactors.storages.storage import UserDetailsDTO, UserActivityPeriodsDTO
from datetime import datetime

class PresenterImplementation(Presenter):

    def get_users_data_response(
            self, user_details_dtos: List[UserDetailsDTO],
            user_activity_period_dtos: List[UserActivityPeriodsDTO]):
        response = []

        user_id_wise_activity_periods = self. \
            _get_user_id_wise_activity_periods(
                user_activity_period_dtos)

        for each_user in user_details_dtos:
            user_activity_periods = user_id_wise_activity_periods[
                each_user.user_id]
            response.append({
                "id": each_user.user_id,
                "real_name": each_user.real_name,
                "tz": each_user.time_zone,
                "activity_periods": user_activity_periods
            })

        return response

    def _get_user_id_wise_activity_periods(
            self, user_activity_period_dtos:
            List[UserActivityPeriodsDTO]) -> dict:
        from collections import defaultdict
        user_id_wise_activity_periods = defaultdict(list)

        user_activity_period_dtos.sort(key= lambda dto:
            (dto.start_time, dto.end_time))

        for each_activity_period in user_activity_period_dtos:
            user_id = each_activity_period.user_id
            dict = {
                "start_time": self._convert_datetime_to_string(
                    each_activity_period.start_time),
                "end_time": self._convert_datetime_to_string(
                    each_activity_period.end_time)
            }
            user_id_wise_activity_periods[
                user_id].append(
                dict)

        return user_id_wise_activity_periods

    @staticmethod
    def _convert_datetime_to_string(datetime_obj: datetime):
        from user.constants.constants import DATE_TIME_FORMAT
        return datetime_obj.strftime(DATE_TIME_FORMAT)
