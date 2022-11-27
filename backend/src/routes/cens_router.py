import os
from flask import Blueprint, redirect, request
import pandas as pd
from utils import validator, response, helper, environment

cens_router = Blueprint("cens_router", __name__)

# @cens_router.route("/")
# def test():
#     mydata = {
#         "name":["John","Danny","Patricia","Rose"],
#         "office":["HR","Sales","Sales","HR"],
#         "salary":[55,67,58,60]
#     }
#     df = pd.DataFrame(mydata)
#     mean_salary = df['salary'].mean()
#     return "The mean salary is %f" % mean_salary

@cens_router.route("/", methods=["POST"])
def uploader():
    try:
        file = request.files['excel']
        if validator.allowed_file(file.filename):
            if 'xlsx' in file.filename:
                df = pd.read_excel(file)
            else:
                df = pd.read_csv(file, thousands='.', decimal=',')
        df["SENSACION TERMICA"] = df.apply(helper.calculate_thermal_feeling, axis=1)
        df['FESTIVO'] = df['FESTIVO'].replace(['SI', 'NO'], [1, 0]);
        dummiesDay = pd.get_dummies(df['NOMBRE DE DIA'])
        dummiesMonth = pd.get_dummies(df['MES'])
        df = pd.concat([df, dummiesDay], axis = 1)
        df = pd.concat([df, dummiesMonth], axis = 1)
        df = df.drop(columns=['NOMBRE DE DIA', 'MES','EVENTO'])
        filename = file.filename.rsplit('.', 1)[0] + ".csv"
        df.to_csv(os.path.join(environment.UPLOAD_FOLDER, filename), index=False)
        return response.json("Excel cargado con exito", df.columns.values.tolist(), 200)        
    except Exception as ex:
        print(ex)
        return response.json("No se ha enviado un archivo excel (.csv, .xlsx) válido", None, 404) 