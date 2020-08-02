def populate_database(file_path="./Test JSON.json"):
    user_data = get_json_data(file_path)
    if user_data:
        populate_user_model(user_data['members'])
        populate_user_activity_period_model(
            user_data['members'])


def populate_user_model(user_data):
    from django.apps import apps
    user_model = apps.get_model(
        'user', 'User')

    user_model_objs = []

    for each_user in user_data:
        user_model_objs.append(
            user_model(
                id=each_user['id'],
                real_name=each_user['real_name'],
                time_zone=each_user['tz']
            )
        )

    user_model.objects.bulk_create(
        user_model_objs)


def populate_user_activity_period_model(
        user_data):
    from django.apps import apps
    user_activity_period_model = apps.get_model(
        'user', 'UserActivityPeriod')
    user_activity_period_objs = []

    for each_user in user_data:
        for each_period in each_user[
                'activity_periods']:
            user_activity_period_objs.append(
                user_activity_period_model(
                    user_id=each_user['id'],
                    start_time=convert_str_to_datetime(
                        each_period['start_time']),
                    end_time=convert_str_to_datetime(
                        each_period['end_time'])
                )
            )

    user_activity_period_model.objects.bulk_create(
        user_activity_period_objs)


def convert_str_to_datetime(
        date_time_str):
    from datetime import datetime

    from user.constants.constants import DATE_TIME_FORMAT
    return datetime.strptime(
        date_time_str, DATE_TIME_FORMAT)


def convert_str_to_datetime_based_on_timezone(
        date_time_str, time_zone):
    from datetime import datetime
    import pytz
    from django.utils.timezone import make_aware

    from user.constants.constants import DATE_TIME_FORMAT
    return make_aware(datetime.strptime(
        date_time_str, DATE_TIME_FORMAT),
        timezone=pytz.timezone(time_zone))


def get_json_data(file_path="./Test JSON.json"):
    import json
    with open(file_path) as file:
        json_data = json.load(file)

    return json_data
