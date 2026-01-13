
def create_trip(city, date, comment):
    """
    Returns a trip dictionary with city, date string, and comment.
    :param city: str - name of the city
    :param date: str - date in dd-mm-yyyy format
    :param comment: str - short comment about the trip
    :return: dict
    """
    return {
        "city": city,
        "date": date,
        "comment": comment
    }