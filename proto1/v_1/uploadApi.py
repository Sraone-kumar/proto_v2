# from ast import mod
import pandas as pd
import django


class Upload:

    def __init__(self, ModelObject, PandasObject):
        print(type(ModelObject))
        print(type(PandasObject))
        assert isinstance(
            ModelObject, django.db.models.base.ModelBase), 'Argument is not of type django Model'
        assert isinstance(
            PandasObject, pd.core.frame.DataFrame), 'Argument is not of type pandas frame'
        assert len(ModelObject._meta.get_fields()) != len(
            PandasObject), 'Excel fields does not match Model fields'

        self.ModelObject = ModelObject
        self.PandasObject = PandasObject

    def uploadChecker(self, ModelCompare, PandasCompare):
        model_rows = list(self.ModelObject.objects.all().values(ModelCompare))

        for model in model_rows:
            for frame in self.PandasObject.iterrows():
                # print(
                #     f" {model[ModelCompare]} ,{frame[1][PandasCompare]} ")
                if model[ModelCompare] == frame[1][PandasCompare]:
                    # self.FinalObjects.append(frame[1][PandasCompare])
                    self.PandasObject.drop(frame[0], inplace=True)

    def printer(self):
        print(self.PandasObject)

    def forienKeyConverter(self, forienKeyModel, ModelCompare, PandasCompare):
        assert isinstance(
            forienKeyModel, django.db.models.base.ModelBase), 'Argument is not of type django Model'
        model_rows = list(
            forienKeyModel.objects.all().values('pk', ModelCompare))
        for frame in self.PandasObject.iterrows():
            for model in model_rows:
                if frame[1][PandasCompare] == model[ModelCompare]:
                    self.PandasObject.at[frame[0], PandasCompare] = forienKeyModel.objects.get(
                        pk=model['pk'])
