from students.models import Asistence
import pandas as pd
from datetime import datetime
from pytz import timezone

def create_asistences_excel(response):
    data=Asistence.create_dict_from_db()
    df = pd.DataFrame(data)
    creation_datetime = datetime.now(tz=timezone('America/Bogota'))
    filename = f"presences_bienestar_digital__{creation_datetime.strftime('%Y-%m-%d %H:%M')}.xlsx"
    response['Content-Disposition'] = f'attachment; filename={filename}'
    df.to_excel(response, index=False)