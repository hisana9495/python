def create_record(city, comment, date_str):
    """
    Returns a travel record as a dictionary.
    city: str - name of the city visited
    comment: str - traveler's comment
    date_str: str - date in format 'dd-mm-yyyy'
    """
    return {
        "city": city,
        "comment": comment,
        "date": date_str
    }