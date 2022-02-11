from datetime import datetime
from .models import CorrectAnswer
def get_date_today(request):
    today = datetime.today()
    return {'today':today}


# def get_date_is_sol(request):
#     coan = CorrectAnswer.
#     return {'today':today}