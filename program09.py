import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination 

data = pd.read_csv('program9.csv');
heartdisease = pd.DataFrame(data);
print(heartdisease);

model = BayesianModel([
    ('age' , 'lifestyle'),
    ('gender' , 'lifestyle'),
    ('family' , 'heartdisease'),
    ('diet' , 'cholestrol'),
    ('lifestyle' , 'diet'),
    ('cholestrol' , 'heartdisease'),
    ('diet' , 'cholestrol')
    ]);

model.fit(heartdisease, estimator = MaximumLikelihoodEstimator);

heartdisease_infer = VariableElimination(model);

print("""For age Enter {
        SuperSenioerCitizen : 0,
        SenioerCitizen : 1,
        middleage      : 2,
        youth          : 3,
        teen           : 4
        }""");

print('''For gender Enter {
        Male   : 0,
        Female : 1
        }''');

print('''For Family History Enter : {
        Yes : 1,
        No  : 0
        }''');

print('''For Diet Enter {
        High   : 0,
        Medium : 1
        }''');

print('''For Life Style Enter {
        Athelte   : 0,
        Active    : 1,
        Moderate  : 2,
        Sedentary : 3
        }''');
print('''For Cholestrol Enter {
        High       : 0,
        BorderLine : 1,
        Normal     : 2
        }''');


q = heartdisease_infer.query(
        variables=['heartdisease'],
        evidence = {
            'age'        : int(input('Enter Age            : ')),
            'gender'     : int(input('Enter Gender         : ')),
            'family'     : int(input('Enter Family History : ')),
            'diet'       : int(input('Enter Diet           : ')),
            'lifestyle'  : int(input('Enter Life Style     : ')),
            'cholestrol' : int(input('Enter Cholestrol     : ')),
            });
print(q);
