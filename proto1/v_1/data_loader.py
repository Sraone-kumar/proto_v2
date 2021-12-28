import pandas as pd



def loader(request):
    print(request.FILES('file_upload'))
    file = pd.read_excel(request.FILES('file_upload'))
    print(file.head())